# Extension — Cache/TTL and current scoped reply

Documentation 0.2 · 7 October 2026 · Simplified DDS Stage A.

The [single DDS Index](../../../../../DDS_CANONICAL_METHOD_INDEX_v0.1.md) governs this study. The local base is **CACHE-TTL-BOUNDED-RECEIVER-0.1** and the object is a bounded candidate receiving/mechanism specification. Its [candidate package](./CANDIDATE_SPECIFICATION_PACKAGE.json), [scope/card](./CURRENT_RUN_CARD.json) and [current record](./CURRENT_STUDY_RECORD.json) identify the selected obligations. Native execution here means the named local library/state, not validation of a provider product.

## Step 1 — technology–problem extension and correspondence

Question: **When can a scoped cache response remain sufficient at use, and where do TTL/metadata/source-truth assumptions fail?**

Human/process contexts and actual parameter changes are explicit in all 9 registered [scenarios](./CURRENT_RUN_CARD.json). The receiver receives permitted requests, configuration and source/resource observations; the evaluator retains expected labels, truth and target state. Scenario/policy simulation-kind markers remain visible to these local models; there is no claim of blind generated-world search or hostile-code isolation.

RFC9111 defines HTTP cache freshness/validation. Redis and Azure provide expiration/cache-aside mechanisms. Their native mechanisms receive full credit; this local composition tests a separate scoped receiving question.

The correspondence is local: task→request/effect, scope→tenant/resource, qualification→current permitted observations, closure→the actual response/receipt/disposition and useful window. It is **not a proved R01/native-product isomorphism**. R01 probability/cost laws, rates and all-policy bounds do not transfer. Any claimed transfer requires a separate admissible relation with preserved inputs, actions, information, cost and acceptance. These conditions are the limits of this Step 1 finding.

## Step 2 — non-isomorphic/additional mechanisms

| Mechanism | Producer/authority | Measured burden and falsifier |
|---|---|---|
| Tenant/key binding | Application and cache-key owner | Tenant-scoped SQLite lookup; CACHE-05 collision is rejected |
| Expiry/generation qualification | Origin supplies version/value; cache records expiry | Origin metadata read/refresh; CACHE-03/CACHE-06 refresh stale data |
| Current authorization at response use | Resource grant owner | Grant/use-boundary reads; CACHE-04 denies and CACHE-09 defers after a source change |
| Admitted deferment | Task owner defines fallback authority | Recorded disposition; CACHE-08/CACHE-09 only count M when fallback is explicitly admitted |
| Producer truth boundary | Source owner; independent evaluator holds world truth | No truth proof added by TTL; CACHE-07 retains an incorrect P answer |

Composition: Expiry and generation refresh interact with current authorization; source changes at use can turn a previously valid hit into an admitted deferment. Different mechanisms may be supplied by conventional application logic. No extra-architecture advantage is presumed; a competent conventional peer is credited fully.

## Sources and boundaries

- [RFC9111 HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111.html) — primary reference for selected semantics; reviewed 2026-10-07; no named-product execution.
- [Redis EXPIRE](https://redis.io/docs/latest/commands/expire/) — primary reference for selected semantics; reviewed 2026-10-07; no named-product execution.
- [Azure Cache-Aside](https://learn.microsoft.com/en-us/azure/architecture/patterns/cache-aside) — primary reference for selected semantics; reviewed 2026-10-07; no named-product execution.

actual SQLite-backed cache/origin/grant; fixed clock, no Redis/HTTP/Azure execution. TTL does not prove source truth, applicability, current authority or correctness. This policy reads origin metadata even on a cache hit.
