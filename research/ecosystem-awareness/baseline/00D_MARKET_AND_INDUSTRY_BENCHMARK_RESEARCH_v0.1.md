# Market and Industry Benchmark Research — Ecosystem Awareness

> **Preserved non-canonical predecessor.** Its market evidence, comparator discipline and negative-result taxonomy are integrated into the sole current [canonical benchmark v0.2](./00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md). Its substantive predecessor content is retained as provenance; this file is not an alternative current benchmark.

> **Independent industry comparison.** This working research applies the universal candidate hypotheses in [00C](./00C_FALSIFIABLE_CANDIDATE_SOLUTION_HYPOTHESES_AND_KPIS.md), derived from the [00A sufficiently-good requirements](./00A_SUFFICIENTLY_GOOD_SOLUTION_REQUIREMENTS.md), to existing industry configurations. It does not define those hypotheses, rank vendors, claim that no implementation has any capability, or establish that EA meets them.

**Version:** 0.1 — 17 September 2026  
**Status:** public working research and benchmark-design input; sources and conclusions require periodic review as agent frameworks and benchmarks change.

## 1. The question to answer

The relevant market question is not whether an AI system can call tools, follow a workflow, expose a trace, request approval, or pass a task benchmark. Those capabilities already exist in useful forms.

The question is narrower and operational:

> When a commitment made at `T1` relied on a decision basis valid at `T0`, can a system detect and qualify a material `T2` change in that basis, preserve what remains unresolved across handoffs, and support a legitimate owner in taking a timely, authorized and bounded response?

That is the [DAOS case](../../../submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/04_ANNEX_III_Challenges_Exposed_by_the_Case.md). The [requirements for a sufficiently good solution](./00A_SUFFICIENTLY_GOOD_SOLUTION_REQUIREMENTS.md) state the neutral conditions, and [00C](./00C_FALSIFIABLE_CANDIDATE_SOLUTION_HYPOTHESES_AND_KPIS.md) supplies the hypothesis/KPI test contract. EA is one candidate solution, not the assumed answer.

## 2. Main conclusion

There is a documented **evaluation and operating-assurance gap** at the intersection of four markets:

1. agent runtimes and orchestration;
2. tool and agent interoperability protocols;
3. governance, security and control planes; and
4. AI-agent benchmarks.

Each market covers an important part of the problem. None of the reviewed public benchmarks jointly tests: a committed decision, a material change in its external basis, residual/unknown preservation, authorized posture selection, response-horizon/capacity, and outcome compared with safe inaction. This is an inference from the documented scope of the sources below, not a claim that every vendor implementation lacks every capability.

The evidence supports a practical proposition: enterprises need more than a model score, an orchestration trace or a compliance declaration when agents act across changing, independently governed systems. They need evidence that the basis for relying on a particular action remains sufficient, and that the response to insufficiency does not create a worse outcome.

## 3. What the available evidence already establishes

| Evidence | Concrete finding | Relevance to the challenge | Limit of the evidence |
| --- | --- | --- | --- |
| **NIST Generative AI Profile** | NIST treats risk as arising across lifecycle, application and ecosystem levels. It notes that systems commonly combine multiple third-party components and data sources, making attribution difficult; it calls for provenance, monitoring, incident response, documented generalizability limits and third-party contingency processes. | Supports material-break awareness, provenance/freshness, owner/capacity and bounded requalification as real operating concerns rather than invented EA features. | It is a risk-management profile, not an operational benchmark or a prescribed EA architecture. |
| **τ-bench** | In dynamic user–tool–policy tasks, the paper reports that GPT-4o completed fewer than 50% of tasks and `pass^8` was below 25% in retail. It measures repeated-run consistency and policy adherence against an end-state database. | Shows that tool calling and policy access do not by themselves establish reliable, repeatable action in a domain workflow. | It does not test a changed decision basis after a commitment, cross-system residual, PNI or capacity of the human response. |
| **AgentDojo** | The benchmark contains 97 realistic tool tasks and 629 security cases. Its reported general agents solved fewer than 66% of benign tasks; prompt-injection defenses reduced attack success but did not provide a general guarantee. | Demonstrates that untrusted external tool data can alter an agent's action path and that security must be assessed jointly with task utility. | It tests adversarial instructions and security properties, not whether non-malicious changing evidence invalidates a commitment. |
| **WebArena** | The original realistic-web benchmark reported its best GPT-4-based agent at 14.41% end-to-end task success, against 78.24% for humans. | Shows the difference between apparent autonomy and reliable long-horizon execution in an interactive environment. | It evaluates task completion, not decision-basis validity, authority, safe posture or response consequences. |
| **OSWorld** | In 369 real computer tasks, the original study reported human completion above 72.36% and its best model at 12.24%; the project also identifies robustness to UI noise and efficiency challenges. | Supports the need to count operational reliability and resource/time burden rather than only model quality. | It is a computer-use benchmark. It does not model external authority, material T2 change or residual epistemic state. |
| **Agent-SafetyBench** | Across 349 environments and 2,000 cases, none of 16 popular LLM agents scored above 60%; the paper identifies lack of robustness and risk awareness, and finds defense prompts alone insufficient. | Supports the need for explicit posture, safety and bounded response criteria beyond an instruction prompt. | It is a broad safety benchmark and does not define an industrial decision-contract or compare with inaction. |

### Primary sources

- NIST, *Artificial Intelligence Risk Management Framework: Generative AI Profile*, 2024. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- Yao et al., *τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains*, 2024. https://arxiv.org/pdf/2406.12045
- Debenedetti et al., *AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents*, 2024. https://arxiv.org/pdf/2406.13352
- Zhou et al., *WebArena: A Realistic Web Environment for Building Autonomous Agents*, 2023. https://arxiv.org/abs/2307.13854
- Xie et al., *OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments*, 2024. https://osworld-v1.xlang.ai/
- Zhang et al., *Agent-SafetyBench: Evaluating the Safety of LLM Agents*, 2024. https://arxiv.org/abs/2412.14470

## 4. What existing market layers do well — and where their boundary is

The gap is not “agents have no controls.” The market already supplies valuable controls. The issue is that their normal contract stops before the full `T0 → T1 → T2` decision-sufficiency problem.

| Market layer | Demonstrated or stated strength | Boundary relevant to this research | Requirement consequence |
| --- | --- | --- | --- |
| **Foundation-model / tool agents** | Translate natural-language tasks into plans and tool calls; can retrieve, reason, act and request help. | A successful task trajectory does not establish that the evidence, authority, dependency or operating conditions behind a commitment still apply. | Test material-break awareness and false continuation separately from task success. |
| **Agent runtimes and orchestration** | State, routing, checkpoints, retries, human approval, guardrails and traces are available. | A runtime normally governs execution flow; it does not automatically know which external conditions make a business decision still valid. | Require an explicit decision basis, posture and requalification boundary. |
| **Control plane / gateway / observability** | Authentication, authorization, quotas, logging, policy enforcement and operational metrics can be centralized. | Control of access or traffic does not establish semantic sufficiency of the information being relied on. | Separate access authority from evidence applicability and current decision support. |
| **MCP** | The host manages client lifecycle, permissions, authorization decisions and context aggregation; servers expose focused resources/tools/prompts behind security boundaries. | Its architecture defines exchange and isolation, not a common representation of decision scope, residual uncertainty, material change or response legitimacy. | Use MCP as a substrate; test whether an added profile can preserve qualification across it. |
| **A2A** | Allows opaque agents to discover, delegate tasks and exchange messages/artifacts; its enterprise guidance covers transport security, authentication, authorization, tracing and API management. | A2A explicitly leaves authorization logic specific to the agent implementation; its core payload offers messages, artifacts and generic metadata, not a decision-basis sufficiency contract. | Use A2A as a transport; test an EHD-equivalent payload rather than claim A2A is deficient. |
| **Governance standards and AI RMF controls** | Set expectations for risk ownership, human oversight, provenance, monitoring, incident response and third-party risk. | They define what organizations should govern, but normally do not supply a runtime test for whether this particular action remains justified after a material change. | Translate governance expectations into case branches and measurable operating evidence. |

### Protocol and framework sources

- Model Context Protocol, *Architecture*, accessed 17 September 2026. https://modelcontextprotocol.io/specification/2025-06-18/architecture
- A2A Protocol, *Core Concepts and Components in A2A*, accessed 17 September 2026. https://a2a-protocol.org/latest/topics/key-concepts/
- A2A Protocol, *Enterprise Implementation of A2A*, accessed 17 September 2026. https://a2a-protocol.org/latest/topics/enterprise-ready/
- OpenAI Agents SDK, *Guardrails*, accessed 17 September 2026. https://openai.github.io/openai-agents-python/guardrails/
- OpenAI Agents SDK, *Human-in-the-loop*, accessed 17 September 2026. https://openai.github.io/openai-agents-python/human_in_the_loop/

## 5. A concrete control-plane finding

The OpenAI Agents SDK illustrates why a runtime control is not automatically an ecosystem-level control. Its documentation states that input guardrails run only for the first agent in a chain and output guardrails only for the final agent; tool guardrails can surround a function-tool call, but do not apply to a handoff itself. Its hosted and built-in execution tools do not use that guardrail pipeline. This is not a criticism of the SDK: it is an explicit scope boundary that makes a system-level evidence and handoff test necessary.

The same distinction applies to any comparable runtime: the benchmark must inspect actual configuration and execution traces, not infer a decision-sufficiency property from the presence of “guardrails,” “HITL,” “memory,” “graph,” “control plane” or “context engineering” in a product description.

## 6. The benchmark-of-benchmarks gap

The existing benchmark landscape is valuable but fragmented.

| Benchmark family | What it measures well | What it does not decide for this challenge |
| --- | --- | --- |
| **Task success:** WebArena, OSWorld, AgentBench | Can an agent complete realistic web, desktop or interactive tasks? | Whether a completed action should have been continued after its original business basis changed. |
| **Reliability and policy:** τ-bench / τ²-bench | Repeated consistency, user interaction, tool use and domain policy adherence. | Whether a policy/evidence source remains applicable at T2, or whether a response is no worse than inaction. |
| **Security:** AgentDojo, Agent-SafetyBench | Prompt injection, unsafe actions, security–utility trade-offs and broad agent safety. | Non-adversarial staleness, dependency changes, cross-domain evidence gaps and requalification of a valid earlier commitment. |
| **Protocol and system evaluation:** interoperability tests, traces, conformance tests | Syntax, transport, identity, tool availability, latency and task lifecycle. | A semantic contract for scope, freshness, residual uncertainty, capacity, authority and legitimate posture across a handoff. |
| **Governance and risk frameworks:** NIST AI RMF and sectoral controls | Risk ownership, documentation, monitoring, human involvement and process expectations. | A reproducible runtime fixture that exposes false continuation, false containment and the decision/resource trade-off. |

This creates a precise research opportunity: **compose**, rather than replace, existing benchmarks. A candidate must inherit their task, security, policy and observability tests, then add the missing changed-basis branch and outcome/accounting measures.

## 7. Market benchmark design

### 7.1 Comparator arms

Every evaluated configuration runs the same frozen case facts, objective, evidence, time horizon and authority conditions.

| Arm | Configuration | What it establishes |
| --- | --- | --- |
| **B0 — ordinary agent** | A capable model with normal tools, retrieval, workflow/orchestration and logging. | The baseline failure mode; not a strawman. |
| **B1 — strong composed peer** | B0 plus provenance/lineage where available, policy checks, prompt-injection defenses, guardrails, approval, tracing, retry/fallback and resource limits. | Whether conventional competent composition already reaches the required outcome without EA-equivalent semantics. |
| **B2 — protocol/control-plane peer** | B1 with A2A/MCP or equivalent transport, identity/access control, observability and explicit handoff configuration. | What interoperable control and exchange contribute, and what they do not preserve by themselves. |

No arm should receive extra evidence, wider authority, a longer deadline or more human attention without recording that difference. A system that performs well only because it asks for unlimited review or exhaustive search has not met minimum sufficient intervention. An EA-versus-peer comparison may be added later, but belongs to [07](./07_EA_CANDIDATE_DIFFERENTIAL_HYPOTHESES_v0.5_REVIEWED_WORKING.md); it is not an arm required to determine whether industry meets the universal tests.

### 7.2 Required case branches

| Branch | T0/T1/T2 condition | Failure exposed | Minimum expected behaviour |
| --- | --- | --- | --- |
| **C1 — valid continuity** | T0 basis remains within declared conditions through T1/T2. | Unnecessary alarms, needless human burden. | Continue under stated qualifications; do not manufacture a change. |
| **C2 — observed material change** | A dependency, policy, authority, capacity, cost or source condition visibly changes after commitment. | Stale-frame continuation. | Identify affected basis, enter a defined posture and request/perform only an authorized response. |
| **C3 — insufficiently established condition** | Relevant evidence becomes stale, conflicting, unavailable or source-dependent; no conclusive change is observed. | UNKNOWN collapsed into PASS, or indefinite escalation. | Preserve unresolved state; select bounded requalification, hold, fallback or another authorized posture. |
| **C4 — adversarial/poisoned evidence** | External content contains prompt injection or manipulated guidance. | Tool/data hijack, authority expansion or unsafe action. | Retain AgentDojo-style security/utility testing and avoid treating a security signal as proof of the whole decision basis. |
| **C5 — capacity/response deadline** | The necessary reviewer, tool, network or rollback capacity cannot meet the response window. | Nominal HITL treated as effective control. | Account for real capacity; contain, abstain or use an authorized fallback rather than converting delay into permission. |
| **C6 — cross-domain handoff** | Two locally valid determinations rely on different scope, freshness or source assumptions. | Wrong-domain substitution, double counting or loss of residual. | Carry declared scope/provenance/unresolved state; do not create a system-wide PASS from local results. |

### 7.3 Universal hypotheses, measures and thresholds

Apply the measures in [00C](./00C_FALSIFIABLE_CANDIDATE_SOLUTION_HYPOTHESES_AND_KPIS.md), not a generic maturity score. The table is a compact industry test map.

| Universal candidate hypothesis | Minimum measure | Failure / falsifier |
| --- | --- | --- |
| **C-H1 — material decision-basis qualification** | Recall/precision for declared material T2 changes; false-continuation rate; threshold calibration. | The system continues after an observed material break without exposing the affected basis, alerts indiscriminately in C1, or claims coverage beyond its evidence boundary. |
| **C-H2 — qualified owner-bound posture** | Correct posture at the owner; unresolved-state preservation; required handoff-field completeness. | It emits only a score/log, collapses UNKNOWN, or loses scope, authority or expiry condition. |
| **C-H3 — bounded authorized response** | Authorized-response and reversibility/containment compliance; false-positive response cost; per-state comparison only where PNI is claimed. | A posture creates an unpermitted/unbounded action; any covered state defeats a claimed PNI action. |
| **C-H4 — timely viable minimum-sufficient requalification** | Deadline pass and response margin; decision-relevant evidence yield; end-to-end burden. | Analysis arrives after no legitimate response remains, or relies on indefinite expansion/review to pass. |
| **C-H5 — scoped handoff and targeted re-entry** | Handoff integrity; wrong-domain closure; targeted re-entry precision/recall and indiscriminate-rerun rate. | A recipient turns a local determination into unsupported global closure or must rerun indiscriminately to recover qualification. |

### 7.4 Determinations after a test

The result must be allowed to be negative or mixed.

| Result | Meaning |
| --- | --- |
| **Industry configuration supports a bounded claim** | A named B0/B1/B2 configuration meets the applicable C-H tests within its declared envelope. |
| **Partial / boundary-limited** | It passes some branches but lacks coverage, response margin, authority or resource evidence for others. |
| **No industry gap on this case** | A strong B1/B2 configuration meets the applicable tests with equal or lower burden; this says nothing about EA's separate differential. |
| **Failure or insufficient evidence** | The configuration adds indecision, cost or unsafe action; or no comparable test evidence exists. |

## 8. What may be said now — and what may not

### Supported now

- Agent reliability, safety and long-horizon task completion remain empirically difficult in realistic interactive benchmarks.
- Tool calling, policy guidelines, prompt defenses, HITL and traces are useful controls but have explicit scope boundaries.
- Third-party components, provenance, attribution, ongoing monitoring, contingency and response capacity are recognized risk-management concerns.
- Existing benchmarks provide reusable components for a fair EA evaluation, but their published task definitions do not jointly cover the full changed-basis challenge.
- The proposed benchmark is a credible way to decide whether the gap has practical value, or whether an existing strong composition already closes it.

### Not supported now

- That EA is uniquely capable, superior, deployable, economically viable or PNI-safe.
- That all agent platforms, control planes or protocols fail the requirements.
- That a protocol needs to be replaced, or that a new standard is necessary before testing.
- That human approval repairs a deficient evidence basis or is available within the useful response window.

## 9. Practical business value of the benchmark

For an enterprise, the benchmark converts an abstract concern—“can we trust the agent?”—into decisions that architecture, risk and operations teams can own:

- identify which commitments may continue, must be requalified or should be contained when dependencies change;
- separate security/access controls from evidence sufficiency and current applicability;
- reveal where a control plane, approval process or trace is present but cannot support the decision in time;
- compare the cost of extra evidence and reviewer attention with the cost of false continuation and false containment; and
- procure or design only the additional semantics/control needed for a named high-value case.

The business value is therefore not “more context.” It is fewer unsupported continuations, fewer blanket holds, and a testable basis for investing in the right level of human and technical control.

## 10. Next research actions

1. Freeze two to four cross-sector cases using C1–C6, including one manufacturing/logistics or regulated-operation case with a genuine T2 dependency change.
2. Select B0, B1 and B2 configurations by documented capability, exact version and configuration—not by marketing category.
3. Reuse τ-bench/AgentDojo/OSWorld-style execution evidence where applicable, and record their boundaries rather than claiming replacement.
4. Pre-register decision contract, materiality threshold, null action, authority, response deadline, human capacity and outcome/resource measures.
5. Run blinded or independent adjudication where practical; retain negative results and counterexamples.
6. Only after the outcome is visible, decide whether a public EA interface profile, benchmark fixture or standards contribution is justified.

## Relationship to the EA corpus

The definition route remains:

**[challenge](../../../submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/04_ANNEX_III_Challenges_Exposed_by_the_Case.md) → [sufficiently good solution requirements](./00A_SUFFICIENTLY_GOOD_SOLUTION_REQUIREMENTS.md) → [universal candidate hypotheses and KPIs](./00C_FALSIFIABLE_CANDIDATE_SOLUTION_HYPOTHESES_AND_KPIS.md) → [EA-specific differential hypotheses](./07_EA_CANDIDATE_DIFFERENTIAL_HYPOTHESES_v0.5_REVIEWED_WORKING.md) → [concrete architecture](./00_CANONICAL_ARCHITECTURE_TOPOLOGY.md).**

This document is adjacent to that route: it provides the external evidence and fair-comparison method for deciding whether B0/B1/B2 industry configurations meet the universal tests and whether an industrial gap remains. It does not change the frozen baseline, recast the challenge as a product claim, or establish an EA result.
