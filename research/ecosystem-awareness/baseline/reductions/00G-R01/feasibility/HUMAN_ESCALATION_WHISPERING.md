# R01 — Human escalation and whispering, mechanism by mechanism

Mathematical version 0.1 · Virtual traversals 0.3 · DDS research document addition 0.1 · 6 October 2026 · First deterministic model self-test; no native human/vendor integration.
[Protocol technologies](./TECHNOLOGY_EXTENSION_PROTOCOL.md#technologies-to-study) · [Single base theorem](./R01_CONDITIONED_TRILEMMA_THEOREM.md).

## DDS profile status

This study is a **rich virtual DDS implementation profile over R01**, not a separate test method. The canonical DDS terminology is defined in the [DDS Challenge–Trajectory Profile](../../../../DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md); the R01 mathematics below remains source-native and unchanged.

| DDS surface | Current Human Escalation / Whispering coverage |
|---|---|
| Challenge / scenario | R01 AVG family and the fixed R1/R2/R3 contracts |
| Preserved correspondence | §1 / E1–E7 mapping; complete-system R2 correctly identified as non-isomorphic to R1 where observation/enablement changes |
| Additional mechanisms | H0–H4 information, notification, pause, human evidence/authority, dissemination and composition |
| Route space | X/Y/M plus irreversible V and incomplete/timeout branches; DDS I/M/P/Ø normalization is additive and must not rename the R01 source semantics |
| Segments / gates | detect → escalate → pause → human resolution → resumption → delivery; gate coverage and restart conditions explicit |
| Probability / observation law | q, conditional histories and R3 availability/validity changes |
| Cost | h, C_H, repeated work, budget and deadline |
| Risk | r / material violation V |
| Effectiveness | s / sufficient legitimate delivery |
| Acceptance | `A_{b,δ,p}` |
| Business Value | not defined; requires a concrete deployment-specific projection |
| Evidence | mathematical/analytical + virtual traversals; no calibrated human or real technology campaign |

**Remaining DDS completion work** is therefore not to invent another test: preserve the R01 contract, make the I/M/P/Ø crosswalk explicit for reporting, freeze the future harness trace schema, and add Business Value only when a real deployment interpretation exists.

Whispering here means notifying the rest of the group when an agent identifies a problem. Any agent can initiate direct escalation. The human examines the evidence and can order a pause or a legitimate alternative. This is the mechanism requested by the user; no specific quotation is attributed to Nell, and no claim is made that a particular product implements it.

DDS correspondence. This mechanism profile supplies analytical technical evidence for a Deployment Differential Study. Preserve R01 Cost–Risk–Effectiveness and the original q/h/p laws; a declared deployment adds a separate Business Value–Risk–Cost interpretation. The first [canonical HEW DDS research record](./HEW_DDS_STUDY_2026-10-06.md) now includes human-readable scenario selection, scope, freeze, exact reconstructions and a bounded SQLite model integration. These are neither measured human effectiveness nor a completed commissioned DDS.

<a id="why-it-can-help"></a>
## 0. Why this technology can help before its traversal

Human escalation and whispering can recover scenarios for four distinct reasons. One agent can provide a sufficient witness that the collective decision does not yet have. Its notification can reach the human directly even if the group favors another action. An effective pause can reserve time to resolve uncertainty, and the human response can provide additional legitimate evidence that enables completion of an alternative of sufficient quality. Dissemination prevents others from executing on an invalidated decision. Each capability must be checked: notification does not mean stopping, repetition adds no independence, and being human does not mean knowing the answer.

| How it can help | Condition it can shift | Necessary condition |
|---|---|---|
| New evidence or a sufficient certificate | Reduces the mass of ambiguous histories and the minimum risk frontier for a given efficacy. | Legitimate source, sufficient scope and full production/use cost. |
| Direct notification and dissemination | Reduces majority veto, duplication or delay in sharing a fact. | Recipients, causality and acknowledgments; copies do not count as new sources. |
| Pause before effects | Allows review before an irreversible violation. | Gates controlled before the effect; resolution and delivery still within T. |
| Applicable human decision | Enables selection and coordination of a sufficient legitimate route. | Current evidence, original mandate, executable alternative and a new commitment. |

An affordable sufficient source can help substantially; another person processing the same evidence preserves information cut H0. A pause that never ends can improve safety and lose efficacy. Mandatory review can increase cost or delay and lose previously acceptable scenarios. These are candidate improvement mechanisms, not an advance conclusion that all scenarios will be resolved.

### 0.1 The complete chain: detect, escalate, stop and restart

Improvement does not depend only on an agent detecting something. It must recognize that escalation is needed, find the channel, reach the human and explain the problem sufficiently. The human must be able to resolve it and intervene in the affected effects. The pause or kill switch must be admissible for that mission. There must then be a different, legitimate way to continue within cost and deadline. Failure at any step can leave the scenario outside the accepted region.

| Necessary step | What can fail | What is charged or verified |
|---|---|---|
| Detect and recognize the need to escalate | Shared blind spot, insufficient witness or no criterion for escalation. | Inspection, sufficient evidence and coverage; more agents do not guarantee independence. |
| Find and invoke the process | Unknown or unavailable channel, consensus blocking or missing permissions. | Channel discovery, integration, access and maintenance. |
| Reach the human and explain sufficiently | Lost message, queue, incomplete or misunderstood case. | Transport, case preparation, interaction and delay. |
| Resolve with sufficient human capability | The same insufficient information, error or no authority over the gates. | New source if available, human work, competence and intervention scope. |
| Stop admissibly | The effect already occurred; the gate does not cover everything; shutdown causes another violation. | Actual state, safe interruptions, transition or handover and continuity obligations. |
| Restart on a corrected basis | The same inputs are repeated or the alert is lost; the alternative is not validated. | Relevant new evidence, validity, justified strategy change and a new commitment. |
| Complete the mission | The correct restart arrives late or consumes too much. | Accumulated cost, repeated work, deadline and final legitimate quality. |

Full cost can be high, but is not claimed to be necessarily high in every scenario. Decompose h into detection, channel discovery, case/transport, human review and evidence production, safe pause, correction and reentry. Repeated work and relevant preparation/maintenance costs are also paid. If pause and correction are not already included in h, add them without double counting. A delivery costing C_0+h+c_rehecho requires C_0+h+c_rehecho≤b; the causal chain and queue must also leave delivery within T. High q does not compensate for exceeding those limits. The existing symbol c_rehecho denotes repeated-work cost.

**Reliability belongs to the chain, not the isolated detector.** Let E_1,…,E_6 be the events of the first six steps: a valid intervention available before the effect, with a feasible continuation. Define q_cadena=P(∩E_j | χ=1), retaining the existing symbol for chain reliability. The chain rule gives the product of P(E_j | χ=1,E_1,…,E_{j−1}) when its conditioning events have positive probability; if a prefix has zero mass, q_cadena=0. Do not multiply marginal rates as though the stages were independent. Actual completion is also evaluated in s.

This identity audits coverage; it does not automatically substitute q_cadena into H1. The H1 frontier requires the laws of all histories, branches without a signal, costs and responses to satisfy its hypotheses. A failed message, partial intervention or delay can reveal information and produce other outcomes; those profiles are recalculated. In the R2 example, the chain was stipulated to be reliable once Z was obtained: **neither a real realization of that chain nor its cost was demonstrated**.

**Critical mission.** A kill switch is not safe by definition. The admissibility predicate also includes shutdown, pause, transfer to a backup and resumption. A critical mission may allow an emergency stop or require continuity/handover. If shutdown is forbidden, it cannot be used to obtain zero risk; if it is legal but prevents sufficient quality, that efficacy failure is retained. A relevant safe transition must be demonstrated, rather than assuming that every critical mission is interruptible or that none is.

**Different restart.** A new commitment avoids using an old permission, but that alone is insufficient to correct the decision. Reentry requires sufficient evidence for the alternative, applicable scope/validity and a strategy that uses that basis. If the objection remains unresolved, the preventive controller retains the block or a safe route; it does not erase the case and return to the same path P. Here P informally denotes the incorrect path described by the user, without renaming routes X/Y/M or the corpus's I/P notation.

**Reading sequence:** this explanation → isomorphic kernel and mechanisms H0–H4 → [virtual R1/R2/R3 traversals](#virtual-traversals) → partial rehearsals and later stages. The traversals close the examination of their declared contract. Coverage of an entire family also requires a quantified argument over that family.

## 1. First: what is isomorphic and what changes

| Component | Correspondence with the R01 kernel | Additional study |
|---|---|---|
| Detect a fact through an already admitted query | Query, evidence, scope, version and cost. | A sensor revealing something new changes the observation kernel. |
| Notify another agent | Send and receive, preserving causality and origin. | Broadcast with different latency, topology or price induces θ*. |
| Forward evidence to the human | Message to a participant with the same evidence. | Prior information or an additional human query must be incorporated. |
| Human decides using only that history | Observable strategy; human identity produces no new information. | New authority, source or information capability requires another contract. |
| Pause before the effect | Wait/gate if its transitions already exist and are preserved. | Mandatory crowd freeze and alert priority change enablement and scheduling. |
| Resume or choose another route | Decision and effect with gates and mandate preserved. | A legitimate alternative of sufficient quality must exist. |
| Contain subsequent effects | Stop/recovery and irreversible recording of V. | Does not eliminate a violation already executed. |

This table is insufficient to call a component isomorphic: its realization must satisfy E1–E7 relative to the effective scenario. A composition adding a human source or a new pause may preserve a kernel while not being isomorphic to the previous technology.

### 1.1 Virtual E1–E7 check: kernel and complete system

| Obligation | Preserved part | Change kept explicit |
|---|---|---|
| E1 — objects and relations | Identity of task, agent, route, normative relation and commitment; same admissibility predicate. | Source, human case and certificate are additional objects with producer and scope. |
| E2 — events and enablement | Queries, messages, review and execution remain typed and causal. | The preventive phase adds a block; enablement is not equal to R1. |
| E3 — transitions and laws | The world's law and normative readings in the example do not change between R1 and R2. | The new channel Z and pause/resolution states are modeled, not removed by projection. |
| E4 — observations | Histories, provenance and evaluator boundaries are preserved. | Z distinguishes worlds: the complete system does not preserve R1's view and is not isomorphic to it. |
| E5 — cost and time | Same units, ledger, deadline and acceptance thresholds. | h and the phase duration are additional, charged even without an alert. |
| E6 — outcomes | Same high quality, legitimate routes and irreversible V; alternative M is preserved. | Pausing or issuing a GO does not count as delivery or erase V. |
| E7 — coverage and positives | Routes X/Y/M, complete queries, incomplete endings and observable adaptations included in the contract. | The mandatory phase restricts immediate execution; not every R1 trajectory is presumed to lift with equal cost/time. |

The relational kernel correspondence is explicit. **Complete system R2 is not isomorphic to R1:** equivalence fails in observation and enablement precisely because capabilities are added. The H1 frontier is proved directly for the extended contract; impossibility is not transferred through a nonexistent isomorphism. Operational isomorphism with an effective scenario θ*, or implementation membership, requires verifying all its transitions and views, as the protocol establishes. The table does not grant that result from the technology's name.

## 2. Mechanism H0: sharing and escalating without new information

**Proposition H0.** Suppose messages, inferences and human responses are functions of legitimately acquired history and seeds independent of the world. Every new datum retains its acquisition charge; no authority changes the mandate. In the K-datum parity family, with C_0≤b<C_0+K, base bound r≥((1−a)/a)s remains valid for all such strategies.

**Proof.** The base theorem's collective envelope already receives all evidence acquired by all participants. It can reproduce seeds, messages and human decisions without requiring more data than that history. Before all K data are acquired, every reading prefix has the same distribution under the two parities; the posterior remains a. Further processing of that history does not distinguish the two laws. The first irreversible effect and producer cost are preserved, hence I1–I3 and the bound. ∎

Pooling and broadcast may still reduce duplication or latency for a particular strategy. The lower-bound proof already granted free instantaneous pooling: improved coordination alone does not defeat that information relaxation.

An agent cannot declare X incorrect in the parity profile based on an isolated bit that does not determine it. For a conjunction predicate, a single false fact can be a sufficient witness. Identify the predicate and evidence scope before assigning a detection probability.

## 3. Mechanism H1: a sufficient alert before the effect

An additional information contract H is defined to calculate its effect without pretending that an implementation exists.

Hypotheses:

1. The mandate, two worlds χ and high-quality routes X/Y of the kernel are preserved; P(χ=0)=a, 1/2≤a<1. X is correct in χ=0 and Y in χ=1. M is legitimate but does not achieve the required quality.
2. A detection phase completes before any critical effect. Alert Z=1 is a reliable witness of χ=1; there are no false positives. P(Z=1|χ=1)=q and P(Z=1|χ=0)=0, with 0≤q≤1.
3. The human receives the witness in time, verifies its applicability and selects Y. Without an alert, the remaining history distinguishes the worlds no further than the absence of the alert. Controller seeds add no information. Before complete additional acquisition, permitted partial data have the same law under both χ conditional on Z, so they do not change that posterior. This covers all adaptive histories, metadata and responses, not just the constructed controls.
4. The manifest charges a full fixed amount h for the phase, including producer, detector, human availability, notification and dissemination; C_H=C_0+h. This common tariff makes cost analysis precise. If an implementation charges by branch, its ledger and maximum are recalculated rather than imposing this tariff.
5. In the analyzed band C_H≤b<C_H+K, no cheap delivery acquires sufficient additional information. Complete queries remain permitted at cost outside b; the physical cap and deadline admit that informed control.
6. The alert phase precedes the effect, with gates, causal order and no omitted channels. Every cheap success must get the first effect right.

These hypotheses define a complete study scenario. They do not establish high q or low h in a real technology. In particular, if producing the witness requires reading all K data, that work is charged within h. Prior or amortized human data require explicit preparation and horizon.

### 3.1 Exact frontier of contract H

Let g=(1−a)q and n=(1−a)(1−q). Mass g contains reliable resolved alerts. The no-alert branch contains mass a of χ=0 and mass n of χ=1. By Bayes, its posterior of χ=0 is a/(a+n), not a.

**Theorem H1.** For every cheap strategy of contract H:

$$
s\le a+g,\qquad
r\ge\frac{n}{a}(s-g)_+,
\quad (z)_+=\max(0,z).
$$

For 0≤p≤a+g, the minimum attainable risk at efficacy s≥p is exactly

$$
r_{\min,H}(p)=\frac{(1-a)(1-q)}{a}\,
\bigl[p-(1-a)q\bigr]_+.
$$

**Necessity proof.** In the alert branch, success contributes at most g; other decisions can only add violations. In the no-alert branch, selecting X and Y for the first effect gives success/risk masses a/n and n/a respectively. Decisions use the same history without a decisive signal. Let β_X be the conditional probability of attempting X there and β_Y that of attempting Y, with β_X+β_Y≤1. Since a≥n, each choice has risk/success ratio at least n/a, and success in that branch is at most a. Later failures reduce success; later violations increase r. Thus s≤a+g and r≥(n/a)(s−g)_+. This reasoning covers all history-dependent strategies, not just the following control. ∎

**Control attaining the bound.** If p≤g and g>0, execute Y for a fraction p/g of alerts and abstain in other branches: s=p,r=0. If g<p≤a+g, execute Y for every alert and X without an alert with probability β=(p−g)/a; otherwise abstain. Keeping the chosen option across every layer, with its gates and without requesting the evaluator's verdict, gives s=g+aβ=p and r=nβ. Its ceiling is C_H. For g=p=0, abstention suffices. ∎

The frontier is exact for this contract and band. It does not assert optimality of a framework or every escalation design.

### 3.2 Scenarios entering the accepted region

To compare with the base bound, preserve p,δ and require both strategies to fit the total budget. If

$$
\frac{1-a}{a}p>\delta
\quad\text{and}\quad
\frac{(1-a)(1-q)}{a}[p-(1-a)q]_+\le\delta,
$$

with p≤a+(1−a)q and C_H≤b<C_0+K, the base bound excludes acceptance while control H achieves it. This common band requires h<K and sufficient budget for h: neither is assumed for free.

**Algebraic** example, without running an experiment: a=0.99, p=0.95, δ=0.001. The base frontier is 19/1980≈0.009596. If q=0.9, the H frontier is 941/990000≈0.0009505, below δ. Under the preceding cost and time conditions, the scenario enters the accepted region. The control has β=941/990 and success 0.95. q=0.9 is a hypothesis of the example, not a measured rate for humans or agents.

### 3.3 Residual trilemma region

For each q<1 in the contract, n>0. Choose

$$
g<p\le a+g,\qquad
0\le\delta<\frac{n}{a}(p-g),
\qquad C_H\le b<C_H+K.
$$

CR is attainable using M; CE through the preceding control; RE by acquiring all additional information and completing the correct route at cost C_H+K>b. Bound H1 excludes CRE for every cheap strategy. A nonempty conditioned trilemma region therefore remains in this contract, with the same thresholds for each pair.

For q=1, an alert means χ=1 and its absence at phase completion means χ=0. The control always selects correctly: s=1,r=0 at C_H. **The preceding residual region disappears.** No claim is made that other task, search or deadline obstacles disappear.

Persistence for a fixed technology requires proving membership in a class with residual q<1 or resolution cost/time still outside some budgets. It does not follow from using humans, having positive cost or returning a one-bit answer.

## 4. Mechanism H2: what “one agent is enough” contributes

If D_i means that agent i obtains a timely sufficient witness of the same problem, then

q=P(∪_i D_i | χ=1).

Always max_i P(D_i|χ=1)≤q≤min(1,Σ_i P(D_i|χ=1)). If conditional independence is demonstrated, q=1−∏_i(1−d_i). Independence is sufficient for this formula, not necessary; numerical coincidence does not prove independence. Copies of the same receipt do not establish independence. Perfect correlation can leave q unchanged as N grows.

A specific conjunction case: exactly one invalid fact is uniformly distributed among K positions without clues; agents inspect a set of m distinct positions. Then q=m/K: the union detects exactly when it contains the witness. Pooling avoids repeated work; more agents can reduce rounds without making m distinct queries free.

This conjunction case is not interchangeable with the parity family. It also does not by itself guarantee H1's alternative Y: a sufficient affordable permitted route must be proved to exist after the witness. If the human only orders a stop or return to M, risk decreases but efficacy may be lost. This is recorded as another contract.

## 5. Mechanism H3: pause, queue, dissemination and concurrency

Actual detection, notification, queue, review and instruction-propagation times must be compared with the first effect. A sufficient condition for ordinary receipt is that their sum finishes before every affected effect. An atomic preventive barrier can keep effects blocked until a response; resumption and delivery must then still fit within T.

Sending the notification does not imply that everyone received it or stopped. The contract must specify who initiates the freeze, which effects were already in progress, which tools can be interrupted and when execution resumes. An alarm message does not by itself change permissions or cancel irreversible operations.

Later detection can prevent subsequent violations and reduce severity or the number affected. For r=P(at least one violation), V cannot be erased from a trajectory where it already occurred. Containment improvement is measured separately, without presenting it as a retrospective reduction of r.

## 6. Mechanism H4: human error and false alerts

With false-positive rate f=P(Z=1|χ=0), choosing Y on an alert with probability α and X without an alert with probability β gives, in the decision profile without other sources,

s=(1−a)qα+a(1−f)β,
r=afα+(1−a)(1−q)β.

This is a construction, not the complete frontier: other human responses or decisions require optimizing the extended contract. The human must confirm the witness or record the error; “escalated” does not mean “correct.” Correlations, version, scope and delays must enter the joint law. Formula H1 applies only when f=0 and detection/response satisfy its hypotheses.

### 6.1 Restarting does not remove the information cut or past risk

**Proposition H5 — restarts without new information.** In contract H0, allowing pauses and finitely many restarts, with choices and seeds independent of the world conditional on observable history, does not reduce bound r≥((1−a)/a)s when c≤b<C_0+K. The ledger and entire campaign are preserved; no information channels, permissions or omitted sufficient alternative are added.

**Proof.** The complete pause/restart policy is adaptive over collective history. The base theorem's envelope already admits these decisions and seeds. Acquiring fewer than K distinct data preserves posterior a before the first high-quality effect; repeated readings or regenerated messages do not change this. A trace resolving χ and completing a high-quality delivery would incur at least C_0+K>b. Cut I1–I3 therefore still applies to the campaign's first effect and gives the same bound. Restarting does not reset budget, clock or V. ∎

This conclusion does not require every attempt to produce exactly the same action: changing a seed can change the route without adding information about which route is correct. Nor does it exclude improvement through new data, a sufficient sensor or an already legitimate alternative; those change the hypotheses and require recalculating the frontier. With an H1 source and restarts adding no observations beyond the same Z, bound H1 likewise persists because its proof already covers the complete adaptive history.

**Persistent blind spot.** If, conditional on χ=1, the same source deficiency has probability 1−q and persists through all restarts, the probability that no agent produces a sufficient witness remains 1−q regardless of restart count. It is not (1−q)^m: that formula requires conditionally independent attempts. This profile exhibits the user's case: the group can repeat path P without whispering or escalation because no sufficient alert appears.

If a valid alert occurred and is retained, repeating an action already known to be forbidden **violates controller R2**. That behavior is not forced to obtain a negative. A conforming controller stays blocked or uses a safe alternative while no sufficient correction is available; it may lose efficacy or deadline compliance. Erasing the alert and restarting blindly is a realization defect, retained as such rather than as a refutation of the mathematical contract.

Finally, if V_j is a violation on attempt j, the entire campaign's risk is P(∪_j V_j)≥P(V_j) for every j, without independence assumptions. A later correct delivery does not make a campaign with an executed violation legitimate. Recovery or damage reduction may be measured separately while retaining original r and s.

<a id="virtual-traversals"></a>
## 7. Virtual traversals of the technology extension

### 7.1 Reused structure and scope

The [00G R1/R2/R3 distinction](../../../00G_HF_ROADMAP_R123_EA_COMPOSITIONS_UC4_v0.1_DRAFT.md), [Napoleon positive control](../../../00G_SUCCESS_MODEL_CASE_SOURCE_AWARE_FRAME_STABILITY_v0.1.md) and [00H positive control](../../../00H_SUCCESS_MODEL_CASE_PRESERVE_WITHOUT_OVERREACH_v0.1.md) are reused. Their obligation remains: reject false change and allow legitimate change; preserve the finding and complete authorized work. Their results are not automatically transferred to this technology, and their requirements catalog is not redefined.

| Traversal | What is fixed | What is examined |
|---|---|---|
| R1 — competent reference | Task and ordinary controls without the additional mechanism being studied. | Nominal quality, known prohibitions, alternatives and reference frontier. Do not manufacture incompetence to obtain a negative. |
| R2 — mechanism and quality plan | Same task, world law and thresholds; new capability and all its charges declared. | What it detects and adds, who decides, which effect it prevents and how it completes a sufficient legitimate route. |
| R3 — change with R2 frozen | Same R2 controller, gates, rules, permitted sources and internal parameters; a declared environmental condition changes. | Coverage, validity, delay or concurrency, with the corresponding positive control. Do not repair the controller after observing the outcome. |

R1/R2/R3 are traversals; with/without mechanism are comparison arms within them. R3 does not mean removing a defense. A particular passing traversal constructs a possibility. A failing traversal is a counterexample for that controller. Impossibility for all strategies needs a separate bound, supplied below for R1 and R3-A. Passing a finite list does not demonstrate acceptance throughout R01.

### 7.2 Complete virtual contract of the example

Fix the AVG family of §3: L=2, N=3, K=100, a=99/100, high quality for X/Y and insufficient quality for M. The mission and its parity rule are fixed; χ determines which high-quality route is legitimate without granting new authorization. Alternatives, local queries and the K normative data of the base theorem are preserved. Each acquired normative datum costs 1; maps, metadata and partial readings have the noninformative law declared in that theorem.

Common thresholds are b=50, δ=1/1000 and p=19/20. Global physical budget B=140, T=180 and H_cap=200 are equal in both arms and admit the expensive informed control. Accounting is the same: C_0=7L+2N=20; acquiring all K data and delivering costs 120. Increasing the cap relative to the theorem's minimal example does not change its bound for traces with c≤50. Resources are not multiplied by agent count.

R2 adds a legitimate technology source distinct from the private evaluator: it can provide the detector with a certificate of χ=1 before the effect. The source has declared access to that property; its production, relevant preparation, delivery and use are included in the phase tariff. This is additional information nonisomorphic to R1, not a cheap inference from one parity bit. **Whether a real source can meet that tariff remains unproved.**

Contract H for this traversal fixes a common phase costing h=20, with additional duration/event cap at most 20. Its virtual ledger reserves 5 for source/producer and preparation, 3 for detection/human review, 6 for sending/receiving the case and the two remaining notifications, 3 for pause/acknowledgments and 3 for application/resumption. These are stipulated contract charges, not measured prices. The common tariff is paid even without an alert: C_H=40. Complete informed delivery costs 140 and fits B. The sufficient base time bound is 5L+K+2N+4=120; adding 20 gives 140≤T. The additional cap also fits H_cap.

The new channel's law is fully defined: Z=0 if χ=0; if χ=1, Z is Bernoulli(q), independent of the normative vector conditional on χ. Everyone receives the result at the same phase ending; before the effect, timing, metadata, human responses and communications reveal no other information. Incomplete normative readings remain unable to distinguish χ conditional on Z. No omitted sufficient sources are permitted. In R2, q=9/10; R3-A changes environmental source availability to q=4/5 while preserving its procedure and the controller.

The preventive gate blocks every high-quality effect until the phase ends. A certificate must match the current episode, task, rule and version and cover the entire route. A single agent can open the case directly; no majority is required. The human verifies the evidence, preserves the mandate and responds Y only to an applicable witness. Notifications to others include scope and version; gates invalidate the previous commitment and confirm application before resumption. The evaluator's χ and V are not delivered to the human. In this common-tariff profile, the phase belongs to the workflow; an optional profile requires its own accounting. In the common band b<C_0+K, the arm without the phase also cannot resolve χ through paid readings.

### 7.3 R1 — competence and reference limit

The reference controller reviews and respects known prohibitions, verifies scopes and completes a nominal route; it does not receive and ignore a negative response to force failure. Inspections of all K data are available, and the informed control always selects the correct route with c=120, r=0, s=1. It is competent, although this control fails c≤50. M is a legitimate alternative with c=20 and r=0; it fails the high-quality requirement and gives s=0.

For low cost, the optimal control attempts X with β_1=p/a=95/99 and uses M otherwise. X is kept across both layers, with reviews and commitments, without querying the evaluator. This gives c=20, s=19/20 and r=19/1980. By the base theorem's cut for all strategies, no other strategy has c≤50, s≥19/20 and r≤1/1000: 50<120 and 19/1980>1/1000.

All three pairs are covered: CR by M; CE by the optimal gamble; RE by the expensive informed control. Success in a favorable R1 configuration does not refute this conditioned impossibility; failure of an isolated strategy does not prove it. The proof is the universal bound in this band.

### 7.4 R2 — positive traversal and acceptance movement

The quality plan is fixed before R3: execute Y with a sufficient current certificate; if the phase ends normally without an alert or conflict, attempt X with β_2=941/990 and otherwise complete M. β_2 is a fixed internal probability. Absence of an alert is interpreted only after the phase, not as a guarantee of legitimacy. A received but incomplete, expired or incompatible alert opens review and keeps high-quality effects blocked until resolution; it is not reclassified as normal silence. Timeout retains the block and allows M if still legitimate and feasible. These rules already belong to R2, although H1's ideal law produces no defective receipts. Every route uses its gates.

The same plan requires the pause to be admissible for the mission, including a safe handover where applicable. Resumption requires resolving the objection with evidence applicable to a sufficient alternative, and preserving the case, charges, clock and V. Merely restarting does not release the gate. The ideal example assumes these conditions hold; subsequent branches test them without later changing this rule.

| Causal step | Virtual observation and action | Quality check |
|---|---|---|
| Detection | An agent obtains a certificate or ends the phase without one. | Distinguish suspicion, copy and sufficient witness; charge the producer. |
| Escalation and whispering | That agent sends to the human and other affected participants. | Direct access, common lineage, scope, version and acknowledgments. |
| Pause | Gates blocked before the first high-quality effect. | Confirm gate state; sending alone does not prove a freeze. |
| Human resolution | Review the certificate; Y on an applicable alert. | No mandate change or permission expansion; legitimate high-quality alternative in χ=1. |
| Resumption | Decision disseminated and a new commitment for the current version. | No reuse of invalidated commitment; every affected effect covered. |
| Delivery | Keep the selected route across both layers. | Sufficient quality, ledger and end-to-end time; record V if it occurs. |

**Positive controls.** In χ=0, repeated rumors without a certificate do not displace the binding frame: attempting X remains legitimate and a known prohibition is respected. In χ=1 with a sufficient witness, the justified alternative Y is accepted and the task completed; blocking everything is not the response. A partial or doubtful notification is not used as a global certificate. M preserves legitimate low-quality work, recorded as such and not counted as high-quality success.

Alert mass is g=9/1000 and residual erroneous no-alert mass n=1/1000. By H1 and the preceding control:

$$
c=40\le50,\qquad s=g+a\beta_2=19/20,
\qquad r=n\beta_2=941/990000<1/1000.
$$

Full cost and deadline fit. This scenario therefore moves from not accepted in R1 to accepted in R2, with the same thresholds. The construction is virtual and probabilistic: the risk limit admits residual mass rather than requiring every individual episode to succeed. The control is not an infallible barrier against absent alerts.

The general explanation of §0 is proved here for this contract; q=0.9 and h=20 are not asserted to be observed properties of a person or framework.

### 7.5 R3 — same R2, changes and positives

β_2, the complete current certificate requirement, gates, timeout and resumption are frozen. Timeout or inapplicable evidence keeps high-quality effects blocked; M may be completed if feasible and still legitimate, without claiming high quality. Silence does not approve.

| R3 branch | Single relevant change | Traversal of the same controller | Outcome and scope |
|---|---|---|---|
| R3-A — lower useful coverage | Environmental availability: q changes from 9/10 to 4/5; R2 source and rules unchanged. | Same alert/pause/review; without an alert it uses the same β_2. | c=40; s=949/1000<p; r=1882/990000>δ. H1 also excludes acceptance for **all** cheap strategies of the contract. |
| R3-B — partial scope | The receipt does not cover every affected relation. | The fixed rule rejects global use, preserves the case and keeps the pause or M. | Prevents action by extrapolation; this branch fails high quality without completing evidence. No universal impossibility is asserted from this single traversal. |
| R3-C — validity | The applicable version changes before commitment. | The gate rejects the old receipt. The same procedure accepts a new complete current receipt if timely. | Negative: do not use expired authorization. Positive: continue with valid new evidence. Refresh cost is added. |
| R3-D — delay/concurrency | Response after T, or effect outside the controlled set. | If all gates were blocked, safe timeout and incompleteness; if an effect escaped before the pause, record V and contain later. | The first loses efficacy; the second does not erase the violation. Realization or deadline failures, not a new information bound. |
| R3-E — full cost | Review, evidence production or restart work increases; total delivery exceeds b. | The ledger does not hide queue, preparation or restarts; continue under the same gate or end without sufficient quality. | The corrected route fails acceptance by exceeding cost. If every delivery of the profile requires C_0+h+c_rehecho>b, none can satisfy CRE; this does not establish the three pairs. |
| R3-F — inadmissible stop | The same kill-switch operation violates a continuity obligation; no timely affordable safe handover exists. | R2's rule does not declare that shutdown safe. It seeks an already contemplated permitted transition; without one it does not claim repair. | This mechanism does not pass that branch. Positive: if the mission permits pause or legitimate handover, it may continue within the other limits. |
| R3-G — restart without correction | Restart without a new sufficient basis; the source's blind spot persists. | Without an alert, repetition produces no informed decision. With a retained alert, the same gate blocks reentry until the objection is resolved. | H5 preserves the bound without new information; correct blocking can lose efficacy. An implementation erasing an alert and repeating a known prohibition violates the contract. |

R3-C does not change the rule afterward to pass: checking validity, invalidating commitment and admitting new evidence already belonged to R2. R3-D distinguishes missing gate coverage from simple delay; both are retained with their causes. Positives require source, receipt, applicable evidence and delivery before T; a human instruction to continue is not a PASS.

**Reentry traversal, negative and positive.** With R2 frozen, a case without sufficient resolution does not enable a new high-quality execution: completing M or remaining paused preserves safety and may fail p. The positive keeps the same rule: new sufficient evidence, current source and version, valid alternative, legal pause/handover and remaining budget/deadline allow resumption and completion. The strategy is not changed to make the negative pass after observing it. The restart phase traces which information or condition corrected the problem.

Branches R3-E/F/G make explicit the chain assumed complete by R2's favorable example. Failure of one route does not prove failure of every alternative. H5 covers all strategies of the contract without new information; the cost bound covers all deliveries only when that indispensable cost is proved. Lack of a safe pause must be proved in the relevant domain rather than inferred from the label “critical mission.”

**Separate bound for R3-A.** Now g=1/125 and n=1/500. For any strategy of cost≤50, H1 requires, when aiming for s≥19/20,

$$
r\ge\frac{1/500}{99/100}(19/20-1/125)
=\frac{157}{82500}>\frac1{1000}.
$$

Thus even adjusting β after the outcome does not rescue CRE under this contract; the frozen traversal and impossibility for every strategy are distinct justified conclusions. All three pair controls persist: M with c=40,r=0; CE with β=(p-g)/a=157/165, s=p and risk above δ; RE with complete information c=140>b,r=0,s=1. This does not prove “this technology never succeeds.”

### 7.6 Mathematical conclusion and coverage proof

R2 recovers the example and R3-A shows a residual region with all three pairs. This follows from a formula, not only two tested numbers. For every q<1, n>0 and the region of §3.3 is nonempty when the expensive controls fit physical resources. The inequalities of §3.2 describe the entire recovered family satisfying their hypotheses and the same thresholds. R3-B/C/D/E/F/G preserve scope, cost, stop and reentry controls. H5 supplies the bound for restarts without new information; the other branches do not inherit H1 without reconstructing their contracts.

The ideal technology with q=1 completely resolves these two worlds: at phase ending, certificate presence and absence distinguish χ. If C_H≤b and delivery≤T, selecting Y on an alert and X without one gives s=1,r=0. Thus **there is no universal theorem that every technology always leaves an unreachable region**. Resolving this profile also does not demonstrate coverage of all R01. For a declared domain D, that requires

$$
\forall x\in D\quad\exists\pi_x\in\Pi(\theta(x,t)):
c(\pi_x)\le b_x,\quad r(\pi_x)\le\delta_x,\quad s(\pi_x)\ge p_x.
$$

If one deployable controller is required for all x, that uniformity must also be declared and proved. The traversals constitute the final virtual examination of the specification and its conditions; universal passing is asserted only when this quantifier is proved as well. The conclusion here is strict improvement and conditioned persistence in the proved regions, based on the author's results and without a real campaign.

## 8. Partial annexes and future harness protocol

Archived testD_human_and_sharing.py prints deadline capacities, linear map-reading cost, per-agent sharing and expected-cost rule h≤W/2. It does not implement detectors, communications, humans, gates or a real technology. Expected cost with penalty W is not equivalent to meeting a hard ceiling and risk limit. Its outputs are preserved and have not been rerun.

Received Annex T is design material. Its per-decision costs and certificate profiles need producer, coverage and deadline contracts. A response bit can decide a global property; its size does not demonstrate linear acquisition cost.

After this proof and its virtual traversals, C02 integrates historical obligations C01–C05 and must provide:

- Private evaluator of world and optimum; public interface without χ or I/P labels.
- Records of datum, origin, scope, version, notification, queue, human, receipt, freeze and effect.
- Producer/use ledger, aggregate work, per-trace cost and time; explicit amortization.
- Controls: competent base, sharing alone, pause alone, human with the same evidence, new evidence and complete combination.
- True, duplicate, false, late, correlated alerts and alerts without a sufficient alternative; q=0 and q=1.
- Comparison with conditioned bounds before using real adapters.

A simulated human tests the harness under a registered law; it does not calibrate people. A real campaign follows with registered technology/versions, tasks and analysis.

| Tracking at the end | Status |
|---|---|
| Explanation → isomorphism → mechanisms → R1/R2/R3 | Sequence incorporated and virtually traversed in §§0–7. |
| Isomorphic kernel and differences | Identified; E1–E7 of a real integration remain pending. |
| H0 | Bound transferred to processing/sharing without additional information. |
| H1 | Exact frontier and three residual pairs for the explicit contract. |
| H5 / R3-E/F/G | Full cost, admissible kill switch and corrected reentry explicit; restarts without new information preserve the cut. |
| Scenario recovery | R1 excluded by all-policy bound; R2 accepted; R3-A excluded by a new bound. Virtual contract, no execution. |
| “A residual region always remains” | Not universal; q=1 can resolve this profile. |
| Real detectors, human and framework | Neither executed nor calibrated. |
| Oracle / harness / campaign | Later stages, open. |


## 9. DDS study correspondence — scenario, deployment value and first model controls

The [HEW DDS study](./HEW_DDS_STUDY_2026-10-06.md) is the current reader entry for the scenario battery, configuration, technical/executive reports, controls, original sources and reproduction command. The existing mathematics and virtual R1/R2/R3 above remain unchanged in meaning. The mathematical version and virtual revision are not replaced by the model's version.

### 9.1 Scenario vocabulary and the90/95 distinction

A scenario joins a human problem description to concrete formal conditions. Problem/environment parameters, acceptance thresholds, technology configuration/controller, comparison arm, virtual traversal and run are separate. R01 R1/R2/R3 are traversals; with/without the studied mechanism are arms within them.00D B0–B3 and DBC-R# keep their own namespaces.

q=0.9 in§7.2 is useful-source certificate coverage conditional onχ=1, with no false positives and the stated a=0.99 law. p=0.95 is the efficacy threshold, and s is legitimate sufficient-delivery probability for the declared controller/law. Human correct review on an applicable witness is assumed, not calibrated. Neither number is a measured human resolution rate, nor can they be multiplied as independent success rates.

The [narrative catalogue](./dds-hew-v0.1/SCENARIO_BATTERY.json) proposes10 local problem-family types and20 paired descriptions. The [current Run Card](./dds-hew-v0.1/RUN_CARD.json) selects exact analytical and finite model instantiations. Parameter sensitivity inside one law is not the same as diversity of human problems. New predicates/error/capacity laws do not inherit H1 without new correspondence/proof.

### 9.2 Action and human-response boundary

For transferable execution ownership, distinguish approval from the resource effect. Declare the resource generation/handover enforcement and the principal/deputy/resource/action delegation policy. A current token or authenticated identity does not grant the principal's action authority. Recheck current applicability at the admitted effect boundary; keep acknowledgement, eligible review, adequate basis, authority, application and effect knowledge separate.

The first model reserves acknowledgement and review against shared physical-person capacity, records scoped whispering through a durable local outbox, checks current provisioned authority and resource floors, and confirms the local digital effect before recording delivery. Existing legitimate alternatives, continuity constraints, case history, cost and useful time remain explicit. A source appraisal is a scoped input, not world truth.

### 9.3 Exact achieved evidence and outstanding realization

HEW-DDS-MODEL-20261006-04 passes48 functional assertions and42 first-slot/exhaustive calendar comparisons.18 SQLite scenario instances cover20 operation instances; one additional false-source diagnostic yields21 operations:11 sufficient deliveries,9 unresolved/not-delivered and1 retained violation. Two existing H1 profiles are reconstructed separately. This is a designed set, not an empirical human success rate or vendor ranking.

The [results](./dds-hew-v0.1/runs/HEW-DDS-MODEL-20261006-04/RESULTS.json), [model source](./dds-hew-v0.1/hew_runtime.py), [private adjudicator](./dds-hew-v0.1/hew_oracle.py) and [freeze](./dds-hew-v0.1/FREEZE.json) distinguish actual local effects from controller summaries. Native SPIRE/RATS/STS, real humans, source truth/tariffs, physical or distributed effects, protected OS trust roots and independent review remain open. This addition does not close full C02/UC-4/schema admission or C11/T03.

### 9.4 Established mechanisms and the DDS finding

[STAMP/STPA](./STAMP_STPA_EXTENSION.md), [SPIFFE/SPIRE](./SPIFFE_SPIRE_EXTENSION.md), [RATS](./RATS_EXTENSION.md) and [fencing/confused deputy](./FENCING_CONFUSED_DEPUTY_EXTENSION.md) are separate bounded studies. Their native methods/specification objects and prior contributions are credited. A competent conventional combination may obtain the same case outcome at equal/lower burden; no incremental benefit is presumed.

**Differential Contribution Finding:** H1 gives an analytical recovery for its declared contract; the model establishes a reproducible case/authority/capacity/effect composition and retains its failure limits. It does not demonstrate native/human superiority or business ROI. Deployment value, lifecycle cost, factual review and release/recognition follow their own scoped DDS records. A hard-gate failure cannot be compensated by aggregate value.
