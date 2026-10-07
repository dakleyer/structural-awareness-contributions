# Extension — Typed output validation and semantic receiving controls

Documentation 0.2 · 7 October 2026 · Simplified DDS Stage A.

The [single DDS Index](../../../../../DDS_CANONICAL_METHOD_INDEX_v0.1.md) governs this study. The local base is **STRUCTURED-OUTPUT-BOUNDED-RECEIVER-0.1** and the object is a bounded candidate receiving/mechanism specification. Its [candidate package](./CANDIDATE_SPECIFICATION_PACKAGE.json), [scope/card](./CURRENT_RUN_CARD.json) and [current record](./CURRENT_STUDY_RECORD.json) identify the selected obligations. Native execution here means the named local library/state, not validation of a provider product.

## Step 1 — technology–problem extension and correspondence

Question: **Which typed receiver obligations are supported by strict local schema validation, and which authority/truth questions require other mechanisms?**

Human/process contexts and actual parameter changes are explicit in all 10 registered [scenarios](./CURRENT_RUN_CARD.json). The receiver receives permitted requests, configuration and source/resource observations; the evaluator retains expected labels, truth and target state. Scenario/policy simulation-kind markers remain visible to these local models; there is no claim of blind generated-world search or hostile-code isolation.

Pydantic supplies strict typed validation; JSON Schema supplies declared structure constraints. OpenAI documents structured generation, refusal/incomplete paths and the possibility of semantic mistakes. Only the local receiver/typing composition is executed here.

The correspondence is local: task→request/effect, scope→tenant/resource, qualification→current permitted observations, closure→the actual response/receipt/disposition and useful window. It is **not a proved R01/native-product isomorphism**. R01 probability/cost laws, rates and all-policy bounds do not transfer. Any claimed transfer requires a separate admissible relation with preserved inputs, actions, information, cost and acceptance. These conditions are the limits of this Step 1 finding.

## Step 2 — non-isomorphic/additional mechanisms

| Mechanism | Producer/authority | Measured burden and falsifier |
|---|---|---|
| Strict selected schema | Application schema owner; Pydantic executes validation | Strict BaseModel validation; S02/S03/S04 reject type/extra/missing fields |
| Duplicate-member guard | Receiving parser owner | Own JSON pre-parser, separate from Pydantic; S05 duplicate is rejected |
| Tenant/current permission/limit | Application/resource authority supplies policy | SQLite policy/effect boundary; S06 and S10 reject wrong tenant/revocation |
| Refusal/truncation fallback | Task owner admits recorded deferment | Authored wire fixtures; S08/S09 record M, not an actual LLM/API observation |
| Semantic source truth | Policy/source owner; evaluator holds independent truth | S07 remains schema-valid P under a false trusted limit; syntax validation cannot prove correctness |

Composition: Strict schema checks and the duplicate-member pre-parser cover different faults. A valid schema still needs tenant/authority/truth checks; a false trusted limit is retained as P. Different mechanisms may be supplied by conventional application logic. No extra-architecture advantage is presumed; a competent conventional peer is credited fully.

## Sources and boundaries

- [JSON Schema object requirements](https://json-schema.org/understanding-json-schema/reference/object) — primary reference for selected semantics; reviewed 2026-10-07; no named-product execution.
- [Pydantic strict mode](https://pydantic.dev/docs/validation/latest/concepts/strict_mode/) — primary reference for selected semantics; reviewed 2026-10-07; no named-product execution.
- [OpenAI Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs) — primary reference for selected semantics; reviewed 2026-10-07; no named-product execution.

actual Pydantic2.13.5 strict selected BaseModel plus JSON duplicate-member pre-parser and SQLite receiving state; no LLM/API generation or full JSON-Schema conformance test. Schema-valid content can be wrong, unauthorized or inapplicable. The cases do not measure model schema-adherence probabilities, language quality or real API latency.
