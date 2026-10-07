# STAMP/STPA — completed scoped DDS review

<!-- DDS terminology revision 1 (2026-10-07): Stage A/B/C only; source scientific version and evidence unchanged. -->

Version0.1 · 6 October2026 · scoped completion edition, same author. This record was prepared against the then-current Stage A source at commitf7d8ed0846b301617197ade855d5237cbd2280f9 (method0.1, clarifications through0.1.4 and current M-floor/failure-type distinction). Under the current [DDS Canonical Method Index](../../../../../DDS_CANONICAL_METHOD_INDEX_v0.1.md), it is a **Stage A scoped completion record** using the [Stage A challenge–trajectory contract](../../../../../DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md); it is not another DDS method, Stage B architecture verification or Stage C native validation. Its crosswalk and conclusions are retrospective; only the separately frozen [boundary Run Card](./BOUNDARY_RUN_CARD.json) was registered before the new result-producing checks. Original cards, freezes, thresholds, scripts and results remain immutable.

**Closure:** performed within the stated analytical/local scope; valid partial DDS. Instrument success, sufficient mission delivery and deployment acceptance are separate. Unmeasured dimensions are unscored, never zero. Full commissioned/native/independent acceptance remains unestablished.

## Question, base and configured scenario

Can the derived maintenance controller permit useful maintenance while avoiding energized entry, interruption of required critical supply and unauthorized control? Can it deliver a legitimate deferment when maintenance cannot safely close?

Base: the authored finite maintenance/supply reduction and frozen selected STPA-derived control model; original run2026-10-06-02. STAMP provides a system-control perspective and STPA supplies hazard/unsafe-control analysis. The executed subject is our finite model produced by that analysis, not the analysis method's universal effectiveness or an industrial plant.

The10 selected narratives cover safe completion, stop not applied, unavailable feedback, supply/backup constraints, mandate, already-safe equipment and admitted/unadmitted deferment. Each retains its pinned private actual context and declared expected result. The64 enumerated contexts cover the discrete stop/entry pair, not every control, duration or organizational hazard.

## Stage1 — technology–problem extension and isomorphism profile

**Performed within scope; no inherited R01 kernel.** Losses L1–L4, hazards H1–H3 and the controller/process-model relation map the selected problem into declared control constraints. The correspondence is documentary plus finite executable realization; no equivalence to a physical installation or R01 is proved.

|Material surface|Correspondence and unresolved boundary|
|---|---|
|Objects/relations|Owner, controller, pump, supply/backup and access gate; real asset/process completeness unvalidated|
|Events/actions|Stop, plant response, entry/deferment; continuous plant dynamics and competing controllers absent|
|Observation/information|Controller view versus private actual context and plant callback; truthful current process-model observations are stipulated|
|Authority|Synthetic current mandate; real permits/responsibilities unvalidated|
|Cost/time|State-query, command and logical feedback counters; no physical duration or sensor/engineering tariff|
|Quality/outcome|I admitted maintenance; M admitted deferment; P realized H1/H2/H3; Ø unresolved; no population law|

No safety certificate, method-completeness claim, all-policy R01 transfer or physical equivalence follows. Continuous timing/duration, real loss severity and expert analysis coverage remain outside this scoped edition.

## Stage2 — mechanisms and interactions

**Performed within scope.** Context-sensitive interlocks, backup/mandate gates, stop-application feedback and a bounded admitted deferment change reachable outcomes relative to the deliberately open-loop diagnostic. Their source is the synthetic process model and actual finite plant callback; their validity is contingent on admitted observation/authority meanings. Commands, effect and evidence of effect are separate.

Stopping without admissible backup can violate supply; refusing every maintenance request loses useful I even if P is avoided; a deferment has M value only when the mandate admits it. An ordinary correctly configured interlock can implement these constraints and receives full credit. The open-loop arm is a misuse diagnostic, not a strong baseline.

Source/feedback burden, controller coordination, sensor validity, backup readiness and maintenance engineering are part of a real composition, but uncalibrated here. A duration-sensitive successor needs a time law and preregistered useful window before it can score delay.

## Execution and material-assumption challenge

Fresh repeat:306 assertions pass, including64 finite contexts; the10 narrative outcomes remain4 I,2 M,4 Ø and0 P. Open-loop misuse still yields5 realized violating cases, kept separate from qualified outcomes. Same-author repeatability is established, not independent analysis or plant safety.

Two new preregistered boundary checks challenge the truthful-view assumption:

|Case|Observed model behavior|Inference|
|---|---|---|
|T-TRUTHFUL-MODEL|One actual plant callback, stop confirmed, entry allowed, I|The selected finite closed-loop path works|
|T-FALSE-CURRENT-OBSERVATION|Actual pump running but view reports stopped; zero plant callbacks, entry allowed, P/H1|The implementation depends on truthful initial state and does not independently confirm this already-stopped branch|

The second check is outside the original truthful-process-model contract. It is not a newly attributed failure of STPA or a retroactive rescore. It exposes a genuine dependency of this derived implementation.

Both branches record feedback_checks=1: this is a logical model-check counter, not a count of actual sensor/plant callback invocations. The frozen Card's generic signature/hash cost wording must not be interpreted as executed STPA cryptography; actual measured fields are state_queries, commands and feedback_checks.

## Cost/Risk/Effectiveness, value and closure

Cost is finite logical operations; analysis effort, plant downtime, sensors, integration, staffing and elapsed useful-world time are unscored. Risk is the declared realized finite hazards; zero P in the selected qualified battery is not zero deployment risk. Effectiveness distinguishes I from useful M and Ø;4/10 is not a population success estimate. Business Value is conditional safe useful maintenance or admitted continuity-preserving deferment; outage/harm valuation and financial return are uncalibrated.

The instrument is accepted against its registered finite expectations. Deployment acceptance and analysis completeness remain unestablished. **Differential finding:** this scoped composition makes safe/admitted finite routes visible and exposes observation dependence; no superiority over a competent conventional controller or other safety-analysis method is established.

**Scoped closure:** the current question has been answered, including the false-observation boundary. A plant-specific claim requires actual control structure/loss review, sensor/backup/authority evidence and timing/actuation validation. Those are conditional next studies, not mandatory extra DDS deliverables.

Sources: [original report/Card](../independent-dds-exercises-v0.1/stamp-stpa/EXERCISE_REPORT.md), [MIT primary method route](https://psas.scripts.mit.edu/home/books-and-handbooks/), [new actual checks](./runs/2026-10-06-01/RESULTS.json), [repeat review](./REPRODUCTION_REVIEW.json). Original frozen source/outcomes remain unchanged.

## EA failure diagnostics and rework scope

The admitted deferment M is explicitly scored in this profile. It is reachable only when the selected mandate/supply context admits it; an Ø elsewhere does not establish failure to reach an available M. I/M/P/Ø and EA Type0/1/2 are different namespaces. P is classified here by the declared material violation; a causal false-qualification finding is required before calling it Type2. This edition retains any residual nondetermination and does not assign population failure-type rates. A hidden minimum-sufficient search/review witness and excess-work estimate are not computed; the reported ledger is actual model work, not proved optimal work. Omitting that optional diagnostic is proportionate to this edition's decision question.
