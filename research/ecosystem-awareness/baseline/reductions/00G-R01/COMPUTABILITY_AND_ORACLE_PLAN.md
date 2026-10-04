# R01 — Computability, bounded execution and oracle work plan

Research work plan v0.1 · 3 October 2026 · Implementation pending

[Start at R01](./README.md#bot-start-here) · [Mathematical feasibility](./MATHEMATICAL_FEASIBILITY.md) · [Technology integration tasks](./extensions/hugging-face/REMAINING_TASKS.txt)

## Objective and starting point

Make the declared R01 traversal and its evaluation executable, prove termination for the bounded model and measure the resources needed to reproduce it. Keep three costs separate: the agents' operational ledger, evaluator/oracle computation, and total experiment infrastructure. Computability, tractability at a declared scale and practical suitability of a technology are different claims.

The retained [C3 v0.4 oracle](../../fixtures/00G-HF-ORACLE-v0.4/README.md) checks authority, commitments, attempts, effects and completion in its original T0/X and T1/Y inspect domain. Its frozen package was rerun on 3 October 2026: 102/102 author-constructed controls passed and the verifier checked frozen hashes. These are evaluator controls, not R01 agent runs. The [R01 adaptation status](../../fixtures/00G-HF-ORACLE-v0.4/ESTADO_00G-R01.md) leaves the full optimum, resource ledger and collective evaluation open.

Preserve that package. Build a versioned R01 evaluator with explicit projections where C3 semantics actually apply. The existing extension checkers provide reusable witness ideas and independent comparison patterns; their simplified execution and observation rules are not the full receiver.

## Bounded implementation contract to complete

| Component | Required behavior and boundary |
|---|---|
| World generator | Freeze graph, lengths, benefits, geometry, connectors, mandates, predicates and seeds. Use finite encoded values; report conditioning/rejection. Keep I/P labels private. |
| Agent interface | Implement the charged explore, relation-inspection, mandate, evidence, state, communication and execution operations of §2.6. No free full-map answer. |
| Exact reference | Find maximum J over complete admissible effective trajectories, retaining ties and all connectors/mixtures. Small exhaustive enumeration is the first independent reference. |
| Trace evaluator | Reconstruct actual effects, valid completion, q, partial technical value, e, violation events, costs and censored latency under §1.4. Candidate verdicts are not ground truth. |
| Recorder and ledger | Record identity, versions, scope, evidence lineage, receipt times and every charge, including discarded candidates, retries, maintenance and execution. Coordination is included in total cost once. |
| Policy runner | Freeze CV-C0/CV-C1/CV-A0/CV-A1/CV-A2 rules for any executed contrast. A policy name is not an implementation; fixture scripts are not autonomous agents. |
| Reproduction bundle | Pin source, environment, parameters, random streams and commands. Store traces, certificates, rejected worlds, failures and timings with explicit coverage. |

Finite graph size alone does not guarantee finite execution: cycles, unbounded memory or zero-cost/zero-time events may allow arbitrarily long runs. Specify a finite event horizon or another well-founded termination argument, finite observations/actions and computable probabilities. If an added cap truncates legitimate R01 behaviors, declare the narrower submodel and the proof's scope.

Declare numeric encoding and input size. Exact enumeration may be exponential; a small successful run does not establish polynomial complexity or cheap execution at scale. An optimized evaluator must be checked against a separately implemented reference, not merely a second entry point into its own logic.

## First bounded target and acceptance

Use the small static first-campaign domain of R01 §2.15: global budget, common task, fixed profiles, separate conjunction and parity blocks. Declare the finite limits on L, population, branching, connectors, seeds and events before execution. Mixed predicates, changing dependencies, larger networks and EA comparisons remain later extensions.

The first delivery needs an end-to-end legitimate trajectory, an inadmissible executed trajectory where the declared policy permits such an error, a detected/blocked alternative, and an incomplete or abstaining run. Never script an agent to fail and present it as emergent behavior. Include a world where a connector changes the optimal admissible route.

Correctness gates precede cost claims. Set a concrete machine and maximum runtime/memory budget before benchmarking; record cold/warm runs, repetitions, timeout behavior and coverage. Report measurements for the tested sizes and an explicit complexity argument where available. Stop at the registered resource ceiling and retain inconclusive runs.

## Remaining tasks — staged bot work plan

<!-- R01_BOT_WORKPLAN_START version="0.3" scope="COMPUTABILITY_AND_ORACLE_PLAN.md" -->
Use the existing shared label `R01_BOT_WORKPLAN_START` and closing `R01_BOT_WORKPLAN_END`. Keep this plan in the document. Preserve task IDs and record owner, UTC date, input commit, code/environment versions, command, expected/actual outcome, evidence path and unresolved scope when changing status.

All tasks are OPEN. C01 can start alongside M01; C02 must agree with M01/M02. Technology adapter preparation can begin after the interface is frozen, but its verdicts require a checked evaluator. A failed mathematical candidate does not prevent implementing a neutral evaluator.

| ID | Stage and dependency | Evidence needed to close |
|---|---|---|
| C01 | Inventory and preserve existing code. | Reproduce C3 and relevant finite checks in isolation; list reusable functions, domain restrictions and hashes. Record inherited documentation-audit failures separately from executable-test outcomes. |
| C02 | Specify schemas and termination after C01. | Machine-readable world/trace/metric contracts, finite encoding, resource rules, event limits and a termination argument. Map every field and exclusion to R01. |
| C03 | Implement generator and independent exact reference after C02. | Correct M/I/P derivation, connectors, ties, fixed profiles and world rejection accounting; hand-checkable witnesses including a superior mixture. |
| C04 | Implement execution, ledger and evaluator after C03. | Charged operations, actual-effect adjudication, q/e/a/f/C/t/K semantics, abstention and late delivery, no cost duplication and no oracle leakage. Record any validated C3 projection. |
| C05 | Verify adversarially after C04. | Exhaustive tiny-world comparison plus targeted invalid traces, relabeling tests, revoked/irrelevant evidence, duplicated provenance, stale certificates and blocked-versus-executed effects. Separate independent reference code from implementation under test. |
| C06 | Make the bounded traversal reproducible after C05. | One command with pinned environment, declared finite policies, fresh recorder traces, seeds, outputs and replay. Demonstrate permitted improvement, rejection and incompleteness without forcing a negative campaign result. |
| C07 | Establish measured compute scope after C06. | Predeclared hardware/resource ceilings; time and peak-memory measurements as L, branching, population and horizon vary; include timeouts and evaluator costs. Distinguish measured sizes from asymptotic claims. |
| C08 | Deepen technical audit and corpus coherence. | Audit numeric precision, RNG coupling, policy competence and termination; verify references and interfaces against M01–M05 and E1–E7. Every unresolved mismatch has a disposition. |
| C09 | Review editorial quality, readability and visual aids. | A new bot can locate setup, command, expected outputs, failure handling and limits. Add a compact execution/evaluation diagram only if it clarifies actual boundaries; verify its rendered labels. |
| C10 | Preservation and final release audit after C01–C09. | File/tree diff, retained old fixtures and results, links, scoped hashes, frozen successor package and adversarial review record. Do not rewrite old freezes or claim independent validation from self-audit. |

Next bot starts at C01. Completion of this plan validates the declared implementation scope, not the entire mathematical claim, full campaign, or technology transfer.


### Strategic revision and execution gates — 3 October 2026

Planning revision v0.2; review against commit `1e940125a18f468268eff8f029a35c32a5f4ff08`. This is a documentary self-review, not a mathematical validation or independent review. Read the [master execution prompt](./STRATEGIC_WORKPLAN_AND_EXECUTION_PROMPT.md) for priorities, the complete task register and release gates. Existing IDs and acceptance criteria remain in force. New tasks are OPEN. A documentary revision does not close an implementation, proof or empirical task.

**Scheduling clarification:** reviews are recurring passes, not a reason to defer source checks, counterexamples or preservation until the end. Start P08/C01 baseline triage, M01/P03/P10 scope and measurement, and the minimum relevant P01/P02/M06 source-and-counterexample review together. Later passes complete their original criteria. Keep mathematical region proof, neutral evaluator implementation, base campaign, technology admission and prospective architecture selection as separate outputs. A rejected mathematical candidate does not block a neutral evaluator or a clearly scoped experiment.

**Shared closure record:** task ID/status, owner, actual UTC date, input commit, exact scope, assumptions, evidence paths, commands and outcomes, review disposition, residual limits and next action. No assigned owner is invented: use UNASSIGNED until responsibility is accepted. Different tasks may reference one evidence artifact, but retain their own acceptance decisions. Reopen affected tasks when a material contract changes. Independent review is desirable evidence, not a prerequisite for starting authorized internal work; self-review must retain its label.

**Implementation ordering:** resource ceilings and observation/schema requirements are fixed in C02/C11 before expensive implementation or benchmarking. C13 begins with C02 and has a checked disposition before campaign execution. C06 is an instrument/reproduction gate, not the statistical campaign itself. C12 adds the missing campaign execution and analysis; C14 is a later, separate selector study. A bounded instrument release may close a scoped C10 pass while C12/C14 remain OPEN; it must not claim completion of this whole plan. A campaign release requires C11–C13; a selector release also requires C14 and P11/P12.

| Added ID / status | Dependency and activity | Evidence needed to close |
|---|---|---|
| C11 — OPEN | Draft with M01/P03/P10; agree with C02 and freeze the campaign protocol before C06/T05. | Early runtime/memory/API-spend ceilings and stop rules; development/calibration vs held-out sets; primary contrasts and independent analysis unit; margins/thresholds, sample/precision justification, grouping, paired randomness, multiplicity and censoring; missing, timeout, retry and infrastructure-error handling. Zero violations has an upper uncertainty bound; insufficient precision gives an unresolved verdict. Scope/resource contract precedes C03; statistical freeze may use development calibration only. |
| C12 — OPEN | After C05–C07, C11 and C13, execute and analyze the bounded base campaign. | Registered finite grid and competent frozen policies; full paired world/campaign traces, costs including no-delivery runs, q/e/a/f/C/t/K and uncertainty; held-out results, mechanism ablations, Pareto/tradeoff report and an adequate/inadequate/unresolved map for evaluated policies. Publish deviations, exclusions and negative results. Distinguish policy failure from a theorem about all policies. Technology campaigns additionally need T04/T05 evidence. |
| C13 — OPEN | Begin at C02; complete after C05 and policy qualification, before C06/C12. | Audit accidental hints and generator conditioning; training/memory/tuning isolation; compatible information and resources; randomness stream coupling; comparator competence on positive controls; replay interventions vs total effects. Check environment receipts against SDK traces and inspect policies for accidental oracle access. Declare intentional predictive factors; absence of detected leakage is not proof of its absence. |
| C14 — OPEN | Later stage after C12 and a separately frozen P11/C11 selector protocol. | Implement recommend/advise-against/indeterminate using only eligible small-pilot observations; isolate selector development and held-out evaluation, including held-out families when claimed. Compare simpler selection rules and competent alternatives; score false recommendations, missed opportunities, abstention/coverage, diagnostic/oversight costs and budget. Retain independently judged outcomes; an architecture cannot certify its own recommendation by assertion. No claim of scale transfer without P12 evidence. |

**Cost containment:** exact tiny-world correctness comes before optimization and broad runtime integration. A solver timeout is an evaluator failure/unknown reference, not automatically an agent failure. Freeze handling of absent complete admissible routes, ties, encoding precision, exhausted budgets and horizon truncation. Exclude only under registered rules and retain rejection rates. A scope change requires a new registration and affected reviews, not silent post-result tuning.

### Orden vigente — controles al servicio de la demostración

Reorganización v0.3: [plan rector](./STRATEGIC_WORKPLAN_AND_EXECUTION_PROMPT.md#mathematical-strengthening). C01–C14 siguen OPEN; sus criterios no se eliminan. C01/P08 hacen triage acotado mientras M12 fija el teorema. C02–C05 preparan primero un instrumento pequeño para F/W y sus controles, con perfil suplementario explícito y sin confundirlo con el oráculo completo de R01; la entrega general conserva obligaciones propias. Los primeros límites de C11 son de recursos/alcance; su registro estadístico se completa antes de campañas, no es un prerrequisito de una prueba simbólica.

M16 es revisión de las demostraciones por otro revisor; M05/C05 son comparación finita independiente. C05 requiere segundo método/código separado del autor, sin importar su recurrencia. Comparar resultados semánticos normalizados por mundo/política/traza y aritmética; dos métodos válidos no necesitan serializar bytes idénticos. Reproducir el MISMO checker sí puede exigir reporte idéntico. Conservar discrepancias. Implementación independiente por el mismo autor no equivale a revisión simbólica independiente.

No ampliar el instrumento ni optimizar antes de fijar qué afirmación ayuda a verificar. C06–C13 y campaña siguen G4; C14 sigue G5. Preparar un evaluador neutral no cierra M03/M04, M13/M17 ni el estudio de selección. Un resultado experimental separado puede continuar si no se reclama transferencia pendiente. Los próximos pasos históricos abajo quedan subordinados al plan vigente.


<!-- R01_BOT_WORKPLAN_END -->
