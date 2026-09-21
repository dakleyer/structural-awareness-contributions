# Canonical Architecture Benchmark and Reference-Scenario Evidence — Ecosystem Awareness

> **Sole current benchmark in the canonical reader route.** This document integrates the EA differential hypotheses, the fair architecture-comparison protocol, the industry benchmark landscape and empirical corroboration of the two reference failure scenarios. It does not report a completed EA experiment, rank products, prove novelty or claim that any cited incident was caused by the absence of EA.

**Version:** 0.2 — 17 September 2026  
**Status:** public working benchmark and evidence register; hypotheses and test design, not validated superiority.  
**Canonical dependencies:** [00 — Requirements: S1–S14, T1–T4, H1–H6 and KPIs](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md), [00 — Architecture Topology](./00_CANONICAL_ARCHITECTURE_TOPOLOGY.md), [00E — 100-million-token reference scenario](./00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md) and [00F — smart-city mobility reference scenario](./00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.1.md).

This file supersedes, in the canonical reading route, the separate [market/industry benchmark v0.1](./00D_MARKET_AND_INDUSTRY_BENCHMARK_RESEARCH_v0.1.md) and [EA differential-hypothesis working file](./07_EA_CANDIDATE_DIFFERENTIAL_HYPOTHESES_v0.5_REVIEWED_WORKING.md). Those files remain preserved as non-canonical provenance; the controlled v0.4 benchmark is unchanged.

## 1. Reading key and terminology

The corpus now uses three different terms deliberately:

| Term | Meaning | Example |
| --- | --- | --- |
| **Failure type** | The epistemic error class defined by the topology: Condition Type 0, Failure Type 1 or Failure Type 2. | Type 1 indefinite determination; Type 2 false closure. |
| **Failure mechanism** | The causal operation by which a type can arise or propagate. | Lossy many-to-one handoff, stale context, correlated-source reuse or incompatible composition. |
| **Reference failure scenario** | A complete, fictional but testable system story that combines mechanisms, gates and observable consequences. | 00E or 00F. |

“Failure mode” remains valid engineering vocabulary for an individual mechanism, but it is no longer the canonical name of the complete 00E/00F cases. This prevents a scenario from being confused with Type 0/1/2.

Earlier notes sometimes called the four differential propositions `CH1`–`CH4`. Their canonical identifiers are **EA-H1–EA-H4**. They are not the foundational H1–H6 in the requirements document and not the preserved non-canonical `C-H1`–`C-H5` candidate tests.

## 2. Benchmark question and claim boundary

The benchmark asks two separate questions:

1. **Requirement coverage:** can a named, configured architecture satisfy the applicable S#, T#, H# and KPI gates under frozen facts, authority, resources and deadlines?
2. **EA differential:** under those same conditions, does an EA-profiled architecture improve the declared error–resource frontier, or preserve the same result with a simpler accountable semantic composition, relative to a strong peer?

The benchmark does **not** ask whether a platform has agents, workflows, guardrails, observability, human approval or a digital twin. Those are useful capabilities. It asks whether the composed implementation preserves and requalifies the decision basis across scope, residual, dependency, authority, capacity and time.

The present evidence supports the **plausibility of the mechanisms and the need for a comparative test**. It does not establish that EA passes, that every standard control architecture fails, or that the literal 100-million-token outcome has occurred in a documented company.

## 3. Evidence grades

Every external source is used at one of four grades. A stronger grade does not automatically support a broader claim.

| Grade | Evidence kind | Permitted inference |
| --- | --- | --- |
| **E1 — formal/analytical** | Information theory, architecture specification or formal result. | A mechanism is structurally possible or a contract has a documented boundary. |
| **E2 — controlled empirical** | Laboratory, field experiment or reproducible benchmark. | The measured effect occurred under the stated experimental conditions. |
| **E3 — investigated occurrence** | Official accident, incident or outage investigation. | The report's documented factors contributed in that real occurrence. |
| **E4 — market/standard evidence** | Official standard, public product documentation or benchmark definition. | The named scope/capability is documented; absence outside that scope is not presumed. |

No analogy is allowed to cross evidence grades silently. In particular, an E3 event can corroborate a failure mechanism without proving that 00E or 00F will occur, and no source below proves EA effectiveness.

## 4. Comparator arms and fairness contract

All arms receive the same frozen facts, task, action library, source access, authority, compute/token ceiling, communication budget, human capacity and deadline.

| Arm | Configuration | Purpose |
| --- | --- | --- |
| **B0 — ordinary implementation** | Capable models/automation with normal retrieval, workflows, tools and logging. | Establish the non-strawman baseline. |
| **B1 — strong conventional implementation** | B0 plus provenance where available, policy/security controls, state/checkpoints, retries, fallback, human approval, tracing, evaluation and resource limits. | Test whether competent implementation already satisfies the requirements. |
| **B2 — strong interoperable control peer** | B1 plus relevant protocol/control-plane features, identity/access control, explicit handoff configuration and cross-system observability. | Test what strong control and transport contribute without assuming decision-sufficiency semantics. |
| **B3 — EA-profiled peer** | The same resources and underlying technology as B2, plus the minimum semantics and gates needed to instantiate the EA candidate. | Test EA-H1–EA-H4 without buying advantage through extra evidence, authority, time or people. |

A capability implemented in B1/B2 counts fully even if its vendor does not call it EA. If a peer reproduces the required behaviour with lower burden, that is a negative EA result. Added agents, review, context or time are charged to the common burden ledger.

### 4.1 Current scenario/technology fixtures

| Reference scenario | Current technology profiles | Comparison already specified by the annexes | Benchmark boundary |
| --- | --- | --- | --- |
| **00E — 100 million tokens** | [Microsoft Agent 365](./00E_A01_MICROSOFT_AGENT_365_IMPLEMENTATION_PROFILE_v0.1.md); [LangGraph/LangSmith](./00E_A02_LANGGRAPH_LANGSMITH_IMPLEMENTATION_PROFILE_v0.1.md) | Standard implementation → excellent implementation → excellent implementation under latent regime change → possible EA-qualified profile. | The parent event, resources and gates are frozen; the products are substrates, not alleged causes. |
| **00F — smart-city mobility divergence** | [FIWARE NGSI-LD / Orion-LD](./00F_A01_FIWARE_NGSI_LD_IMPLEMENTATION_PROFILE_v0.1.md); [AWS IoT TwinMaker / IoT Core](./00F_A02_AWS_IOT_TWINMAKER_CORE_IMPLEMENTATION_PROFILE_v0.1.md) | Standard implementation → top governed/monitored implementation → top implementation under hidden or gradual pivot → possible EA-qualified profile. | Safety authority and actuation remain with legitimate city/fleet/vehicle systems; the benchmark tests qualification and composition. |

These profiles are design analyses, not measured B0–B3 results. A future execution must map their exact configurations to the arms above and may find that a top native implementation closes some or all of the proposed gap.

## 5. What the industry already provides

The benchmark is a complement test, not an assertion that existing systems have no controls.

| Layer | Documented strength | Boundary that must be tested rather than assumed |
| --- | --- | --- |
| Foundation-model and tool agents | Planning, retrieval, reasoning, tool use and escalation. | Task completion does not establish continuing validity of the decision basis. |
| Agent runtimes/orchestration | State, routing, checkpoints, retries, interrupts, human review and traces. | Execution flow does not by itself define material external change, residual or a sufficient downstream handoff. |
| Control planes/gateways | Identity, authorization, policy enforcement, quotas, logging and operational monitoring. | Access and execution control do not by themselves establish semantic sufficiency or current applicability of evidence. |
| MCP/A2A or equivalent transport | Controlled resource/tool access and agent/task/message/artifact exchange. | Transport and extensibility do not by themselves define decision scope, structural residual, response legitimacy or requalification. An implementation may add them. |
| Governance and risk frameworks | Ownership, documentation, provenance, monitoring, incident response and human oversight expectations. | Governance requirements do not automatically create a runtime determination for one action after a material frame change. |

This boundary is configuration-specific. The benchmark must inspect the implemented payloads, policies and traces and must not infer capability or absence from marketing labels.

### 5.1 Concrete scope example: guardrails are placed controls, not a system-wide sufficiency claim

The current OpenAI Agents SDK documentation illustrates the distinction without implying a product deficiency. Input guardrails run for the first agent in a chain and output guardrails for the final-output agent. Tool guardrails can wrap guarded function-tool invocations, while handoffs use a different pipeline; hosted and built-in execution tools do not use the function-tool guardrail pipeline. Blocking and parallel guardrail execution also have different token/tool side-effect timing.

Those are explicit, useful workflow boundaries. A competent implementation can add checks at the needed seams. The benchmark consequence is simply that the evaluator must verify the actual chain, tools, handoffs and execution mode; the presence of the word “guardrail” is not by itself evidence that scope, residual, dependency and validity survive every transition.

## 6. EA-H1–EA-H4: the differential hypotheses

The four propositions below conserve the prior reviewed wording and remain hypotheses to falsify.

| EA-specific hypothesis | Conserved architecture elements and EA functions | Plausible positive effect | Decisive falsifier |
| --- | --- | --- | --- |
| **EA-H1 — scoped non-fungible determination** | A/B/C/D; F3/F4/F5/F6/F8. Preserve four-position in/out-window state, source dependence and domain-specific residual; do not average unrelated claims into a global verdict. | Fewer apparently supported decisions created by duplicated evidence, cross-domain compensation or local-to-global promotion; clearer affected-domain correction. | A strong peer reaches the same decisions and explanatory trace without an equivalent composition layer or extra burden. |
| **EA-H2 — proportionate window requalification** | E and APQ consequence; F1/F2/F7/F9. Qualify `W(d,t)` to consequence, sensitivity, reversibility, residual tolerance, acquisition burden, effective capacity and remaining response time. | Fewer stale-frame commitments at high exposure and/or less low-value acquisition/review at low exposure, without losing useful response time. | A fixed broad/narrow or strong value-of-information/source-lineage peer reaches an equal or better decision/resource frontier on matched facts and budgets. |
| **EA-H3 — orthogonal assessment and posture** | F; F5/F6/F7/F8. Keep epistemic management condition and residual distinct from Normal/Containment/Migration preparation and independent actuation authority. | Preserve warranted normal operation under bounded residual; avoid both premature blanket holds and unjustified continuation after a material frame change. | A peer separates the conditions with equal correctness, timeliness and burden; or EA adds indecision without reducing either error. |
| **EA-H4 — interoperable re-entry** | G; F4/F8/F9 with F1/F2/F5/F6. Carry scope, window, inherited uncertainty, dependency, capacity and validity through transport-neutral handoff; reopen only failed assumptions. | Less downstream loss of qualification and fewer indiscriminate reruns/escalations; more traceable return-to-operation decisions. | A2A/MCP/attestation/UQ/tracing composition reproduces the handoff and targeted re-entry with no extra semantics or materially simpler implementation. |

The highest-value coupled test remains **EA-H1 + EA-H2**: preventing false systemic closure matters operationally only if the system can identify worthwhile requalification before the response window closes. EA-H3 tests whether uncertainty is managed without turning into a universal halt; EA-H4 tests whether qualification survives handoff and return.

## 7. EA hypotheses against the canonical requirement language

| Differential | Primary S# surface | T# that must be satisfied | Foundational H# and KPI families used as evidence |
| --- | --- | --- | --- |
| **EA-H1** | S5, S9, S11, S14 | T2, T4 | H2/H3/H4: wrong-domain/systemic closure, correlated-evidence error, residual-scope preservation, handoff integrity. |
| **EA-H2** | S3, S4, S10, S14 | T1, T4 | H1/H5/H6: material-break recall/precision, false continuation, freshness, requalification latency, deadline pass, evidence yield, total burden. |
| **EA-H3** | S1, S3, S4, S5, S14 | T2, T3, T4 | H1/H2/H6: explicit-indeterminate rate, posture correctness, false continuation/containment, authorized-response compliance, human-capacity binding, response margin. |
| **EA-H4** | S6, S8, S9, S11, S12, S13, S14 | T2, T4 | H2/H4/H5: qualification-loss rate, required-field completeness, inherited-indeterminacy detection, targeted re-entry precision/recall, recovery success. |

A KPI pass is evidence for the declared scope; it does not prove an S# challenge solved in general. Good results in one domain cannot compensate for failure in another domain.

## 8. Required benchmark branches

| Branch | Condition | Failure exposed | Minimum conforming behaviour |
| --- | --- | --- | --- |
| **C1 — valid continuity** | The declared basis remains valid. | Unnecessary alarms, review or containment. | Continue under stated qualifications without manufacturing a break. |
| **C2 — observed material change** | A dependency, source, authority, capacity, cost or operating condition visibly changes. | Stale-frame continuation. | Identify affected scope and select an authorized bounded posture. |
| **C3 — insufficiently established state** | Evidence is stale, conflicting, unavailable or dependent; no conclusive change is observed. | UNKNOWN collapsed to PASS or indefinite escalation. | Preserve unresolved state and select finite requalification, fallback, hold or no commitment. |
| **C4 — adversarial/poisoned evidence** | External content attempts to manipulate action or authority. | Tool/data hijack or improper permission expansion. | Preserve security testing without treating a security signal as proof of the whole decision basis. |
| **C5 — capacity/deadline failure** | Reviewer, tool, network or rollback capacity cannot meet the useful response window. | Nominal HITL treated as effective control. | Apply the declared authorized fallback; delay is not permission. |
| **C6 — cross-domain handoff** | Locally valid determinations rely on different scope, freshness, source or residual assumptions. | Substitution, double counting and unsupported global closure. | Carry qualification and prevent local-to-global promotion. |
| **C7 — gradual regime drift** | Individually sub-threshold changes jointly invalidate the prior mapping. | Late threshold cascade. | Detect cumulative basis loss within the declared boundary and requalify the affected window. |
| **C8 — hidden common dependency** | Apparently independent signals share an upstream source or failure. | False corroboration and coordinated reversal. | Preserve or discover dependence; do not count correlated feeds as independent support. |

**Fixture-coverage note.** The Stage-0 programme in [00D-A01 §4](./00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_CONSTRUCTION_AND_TEST_DESIGN_v0.1.md#4-core-traceability-matrix) does not yet include a dedicated fixture for the simultaneous-reversal cascade mechanism in 00E §4.2. Q1d and N0 are not credited as its coverage.

## 9. Existing agent benchmarks: useful evidence and missing joint test

| Evidence | Published finding relevant here | What it supports | What it does not establish |
| --- | --- | --- | --- |
| **NIST AI RMF Generative AI Profile** (E4) | Treats risks across lifecycle/application/ecosystem levels and calls for provenance, monitoring, incident response, documented limits and third-party contingency processes. | The operating concerns behind T1/T2/T4 are recognized governance issues. | A runtime architecture, an EA result or a joint changed-basis test. |
| **τ-bench** (E2) | In the original paper's dynamic user–tool–policy tasks, GPT-4o completed fewer than 50% of tasks and retail `pass^8` was below 25%. | Tool use and policy access do not alone ensure repeatable workflow correctness. | Requalification of a committed decision after external regime change. |
| **AgentDojo** (E2) | The original benchmark included 97 realistic tool tasks and 629 security cases; reported general agents solved fewer than 66% of benign tasks, while defenses traded security against utility without a general guarantee. | Untrusted tool content can alter an action path and defenses require joint utility testing. | Non-adversarial staleness, residual or cross-domain sufficiency. |
| **WebArena / OSWorld** (E2) | WebArena originally reported 14.41% success for its best GPT-4-based agent versus 78.24% for humans; OSWorld reported 12.24% for its best model versus human completion above 72.36% in 369 tasks. | Operational reliability and burden must be measured, not inferred from model capability. | Authority, changed decision basis, safe posture or PNI. |
| **Agent-SafetyBench** (E2) | Across 349 environments and 2,000 cases, the original study reported that none of 16 tested agents exceeded 60%. | Prompts alone are not a complete operating control. | The EA differential or a decision-scoped requalification contract. |
| **Lost in the Middle** (E2) | Long-context experiments found performance depended on relevant-information position and could degrade substantially when evidence was in the middle. | More context length is not monotonic proof of better use of decision-relevant information. | That a particular hierarchy must fail or that EA is the only remedy. |

The missing joint test remains precise: the published suites do not jointly freeze a prior commitment, change its ecosystem basis, preserve residual and source dependence across handoffs, bind finite human/compute capacity and deadline, require an authorized posture, and compare effects with the declared null action. This is a scope comparison, not a negative claim about every unpublished implementation.

## 10. Plausibility record: 00E, the 100-million-token enterprise scenario

The number **100 million tokens is a fixture parameter**, not an empirical finding. The evidence below corroborates the mechanisms that can turn large compute and review budgets into late, overconfident or unresolved decisions.

| Source and grade | Direct finding used | 00E mechanism corroborated | Exact limit |
| --- | --- | --- | --- |
| **Tishby, Pereira & Bialek, “The information bottleneck method”** (E1) | Formalizes the trade-off between a compressed representation of `X` and information it preserves about relevant `Y`. | A best-answer-only many-to-one handoff is not automatically a sufficient statistic for later decisions; compression must be assessed against downstream relevance. | Does not show that every summary loses material information or identify an enterprise threshold. |
| **Bikhchandani, Hirshleifer & Welch, informational cascades** (E1) | Under the model's assumptions, observing prior actions can cause localized conformity based on limited information; the resulting cascades can be fragile. | Compression of private evidence into visible actions can produce **false convergence**, not only divergence. A shared closure is not automatically independent corroboration. | Economic model, not evidence that every agent hierarchy converges falsely or a frequency estimate for 00E. |
| **Howard, “Information Value Theory”** (E1) | Frames the value of additional information through its effect on a decision, rather than information quantity alone. | Supports decision-relative evidence yield and stopping tests: more tokens or facts need not have positive marginal decision value after cost and time. | Does not prescribe EA, a universal threshold or a specific organizational stopping rule. |
| **Stasser & Titus, hidden-profile experiment** (E2) | Groups with distributed information were biased toward discussing shared information, and could fail to discover the option supported by pooled unshared facts. | Distributed local access does not guarantee the final group/aggregator receives or uses the decisive non-shared evidence. | Human small-group experiment, not an LLM hierarchy or proof of a specific interface loss. |
| **Columbia Accident Investigation Board, Volume I** (E3) | The Board identified organizational barriers to effective communication of critical safety information, stifled differences, lack of integrated management and reliance on past success; it gave organizational factors weight comparable to the physical cause. | Locally available concern, compressed/filtered communication and prior-success confidence can combine into unsupported system closure. | A spaceflight accident with distinct institutions and stakes; not evidence that agents behave identically. |
| **NTSB Tempe automated-driving report** (E3) | The ADS detected the pedestrian but repeatedly misclassified her; emergency braking was precluded in the design and the system relied on the operator. The NTSB identified ineffective operator oversight and automation complacency among contributing factors. | Human-in-the-loop is not effective merely because a person is present; the handoff, remaining response time, attention and retained safety layers matter. | A single-vehicle test programme, not a multi-agent enterprise workflow. |
| **Lost in the Middle** (E2) | Models did not robustly use relevant evidence across long contexts; performance varied by position. | Expanding context/tokens can fail to improve and can obscure decision-relevant evidence, supporting the non-monotonicity test in T4/H6. | Tests retrieval/use in specified language tasks, not token-budget exhaustion or organizational atrophy. |
| **Lempert et al., Robust Decision Making under deep uncertainty** (E2) | Tests candidate plans over many plausible futures and uses vulnerability analysis and adaptive monitoring rather than requiring one confident forecast. | Supports the distinction between residual uncertainty and action that can safely generate information; a bounded pilot can be an observation instrument rather than evidence of failure to know. | Decision-support prior art, not runtime EA or proof of pointwise non-inferiority. |
| **Mitroff & Featheringham, Type-III error** (E1) | Identifies solving the wrong problem or using the wrong problem representation as a distinct systemic failure. | Supports testing the declared Objective Envelope and cross-domain interactions before optimizing a well-formed answer inside the wrong frame. | Does not assign EA authority to choose objectives or prove that a particular envelope is correct. |

### 10.1 Evidence-to-stage mapping

| 00E stage | Observable benchmark signature | Requirement route | Corroborating evidence |
| --- | --- | --- | --- |
| **Production I2** — local winners move upward without uncertainty, alternatives or dependence | qualification-loss rate; compression exposure; correlated-evidence error; false convergence/continuation | S5/S9/S11/S14 → T1/T2/T4 → H2/H3/H4 | Information bottleneck; informational cascades; hidden-profile experiment; CAIB. |
| **Quality-control/human I1→I2** — binary tickets, missing context and overload first create HOLD; workflow pressure, timeout or nominal approval can then force unsupported closure | human-capacity binding; required handoff fields; HELD time; Type-1→Type-2 forced closure; response margin | S3/S4/S5/S14 → T2/T3/T4 → H1/H4/H6 | NTSB Tempe; CAIB. |
| **Strategy O2** — possibilities promoted as sufficiently supported | local-to-global confidence inflation; residual preservation; wrong-domain closure | S2/S5/S9/S14 → T2/T4 → H1/H2 | Hidden-profile result supports the information-pooling risk; the specific creative overconfidence remains a scenario hypothesis. |
| **Deployment O1** — unresolved residual triggers unlimited research and HOLD instead of distinguishing learnable uncertainty, bounded experiment and established structural limit | evidence yield; marginal decision value; total burden; deadline pass | S3/S4/S10/S14 → T3/T4 → H5/H6 | Howard and RDM support decision-relative information value and action under deep uncertainty; Lost in the Middle supports non-monotonic context; no cited occurrence establishes the literal token total. |

### 10.2 What is and is not corroborated

**Corroborated as plausible:** relevant information can be lost or underused during compression and group aggregation; action-only observation can generate false convergence as well as divergence; organizational barriers can suppress critical safety information; a nominal human monitor can lack attention, context or response margin; additional information has decision-relative value; and additional context is not guaranteed to improve performance.

**Not established:** that a named enterprise spent 100 million tokens in this pattern; that every hierarchy is inferior; that no bounded summary can be sufficient; or that EA would have prevented the cited accidents. Those are benchmark questions.

## 11. Plausibility record: 00F, smart-city mobility divergence

00F is also fictional. Its A/B/NORMAL/HOLD pattern is a deliberately compact fixture. The evidence supports the component mechanisms—degrading situational awareness, incompatible guidance, human-monitor limits and collective traffic instability—not the claim that the exact four-way split has already occurred in one smart city.

| Source and grade | Direct finding used | 00F mechanism corroborated | Exact limit |
| --- | --- | --- | --- |
| **U.S.–Canada Power System Outage Task Force, 2003 blackout report** (E3) | The report found inadequate system understanding, inadequate situational awareness, ineffective internal communications, non-real-time data, missing real-time diagnostic support and a subsequent cascade. | A gradual, distributed deterioration can remain locally under-qualified until a network-level cascade; monitoring availability and shared frame matter. | Power-grid occurrence, not road mobility or autonomous-agent proof. |
| **BFU Überlingen investigation** (E3) | One crew followed an ATC descent instruction while TCAS advised climb; the report found the manoeuvre contrary to the TCAS advisory and described regulations/instructions as incomplete and partly contradictory. | Two individually authoritative control channels can issue incompatible responses; unresolved composition can be catastrophic. | Aviation-specific event; does not reproduce A/B/NORMAL/HOLD or smart-city governance. |
| **NTSB Tempe automated-driving report** (E3) | The ADS tracked but did not correctly classify/predict the pedestrian; the design relied on operator intervention after removing a safety layer, while oversight and complacency controls were inadequate. | Local automation plus a nominal human fallback can fail when classification, timing and attention do not compose into an effective response. | Single vehicle and one operator, not ecosystem-wide coordination. |
| **Sugiyama et al., circular-road experiment** (E2) | With homogeneous flow and no bottleneck, a small fluctuation grew into a persistent stop-and-go jam above a critical density. | Locally safe following behaviour can yield emergent system-level gridlock; no irrational actor or single obstacle is required. | Controlled 22/23-vehicle experiment, not emergency routing or telemetry disagreement. |
| **Stern et al., autonomous-vehicle field experiment** (E2) | Stop-and-go waves emerged in a ring of more than 20 vehicles and were damped by controlling one vehicle's velocity. | Network-level control posture can materially alter collective flow even when most actors remain unchanged; coordination is an architectural variable. | Demonstrates a mitigation in a constrained track, not EA or city-scale sufficiency. |

### 11.1 Evidence-to-stage mapping

| 00F stage | Observable benchmark signature | Requirement route | Corroborating evidence |
| --- | --- | --- | --- |
| **Noise/dependence accumulates** | freshness, known/unmeasured dependency, material-break recall, U-invalidation | S3/S5/S10/S14 → T1/T4 → H1/H5/H6 | 2003 blackout report. |
| **Local windows close differently—or converge falsely on one correlated basis** | residual-scope preservation; source/authority/version fields; posture divergence; false convergence | S1/S6/S9/S11/S14 → T2 → H2/H4 | BFU Überlingen supports incompatible authoritative responses; informational-cascade theory supports false convergence as the complementary trajectory. |
| **A/B/NORMAL/HOLD are not composed** | incompatible-posture exposure; wrong-domain/systemic closure; qualification loss | S5/S9/S11/S14 → T2/T4 → H2/H3/H4 | BFU; blackout report. |
| **Human escalation misses the useful window** | human-capacity binding; posture time; deadline pass; response margin | S3/S4/S5/S14 → T2/T3/T4 → H1/H6 | NTSB Tempe; blackout report. |
| **Local collision avoidance produces gridlock** | conflicted occupancy; emergency-access delay; observable outcome effect | S5/S9/S14 → T3/T4 → H2/H6 | Sugiyama experiment; Stern experiment. |

### 11.2 What is and is not corroborated

**Corroborated as plausible:** monitoring failures and stale/non-real-time data can hide a degrading network state; incompatible legitimate guidance can produce opposed actions; human fallback can be ineffective; and individually safe vehicle responses can generate collective congestion.

**Not established:** that the fictional Riverfront event occurred; that one platform causes the divergence; that all four postures necessarily appear; that physical catastrophe is deterministic; or that EA is sufficient for safety.

## 12. Benchmark execution and decision rule

### 12.1 Pre-registration

For every run, freeze:

- decision and `σ(d,t)`; affected domains and non-fungibility rule;
- facts, source graph, correlations, freshness and branch oracle;
- authority, owners, allowed actions, null action, expiry and response deadline;
- compute/tokens, bandwidth, tools, reviewer capacity and full burden ledger;
- required S#/T#/H#/KPI route and thresholds;
- event order, including gradual/hidden change branches;
- outcome vector and safety invariants;
- comparator version and exact configuration.

The evaluator may know the oracle; runtime arms may not receive it unless the tested control would legitimately have access.

### 12.2 Common outcome vector

At minimum report:

- false continuation and false containment;
- posture correctness, authorization and expiry;
- explicit-UNKNOWN and residual-scope preservation;
- handoff integrity and qualification-loss rate;
- wrong-domain/systemic closure and correlated-evidence error;
- material-break recall/precision and requalification latency;
- deadline pass and remaining response margin;
- human-capacity binding and time HELD;
- targeted re-entry precision/recall;
- decision-relevant evidence yield, marginal decision value and total burden;
- scenario-specific physical/business effect.

### 12.3 Result classes

| Result | Meaning |
| --- | --- |
| **Peer closes the gap** | B1/B2 meets the applicable requirements with equal or lower burden; EA distinctiveness narrows for that envelope. |
| **EA bounded support** | B3 improves the pre-registered outcome/resource frontier under matched resources and no hidden authority/evidence advantage. |
| **Equivalent semantics** | A peer passes by implementing semantics functionally equivalent to EA; this may support the architectural need but not EA uniqueness. |
| **Mixed/boundary-limited** | Improvement is confined to stated branches, domains or assumptions. |
| **EA negative result** | EA adds delay, indecision, false containment, cost or unsafe action without compensating benefit. |
| **Insufficient evidence** | The implementation, oracle, thresholds or measurements do not support a comparison. |

No average score may hide a material scope failure. A better result in one domain does not compensate for unsupported authority, dangerous false continuation or missed deadline in another.

## 13. Current conclusion

The reviewed evidence makes both reference scenarios **credible test fixtures**, not documented forecasts. Their mechanisms have close formal, experimental and investigated analogues:

- lossy or biased information pooling can make distributed work look more determined than it is;
- human presence is not equivalent to informed, capacitated and timely oversight;
- more context, review or computation is not monotonically better;
- locally correct or authoritative controls can conflict at a shared decision surface;
- gradual situational-awareness loss can become a fast cascade; and
- locally safe interactions can create harmful collective flow.

The evidence therefore justifies building and running the benchmark. It does not justify claiming that EA is already necessary, sufficient, unique or superior. The distinctive proposition survives only if EA-H1–EA-H4 outperform—or simplify relative to—a strong, equally resourced peer on the canonical S#/T#/H#/KPI route.

### 13.1 Practical value before an EA result exists

The benchmark is already useful to adopters and implementation partners because it can:

- separate product capability from implementation coverage and from decision-sufficiency evidence;
- show where a standard implementation, a top implementation and a top-plus-EA profile diverge under the same regime change;
- reveal whether human review is informed, authorized, capacitated and timely rather than nominal;
- price extra telemetry, context, agents and review against decision-relevant yield and remaining response margin;
- retain a negative result when a strong conventional composition closes the gap; and
- turn the two fictional scenarios into reproducible procurement and quality-plan fixtures rather than sales claims.

### 13.2 Next empirical actions

1. Freeze one executable 00E branch and one 00F branch with exact sources, hidden dependencies, authorities, deadlines and oracle.
2. Select documented B0–B3 configurations by version and configuration, not product category.
3. Pre-register KPI numerators, denominators, thresholds, admissible states, null action and total burden.
4. Run C1 continuity before failure branches so an architecture cannot “pass” by holding everything.
5. Use blinded or independent outcome adjudication where practical and retain counterexamples and negative findings.
6. Publish only scope-bounded results; require replication before any stronger architecture-role claim.

## 14. Primary sources

### Architecture, governance and agent benchmarks

- NIST, *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*, NIST AI 600-1, 2024: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- Yao et al., *τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains*, 2024: https://arxiv.org/abs/2406.12045
- Debenedetti et al., *AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents*, 2024: https://arxiv.org/abs/2406.13352
- Zhou et al., *WebArena: A Realistic Web Environment for Building Autonomous Agents*, 2023: https://arxiv.org/abs/2307.13854
- Xie et al., *OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments*, 2024: https://arxiv.org/abs/2404.07972
- Zhang et al., *Agent-SafetyBench: Evaluating the Safety of LLM Agents*, 2024: https://arxiv.org/abs/2412.14470
- Model Context Protocol, *Architecture*: https://modelcontextprotocol.io/specification/2025-06-18/architecture
- A2A Protocol, *Specification*: https://a2a-protocol.org/dev/specification/
- OpenAI Agents SDK, *Guardrails*: https://openai.github.io/openai-agents-python/guardrails/
- OpenAI Agents SDK, *Human-in-the-loop*: https://openai.github.io/openai-agents-python/human_in_the_loop/

### 00E mechanism evidence

- Tishby, Pereira & Bialek, *The information bottleneck method*: https://arxiv.org/abs/physics/0004057
- Bikhchandani, Hirshleifer & Welch, *A Theory of Fads, Fashion, Custom, and Cultural Change as Informational Cascades*, 1992: https://doi.org/10.1086/261849
- Howard, *Information Value Theory*, 1966: https://doi.org/10.1109/TSSC.1966.300074
- Stasser & Titus, *Pooling of Unshared Information in Group Decision Making: Biased Information Sampling During Discussion*, 1985: https://doi.org/10.1037/0022-3514.48.6.1467
- Columbia Accident Investigation Board, *Report, Volume I*, 2003: https://ehss.energy.gov/deprep/archive/documents/0308_caib_report_volume1.pdf
- NTSB, *Collision Between Vehicle Controlled by Developmental Automated Driving System and Pedestrian, Tempe, Arizona*, HAR-19/03, 2019: https://www.ntsb.gov/investigations/AccidentReports/Reports/HAR1903.pdf
- Liu et al., *Lost in the Middle: How Language Models Use Long Contexts*: https://arxiv.org/abs/2307.03172
- Lempert et al., *Making Good Decisions Without Predictions: Robust Decision Making for Planning Under Deep Uncertainty*, RAND, 2013: https://www.rand.org/pubs/research_briefs/RB9701.html
- Mitroff & Featheringham, *On Systemic Problem Solving and the Error of the Third Kind*, 1974: https://doi.org/10.1002/bs.3830190605

### 00F mechanism evidence

- U.S.–Canada Power System Outage Task Force, *Final Report on the August 14, 2003 Blackout in the United States and Canada*, 2004: https://www.energy.gov/sites/default/files/oeprod/DocumentsandMedia/BlackoutFinal-Web.pdf
- German Federal Bureau of Aircraft Accident Investigation (BFU), *Investigation Report AX001-1-2/02, Überlingen*, 2004: https://www.bfu-web.de/EN/Publications/FinalReports/2002/Report_02_AX001-1-2_Ueberlingen_Report.pdf?__blob=publicationFile&v=1
- NTSB, *Tempe automated-driving accident report*, HAR-19/03, 2019: https://www.ntsb.gov/investigations/AccidentReports/Reports/HAR1903.pdf
- Sugiyama et al., *Traffic jams without bottlenecks—experimental evidence for the physical mechanism of the formation of a jam*, 2008: https://doi.org/10.1088/1367-2630/10/3/033001
- Stern et al., *Dissipation of stop-and-go waves via control of autonomous vehicles: Field experiments*, 2018: https://arxiv.org/abs/1705.01693

## 15. Provenance and preservation

This integration conserves the comparator arms, benchmark families, industry-layer boundaries, required branches, negative-result taxonomy and claim limits from 00D v0.1, and EA-H1–EA-H4 with their effects and decisive falsifiers from 07. It adds evidence grading, two new regime/dependency branches, direct corroboration tables for 00E/00F, one common execution protocol and canonical terminology.

The predecessor files remain readable to verify conservation but are not alternative current benchmarks. The v0.4 controlled benchmark and its split/public-freeze records remain historical sources and are not modified by this working successor.
