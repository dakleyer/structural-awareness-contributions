<a id="00g-r01-reducción-de-00g"></a>
# R01 Probabilistic exploration and validation cost

Base specification v0.6 · Reading organization 3 October 2026 · Non-canonical research study

[Complete base scenario](./Escenario-creatividad-validacion.md) · [Reductions](#reductions) · [Three extensions](#extensiones) · [Preservation record](./ORGANIZATION_TRACE.md)

[Differential and value of the experiment](./DIFFERENTIAL_AND_EXPERIMENT_VALUE.md): the technology–problem suitability map, cost/risk/effectiveness, related work, candidate contribution, oracle priorities and remaining review passes.

<a id="bot-start-here"></a>
## Start here — research work plans for bots

The canonical pending-work discovery label is **`R01_BOT_WORKPLAN_START`**, closed by **`R01_BOT_WORKPLAN_END`**. This is the existing label in the differential document; all plans below reuse it exactly. A scope attribute or task ID identifies a workstream, not a different discovery label.

| Order | Document and first task | Purpose |
|---|---|---|
| 1 | [Mathematical feasibility and infeasibility regions](./MATHEMATICAL_FEASIBILITY.md) — M01 | Define the claim and policy class; prove or reject a region, allowing it to be empty. |
| 2 | [Computability, bounded execution and oracle](./COMPUTABILITY_AND_ORACLE_PLAN.md) — C01 | Make the traversal and evaluator executable; verify correctness, termination and measured compute requirements. Inventory can begin alongside M01. |
| 3 | [Hugging Face concrete technology remaining tasks](./extensions/hugging-face/REMAINING_TASKS.txt) — T01 | Qualify three runtime configurations, implement adapters and test transfer against the checked contracts. |
| Continuing review | [Differential and experiment value](./DIFFERENTIAL_AND_EXPERIMENT_VALUE.md#robot-review-plan) — P01–P09 | Preserve and continue the earlier research, reference and editorial review tasks. |

From this R01 folder, find all work plans with `rg -n 'R01_BOT_WORKPLAN_START' .`. Read each plan's dependencies and evidence required for closure. These are staged research plans, not completed proofs, implementations or technology tests. Every plan includes adversarial audit, source/corpus coherence, readability, visual review and content preservation.

**Strategic review and complete execution prompt:** [Priorities, scores, 49 tasks and release gates](./STRATEGIC_WORKPLAN_AND_EXECUTION_PROMPT.md). Start with baseline/integrity triage (P08/C01), scope and measurement (M01/P03/P10), and targeted prior-art/counterexample review (P01/P02/M06). Then freeze C02/C11/C13 and build the tiny independent oracle. The table's document order is navigation, not a requirement to finish every mathematical task before implementation. The full campaign and later pilot-based selector have separate gates; qualify all three technologies, then stage their implementation through T11. All scientific/implementation tasks remain open.

The planning self-review reproduced all three extension finite reports, while the unchanged common audit still fails at the current scenario hash and all three extension README manifests mismatch. The [review evidence](./WORKPLAN_REVIEW_EVIDENCE_2026-10-03.json) distinguishes those scopes. Historical hashes are retained; repair remains P08.


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

From this `00G-R01/` folder:

```sh
python3 extensions/verify_audit.py --verify
```

The [common verifier](./extensions/verify_audit.py) runs the three checkers in temporary folders, compares their reports and verifies the textual hashes. It uses Python 3 and its standard library. The [common report](./extensions/audit_results.json) preserves results per package; it does not add them together as independent samples. The individual guides remain available in the extensions table.

This is an internal rerun of the published code, not an independent replication or an EA evaluation. The editorial procedure, content preservation and limits of this review are in the [package review](./extensions/EDITORIAL_REVIEW.md).

<a id="archivos-y-reproducción-editorial"></a>
## Files and editorial reproduction

The existing Word and PDF files preserve **v0.6 before the reading separation**. They include the former case chapter; the current separated reading edition is in Markdown. This section describes the exports of the **base scenario v0.6**. In the extensions, the current review is in Markdown; the Infoblox Word file preserves the v0.5 edition preceding its later additions, identified in its case record.

Markdown is the current text source; the retained Word and PDF files are exports of the earlier complete v0.6 text. The two figures and their scripts are in this package. `build_figures.py` regenerates the figures with Matplotlib and `build_document.py` regenerates Word with python-docx. The PDF is exported from Word with LibreOffice. The scripts resolve their paths from this folder. A simulator is not yet included: the experiment's executable rules remain pending.

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

