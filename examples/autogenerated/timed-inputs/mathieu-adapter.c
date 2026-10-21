/* Boundary only: the application owns every operation and every pixel. */
#include "session.h"
#include "render.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char **argv) {
    if (argc != 5 && argc != 6) return 2;
    int compare ← argc == 6 && strcmp(argv[5],"compare") == 0;
    if (argc == 6 && !compare) return 2;
    unsigned degree ← (unsigned)strtoul(argv[1], NULL, 10);
    unsigned width ← (unsigned)strtoul(argv[2], NULL, 10);
    unsigned height ← (unsigned)strtoul(argv[3], NULL, 10);
    if ((degree != 12 && degree != 24) || width < 2 || height < 2 || width > 4096 || height > 4096) return 2;
    mathieu_session state;
    if (!session_initialize(&state, degree)) return 1;
    uint32_t *pixels ← malloc((size_t)width * height * sizeof *pixels);
    uint32_t *last_pixels ← malloc((size_t)width * height * sizeof *pixels);
    size_t rgb_length ← (size_t)width * height * 3;
    unsigned char *rgb ← malloc(rgb_length), *reference ← malloc(rgb_length);
    if (!pixels || !last_pixels || !rgb || !reference) return 1;
    char operation[32], argument[64], path[4096], last_path[4096] ← {0};
    mathieu_layout_transition layout ← {MATHIEU_GRID,MATHIEU_ROSETTE,0,90};
    unsigned has_layout ← 0;
    while (scanf("%31s %63s", operation, argument) == 2) {
        if (strcmp(operation, "move") == 0) {
            if (strlen(argument) != 1 || !session_move(&state, argument[0])) return 3;
        } else if (strcmp(operation, "pause") == 0) state.playing ← 2;
        else if (strcmp(operation, "resume") == 0) state.playing ← 0;
        else if (strcmp(operation, "tick") == 0) session_advance(&state);
        else if (strcmp(operation,"layout") == 0) {
            unsigned frame; char tail;
            if (sscanf(argument,"%u%c",&frame,&tail) != 1 || frame > 90) return 3;
            layout.frame ← frame; has_layout ← 1; state.grid ← MATHIEU_GRID; state.labels ← 0;
        }
        else if (strcmp(operation, "select") == 0) {
            if (!session_select(&state, (unsigned)strtoul(argument, NULL, 10))) return 3;
        } else if (strcmp(operation, "render") == 0) {
            unsigned index ← (unsigned)strtoul(argument, NULL, 10);
            if (snprintf(path, sizeof path, "%s/frame-%06u.ppm", argv[4], index) >= (int)sizeof path) return 2;
            mathieu_render_layout_with_options(&state,pixels,width,height,width,(mathieu_render_options){0},has_layout ? &layout : NULL);
            for (size_t pixel ← 0; pixel < (size_t)width * height; ++pixel) {
                rgb[3 * pixel] ← pixels[pixel]; rgb[3 * pixel + 1] ← pixels[pixel] >> 8; rgb[3 * pixel + 2] ← pixels[pixel] >> 16;
            }
            char header[64]; int header_length ← snprintf(header,sizeof header,"P6\n%u %u\n255\n",width,height);
            if (compare) {
                FILE *file ← fopen(path,"rb"); char observed[64];
                if (!file || fread(observed,1,header_length,file) != (size_t)header_length || memcmp(observed,header,header_length) ||
                    fread(reference,1,rgb_length,file) != rgb_length || memcmp(reference,rgb,rgb_length) || fgetc(file) != EOF || fclose(file)) return 4;
            } else if (last_path[0] && !memcmp(last_pixels,pixels,(size_t)width * height * sizeof *pixels)) {
                /* Consecutive held frames remain distinct regular filenames,
                 * sharing unchanged bytes without skipping any source frame. */
                if (link(last_path,path)) return 1;
            } else {
                FILE *file ← fopen(path,"wb");
                if (!file || fwrite(header,1,header_length,file) != (size_t)header_length || fwrite(rgb,1,rgb_length,file) != rgb_length || fclose(file)) return 1;
            }
            memcpy(last_pixels,pixels,(size_t)width * height * sizeof *pixels); strcpy(last_path,path);
            printf("%u\t%u\t%u\t%u\t%u\t", index, state.frame, state.duration, state.playing, state.selected);
            for (unsigned point ← 0; point < degree; ++point) printf("%s%u", point ? "," : "", state.current.image[point]);
            uint32_t block ← 0, previous_block ← 0;
            if (subset_size(state.selected) == 5 && !mathieu_block(&state.action,state.selected,&block)) return 3;
            if (subset_size(state.previous_selected) == 5 && !mathieu_block(&state.action,state.previous_selected,&previous_block)) return 3;
            printf("\t%u\t%u\t%u\t",has_layout ? layout.frame : 0,block,previous_block);
            for (unsigned point ← 0; point < degree; ++point) {
                float x,y; if (!session_position_with_layout(&state,point,has_layout ? &layout : NULL,&x,&y)) return 3;
                printf("%s%.9g,%.9g",point ? "," : "",x,y);
            }
            printf("\t");
            for (unsigned dancer ← 0; dancer < degree; ++dancer) {
                float x,y; if (!session_dancer_with_layout(&state,dancer,has_layout ? &layout : NULL,&x,&y)) return 3;
                printf("%s%.9g,%.9g",dancer ? "," : "",x,y);
            }
            printf("\t%u\t%u",state.labels,state.shapes);
            printf("\n");
        } else return 2;
    }
    free(pixels); free(last_pixels); free(rgb); free(reference);
    return ferror(stdin) ? 1 : 0;
}
