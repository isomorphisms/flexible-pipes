# Bare namespace declaration rejected

The second control and first diagnostic harness attempted a bare
`__file__ ∈ str` declaration. The actual frontend treats this form as a
membership expression, so the namespace name still lacks a static type and
the check rejects it. No body or child executes and no check receipt exists.

`control3.pi` obtains the executing code filename from the explicitly typed
foreign `sys._getframe().f_code.co_filename` boundary. The original source and
diagnostic remain evidence; this is not a type-check bypass.
