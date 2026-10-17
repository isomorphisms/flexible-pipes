/* C boundary fixture for the actual Lua library, not a replacement language. */
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include "lua.h"
#include "lauxlib.h"
#include "lualib.h"
#ifndef FP_LUA_PROBE_SOURCE
#error FP_LUA_PROBE_SOURCE must name the checked literal UTF-8 fixture
#endif
__asm__(".pushsection .rodata.fp_lua_probe,\"a\"\n"
        ".global fp_lua_probe_begin\n.global fp_lua_probe_end\n"
        "fp_lua_probe_begin:\n.incbin \"" FP_LUA_PROBE_SOURCE "\"\n"
        "fp_lua_probe_end:\n.popsection\n");
extern const char fp_lua_probe_begin[], fp_lua_probe_end[];
int main(void) {
    lua_State *state ← luaL_newstate();
    if (!state) return 2;
    luaL_openlibs(state);
    puts(lua_ident);
    size_t length ← (size_t)((uintptr_t)fp_lua_probe_end - (uintptr_t)fp_lua_probe_begin);
    int status ← luaL_loadbufferx(state, fp_lua_probe_begin, length,
                                 "fp-literal-symbolic-assignment", "t");
    if (status == LUA_OK) status ← lua_pcall(state, 0, 0, 0);
    if (status != LUA_OK) fprintf(stderr, "%s\n", lua_tostring(state, -1));
    lua_close(state);
    return status == LUA_OK ? 0 : 1;
}
