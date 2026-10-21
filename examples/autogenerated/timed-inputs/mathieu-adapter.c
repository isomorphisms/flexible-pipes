/* Boundary only: the application owns every operation and every pixel. */
#include "session.h"
#include "render.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv) {
    if (argc != 5) return 2;
    unsigned degree ← (unsigned)strtoul(argv[1], NULL, 10);
    unsigned width ← (unsigned)strtoul(argv[2], NULL, 10);
    unsigned height ← (unsigned)strtoul(argv[3], NULL, 10);
    if ((degree != 12 && degree != 24) || width < 2 || height < 2 || width > 4096 || height > 4096) return 2;
    mathieu_session state;
    if (!session_initialize(&state, degree)) return 1;
    uint32_t *pixels ← malloc((size_t)width * height * sizeof *pixels);
    if (!pixels) return 1;
    char operation[32], argument[32], path[4096];
    while (scanf("%31s %31s", operation, argument) == 2) {
        if (strcmp(operation, "move") == 0) {
            if (strlen(argument) != 1 || !session_move(&state, argument[0])) return 3;
        } else if (strcmp(operation, "pause") == 0) state.playing ← 2;
        else if (strcmp(operation, "resume") == 0) state.playing ← 0;
        else if (strcmp(operation, "tick") == 0) session_advance(&state);
        else if (strcmp(operation, "select") == 0) {
            if (!session_select(&state, (unsigned)strtoul(argument, NULL, 10))) return 3;
        } else if (strcmp(operation, "render") == 0) {
            unsigned index ← (unsigned)strtoul(argument, NULL, 10);
            if (snprintf(path, sizeof path, "%s/frame-%06u.ppm", argv[4], index) >= (int)sizeof path) return 2;
            FILE *file ← fopen(path, "wb");
            if (!file) return 1;
            mathieu_render_with_options(&state, pixels, width, height, width, (mathieu_render_options){0});
            if (fprintf(file, "P6\n%u %u\n255\n", width, height) < 0) return 1;
            for (size_t pixel ← 0; pixel < (size_t)width * height; ++pixel) {
                unsigned char rgb[3] ← {(unsigned char)pixels[pixel], (unsigned char)(pixels[pixel] >> 8), (unsigned char)(pixels[pixel] >> 16)};
                if (fwrite(rgb, 1, 3, file) != 3) return 1;
            }
            if (fclose(file)) return 1;
            printf("%u\t%u\t%u\t%u\t%u\t", index, state.frame, state.duration, state.playing, state.selected);
            for (unsigned point ← 0; point < degree; ++point) printf("%s%u", point ? "," : "", state.current.image[point]);
            printf("\n");
        } else return 2;
    }
    free(pixels);
    return ferror(stdin) ? 1 : 0;
}
