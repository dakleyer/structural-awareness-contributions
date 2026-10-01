# Handoff to the independent native/Codex lane

Status: pure service mapping and bounded temporal checks implemented; **runtime integration and paired execution remain unadmitted/unexecuted**. Follow [CODEX_START_HERE.md](../../implementation/00G-HF-PARALLEL-v0.1/CODEX_START_HERE.md) for the unchanged native lane. Do not import this component into an already frozen native baseline run.

## Available contract

Call `adapt_native(initial_public_view, host_service_exchanges, decision, now, timing)` to obtain `snapshot`, explicit gaps, raw report provenance and acquisition accounting. Then call `compare(previous_snapshot, current_snapshot)`. Both are pure functions. They do not query sources, wait, deliver signals, enforce permissions or select model actions. The integration runner must capture the original service responses and construct the exchange projection; never pass the hidden `Episode.world` or expected outcomes.

| Native surface | Current mapping | Integration consequence |
|---|---|---|
| authority transition/access | Point observations from principal/asset bindings; version and valid_until null. | Preserve current denials/permissions as returned; do not fabricate a forward lease. Native guards keep their own decision/effect-time checks. |
| applicability Q | Point observation from the applicability binding. | Observed changes can be compared, but continued truth is unproven. |
| reports | Declared fixture lineage and supplied expiry; revoked/malformed records excluded with reasons and raw fields retained. | No inferred statistical independence; T1/Q binding is a fixture assumption. |
| peer text | No mapping to authority or evidence. | Natural-language extraction remains outside this profile. |
| basis_version | Host label preserved separately. | Never treat a new host label as a source revision or renewed authority. |
| temporal result | Qualification, metadata and point changes separated. | NO_OBSERVED_CHANGE is not proof of stability; UNKNOWN is not operational success. |

## Conditions before admission

Freeze the host bindings, snapshot/query timing, model/configuration, native controls, source access, interpretation of point-only signals, processing and transport cost, response budget and scoring before either arm runs. If additional source metadata or a freshness policy is added, give the same information and policy to the native comparator and use a new native candidate version. No free EA-only acquisition. Record signal emission, reception, receiver decision, attempt, effect and legitimate completion independently. Preserve successful native controls and cases where EA is ignored, arrives late or adds burden without benefit.

The six recorded scripts only acquire information. They do not measure the ability of a receiver to use it, do not reproduce production timing and do not supply an A25/H2–H6 verdict. The next empirical action remains native E1, followed by the prospectively matched E3 comparison.
