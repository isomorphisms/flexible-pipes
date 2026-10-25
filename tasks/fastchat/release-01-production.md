# FastChat paired-production registration candidate

Register FastChat with the existing `android-native-apk` pipeline and Android
application allowlist. The application owns its contract and paired recipe;
Flexible Pipes keeps exact-source, approved-policy and required-artifact checks.
No new producer or model-job dispatcher is added.

The application implementation continues the existing
isomorphisms/fastchat PR #17, “Native FastChat: composer, provider setup, durable
drafts and paired APKs” (https://github.com/isomorphisms/fastchat/pull/17).
The fixed registered runner invokes a Bash recipe path; FastChat's wrapper
only transfers control to its canonical `scripts/build-paired.grease` under the
explicit digest-checked Grease runtime. The recipe builds and repeat-packages
both ABIs through its existing ICK/HTTP2/native/packager routes. FP still runs
the independent ai-ci companion verifier afterward.

## Required inputs and boundaries

Keep the existing FP_ANDROID_* source, ICK witness, Cat Food, ai-ci, packager
and output inputs. The FastChat recipe additionally requires the explicit
GREASE_BINARY, FC_NDK_ROOT, FC_ICKY_LUA_SOURCE, FC_HTTP2_SOURCES, FC_CMAKE,
FC_ICK_ARM_DRIVER, FC_ICK_ARM_SUPPORT, FC_ICK_ARM64_DRIVER and
FC_ICK_ARM64_SUPPORT inputs and its SDK build-tools path. No device compiler
is installed or invoked.

This registry entry is a source candidate. It does not approve a Cat Food
planning identity, application source, signing identity, Grease closure,
Kitchen procedure, independent ai-ci result or physical-device behavior.

At Cat Food main eafd7fa9e61138a664b205bf8ba82ec6837bbbb9, the real planner
rejects FastChat: `missing or duplicate approved launcher identity`.
Reuse isomorphisms/catfood PR #136, “FC-M2/M4: register FastChat planning
identity and classify captured devices” (https://github.com/isomorphisms/catfood/pull/136).
The independent stable FastChat signer must also be recognized by approved
ai-ci policy. None of those policies is fabricated or bypassed here.

The source-producer repair in isomorphisms/fastchat PR #16, “Repair remaining
FastChat workflows with pinned Grease producer”
(https://github.com/isomorphisms/fastchat/pull/16), still has an actual failing
Grease qualification. A downloaded byte-identical test runtime does not waive
that production boundary. Physical A1/C67 and live-provider acceptance remain
NOT_RUN.
