## Annex Evidence

### E.1 — Run record and measurements

For each executed branch retain: scenario and version; technology/model/configuration versions; R0/R1/R2 designation; fixed inputs and authority regime; injected change and its observable signal; resources and deadline; gate evidence and reasons; timestamps; actual action; permitted outcome; disagreement and missing evidence; and the total cost of review, waiting, messages, queries and computation. Retain the defender's configuration and successful counterexamples as well as failures.

The applicable measurements are inherited from the six quality plans:

| Measurement group | What must be observable |
|---|---|
| Evidence preservation | Source retrievability, retained decision-relevant qualifications, compression losses, scope/freshness and dependence through each material handoff |
| Decision discrimination | Unsupported continuation, unnecessary restriction, correlated-evidence mistakes, false agreement and incorrect promotion of a narrow claim |
| Change handling | Material-change detection, false alarms, time to reassess the affected dependency, stale decisions and check-to-act changes |
| Composition | Conflicting actions or scopes, campaign membership, inherited authority, veto scope/expiry and actual aggregate effect |
| Capacity and timing | Review demand versus available capacity, unresolved waiting, response margin, useful information yield and deadline success |
| Outcome and burden | The real downstream effect, propagation reach and delay, oscillation, resource use, human work and privacy/disclosure burden where applicable |

Before a run, define each selected metric's numerator, denominator, threshold and measurement window. A qualitative reconstruction does not supply numeric rates. Record **PASS**, **FAIL**, **NOT EVALUABLE**, **NOT EXERCISED** or a justified **NOT APPLICABLE** at the relevant granularity; an explicit limited conclusion must state exactly what was established. These recording labels do not define a runtime protocol.

### E.2 — Evidence classes and claim limits

| Evidence | What it supports | What it does not support |
|---|---|---|
| Constructed scenario | An inspectable failure scenario with fixed relationships | A claim that a named customer experienced the story |
| Official product description | Availability and scope of documented facilities at the recorded version | Execution of this case or the configuration's end-to-end sufficiency |
| Documentary implementation walkthrough | A reviewable path through a declared configuration | Measured failure frequency or a deployed benchmark result |
| Bounded diagnostic or symbolic exercise | Only its modeled states, assumptions and recorded observations | Every concurrent execution, product profile or family extension |
| Instrumented product reproduction | The particular pinned branch and its observed result | Untested products, configurations, workloads or future changes |

The nine profiles here remain documentary. The 27 profile/route positions are documentary, not product runs. This edition reports no new product experiment.

### E.3 — Existing functions and primary references

The duplication check asks whether existing functions **jointly meet the scenario criteria at the receiving decision**. It does not assert that provenance, context-sensitive authorization, freshness or change handling are absent from other work.

| Existing function | Primary reference | Question retained by this case |
|---|---|---|
| Workload identity | [SPIFFE concepts](https://spiffe.io/docs/latest/spiffe-about/overview/) | Which decision-relevant conclusions beyond attributed identity are supported? |
| Attestation and freshness | [RATS architecture, RFC 9334](https://www.rfc-editor.org/rfc/rfc9334.html) | Does the actual receiving decision preserve relevant dependencies and validity through use? Freshness and race conditions are already recognized subjects. |
| Token exchange | [RFC 8693](https://www.rfc-editor.org/rfc/rfc8693.html) | What current application authority and aggregate effect does the exchanged credential cover? Do not equate exchange alone with a complete downstream decision model. |
| Threat information and relationships | [STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html) | How does the implementation use represented provenance and relationships to avoid correlated evidence at this decision? Do not claim STIX cannot represent relationships. |
| Agent interaction | [A2A specification](https://a2a-protocol.org/latest/specification/); [MCP architecture](https://modelcontextprotocol.io/specification/2025-11-25/architecture) | Which application-level gate evidence survives the actual interaction? No claim of protocol-level impossibility is made. |
| Risk management | [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) | What concrete branch evidence demonstrates that the declared risk controls meet these acceptance conditions? |

These are overlapping references, not an exhaustive survey or proof of unique coverage. “Not already solved” remains a configuration- and criterion-specific proposition requiring evidence, not a premise of the case.

### E.4 — Product-profile source entry points

The technology profiles record dated source reviews. Links below identify the primary documentation for reproducing the profiles; mutable documentation must be pinned again for an actual product test.

- Microsoft: [Agent 365 security](https://learn.microsoft.com/en-us/security/security-for-ai/agent-365-security).
- LangGraph: [Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts).
- FIWARE: [Catalogue](https://fiware.org/catalogue/).
- AWS: [IoT TwinMaker](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/what-is-twinmaker.html).
- OpenAI: [Agents API introduction](https://openai.com/index/introducing-the-agents-api/).
- Anthropic: [Agent SDK hooks](https://code.claude.com/docs/en/agent-sdk/hooks).
- Stripe: [Radar rule reference](https://docs.stripe.com/radar/rules/reference).
- AWS: [RDS immediate versus scheduled changes](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ModifyInstance.ApplyImmediately.html).
- TEMS: [Trial 7, rights across systems](https://tems-dataspace.eu/tems-trial-7-how-rights-travel-across-systems/).


### E.5 — Full common metric definitions

Select the applicable measures before the run. `U` means the declared evidence/observation scope, not a claim to exhaust all relevant reality. “Posture” means the recorded operational decision or disposition, including a bounded hold. Report numerator, denominator, branch, configuration, observation interval and threshold; a zero denominator is not a perfect score. Keep unknown measurements visible. Do not pool heterogeneous branches to hide a material failure.

The common outcome vector is: **false continuation; false containment; correctness of the permitted decision; deadline success; handoff integrity; actual downstream effect; total decision burden**.

#### Decision evidence

**Local determinacy margin:** declared determined evidence/conditions relative to the threshold for the decision; report with evidence and sample coverage inside U. **Explicit-indeterminate rate:** outputs preserving INDETERMINATE/UNKNOWN where the branch oracle requires it ÷ applicable branches. **Material-break recall:** oracle-declared material breaks exposed with affected basis ÷ oracle-declared material-break branches. **Material-break precision:** exposed material breaks confirmed by oracle ÷ exposed material-break alerts. **False-continuation rate:** CONTINUE/PASS after a break requiring requalification or containment ÷ applicable break branches. **Time in HELD/unresolved state** and **human-capacity binding/escalation demand** are reported with each branch.

#### Scope and residual

**Local-to-global confidence inflation:** downstream confidence/closure beyond the declared U and scope, reported against the branch oracle. **Wrong-domain or systemic-closure rate:** unsupported system-wide closure from local/insufficiently scoped determination ÷ applicable composition branches. **Residual-scope preservation:** required unresolved, scope and residual fields retained ÷ cases requiring them. **Known versus unmeasured dependencies** and **inherited-indeterminacy detection rate** are reported for each receiving decision.

#### Source independence and composition

**Source diversity and primary-source retrievability:** independent source routes and retrievable primary sources ÷ required material source routes. **Correlated-evidence error rate:** closures treating duplicated/correlated evidence as independent corroboration ÷ designated correlated-source branches. **Compression exposure:** number and criticality of downstream decisions dependent on one compressed source; propagation depth of compressed closures. **Systemic decision error** and **false confidence from recursive closure reuse** are reported against the oracle.

#### Handoff integrity

**Handoff integrity:** required `scope, provenance/freshness, dependency, unresolved state, capacity, authority, expiry` fields delivered and interpretable at receiver ÷ required fields. **Qualification-loss rate:** qualified fields absent, flattened or contradicted without declared requalification ÷ handoffs. **Information retained/discarded at inter-agent boundary:** required decision-relevant fields retained ÷ required fields, with **latency, bandwidth, privacy and disclosure cost**. **Targeted re-entry precision/recall:** correctly reopened assumptions ÷ reopened assumptions; correctly reopened assumptions ÷ oracle-invalidated assumptions.

#### Material change and freshness

**Estimated U-invalidation rate:** material changes invalidating a declared U/window ÷ relevant observation intervals. **Freshness/staleness:** age of each material source at determination and number of stale inputs relied on ÷ required material inputs. **Churn:** participant/dependency changes and window changes by domain per period. **Requalification latency** and **missed material contextual changes from Type-2 under-observation** are reported against fixed observation/verification budget. **Containment frequency and recovery success** distinguish a bounded response from repeated unresolved escalation.

#### Time, capacity and burden

**Window breadth and freshness by domain:** observation scope and source age for each decision, compared with sensitivity/consequence/reversibility. **Deadline-pass rate:** permitted posture with reachable authorized response before deadline ÷ applicable runs. **Remaining response margin:** deadline minus posture time. **Decision-relevant evidence yield:** acquisitions/reviews changing justified posture or action set ÷ total acquisitions/reviews. **Total decision burden:** compute, tokens, bandwidth, tool, communication, waiting, reviewer, privacy/disclosure and response cost per run. **Risk/sensitivity mismatch:** qualified-window assumptions inconsistent with observed downstream consequence ÷ applicable runs. **Marginal decision value:** additional decision-relevant changes ÷ incremental observation and assessment cost.

#### Response and legitimate-activity measures

- **Posture correctness:** runs whose posture is within the branch oracle’s permitted set ÷ applicable runs.
- **Authority-field completeness:** handoffs containing owner, authority, scope, freshness, dependency and expiry fields ÷ handoffs requiring them.
- **Authorized-response compliance:** non-null actions within the declared authority/action library ÷ non-null actions.
- **Reversibility/containment compliance:** applicable responses meeting their declared bound ÷ applicable responses.
- **False-positive response cost:** cost of unnecessary non-null actions ÷ valid-continuity runs.

**False-containment rate:** control branches in which permitted legitimate activity is unnecessarily prevented ÷ applicable legitimate-activity control branches. Report timing and burden as well as counts.

#### Cross-cutting trajectory and stress measures

Use these only when the corresponding mechanism is injected or observable.

| Measure | Calculation |
|---|---|
| **Type-1→Type-2 forced-closure rate** | Runs in which acknowledged unresolved state is closed by timeout, default, queue pressure or approval without new qualifying evidence ÷ runs reaching the declared Type-1 boundary. |
| **Type-2→Type-1 reopened-loop rate** | Invalidated false closures that enter repeated HOLD/search because discarded material qualification cannot be reconstructed ÷ invalidated Type-2 closures. |
| **False-convergence rate** | Runs in which multiple actors produce the same unsupported closure from correlated, imitated or recursively reused evidence ÷ designated convergence branches. |
| **Incompatible-posture exposure** | Duration and consequence-weighted extent of incompatible postures over the same material decision or resource-time segment. |
| **Posture oscillation rate** | Reversals among continue/requalify/contain/HOLD within the decision horizon, reported with dwell time and the share occurring without new material evidence. |
| **Qualifier-saturation burden** | Immaterial, duplicated, stale or expired qualifiers and rechecks ÷ all transmitted qualifiers/rechecks, with latency, reviewer load and missed-deadline effect. |
| **Defensive-UNKNOWN effect** | Unsupported or strategically emitted UNKNOWNs that transfer responsibility or trigger HOLD/containment ÷ designated incentive-stress branches; report whether the path remains Type 1 or is later forced into Type 2. |
| **Injected-doubt effect** | False HOLD/containment or posture reversal caused by poisoned freshness, dependency or uncertainty signals ÷ designated adversarial branches; report rejection/recovery time. |
| **Cascade latency and reach** | Time from first material qualification loss to dependent closure reversal, plus affected downstream scopes/decisions. |

A high `UNKNOWN` rate is not by itself failure, and a low one is not by itself success. The branch oracle, materiality, incentives, scope, owner, response window and downstream effect determine whether uncertainty was correctly preserved, defensively inflated or silently suppressed.


### E.6 — Complete run record

| Record group | Required entries |
|---|---|
| Claim and trial design | Case acceptance, HC, HR, HS or selected H1–H6; implementation route R0/R1/R2; causal condition A–D where applicable; response candidate/component comparison where applicable; declared candidate/intervention domain and family-admission record. Keep these identifiers separate. |
| Identity and freeze | Run ID; scenario/variant; selected R0/R1/R2; technology/model/API versions; code/configuration hashes; date; tester; independent assessor if any. |
| Decision and authority | Receiving decision and owner; grantor, grantee, scope, purpose, expiry and governing regime; legitimate action owners; source-of-truth records; distinction between simulated and real components. |
| Fixture | Fixed facts and snapshots; source lineage; input/event order; independent oracle; permitted actions; materiality/freshness thresholds; capacity; deadline; stop and fallback rules. |
| R1 correction / R2 intervention | Baseline gate/control evidence; frozen safeguards and generic adaptation; admitted change fields, values, timing and observable signal; unchanged/harmless-change comparison; no post-outcome engineering. |
| Per-gate trace | Gate ID; input and versions; evidence available at the time; control present/invoked status; result/reason; next step; actual owner/action/effect; timestamp; uncertainty and unexercised fields. |
| Measurements | Declared numerators, denominators, thresholds and intervals; false continuation/containment; timing; source/review/query/token/resource burden; actual business outcome. |
| Hypothesis conclusion | Separate from the implementation result: support within scope, rejected candidate, bounded refutation, not tested or inconclusive, with the claim-specific reason and causal/response evidence. A case FAIL may support an admitted causal witness; a case PASS does not establish every hypothesis. |
| Conclusion | Scope-specific PASS/FAIL/NOT EVALUABLE/NOT EXERCISED/justified NOT APPLICABLE; disagreements; successful defences; excluded interpretations; reproduction instructions. |

For stochastic systems, include the predeclared repetitions, pairing/randomization, seeds when available, confidence/uncertainty method and minimum relevant effect. A documentary expectation cannot be entered as an observed result. Register stronger defender configurations before their outcomes are known; failure of a weaker configuration cannot substitute for testing them.

### E.7 — Source boundary and publication status

This is a **contributor use-case draft for review**, not an adopted standard or an implementation specification. The short narratives, full scenarios, technology profiles and family mappings retain their distinct roles. Scenario facts are synthetic unless explicitly attributed; external incidents support only the bounded analogy stated alongside each source. Public documentation dates and version limits are retained in the relevant profiles. They do not establish present availability in every deployment or measured sufficiency.

The case and all necessary technical annexes are contained in this directory and listed in the root README. The separate submission form maps the contribution into the FG-TIDA proposal fields. Figures and the four S5 JSON design skeletons are supplied under `assets/` and `fixtures/` at the package root; the full JSON is also printed in T08. No unpublished architecture, historical preservation archive or later specification is required to interpret the case. A real-world run must declare its own applicable legal regime and operating permissions; this synthetic fixture does not confer them.
