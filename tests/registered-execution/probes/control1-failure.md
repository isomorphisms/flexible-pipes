# Initial control rejected before execution

The actual Ithon frontend rejected `control1.pi` because the runtime-injected
`__file__` name lacked a static declaration. Exit status was 1, no successful
check receipt was emitted, and the child was never invoked. Preserve this
source as the first attempt. `control2.pi` declares the foreign runtime value
with `__file__ ∈ str`; it does not bypass the checker.
