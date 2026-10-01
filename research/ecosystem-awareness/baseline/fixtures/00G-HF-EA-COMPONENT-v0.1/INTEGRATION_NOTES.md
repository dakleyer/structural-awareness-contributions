# Integration boundary — Codex/native and EA component

**Status: adapter not implemented or admitted.** The native lane can run independently. This file identifies the concrete differences to resolve before coupling; compatible-looking JSON is not sufficient evidence of semantic equivalence.

| Native v0.1 surface | EA v0.1 input | Required treatment before paired execution |
|---|---|---|
| `Episode.initial_view()` recipient, task/resource and mission | Full `decision` scope and basis version | Register identifiers/basis representation in the host. A required deliverable does not grant permission. Same mission and metadata available to the control arm. |
| `authority` service returns current transition/access booleans and observation time | Separate `mandate` and `access` source-qualified observations | The existing response omits explicit source-native version and validity interval. Do not invent a lease or future non-revocation. Register a service-contract extension or a revised EA profile that preserves this missing qualification. |
| `applicability` returns current Q and observation time | Source-native proposition qualification | Same version/freshness gap; current truth is not a guarantee until the later effect. Revalidation remains under the native service/guard. |
| `reports` contains report IDs, roots, qualification and intervals | Typed evidence with declared lineage binding and full scope | Bind only fields justified by the native service's recorded contract. Root labels are fixture lineage, not statistical independence. Preserve `revoked` information; the adapter must not revive a revoked report by dropping that field. |
| Peer message text | Optional instruction record | Never synthesize a positive authority or evidence record merely because a peer claims it. Natural-language extraction is outside EA v0.1. |
| Synthetic ticks and tool duration | Emission/receipt/response bounds | Charge acquisition, EA processing, transport and receiver response to the registered budget. Distinguish assumed tick costs from measured wall time. |
| Native host recorder and frozen C3 scoring | Separate signal journal plus native actions | Record signals as extra host events without changing the frozen oracle's event semantics. Score valid native traces with C3; assess signal properties separately. |

Missing source-native metadata must remain missing. A future adapter may use a declared local freshness policy, but must label it as a policy assumption available identically to both arms, not as an authoritative promise or evidence of no change. Revising this input contract requires a new version and fixtures; do not patch v0.1 after seeing paired results.

The EA candidate's accepted-source names are profile bindings controlled by the host, not a mechanism that trusts a peer-supplied string. A runtime implementation must construct those records from approved service results and keep untrusted text separate. Arbitrary tool output cannot label itself `principal-service` and thereby become authorized.

For the first paired lot, freeze the exact mapping, same underlying model, instructions/common transport, available sources, native controls and limits before either arm runs. Give the native comparator equal eligible source access and charge all EA calls. Retain the attention/transport contrast if signal delivery changes attention. Do not claim isolated EA effect if the EA arm alone obtains better information or extra time.

The current native v0.1 guard already queries trusted current facts at request/effect time. It may be sufficient for these cells. The component may add only explanation or no measurable benefit; preserve that result. Any weakening of native controls is a different registered question, not a prerequisite for showing EA value.

**Readiness gate:** A component package passing its own fixture checks is not yet an admitted native/EA adapter. Publish the mapping, its tests and unresolved information assumptions, then freeze a new comparison lot. No blind or empirical claim is supplied by the two author sessions working separately.
