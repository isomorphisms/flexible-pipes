#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define PANEL_COUNT 5
#define DEGREE_COUNT 10
#define MAX_CELLS 50

struct cell {
    int panel;
    int degree;
    int sign;
    int seed_origin;
    int branch;
    int color;
};

enum panel_color {
    COLOR_BLACK = 1,
    COLOR_PURPLE = 2,
    COLOR_GREEN = 3,
    COLOR_ORANGE = 4,
    COLOR_BLUE = 5
};

static int fail(const char *label) {
    fprintf(stderr, "FAIL %s\n", label);
    return 0;
}

static int append_seed(struct cell *cells, int *count, int panel,
                       int degree, int sign, int origin) {
    if (*count + 2 > MAX_CELLS) return 0;
    cells[*count] = (struct cell){panel, degree, sign, origin, 0, panel};
    *count += 1;
    cells[*count] = (struct cell){panel, degree + panel, -sign, origin, 1, panel};
    *count += 1;
    return 1;
}

/* Independent construction from B_n = n - sum(q^j), A_n = B_n - q^n B_n.
 * This file does not include, link, or call the leaf implementation. */
static int append_panel(struct cell *cells, int *count, int panel) {
    if (!append_seed(cells, count, panel, 0, 1, 0)) return 0;
    for (int origin = 1; origin < panel; ++origin) {
        if (!append_seed(cells, count, panel, 0, 1, origin)) return 0;
        if (!append_seed(cells, count, panel, origin, -1, origin)) return 0;
    }
    return 1;
}

static int build_prefix(int panel_count, struct cell *cells) {
    int count = 0;
    for (int index = 0; index < panel_count; ++index) {
        if (!append_panel(cells, &count, PANEL_COUNT - index)) return -1;
    }
    return count;
}

static void count_degrees(const struct cell *cells, int count,
                          int *positive, int *negative, int *coefficient) {
    memset(positive, 0, DEGREE_COUNT * sizeof(*positive));
    memset(negative, 0, DEGREE_COUNT * sizeof(*negative));
    memset(coefficient, 0, DEGREE_COUNT * sizeof(*coefficient));
    for (int index = 0; index < count; ++index) {
        int degree = cells[index].degree;
        if (degree < 0 || degree >= DEGREE_COUNT) continue;
        if (cells[index].sign > 0) positive[degree] += 1;
        if (cells[index].sign < 0) negative[degree] += 1;
        coefficient[degree] += cells[index].sign;
    }
}

static int validate_prefix(const struct cell *actual, int actual_count,
                           int panel_count) {
    struct cell expected[MAX_CELLS];
    int expected_count = build_prefix(panel_count, expected);
    if (actual_count != expected_count) return 0;
    for (int index = 0; index < actual_count; ++index) {
        if (actual[index].panel != expected[index].panel ||
            actual[index].degree != expected[index].degree ||
            actual[index].sign != expected[index].sign ||
            actual[index].seed_origin != expected[index].seed_origin ||
            actual[index].branch != expected[index].branch ||
            actual[index].color != expected[index].color) return 0;
    }
    return 1;
}

static int check_prefixes(void) {
    static const int expected[PANEL_COUNT + 1][DEGREE_COUNT] = {
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        {5, -1, -1, -1, -1, -5, 1, 1, 1, 1},
        {9, -2, -2, -2, -5, -4, 2, 2, 1, 1},
        {12, -3, -3, -5, -4, -3, 2, 2, 1, 1},
        {14, -4, -5, -4, -4, -3, 2, 2, 1, 1},
        {15, -5, -5, -4, -4, -3, 2, 2, 1, 1}
    };
    for (int prefix = 0; prefix <= PANEL_COUNT; ++prefix) {
        struct cell cells[MAX_CELLS];
        int positive[DEGREE_COUNT], negative[DEGREE_COUNT];
        int coefficient[DEGREE_COUNT];
        int count = build_prefix(prefix, cells);
        if (count < 0 || !validate_prefix(cells, count, prefix))
            return fail("panel/provenance construction");
        count_degrees(cells, count, positive, negative, coefficient);
        for (int degree = 0; degree < DEGREE_COUNT; ++degree) {
            if (coefficient[degree] != expected[prefix][degree])
                return fail("prefix coefficient");
        }
    }
    return 1;
}

static int check_mutants(void) {
    struct cell base[MAX_CELLS], mutant[MAX_CELLS];
    int count = build_prefix(PANEL_COUNT, base);
    if (count != MAX_CELLS || !validate_prefix(base, count, PANEL_COUNT))
        return fail("baseline mutation fixture");

    memcpy(mutant, base, sizeof(base));
    mutant[1].degree += 1;
    if (validate_prefix(mutant, count, PANEL_COUNT)) return fail("wrong shift survived");

    memcpy(mutant, base, sizeof(base));
    mutant[0].sign = -mutant[0].sign;
    if (validate_prefix(mutant, count, PANEL_COUNT)) return fail("wrong sign survived");

    memcpy(mutant, base, sizeof(base));
    mutant[0].color = COLOR_ORANGE;
    if (validate_prefix(mutant, count, PANEL_COUNT)) return fail("color swap survived");

    memcpy(mutant, base, sizeof(base));
    mutant[0].panel = 4;
    if (validate_prefix(mutant, count, PANEL_COUNT)) return fail("panel swap survived");

    if (validate_prefix(base, count - 1, PANEL_COUNT)) return fail("cell deletion survived");

    memcpy(mutant, base, sizeof(base));
    mutant[2].degree += 1;
    if (validate_prefix(mutant, count, PANEL_COUNT)) return fail("degree reorder survived");
    return 1;
}

static int check_source_distinctions(void) {
    int product[16] = {1};
    int next[16];
    for (int factor = 1; factor <= PANEL_COUNT; ++factor) {
        memcpy(next, product, sizeof(product));
        for (int degree = factor; degree < 16; ++degree)
            next[degree] -= product[degree - factor];
        memcpy(product, next, sizeof(product));
    }
    if (product[0] != 1 || product[15] != -1)
        return fail("finite product reference");
    return 1;
}

static int write_trace(const char *path) {
    static const int expected_positive[DEGREE_COUNT] = {15,0,0,1,1,2,2,2,1,1};
    static const int expected_negative[DEGREE_COUNT] = {0,5,5,5,5,5,0,0,0,0};
    struct cell cells[MAX_CELLS];
    int positive[DEGREE_COUNT], negative[DEGREE_COUNT], coefficient[DEGREE_COUNT];
    int count = build_prefix(PANEL_COUNT, cells);
    FILE *output = fopen(path, "wb");
    if (output == NULL) return fail("open trace");
    count_degrees(cells, count, positive, negative, coefficient);
    if (fprintf(output, "degree\tpositive_cells\tnegative_cells\tcoefficient\n") < 0)
        return fail("write trace header");
    for (int degree = 0; degree < DEGREE_COUNT; ++degree) {
        if (positive[degree] != expected_positive[degree] ||
            negative[degree] != expected_negative[degree])
            return fail("signed-cell census");
        if (fprintf(output, "%d\t%d\t%d\t%d\n", degree, positive[degree],
                    negative[degree], coefficient[degree]) < 0)
            return fail("write trace row");
    }
    if (fclose(output) != 0) return fail("close trace");
    return 1;
}

int main(int argc, char **argv) {
    if (argc != 2) {
        fprintf(stderr, "usage: %s TRACE.tsv\n", argv[0]);
        return 2;
    }
    if (!check_prefixes() || !check_mutants() || !check_source_distinctions() ||
        !write_trace(argv[1])) return 1;
    puts("PASS independent formula, provenance, prefixes, hostile mutations, and source distinctions");
    return 0;
}
