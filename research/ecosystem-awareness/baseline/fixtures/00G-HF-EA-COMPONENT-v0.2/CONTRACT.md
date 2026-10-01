# EA component v0.2 — temporal comparison and conservative native adapter

Author development experiment, 1 October 2026. Additive successor to the preserved [v0.1 contract](../00G-HF-EA-COMPONENT-v0.1/CONTRACT.md); not a canonical interface change. The exact v0.1 qualifier is imported by path and pinned in the run registration. C3 and the native candidate remain unchanged.

## Boundary and input

`compare(previous, current)` receives two host-delivered snapshots, each with exactly `view` and `point_observations`. `view` obeys the v0.1 contract; only source-qualified records with supplied version/validity can populate its checks. `point_observations` preserves native check responses with name, source, decision scope, observed_at and boolean value; version and valid_until must be null. Such observations can establish what a service returned at a particular time, never a future lease. Neither function accepts hidden worlds, expected verdicts or future schedules.

The host owns channel bindings and snapshot construction. JSON strings and hashes do not establish provenance against a malicious host. Times use one declared logical clock. Input bounds are inherited from v0.1 plus at most three point observations, one per dimension. Future observations and malformed shapes raise ValueError. Scope/source mismatches remain unqualified, not successful checks. The component does not acquire information or call tools.

## Current qualification and temporal meaning

The unchanged v0.1 qualifier evaluates the interval-qualified `view`. Point observations are returned in a separate channel and **cannot fill its missing checks**, even when positive. Consequently native v0.1 generally yields UNKNOWN for interval sufficiency. This is an information/contract mismatch, not a demonstrated failure of the native guard. A negative native response is retained for the owner to act on; the adapter does not weaken the native guard or replace it with EA.

Temporal comparison requires identical decision identity/scope apart from the host's basis_version and a strictly later current snapshot. A different recipient/task/resource/operation/claim/id is NOT_COMPARABLE; it is not a context-change finding. The host's basis_version is not a source-native version and never grants authority.

For comparable snapshots return separately:

- dimension status changes in the qualified views; loss through expiry is QUALIFICATION_CHANGE, not proof the underlying world changed;
- source version, qualified evidence-root or host basis-label changes; version-only change does not establish a material semantic change;
- point-value changes only for matching trusted source/scope and strictly increasing observation times; these prove a change between service responses, not its exact occurrence time, persistence, cause or future validity;
- current sufficient qualification after prior insufficiency, labelled QUALIFIED_RECOVERY_WITHIN_VIEW. This is a supported present basis, not permission to act or evidence that EA caused recovery;
- NO_OBSERVED_CHANGE if no supplied distinction changed. This never means the hidden world is unchanged. Endpoint comparison can miss a transient change and return to the original state.

`authority_effect` is always NONE. Timing/margin is the current qualifier's declared logical bound; point-only information provides no qualified validity horizon. A change can be detected too late. Identical delivered views give identical outputs despite different hidden worlds.

## Native-service mapping

`adapt_native(initial, exchanges, decision, now, timing)` accepts a host-produced projection of the initial public view and recorded service exchanges, **not Episode/world/oracle objects**. Each exchange carries action, requested_at, response_at and the exact returned result. Requests and responses must be ordered, with native observation time equal to response time, and no future response relative to now. Only authority, applicability and reports are admitted; unknown actions raise ValueError. Service errors are retained as gaps and cannot become positive evidence. Latest successful response wins by observed time; an error does not erase an earlier observation, whose age remains visible. This freshness selection is not source versioning.

The registered native binding is R / T1 / Y / inspect / Q. Authority transition maps to mandate; access maps to access; applicability maps to Q. Source names are assigned by the host's tool binding, not copied from peer text. These three services supply neither version nor lease, so all three remain point observations with null version/valid_until. The initial reports and later reports response supply fixture lineage, report intervals and current revoked flags. Revoked, malformed or unqualified records cannot be revived by dropping metadata. Missing report expiry is kept unqualified; no infinity is invented. Native reports lack per-report task/resource scope: binding to T1/Q is an explicit synthetic fixture assumption, not a general adapter or discovered authority. Peer instructions never become evidence.

This is a conservative service projection for component testing, **not an admitted runtime integration**. No automatic query policy or signal delivery to a model is implemented here. The scripted acquisition recipe costs three native calls/ticks per snapshot. A wait is charged separately. Future comparisons must expose identical service access, record EA processing/transport/response cost and freeze both arms before execution. This package cannot close E1/E3, H2–H6, empirical prevention or real-time production readiness.

## Acceptance and evidence

Fixtures cover unchanged, authority/applicability change, dependency collapse, expiry, missing observation, recovery, version-only/basis-only refresh, scope mismatch, out-of-order time, a late signal, point-only change and indistinguishable hidden states. Software integration checks exercise recorded native calls across all six cells plus revoked reports and rejection paths. Scripted calls are not agent decisions. Expected properties and this contract are hashed before execution; code and dependency hashes are registered before every run. Same-author development and public fixtures are neither blind nor external validation. The runner keeps every output and fails on unmet expectations. Prior results are never overwritten.
