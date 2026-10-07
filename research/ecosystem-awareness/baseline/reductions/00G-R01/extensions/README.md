# DDS technology extensions — study home

<!-- DDS terminology revision 1 (2026-10-07): Stage A/B/C only; source scientific version and evidence unchanged. -->

Version0.2 ·6 October2026.

This is the home for technology-extension documentation and its DDS records. The [DDS Canonical Method Index](../../../../DDS_CANONICAL_METHOD_INDEX_v0.1.md) is the single programme-wide method entry point. The current extension leaves primarily instantiate **DDS Stage A — Specification Discovery**—often as Simplified Stage A profiles—because their object under test is a bounded mechanism/configuration specification rather than an architecture realization or deployed product. Each leaf identifies its base/configuration, Stage1 correspondence/isomorphism profile, Stage2 additional mechanisms/composition, scenarios, sources, Cost/Risk/Effectiveness, conditional Business Value, evidence, acceptance, limits and scoped closure. Folder placement under R01 does not make another base isomorphic to R01 or import R01's all-policy bounds. A later successor that verifies a frozen architecture package belongs to Stage B; a pinned implementation validated against observed Challenge effects belongs to Stage C.

**Historical frozen-record rule.** Run Cards, FREEZE files and RESULTS created on 6 October may preserve the then-current field/path `canonical_DDS_profile = DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md` and wording such as “single canonical DDS technical profile”. Those evidence-bearing records are intentionally not rewritten. The [DDS Index](../../../../DDS_CANONICAL_METHOD_INDEX_v0.1.md) now supplies their current interpretation: the old path is Stage A, while the complete method is Index + Stages A/B/C.

[Drive extensions home](https://drive.google.com/drive/folders/1WKUyHAPmqAKydY4SunPOMGr-SOGjpTPs) · [Native catalogue](https://docs.google.com/document/d/1skJnoww99FlHNPuV7LCM2Z5vsJ3rFHovgM9r7ckn8Gg/edit) · [Machine-readable catalogue](./CATALOGUE_2026-10-06.json) · [Source custody](./SOURCE_CUSTODY_2026-10-06.json) · [Primary-source register](./COMMON_TECHNOLOGY_SOURCES_2026-10-06.json).

## First practical common-component series

These are common architectural families selected for useful tractable questions, not a statistical ranking of adoption. Each was prepared and executed serially in this batch.

|Technology / extension|Current scoped DDS|Cases / checks|Actual evidence and ceiling|
|---|---|---|---|
|[RAG retrieval and evidence admission](./rag/EXTENSION.md)|[Report](./rag/DDS_STUDY.md)|8 /16|actual SQLite FTS5; authored deterministic extraction/admission, generator not executed|
|[OAuth/OIDC identity and local resource admission](./oauth-oidc/EXTENSION.md)|[Report](./oauth-oidc/DDS_STUDY.md)|11 /22|actual RSA2048/RS256 + local SQLite selected-profile effect; native flow not executed|
|[MCP selected tool-call admission](./mcp-tool-calling/EXTENSION.md)|[Report](./mcp-tool-calling/DDS_STUDY.md)|9 /18|actual serialized request parser/local SQLite effect; official SDK/transport/full conformance absent|
|[SQL transactions and resource idempotency](./sql-transactions-idempotency/EXTENSION.md)|[Report](./sql-transactions-idempotency/DDS_STUDY.md)|9 /18|actual SQLite transactions/two connections/second local file; distributed products not executed|
|[Durable workflow/retry and useful closure](./durable-workflows-retries/EXTENSION.md)|[Report](./durable-workflows-retries/DDS_STUDY.md)|9 /20|actual SQLite persisted model/restart, same-contract M witness; Temporal native not executed|

Every leaf contains EXTENSION.md, DDS_STUDY.md, RUN_CARD.json, FREEZE.json, study.py, actual runs and its sole owning README_VNext.md. Current selected outcomes are retained, including source-falsehood, cross-domain-effect and duplicate-effect P counterexamples. All registered expectations pass, including expected negatives; this is not every mission or deployment accepted. Different predicates/denominators are not pooled into a success rate.

The RAG generation model and native OAuth/MCP/Temporal/provider integrations are unexecuted. Actual local SQLite/RSA/parsing operations and authored model behavior are explicitly distinguished. The RAG preflight/source-view/evaluator corrections retain all predecessors and do not regrade their results.

## Existing extensions and studies — preserved, now also housed here

|Existing object|Documentation / evidence route|Actual scope|
|---|---|---|
|Human Escalation / Whispering|[Extension](./HUMAN_ESCALATION_WHISPERING.md), [current report](./dds-study-completion-v0.1/HEW_COMPLETION_REPORT.md), [frozen local package](./dds-hew-v0.1/TECHNICAL_REPORT.md)|Analytical/virtual source and finite SQLite companion; no real human/native campaign|
|STAMP/STPA|[Extension](./STAMP_STPA_EXTENSION.md), [current report](./dds-study-completion-v0.1/STPA_COMPLETION_REPORT.md), [exercise](./independent-dds-exercises-v0.1/stamp-stpa/EXERCISE_REPORT.md)|Derived finite control model; no industrial plant/method-completeness certificate|
|SPIFFE/SPIRE|[Extension](./SPIFFE_SPIRE_EXTENSION.md), [current report](./dds-study-completion-v0.1/SPIFFE_COMPLETION_REPORT.md), [exercise](./independent-dds-exercises-v0.1/spiffe-jwt/EXERCISE_REPORT.md)|Selected actual RSA/JWT fixture, no native SPIRE/full conformance|
|RATS|[Extension](./RATS_EXTENSION.md), [current report](./dds-study-completion-v0.1/RATS_COMPLETION_REPORT.md), [exercise](./independent-dds-exercises-v0.1/rats-jws/EXERCISE_REPORT.md)|Local hash/JWS appraisal; simulated application confirmation is not external actuation|
|Fencing/confused deputy|[Extension](./FENCING_CONFUSED_DEPUTY_EXTENSION.md), [HEW supporting analytical tests](./dds-hew-v0.1/prior-analytical/fencing_deputy_results_v0.1_2026-10-06.json)|Supporting analytical/local mechanisms, not another native independent DDS|
|Hugging Face|[Existing case record](./hugging-face/README.md)|Historical motivation with synthetic modules; historical causation/native admission unestablished as stated|
|Infoblox/DNS-AID|[Existing case record](./infoblox/README.md)|Proposed technological correspondence and local witness; native integration unestablished|
|Constructed H/L/W family|[Existing family](./family/README.md), [kernel/E1–E7](./family/KERNEL_AND_PROOF.md)|Constructed reference framework, not a third vendor technology|

[Unchanged Drive copy of the four-study completion document](https://docs.google.com/document/d/1YbshiBIQvNqyORGptsCX84E5xIOlOs7yzA-wUqqRQ0c/edit) is inside existing-studies. Originals in feasibility remain untouched pinned custody; the92 source replicas are recorded by origin/path/blob. Their older own VNext files are replicas of the same historical reviews, not newly independent reviews or canonical methods. Five routing files link shared base sources at their immutable origin instead of copying/replacing proof authority or third-party received annexes. Excluded contents are not republished.

The [existing R01 extension protocol](./TECHNOLOGY_EXTENSION_PROTOCOL.md) remains R01-specific authority. [Historical three-case criteria](./CRITERIA_AND_AUDIT.md) and [methodological foundations](./METHODOLOGICAL_FOUNDATIONS.md) preserve their own scope/versions; they do not retrospectively grade this series or every new technology.

## Coverage, value, delivery and continuation

Each scoped report records supported useful conditions, failure/residual risk, practical value limits, source validity and measured versus unscored costs. The [common delivery map](./DELIVERY_SCOPE_2026-10-06.json) retains the six programme categories. This is completed partial research scope with documentation, local tests and custody, not a commissioned complete report package, recognition, DOI, native product acceptance or international submission. A future reduced study can be fully delivered within an agreed scope; omitted dimensions are not zero or passed controls.

Minimum legitimate M is defined only where actually admitted. Ø/P are not universal EA Type1/2 labels; the workflow profile executes a specific same-contract M witness. Optional optimal-work/rework and empirical superiority are unscored. A strong conventional solution receives full credit; no study is required to make its technology win.

Next candidate families are caching/TTL, queues/redelivery, structured LLM outputs and observability/response. They are **not prepared or executed in this batch**. Continuing them requires the next bounded question/source/configuration, the same two stages and prospective tests where feasible; it does not add a universal battery or a new commercial promise. [Owning catalogue review](./README_VNext.md).


## Current-source reporting clarification0.2

The current sole DDS source 09b8fe09082f15612114ebe0fd3be8418be7a061 adds blind/private-map, minimum-work, M-admission and Type1/Type2 reporting surfaces. [Current compatibility record](./CURRENT_DDS_COMPATIBILITY_2026-10-06.json) and one coverage sidecar per new leaf declare these unscored/not established as estimates. The workflow M witness is descriptive local evidence; complete current-rule eligibility/physical budget admission is not established. No blind/population estimate or old score upgrade. Documentation0.1 preserved; cards/code/freezes/runs stay unchanged.
