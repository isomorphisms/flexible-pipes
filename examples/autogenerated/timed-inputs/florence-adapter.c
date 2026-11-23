/* Reuse the complete original sample-window and rendering implementation. */
#define main original_nightingale_main
#include "nightingale_movie.c"
#undef main

int main(int argc, char **argv) {
    if (argc != 3) return 2;
    size_t pcm_count ← 0;
    int16_t *pcm ← read_pcm(argv[1], &pcm_count);
    if (!pcm) return 1;
    unsigned index; size_t end;
    while (scanf("%u %zu", &index, &end) == 2) {
        if (!end || end > pcm_count) return 2;
        char path[4096];
        if (snprintf(path, sizeof path, "%s/frame-%06u.ppm", argv[2], index) >= (int)sizeof path || !render_frame(pcm, pcm_count, end, path)) return 1;
        float samples[SAMPLE_COUNT];
        struct complex_value coefficients[SAMPLE_COUNT];
        window_samples(pcm, pcm_count, end, samples);
        if (!fourier_dft_real(samples, SAMPLE_COUNT, coefficients, SAMPLE_COUNT)) return 1;
        printf("%u\t%zu", index, end);
        for (unsigned term ← 1; term < TERM_COUNT; ++term)
            printf("\t%.17g,%.17g", coefficients[term].real, coefficients[term].imaginary);
        printf("\n");
    }
    free(pcm);
    return ferror(stdin) ? 1 : 0;
}
