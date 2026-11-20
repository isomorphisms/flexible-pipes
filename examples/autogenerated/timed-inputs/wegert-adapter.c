/* Report the context that actually draws the source frames, in this process. */
#include "wegert_offscreen_gles.h"
#include <GLES3/gl3.h>
#include <stdio.h>
static bool observed_initialize(struct wegert_offscreen_gles *offscreen,
    int width, int height, const char *fragment, char *error, size_t capacity) {
    if (!wegert_offscreen_gles_initialize(offscreen,width,height,fragment,error,capacity)) return false;
    fprintf(stderr,"GL_VENDOR\t%s\nGL_RENDERER\t%s\nGL_VERSION\t%s\n",
        glGetString(GL_VENDOR),glGetString(GL_RENDERER),glGetString(GL_VERSION));
    return true;
}
#define wegert_offscreen_gles_initialize observed_initialize
#include "wegert_render_frames.c"
