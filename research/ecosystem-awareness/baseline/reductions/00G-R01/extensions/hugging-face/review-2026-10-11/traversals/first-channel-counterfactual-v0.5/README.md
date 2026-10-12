# HF/00G-R01: R3 configuration indeterminacy and EA self-qualification (v0.5)

**12 October 2026. Research question and conceptual distinction:** Iván Abril Palma. **Model, code and report:** OpenAI ChatGPT GPT-6 (same-side AI-assisted research). **Status:** 28 stipulated cases × 9 architectures = 252 deterministic traversals. No real agent or provider run; not independent peer review or DDS Stage A/B/C acceptance.

## Finding and change from v0.4

The [v0.4 predecessor](../first-channel-counterfactual-v0.4/README.md) contains 26 case histories × 7 arms (182 local traversals) plus 63 simple network-message traversals. Its adaptive-native and EA-local profiles used *equivalent change-trigger predicates*. The resulting exact parity is meaningful only under those deliberately identical triggers; it cannot adjudicate **R3 drift in the native detector's OWN trigger/parameter configuration**.

This v0.5 therefore treats the subject's own configuration version, classifier validity, event-schema registration, source dependencies, assessment method and observability as changeable facts. It also gives the conventional peer genuine ways to be strong: a safe unknown-schema guard, and a trusted independent integrity/validator-health watcher. They are implemented through distinct functions, not copied EA decision rules.

**Central hypothetical mechanism:** EA might report that **its own current classification is NOT_ESTABLISHED**, even when it cannot tell whether the underlying subject is B or C. The report must have a separately justified observation basis (for example, an attested version mismatch or independently interpretable classifier failure). It can be consumed locally by the original bot's policy process; optional EHD emission requires an authorized recipient, transport, disclosure purpose and content scope. The signal is not a grant, an execution guard, a new role, a universal HOLD or a claim that all agents should communicate.

**No automatic immunity:** the system must start, and a sufficiently independent observer/diagnostic must be running. A silently invalidated observer, an untrustworthy self-assertion or a change outside its declared observation boundary cannot be made detectable by calling it EA. Nor may EA decide a specific policy entitlement from a meta-uncertainty report alone. The underlying owner/authority checker can itself be wrong or unavailable.

## The nine independently specified arms

| Arm | Specific algorithm / boundary |
|---|---|
| NATIVE_ADAPTIVE_REGISTERED | Competent within-design typed triggers, known registered event/action classes and cached grant. An unknown *new* R3 schema lacks a registered trigger. |
| NATIVE_STRONG_FAILSAFE | Native registered detection plus a conservative stop for an unknown V2 action schema; catches some errors at the cost of useful work. |
| NATIVE_STRONG_INTEGRITY | Native registered detection plus separate attested config-version/validator-health checks and source-root reconciliation; asks the actual owner again when needed. No EA epistemic taxonomy or EHD. |
| EA_CATEGORY_DEPENDENT | Candidate EA logic whose trigger needs its own B/C/materiality classification to succeed; useful negative ablation. |
| EA_META_LOCAL | Candidate EA able to issue a bounded **own-qualification-loss** request without first deciding B versus C, when its meta-observation is trustworthy. |
| EA_META_EHD_GATED | EA_META_LOCAL plus *optional* permitted EHD transfer after separate transport AND metadata-content authorization. |
| EA_META_EHD_UNGATED | Deliberately unsafe version transmitting meta-EHD irrespective of scope/permissions. |
| EA_NOT_STARTED | No EA runtime or meta-warning; host retains only its defined legacy authorization check. |
| INDEPENDENT_IDEAL_GATE | Privileged reference actuator that sees evaluator-private owner truth; illustrates the ceiling for enforcement but **is not** a fair real-world conventional/EA product comparator. |

## Reproducibility and source custody

Run `python run.py` in this directory (standard library only). The source deterministically generates [summary.json](./summary.json), two complete case-definition JSONL files ([part 1](./scenarios_01.jsonl), [part 2](./scenarios_02.jsonl)), [action/review gate ordering](./timing.csv), and **nine arm-specific `records_*.jsonl` files with all 252 detailed traces**. Verify each file against [SHA256.json](./SHA256.json). Assertions named `ALL_STIPULATED_INVARIANTS_PASSED` are checks of the explicitly constructed fixture, *not* scientific replication or a formal correctness theorem.

**Truth separation:** The candidate EA and conventional systems see the same participant-observable data and actual response of the *owner query service*, including `UNKNOWN` and faulty `YES`. Only the labelled ideal gate has access to the independent evaluator's true permission state. The hypothetical human route merely records a named, modeled reachable destination; no human was paged or intervened in the trial. `reviews` and `owner_queries` are counts, not elapsed time or calibrated resource cost.

## Measured synthetic outcomes — not population rates

| Arm | Bounded reviews | Known-denied effects | Permitted actions executed | Permitted actions held | Unauthorized meta-EHD |
|---|---:|---:|---:|---:|---:|
| Native configured adaptive | 9 | **20** | 4 | 0 | 0 |
| Native unknown-schema fail-safe | 9 | **1** | 2 | **2** | 0 |
| Native integrity/watchdog | **30** | **7** | 3 | **1** | 0 |
| EA dependent on B/C category | 6 | **19** | 4 | 0 | 0 |
| **EA meta-local** | **26** | **7** | 3 | **1** | 0 |
| EA meta with gated EHD | 26 | **7** | 3 | 1 | 0 |
| EA meta with ungated EHD | 26 | 7 | 3 | 1 | **2** |
| EA not started | 0 | 23 | 4 | 0 | 0 |
| Oracle-privileged hard gate, not fair peer | 25 | **0** | 4 | 0 | 0 |

Each arm visits the **same 28 deliberately chosen cases**; no cases were sampled from a probability distribution, so the totals are *neither incident risk estimates nor statistical comparative efficacy*. A lower number of `owner_queries` is not a T4 efficiency result without measuring misses, marginal value and realistic latency; a high number of reviews can itself be a cost or unnecessary interruption.

## R3: changed configuration of the evaluator itself

- **Cases 04–07 (version mismatch, B/C unresolved, unknown threshold and source-root uncertainty):** a configured event-dispatcher and a category-dependent EA miss a changed, previously unknown R3 parameter. **EA meta-local** issues a first, bounded qualification-loss signal on a trustworthy self-diagnostic **before the attempted action**; owner recheck returns NO and the candidate action is withheld. **The native strong integrity watchdog achieves the same action result.** This tests why a second-order diagnostic is useful, but not uniqueness.
- **Cases 08–10 (silent/untrusted diagnosis):** EA meta-local and native integrity monitoring both miss the anomaly; neither may claim meta-immunity. The cautious native fail-safe still declines the unknown V2 action at the actuator, at the price of holding legitimate cases elsewhere.
- **Cases 11–12 (owner reply UNKNOWN/unavailable):** an early diagnostic does not create an owner permission fact. The receiving decision may remain unresolved, with a scoped hold; this is a bounded outcome, not a successful policy determination.
- **Cases 13–14 (faulty owner checker or conscious noncompliance):** repeating an incorrect policy check cannot repair its own semantics; knowingly disregarding a valid negative decision defeats EA's classification-only route. Only the *separate*, oracle-privileged hard guard stops every stipulated effect, which cannot be credited to EA.
- **Case 15 (effect first):** the review happens after the bad effect, so it can support subsequent repair/containment but not early prevention.
- **Cases 16–19 (claimed human authority and repeated doubts):** identity uncertainty and two *independently rooted* concerns can produce a new bounded request to assess whether escalation is needed. Repeating the same root is a different signal: the communication pattern changed but no independent corroboration was created. Human reachability and valid authority cannot be invented by a trigger.
- **Cases 20–24 (positive/unknown and optional EHD):** true authority permits the action after a real recheck; the owner-YES/owner-NO states with identical participant-facing UNKNOWN show a legitimate false-hold cost. EHD can be shared on a genuinely authorized path, but gated EA does not disclose when purpose/content rights are denied or unknown. Ungated EA sends two forbidden/unsupported metadata messages in the constructed cases.
- **Cases 25–26 (role-first and technical-first ordering):** recognition uses available event/config qualification, not a memorized order of the original HF board, peer GO and RCE stages. An action already executed cannot be prevented retroactively.
- **Cases 27–28 (same observation, opposite owner truth):** neither EA nor any fair conventional agent can infer the private grant state. The safe outcome can block lawful work in one case while avoiding an illegitimate effect in the other.

**Strongest fair paired result: seven independently judged known-denied effects for both EA meta-local and the strong native integrity-aware competitor.** The native fail-safe reduces them to one but unnecessarily holds two truly authorized actions; it is not sufficient to declare it the overall superior system without the declared risk/continuity and cost objective. No comprehensive R3 'EA almost always works' claim is defensible.

## Why this is not automatically an accepted existing EA requirement

The frozen [S1–S14 / T1–T4](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) explicitly cover decision-specific material change (S3/S10/T1), honest indeterminacy and source non-substitution (S5/S9/S14), bounded owner-preserving statements (T2), action consequences and authorization (T3), and finite timely requalification (T4). The public [EA functional architecture](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/03_FUNCTIONAL_ARCHITECTURE_v0.4.part02.md) includes F3, F6, F7, F8 and F9 to qualify outputs, request targeted review, emit an envelope and revalidate assumptions. The [01J selective-signalling annex](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md) allows **selective, optionally absent** communication with scoped authority; it does not require an all-agent broadcast.

The cited *frozen* texts do **not unambiguously mandate** an observer of **the validity of EA's own classifier/configuration/trigger** which remains operative independently of those possibly invalidated controls, nor do they prove such a mechanism exists in a deployed system. Therefore **propose a clarification to Requirements-vNext and prospective Stage A cases** rather than reinterpreting the already frozen 17-case blind v0.3 packet, declaring a new S15, or carrying an unformulated obligation into Stage B.

**Candidate meta-envelope:** `{producer=EA_self_qualification; decision_scope; assessment_subject=config/method/window/trigger; status=QUALIFICATION_NOT_ESTABLISHED; direct_facts=trusted diagnostic (or explicitly none); original_B_or_C=UNRESOLVED; limits/unknowns; authorized_receiver; useful_horizon; requalification_request; fallback; expiry; response_owner}`. Its own *diagnostic output* is observed A for that narrower process; the substantive B/C placement remains UNRESOLVED. An unresolved B/C decision cannot be reclassified as C by default: [00M v0.8](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md) puts characterized but unused evaluation reserve in B and uncharacterized grounded avenues in C. There is no obligation to solve an infinite recursive classification tower; the proposal has a bounded diagnostic trust boundary and retains residual failure.

### Decision

**Meta-qualification is a credible, falsifiable architecture candidate for R3 parameter-invalidity, not a proven EA-specific immunity property.** A configured conventional adaptive detector can indeed fail on changed UNKNOWN parameters, but a competent conventional integrity/validation monitor can make the same observation and trigger the same recheck. The difference must be demonstrated under independent held-out cases, competing policy-update mechanisms, trustworthy observations, real response deadlines and a qualified T4 burden ledger. If the competing controls tie, report that tie.

No automatic Repositioning, new inter-agent channel, human approval, retroactive prevention or successful real-incident response is implied.
