<a id="00g-r01-reducción-de-00g"></a>
# R01 Probabilistic exploration and validation cost

Base specification v0.6 · Reading organization 4 October 2026 · Non-canonical research study

**Status terminology:** `Non-canonical research study` describes R01's external/institutional status: R01 is not an adopted standard or an externally canonical corpus. `Current canonical mathematical reference` below means only the internally governing mathematical statement for the present R01 line; it does not make the whole study canonical.

[Complete base scenario](./Escenario-creatividad-validacion.md) · [Reductions](#reductions) · [Three extensions](#extensiones) · [Trace policy](./TRACE_POLICY.md) · [Preservation record](./ORGANIZATION_TRACE.md)

<a id="canonical-conditioned-trilemma"></a>
**Current canonical mathematical reference:** [Mathematical validation of the conditioned trilemma in R01, v0.2](./feasibility/R01_CONDITIONED_TRILEMMA_THEOREM.md). This standalone document governs the mathematical statement, conditions and viability regions. [R01's explanation](./Escenario-creatividad-validacion.md#r01-conditioned-mathematical-validation) links to the same reference; [audit and repairs](./feasibility/R01_AUDIT_CONTINUITY_AND_REPAIRS.md) support it. External reviews have been received; the remaining coverage is tracked by version and proposition in [the current register](./feasibility/WORKPLAN_STATUS.json). The [extension consistency review](./feasibility/EXTENSION_CONSISTENCY_REVIEW.md) is complete as an own review. Continue with [technologies inside the extension protocol](./feasibility/TECHNOLOGY_EXTENSION_PROTOCOL.md#technologies-to-study), starting with human escalation and whispering.

The dated plans and state snapshots below are retained as history. For the current mathematical formulation, use the canonical document above; their original task criteria remain available.


**How to read the evaluation:** [problem + technology → operating scenario → execution strategy → performance → acceptance](./Escenario-creatividad-validacion.md#from-the-practical-problem-to-acceptance). The diagram distinguishes the accepted performance region from whether any permitted strategy can reach it.

[Differential and value of the experiment](./DIFFERENTIAL_AND_EXPERIMENT_VALUE.md): the technology–problem suitability map, cost/risk/effectiveness, related work, candidate contribution, oracle priorities and remaining review passes.

<a id="bot-start-here"></a>
## Start here — current work

[Current queue](./feasibility/WORKPLAN.md) · [task register](./feasibility/WORKPLAN_STATUS.json) · [continuation prompt](./feasibility/CONTINUATION_PROMPT.md).

The sole active queue is discovered by `R01_BOT_WORKPLAN_START` / `R01_BOT_WORKPLAN_END` in `feasibility/WORKPLAN.md`. Other marked documents point to it; they do not create independent pending-task lists.

| Order | Current work | Status |
|---|---|---|
| 1 | [Technologies of the extension protocol](./feasibility/TECHNOLOGY_EXTENSION_PROTOCOL.md#technologies-to-study): [human escalation and whispering first](./feasibility/HUMAN_ESCALATION_WHISPERING.md), then the registered frameworks. | Mathematical contract available; technology review and implementation correspondence in progress. |
| Remaining review | M16 independent coverage, M17 source-clause fidelity, P08 version-aware integrity. | Retain actual gaps; do not repeat completed own repairs or extension consistency review. |
| C02 instrument | [Neutral R01 oracle / harness](./oracle/README.md) aligned first to Nelson Trasatti's UC #4 testbed: adapter contract, UC4 sidecar, dual exact reference paths and Stage-0 positive/boundary/rejection self-test fixtures. | Limited implementation draft; instrumentation only. No real technology or EA differential executed. Source-contributor review requested before claiming UC4 compatibility. |\n| Later | C11 registered campaign → T03 real adapter and technology campaign. | Remain gated on C02 verification/admission; no real technology execution. |

The 55 historical IDs and criteria remain traceable: four active tasks, three later deliveries, four historical completions, three own-scope deliveries complete, 37 consolidated obligations and four tasks outside the current scope. Consolidation is not scientific validation. [Full old queues](./feasibility/previous-work/QUEUE_SNAPSHOT_2026-10-04.json) · [updated master prompt](./STRATEGIC_WORKPLAN_AND_EXECUTION_PROMPT.md).

The earlier proof records remain accessible through [previous work](./feasibility/previous-work/README.md). The [partial exercises and received Annex T](./feasibility/partial-experiments/received/2026-10-04/README.md) are preparation annexes, not canonical proofs or executed technology validation. Historical hash discrepancies remain P08; do not overwrite their manifests.

### Canonical route and retained historical material

The current R01 route is: this README → the active scenario and [conditioned theorem v0.2](./feasibility/R01_CONDITIONED_TRILEMMA_THEOREM.md) → the [technology extension protocol](./feasibility/TECHNOLOGY_EXTENSION_PROTOCOL.md) and current workplan → the [version-aware verifier](./extensions/verify_audit_v2.py). Retained files are not automatically active research.

In particular, the three `extensions/*/proof/README.md` files are **historical supporting material outside the current canonical route**. They preserve the finite-checker instructions and context of earlier extension editions. Their references to `verify_audit.py --verify` are historical reproduction instructions, not the current package gate. The bounded checker/results remain evidence within their declared scope, but preserving them does not reactivate an experimental line that has been superseded or left outside the current programme.

### Claim status at the current gate

| Claim | Current status | Governing evidence / open gate |
|---|---|---|
| Conditioned R01 theorem v0.2 | Author-reconstructed symbolic proof; received external reviews are recognized, but current proposition-by-proposition independent coverage is not yet established. | [Theorem](./feasibility/R01_CONDITIONED_TRILEMMA_THEOREM.md) · [review](./feasibility/R01_CONDITIONED_TRILEMMA_REVIEW.md) · **M16 open** in [status register](./feasibility/WORKPLAN_STATUS.json). |
| Fidelity from the current theorem back to all governing source clauses | Not closed. | **M17 open** in [status register](./feasibility/WORKPLAN_STATUS.json). |
| Three retained finite extension checkers reproduce their historical reports | Current substantive reproduction passes under v2; documentary differences remain versioned separately. | [Version-aware verifier](./extensions/verify_audit_v2.py) · historical [audit report](./extensions/audit_results.json) · **P08 in progress**. |
| Human escalation / whispering technology line | Virtual/contract traversal and own review only; no human calibration or real technology run. | [Technology study](./feasibility/HUMAN_ESCALATION_WHISPERING.md) · current register. |
| Full R01 campaign and comparative EA benefit | Not executed or established. | Later gates: C02 neutral oracle/harness → C11 registered campaign → T03 real adapter/technology campaign. |

<a id="r01-in-plain-language"></a>
## What R01 studies

An agent knows a permitted procedure for completing its task. While working, it explores alternatives that may produce a better result. Each alternative takes effort to discover and to check. Other agents may share findings and checks, but their reports do not by themselves authorize the action.

The study asks when this process finds a good permitted solution within its budget and deadline, and when it instead executes an inadmissible alternative, spends too much on checking, settles for lower quality or leaves the task incomplete. Benefits and distances vary across the fixed world; search and policy randomness are recorded. Failure is a possible result to measure, not a required outcome.

**R01's practical objective is to design small, bounded pilots for choosing an architecture.** They should help determine whether a problem has an adequate solution through an R01-compatible architecture, when another procedure is preferable and when more evidence is needed. Human supervision also has information and cost limits. A small pilot supports conclusions about its tested scope; suitability at scale needs additional justification. Ecosystem Awareness is one candidate add-on for improving that scope, subject to the same comparisons.

| Route | Meaning |
|---|---|
| M — known procedure | A permitted starting plan; it may deliver lower quality. |
| I — ideal permitted alternative | The best complete admissible solution, calculated by the evaluator. |
| P — attractive forbidden alternative | A technically attractive route whose composition violates the obligation. |

These are the known route and two alternative references. Agents are not told which candidate is I or P. They discover candidates, review the relevant relations, decide whether to proceed and record the effect. A local check may leave important conditions unresolved; sufficient applicable evidence may resolve them.

**[Read the complete R01 scenario](./Escenario-creatividad-validacion.md).** It contains the problem, route construction, probabilistic exploration, decision cycle, validation, costs, configurations and required traces. This README is its entrance and extension index. The complete R01 campaign is specified but has not yet been implemented and executed.

| Question | Direct section in the complete document |
|---|---|
| How does R01 support architecture selection with limited pilots? | [Pilot objective and supervision §1.7](./Escenario-creatividad-validacion.md#17-cómo-detectar-el-área-y-qué-aporta-la-supervisión-humana) · [Bounded pilot protocol](./Escenario-creatividad-validacion.md#bounded-pilots-for-architecture-selection) · [Two areas and trilemma §1.2](./Escenario-creatividad-validacion.md#12-dos-áreas-y-un-trilema) |
| What are the routes and how are alternatives found? | [Routes §2.1](./Escenario-creatividad-validacion.md#21-tarea-y-trayectorias-de-referencia-etiquetadas) · [Benefits §2.3](./Escenario-creatividad-validacion.md#23-beneficios-heterogéneos-con-promedio-fijado) · [Search radius §2.4](./Escenario-creatividad-validacion.md#24-proximidad-y-radio-creativo) |
| What does an agent do, step by step? | [Decision cycle §2.7](./Escenario-creatividad-validacion.md#27-secuencia-de-decisión) · [Own review §2.8](./Escenario-creatividad-validacion.md#28-validación-convencional-hacia-atrás-y-hacia-delante) · [Social evidence §2.10](./Escenario-creatividad-validacion.md#210-señalización-y-validación-social) |
| How are costs and resources counted? | [Costs §2.11](./Escenario-creatividad-validacion.md#211-coste-de-exploración-y-coste-de-revisión) · [Budget §2.12](./Escenario-creatividad-validacion.md#212-presupuesto-y-plazo) |
| Where are the traces? | [Required trace fields §2.16](./Escenario-creatividad-validacion.md#216-qué-debe-registrar-una-trayectoria-auditable) · [States §2.17](./Escenario-creatividad-validacion.md#217-estados-y-requisitos-verificables-antes-de-ejecutar) · [Earlier executed trials](./extensions/hugging-face/README.md#retained-oracle-and-trial-history) |

<a id="reductions"></a>
## Reductions

A reduction removes particular details while preserving the relation needed for the stated claim. The documented origin of R01 is listed below; reduction status is separate from the three extensions.

| Documented reduction | What is simplified and retained | Explanation and proof status |
|---|---|---|
| 00G to R01 | Remove the particular narrative; retain the obligation, received interpretation, source dependencies, authority and decision in the candidate social subfamily. | [Reduction document](./reductions/00G-to-R01/README.md). Candidate relation under review; it does not classify every R01 configuration as a 00G instance. |

<a id="extensiones"></a>
## Extensions

An extension applies R01's task and decision questions to a concrete case. Each document starts with the problem, a step-by-step scenario and the parallel with R01, then identifies its proof, results, limits and sources. The mix contains selected parallels; it does not claim that every real incident has every R01 mechanism.

<a id="incident-scope"></a>
**Scope of the constructed extensions.** Their purpose is to study selected failure modes with features compatible with R01, motivated by the documented cases. They do not aim to reconstruct every detail of those cases or exactly reproduce the Hugging Face incident investigated by METR and Redwood. The modeled failure need not be the causal mechanism of the reported incident; this work does not establish that identification, and the mechanisms may differ.

If an R01 failure does not appear, or its assumptions do not fit a historical episode, that limits the claim about the tested model or proposed correspondence. It does not imply that the reported incident did not occur, nor rule out other mechanisms producing similar outcomes. Conversely, producing a similar failure in the model does not establish its historical cause. Formal preservation claims still require their stated contracts; similarity alone does not satisfy them.

The [common scope rule](./extensions/CRITERIA_AND_AUDIT.md#historical-and-constructed-scope) applies to all three cases. The [scope preservation record](./INCIDENT_SCOPE_TRACE.md) verifies retention of the preceding text.

| Extension | The problem in words | Complete case document |
|---|---|---|
| <a id="openai--hugging-face"></a>Hugging Face | Agents share useful alternatives; the receiver must establish whether using an alternative fits its task and permissions. | [Case, scenario, R01 parallel, proof, results and history](./extensions/hugging-face/README.md) |
| <a id="extensión-al-caso-infoblox"></a>Infoblox | A DNS diagnosis combines sources and a specialist; identity and earlier checks may not authorize the new combination or export. | [Case, scenario, R01 parallel, proof, results and history](./extensions/infoblox/README.md) |
| <a id="familia-extendida-con-nucleo-funcional-isomorfo"></a>Mix of other failure modes | Cases involving out-of-scope resources, an accepted answer that misses the real task, or a working but unauthorized communication channel. | [Cases, selected parallels, conditional proof, results and sources](./extensions/family/README.md) |

All three use the [same evidence and review criteria](./extensions/CRITERIA_AND_AUDIT.md). Their detailed statuses and existing evidence remain in their own documents and the [technical table](./extensions/CRITERIA_AND_AUDIT.md#retained-extension-review-table).

<a id="guía-de-lectura"></a>
## Reading guide

| To consult | Entry |
|---|---|
| Problem, rules and base configuration | [R01 scenario v0.6](./Escenario-creatividad-validacion.md). |
| Method governing the three extensions | [Contract, evidence, fifteen groups and A25](./extensions/CRITERIA_AND_AUDIT.md). |
| Proof and scope of transfer | [Kernel and obligations E1–E7](./extensions/family/KERNEL_AND_PROOF.md) · [References and EA–control comparison](./extensions/METHODOLOGICAL_FOUNDATIONS.md). |
| Each case and its checks | [Table of the three extensions](#extensiones). |
| Earlier trials and retained results | [Case history](./extensions/hugging-face/README.md#historial-de-ensayos-y-trabajo-pendiente). |
| Joint reproduction and editorial review | [Common command](#reproducción-conjunta-de-las-comprobaciones) · [Review procedure and outcome](./extensions/EDITORIAL_REVIEW.md). |

The conditional formal proof, finite checks and experiments with agents are different forms of evidence. The first two have documents and bounded results; the full execution of R01 and the EA comparison remain pending. Current verdicts are consulted in the common records; earlier work retains its date and scope.

<a id="reproducción-conjunta-de-las-comprobaciones"></a>
## Joint reproduction of the checks

From this `00G-R01/` folder, use the version-aware verifier:

```sh
python3 extensions/verify_audit_v2.py --verify
```

The [version-aware verifier](./extensions/verify_audit_v2.py) separates **substantive reproduction** from **documentary integrity**. It reruns the three finite checkers in temporary folders, compares their reports with the preserved historical audit, replays the bounded logical falsifiers and verifies the checker/result fingerprints. Historical document manifests are then checked separately against the current reading edition.

A current document differing from a historical manifest is reported as `STALE_HISTORICAL_MANIFESTS`; it does not invalidate an unchanged checker/result pair and it is not silently rewritten to manufacture a new historical PASS. Conversely, a checker/result mismatch is a substantive failure.

The original [historical verifier](./extensions/verify_audit.py) and [historical common report](./extensions/audit_results.json) are retained unchanged as records of the edition they reviewed. They must not be interpreted as a current-document integrity certificate. A fresh dynamic report can be written, without overwriting the historical record, with:

```sh
python3 extensions/verify_audit_v2.py --write-current
```

This remains an internal rerun of published code and bounded logical checks, not an independent replication, a full R01 campaign or an EA evaluation. M16 independent coverage and M17 source-clause fidelity remain separate review obligations. The editorial procedure, content preservation and limits of the earlier review remain in the [package review](./extensions/EDITORIAL_REVIEW.md).

<a id="archivos-y-reproducción-editorial"></a>
## Files and editorial reproduction

The existing Word and PDF files preserve **v0.6 before the reading separation**. They include the former case chapter; the current separated reading edition is in Markdown. This section describes the exports of the **base scenario v0.6**. In the extensions, the current review is in Markdown; the Infoblox Word file preserves the v0.5 edition preceding its later additions, identified in its case record.

Markdown is the current text source; the retained Word and PDF files are exports of the earlier complete v0.6 text. The two original figures, the new scenario–acceptance diagram and their generation script are in this package. `build_figures.py` regenerates the figures with Matplotlib and `build_document.py` regenerates Word with python-docx. The PDF is exported from Word with LibreOffice. The scripts resolve their paths from this folder. A simulator is not yet included: the experiment's executable rules remain pending.

The current reading edition separates the base and case documents; the earlier complete text is preserved in the organization record. Local drafts 0.1–0.5, conversational revisions, verification renders and temporary files are not part of the package. Public earlier work remains linked for its documentary role.

## Earlier section links

<a id="lugar-de-la-reducción-dentro-de-00g"></a>
[Reduction explanation](./reductions/00G-to-R01/README.md#lugar-de-la-reducción-dentro-de-00g).

<a id="fundamento-y-prueba-de-la-reducción"></a>
[Reduction explanation](./reductions/00G-to-R01/README.md#fundamento-y-prueba-de-la-reducción).

<a id="cómo-se-hace-la-reducción"></a>
[Reduction explanation](./reductions/00G-to-R01/README.md#cómo-se-hace-la-reducción).

<a id="identificación-y-estado"></a>
[Reduction explanation](./reductions/00G-to-R01/README.md#identificación-y-estado).

<a id="control-del-test-y-alcance-del-oráculo-c3"></a>
[Earlier evaluator and trial history](./extensions/hugging-face/README.md#control-del-test-y-alcance-del-oráculo-c3).

<a id="historial-de-ensayos-y-trabajo-pendiente"></a>
[Earlier evaluator and trial history](./extensions/hugging-face/README.md#historial-de-ensayos-y-trabajo-pendiente).


<a id="viability-work-in-progress"></a>
<a id="viabilidad-del-trilema--trabajo-en-desarrollo"></a>

## Trilemma feasibility — work in progress

The study is gathered in its own R01 subfolder. Scenarios, reductions, results and exports remain intact. Previous queue contents are preserved in [the snapshot](./feasibility/previous-work/QUEUE_SNAPSHOT_2026-10-04.json); the only current order is in [WORKPLAN.md](./feasibility/WORKPLAN.md): four active tasks and three subsequent deliverables.

| Work | Entry point | Status and next step |
|---|---|---|
| Feasibility document | [Full study](./feasibility/README.md) · [Base mathematical proof](./feasibility/PURE_MATHEMATICAL_TRILEMMA.md) | Trilemma by families and viable regions; not impossibility in every configuration. F derivation available, independent review and bridge to R01 pending. |
| Pending work | [Current plan and 55 tasks](./feasibility/WORKPLAN.md) · [Status register](./feasibility/WORKPLAN_STATUS.json) | Core and self-review published; continue with human escalation and whispering within the technology protocol. Oracle and harness after the contract. |
| Partial experiments | [Separate inventory](./feasibility/partial-experiments/README.md) | Scripts, fixtures, outputs and additional material preserved. Bounded diagnostics; they are not the independent oracle/harness. |
| Drafts and preservation | [Previous work](./feasibility/previous-work/README.md) · [Relocation map](./feasibility/RELOCATION_MANIFEST.json) · [Verification](./feasibility/PRESERVATION_CHECKS.json) | History preserved; previous results are not replaced and the corpus is not deleted. |
| Continuation | [Full prompt](./feasibility/CONTINUATION_PROMPT.md) | Keep work within this subfolder and tracking at the end of the READMEs. |
| Independent manuscript | [Conditioned trilemma of cost, risk and efficacy](./feasibility/CONDITIONED_TRILEMMA.md) | Self-contained hypotheses and proofs, exact frontiers, pairwise regions and legitimate success; prepared for review, without announcing external validation. |
| Manuscript audit | [Adversarial self-review](./feasibility/CONDITIONED_TRILEMMA_SELF_REVIEW.md) · [Publication record](./feasibility/CONDITIONED_TRILEMMA_RELEASE.json) | Includes biased AVG prior and WC contrast; M16/M17 remain pending. No new scientific tests are executed. |
| In-depth audit and transfer | [Full verdict](./feasibility/CONDITIONED_TRILEMMA_DEEP_AUDIT.md) · [Mapping, local proof and R01 family G](./feasibility/R01_TO_CONDITIONED_TRILEMMA_MAPPING.md) | Distinguishes physical capacity/target, e/σ and risk/Pareto frontier; G presents a conditioned trilemma with arbitrary sizes and an explicit catalog. The same F formula is not extended indiscriminately. Self-review, not external review. |
| Status after audit, 4 October | [Manuscript v0.2](./feasibility/CONDITIONED_TRILEMMA.md) · [Audit record](./feasibility/DEEP_AUDIT_RELEASE.json) | Historical status of that deliverable; the current cleaned register governs continuation. M17 moves to IN_PROGRESS through mapping/proposition/G result; no scientific task is closed and no new tests are executed. M16 and the harness remain pending. |
| Conditioned theorem in R01 — current development | [Main proof](./feasibility/R01_CONDITIONED_TRILEMMA_THEOREM.md) · [Self-review](./feasibility/R01_CONDITIONED_TRILEMMA_REVIEW.md) | Theorem over the R01 domain: information cut for every policy, regions for all three pairs and viable region; global-dependency family with K data items, arbitrary N and growing information cost. Success cases compatible with the trilemma. Independent review pending. |
| R01 theorem record and continuation | [Deliverable](./feasibility/R01_CONDITIONED_TRILEMMA_RELEASE.json) · [Current prompt at the end](./feasibility/CONTINUATION_PROMPT.md) | Paid technical context, explicit ledger and producers; keep source and historical experiments intact. Historical task snapshot; the current queue is cleaned. No new scientific execution in this update. |


<a id="cierre-del-núcleo-matemático--revisión-de-continuidad-v02"></a>

## Mathematical core closure — continuity review v0.2

4 October 2026. This update retains the already published proof and applies minimal repairs: reciprocal certificate multiplier, send/receive charge, consistent deadline and control without a normative verdict. It does not apply technologies.

| Current reading | Status |
|---|---|
| [Conditioned R01 theorem v0.2](./feasibility/R01_CONDITIONED_TRILEMMA_THEOREM.md) | Complete domain, certificate and all-policy cut; nonempty viable and trilemma regions; exact AVG/WC family frontiers. |
| [Audit and repairs](./feasibility/R01_AUDIT_CONTINUITY_AND_REPAIRS.md) · [Self-review](./feasibility/R01_CONDITIONED_TRILEMMA_REVIEW.md) | Self-reconstruction completed. M16 OPEN; independent fidelity M17 IN_PROGRESS. |
| [Preservation record](./feasibility/R01_AUDIT_CONTINUITY_RELEASE.json) | Scenario and historical files intact; no new scientific executions. |
| Next phase | Protocol defined; apply its steps to human escalation and whispering as the first technology. |

**Canonical reference — subsequent documentary status:** [R01 trilemma v0.2](./feasibility/R01_CONDITIONED_TRILEMMA_THEOREM.md), independent document with statement and proofs preserved. [Linked explanation](./Escenario-creatividad-validacion.md#r01-conditioned-mathematical-validation). Explicit thresholds b, δ and p; self-validation and external reviews acknowledged, remaining coverage delimited.


<a id="continuación-verificada-revisión-de-extensiones-y-tecnologías-por-mecanismos"></a>

## Verified continuation: extension review and technologies by mechanisms

4 October 2026. The published closure of core v0.2 was verified and the self-review of consistency of the three extensions was completed. Previous statuses are archived in full; the current queue replaces their continuation instructions.

| Current work | Evidence and scope |
|---|---|
| Mathematical core | [Single theorem](./feasibility/R01_CONDITIONED_TRILEMMA_THEOREM.md); observable cut made explicit and global budget clarified, without changing frontiers. |
| Three existing extensions | [Consistency review](./feasibility/EXTENSION_CONSISTENCY_REVIEW.md); scopes preserved and inherited hash discrepancies recorded, without executing checkers. |
| Ordered technology extension | [Protocol](./feasibility/TECHNOLOGY_EXTENSION_PROTOCOL.md): first isomorphic core, then additional mechanisms and acceptance/persistence proofs. |
| Human escalation and whispering | [First mathematical fiche](./feasibility/HUMAN_ESCALATION_WHISPERING.md): bound with shared information, sufficient-alert frontier and controls; conditioned cost and deadline. |
| Pending validation | M16 OPEN, M17 IN_PROGRESS; P08 retains the documentary discrepancies; integration, harness and campaign unexecuted. |
| Status | Four current tasks and three subsequent deliverables; all 55 IDs and historical criteria remain traceable. No new scientific validation is declared. |


| Virtual technology traversals — update at the end | Status |
|---|---|
| [Human escalation and whispering](./feasibility/HUMAN_ESCALATION_WHISPERING.md#virtual-traversals) | General explanation incorporated before the traversals; R1/R2/R3 examined under contract with positive controls. R2 recovers scenarios and R3-A preserves a residual region. |
| Continuation | Same queue: four active workstreams and three later stages. The first virtual delivery is complete; subsequent candidates reuse its structure. |
| Scope | Author's mathematical/virtual review; no real technology, campaign or new scientific execution. Previous rehearsals remain noncanonical partial annexes. |
| Document language | Current technology-extension profile, protocol, workplan and continuation are in English. Historical originals and prior README content retain their provenance and content. |
