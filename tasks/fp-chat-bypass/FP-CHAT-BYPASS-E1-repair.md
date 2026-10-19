# E1 repair: call independent acceptance before sending

The first E1 continuation established a standalone transfer oracle but did not
wire it into the actual delivery controller. On predecessor FP
`df4e3d268a6915e58be643dc92131e4e8f6fb2b9` with AI-CI
`063d2f5672b0209456424ce9be9b205e644ae7b7`, the new regression executed the
existing APIs under checked Ithon `d6e83969f82512e920fb17b44326cb54f31d015c`:

| Case | Predecessor observation | Required repair result |
| --- | --- | --- |
| Bare transport sender, incident command recomposed as a valid transfer stage | ACCEPTED; sink called once | Operation gate required; zero sends |
| Resumable controller, same bad candidate and self-consistent metadata | ACCEPTED; sink called once | Operation gate required; zero sends |
| Destination changed and contract recomputed against unchanged supervisor admission | Authority accepted | Reject operation substitution before send |

The specimen remained inert bytes in a disposable fixture. No `gh` command was
executed by these sink functions. The original regression failed with all three
observations, rather than passing merely because it detected its own new API.

The repair keeps the existing FP sender/controller and AI-CI acceptance owner.
Both FP delivery APIs now require the operation candidate gate before sending.
AI-CI snapshots the independently supplied complete admission, includes operation
metadata in authority comparison, checks Kitchen HEAD and clean transfer source,
and regenerates the exact recipe. It checks proposed rendering before send and
actual readback afterward. Failed revalidation removes saved success before any
check can throw, retaining the accepted presentation history.

The complete recipe contains shell redirections. Plain rendering fails the
existing HTML exclusion; the supported fixture chooses literal presentation
explicitly and rejects extra surrounding text. This is not a claim that a
physical Android client accepts CodeBlocks. The default for other payloads is
still ordinary text, and unsupported presentation now fails before send.

The expanded AI-CI delivery suite executes bad-recipe, changed/removed operation,
worker-recomputed admission, raw-rendering, added-summary, wrong-revision and
dirty-source controls. Its positive controller sends the exact recipe once,
resumes without sending again, and invalidates the saved result when source
revalidation fails. The existing 83 FP runtime cases, eight transfer-command
cases, 66 independent delivery cases and nine rejection transitions remain.

Hosted results must always be read against their exact published head; the
initial E1 hosted result in the TSV remains historical. Review-branch receipts
carry the new composed heads and run URLs. No merge or activation follows from
green fixtures.

The original incident remains open at the platform boundary: no authenticated
ChatGPT original-request/correction admission, committed-response interception,
or client-presentation acknowledgement is exposed here. Fixture adapters and
local hashes cannot manufacture that interface. Live transfer, production
adapter acceptance, and physical presentation remain NOT_RUN/NOT_VERIFIED.
