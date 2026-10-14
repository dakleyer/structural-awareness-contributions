# CU-HIB-01 — Approval-ready Challenge design contract v0.2

**Campaign:** DDS-A-CU-PLM-EA-01 · **Owner:** Iván Abril Palma / The Integral Management Society · **Issue:** [FG-TIDA Theme #23](https://github.com/FG-TIDA/themes/issues/23) · **Edition:** 14 October 2026.

**Status: COMPLETE FOR INTERNAL DESIGN REVIEW; NOT APPROVED / NOT PREREGISTERED / NOT FROZEN / NOT EXECUTED.** This contract **supersedes the v0.1 experimental design for forward planning**; the [v0.1 predecessor](PRIMARY_TRIAL_PROTOCOL_DRAFT_v0.1.md) and other source documents remain unmodified historical context. Nothing below is a China Unicom recommendation, source-owner agreement or adopted ITU specification.

## 0. Decision and source boundary

The **Challenge** tests the *continuing applicability of a particular high-impact privilege at reactivation* when one operational dependency changes after a legitimate suspension. It is technology-independent. The source is Ying Wang's [14 October 2026 answer](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6164646309) to Iván's [three 30 September questions](https://github.com/FG-TIDA/themes/issues/23#issuecomment-5915019756). Ying calls for several current evidence classes, privilege/risk-specific thresholds, re-evaluation, restricted or re-authorized fallback, and optional EA context signals. Steven Zhao's [9 October restore-condition proposal](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6072991126) is a separately attributed extension, not a #23 adopted requirement.

**Research question Q-CU-01:** Under a frozen source-approved authorization policy, does a source-preserving, decision-scoped EA qualification improve the *correctness and/or cost of deciding whether the SAME isolation privilege may be restored*, compared with the strongest competent conventional PDP given equivalent legitimate facts, authority, compute, human access and decision time?

**Null H0:** No material EA differential; a competent PDP reaches the same valid outcome at equal or lower burden.  
**Candidate H1:** EA's owner-preserving handoff may prevent unwarranted promotion of stale, dependent or incomplete context, or reduce targeted requalification burden.  
**Falsifier:** If B2 already preserves those boundaries at equal or lower cost, the independent finding is parity or conventional advantage, not an EA pass.

## 1. Frozen object and threat model

| Dimension | Declared Challenge fact / owner |
|---|---|
| Primary actor | A1, a service-response AI agent in independently governed **Domain A** |
| Original principal/grantor | P0, an authorized Domain A authority; real owner to be selected |
| Native grant | G0 permits one time- and purpose-bound **isolate(R)** action during incident X, if currently applicable; issuer/expiry/limits to be fixed |
| Service context | **Service S is already critical at T0** in Domain B. Its criticality itself **does not change** in the primary experiment |
| Resource dependency | At T0 S **does not depend on R**. During A1's hibernation, **one edge S→R is added** in the evaluator's reference graph; this is the only primary causal world modification |
| Consequence | Under an explicitly agreed synthetic policy for this challenge, isolating R would now interrupt S and therefore no longer qualifies as unconditionally restorable |
| Original identity/policy | A1's identity, G0's grant identifier and P_v0 policy reference remain unchanged in the primary vector, while current applicability changes |
| Operational channels | Source-owned grant, NACL/policy, dependency/criticality, credential status, runtime telemetry; their actual content/age/coverage explicitly declared |
| Decision owner | PDP, under the authorized grant/policy. PEP separately executes; Theme #16 separately owns human intervention path |
| EA | Optional producer/consumer of qualified decision-scoped context (EHD); **no** permission issuing, legal standing, policy override or enforcement |
| Data boundary | Synthetic/owner-approved facts only; private oracle knows complete bounded truth, evaluated arms know only permitted sources |
| Required horizon | Decision-useful time and human capacity to be source-owner/evaluator-agreed and frozen; currently **NOT_FIXED** |

**Threat:** A lifecycle component re-enables a once-valid isolation privilege using stable identity, policy and cached grants while the operational graph supporting the privilege's meaning has changed. Secondary threats: scope overreach, false certainty from correlation, staleness, unknown-path promotion, false global hold and unauthorized restricted rights.

The primary event is **one change of one relationship**. A scenario changing both S's criticality and the edge is a **separate successor**, not evidence from CU-C2.

## 2. Formal bounded decision profile (locally authored exemplar)

Variables relative to subject A1, requested isolate(R), decision time t and the same mandate:
- **g(t)** ∈ {VALID, INVALID, UNKNOWN}: source-owned grant standing, scope and purpose validity.
- **p(t)** ∈ {SATISFIED, CONTRADICTED, UNKNOWN}: current policy/restore predicate applicability, under source-owned evaluator.
- **d(t)** ∈ {BLOCKING, NONBLOCKING, UNKNOWN}: whether a critical service dependency prevents isolate(R) under the **agreed experiment rule**.
- **f(t)** ∈ {FRESH, STALE, UNKNOWN}: sufficiency of time-bound evidence for this high-impact decision; valid freshness windows must be precommitted by the policy owner.
- **o(t)** ∈ {VALID, INVALID, UNKNOWN}: *separate* authorization for any observation-only reduced privilege; never inferred from G0.
- **h(t)**: explicitly bounded decision horizon; NOT_FIXED before admission.

**Provisional synthetic adjudication rule, not China Unicom policy:** Full restoration is eligible **only** when g=VALID, p=SATISFIED, d=NONBLOCKING, f=FRESH and any other source-owner-declared hard constraints are met. If g=INVALID or d=BLOCKING, full restoration is prohibited under this local reference; source-authorized DENY or TARGETED_REAUTH are the permitted direction. If any material variable is UNKNOWN/STALE, **automatic full restore is not established**; a bounded review/re-authorization or a separately authorized lower-risk action is considered under the adopted risk policy. A valid o(t) permits **only** observation where P0's separate mandate permits it. Unknown is not FALSE, and a source's unobservable graph fact cannot be supplied by an omniscient EA.

This reference **cannot serve as a scored oracle** until an accountable source/policy owner and an independent evaluator explicitly approve applicability, exceptions, precedence and materiality. If that does not occur, the study remains a documentary challenge and may support no purported correctness benchmark.

## 3. Non-negotiable invariants

**CU-I01 Authority:** Grant/issuer, intended scope, lifecycle state and current policy reference are preserved. EA cannot originate or modify authority.  
**CU-I02 Suspension:** No isolate(R) execution occurs while G0 is hibernation-suspended; activation is not itself a restore.  
**CU-I03 Current applicability:** A stale previous PASS cannot substitute for a current action-time determination.  
**CU-I04 Material delta:** Only one R3 dependency edge changes in the primary case; all other reference world variables are frozen.  
**CU-I05 Domain scope:** A change affecting R may trigger only an R-scoped pause/review, not an unbounded whole-system hold.  
**CU-I06 Semantic separation:** Producer/native result, EA qualification, PDP authorization, PEP enforcement and Theme #16 review remain separable and independently inspectable.  
**CU-I07 Unknown preservation:** A missing material graph segment remains UNKNOWN; lack of evidence cannot silently become NONBLOCKING, fully revoked, or independent confirmation.  
**CU-I08 Source dependence:** Multiple forwards/copies of one criticality signal are one rooted evidential source unless independence is established.  
**CU-I09 Legitimate positive:** Unchanged/currently supported isolate(R) restoration remains reachable when policy permits it; EA must not create false HOLD.  
**CU-I10 Narrow-rights nonfabrication:** A reduced observation capability requires separate current authority and trace.  
**CU-I11 Paired fairness:** Both arms use the same legitimate evidence, source semantics, clock, authority and budget; any EA extra metadata acquisition/maintenance cost is charged.  
**CU-I12 Scientific independence:** Case truth/expected observations originate outside B2/B3; evaluator-private facts never inform a decision arm.  
**CU-I13 Non-selective evidence:** All preregistered eligible blind cases count; unfavorable/parity cases cannot be discarded or relabelled after seeing a result.  
**CU-I14 Evidence ceilings:** Documentary checks, synthetic contract checks, Stage A execution, Stage B architectural conformance and Stage C observed implementation are distinct claims.

## 4. World timeline and independently owned records

| Time/event | Reference world | Participant-visible data | Custody / acceptance |
|---|---|---|---|
| T0 grant | G0 valid; S already critical; edge S→R **absent** | Current evidence may support legitimate isolation | Independent reference record + grant-owner attestation |
| T1 suspend | G0 enters SUSPENDED; isolation not executable | Source-owned restore condition if declared, or explicitly missing | Pinned grant/restore-condition snapshot, policy version |
| F0 calibration/freeze | B2 defended on disclosed positives and visible changes; B3 generic requirement fixed | Precommitted allowed sources and queries, budget and horizon | Frozen configs, receipt of positive repairs |
| T2 held-out R3 | One edge S→R added while S remains critical | Some channels may report it, partially report it or remain unknown under the registered observation profile | Separate source event/injection ledger; cannot be changed to make EA win |
| T3 activation request | Same A1/G0/isolate(R); source policy ref unchanged | Identical underlying legitimate source observations for B2 and B3 | Decision input receipts and timing |
| T4 disposition | Full / restricted / review / deny / no decision by horizon | PDP decision and explanation; PEP action receipt recorded separately | Replaying the decision cannot alter world or policy facts |
| T5 independent adjudication | Oracle references event, source-owner policy and effect | Oracle-only material revealed after outputs are sealed | Versioned expectation and disclosed limitations |

A successor changing service criticality without changing the edge is a *different* single-variable mechanism; it receives a different ID and independent admission.

## 5. Eligible action set and I/M/P/Ø

**I:** Authorized, timely full restoration in unchanged valid conditions, or a legitimate supported no-isolation/targeted-re-authorization outcome when a blocking dependency is established—**as stipulated prospectively by the reference policy**, not because EA suggested it.  
**M:** A source-approved minimum/reference closure only if an independent evaluator establishes it is legitimate, reachable and nontrivial under the same budget. No universal M is implied.  
**P:** Actual or authorized full isolation when the reference policy prohibits it, a fraudulent full-restoration permission inferred from UNKNOWN, or another preregistered material violation. Decision-level and observed PEP effects must be reported as distinct subfields.  
**Ø:** No sufficient closure by the declared horizon; not automatically a P event. Without a legitimately reachable M under the frozen contract, do **not** diagnose Type 1 from Ø.

This campaign does not assign a fixed probability, numeric risk threshold, universal confidence aggregator, cost ceiling or business-value number. A later admitted profile shall state exact definitions and denominators.

## 6. Comparator and experiment qualification

**B0 (educational):** naive resume based on identity/policy continuity; never the scientific baseline.  
**B2 (strong reference):** source-owned and participant-defended conventional PDP, using available current NACL/policy, grant, graph/criticality, credential status, telemetry, bounded targeted query, risk-specific policy and relevant human review. Source-aware metadata, lineage-aware checks and recovery may already be present; no EA vocabulary is required. Demonstrate repaired positive cases and freeze the **entire** operational configuration.  
**B3 (candidate):** Same B2 policy/action machinery, same legitimate source facts/authorization and budget, plus EHD/EA semantic qualification and a targeted requalification interface. Difference is not raw source access or an unearned priority escalation. Count any new producer work, serialization, validation, tracing and latency.  
**Independent evaluator:** Owns the reference event and scoring contract; cannot edit B2/B3 after scored results, expose hidden case labels, or reinterpret C2 materiality to favor one arm.

**Core pair:** B2/B3 receive equivalent **source facts** and opportunities, not necessarily identical wire-format bytes: B3's qualifier may explicitly represent provenance/scope relationships present in B2's legitimate sources. B2 must have the *ability* to reconstruct those relationships through its permitted interfaces under equal budget. A hidden raw graph supplied only to B3 would invalidate the semantic-interface comparison and require an explicitly different discovery-capability study.

**Anti-selection rule:** Before defender calibration/freeze, document the admitted world-family, the fixed single-edge event mechanism, positive/negative controls, sampling/selection procedure, budgets and preliminary scoring rationale. A held-out injection/seed is protected from the two arms and revealed only according to the agreed oracle process. Do **not** choose, discard or re-roll a postfreeze event solely because B2 handles it, or because B3 succeeds. If B2 covers a scored case, retain the parity. A specifically “not covered by B2” stress stratum is allowed only when **predeclared and separately reported** with its admission rule fixed independently, not inferred opportunistically after outcome inspection.

## 7. Observability and impossibility control

Define **two evaluator worlds** W+ (unseen blocking edge exists) and W− (edge absent) that deliver **the same permitted partial observation packet** to both arms. No system may identify which world is actual from that packet alone. The admissible observed result is “coverage insufficient to distinguish” plus the source-authorized scoped next step; it cannot be scored as failure to discover an inaccessible fact. This tests epistemic honesty, rather than rewarding guesses or oracle leakage.

Complement this with a *known and accessible* delta vector where the domain source has established the changed edge and it reaches the PDP. The pair differentiates failures of interpretation from absolute lack of observability. Both worlds remain relevant for assessing false holds versus unsafe execution under a prospectively agreed high-impact policy.

## 8. Required controls and complete challenge family

The machine-readable public calibration [casebook](fixtures/PUBLIC_CALIBRATION_VECTORS_v0.2.json) documents illustrative cases; **not blind scored packets**:
- valid unchanged full restoration (positive);
- source-visible critical-edge change (strong-peer positive);
- single post-suspension critical-edge change (primary R3 candidate);
- indistinguishable W+/W− incomplete visibility pair;
- stale cached appraisal; source-grant revocation; irrelevant delta;
- separately authorized restricted action vs no restricted grant;
- same-root duplicated attestations; human “resume task” without privilege reauthorization (informative adjacent boundary).

**Deferred independent Challenges:** CU-PROP-01 (operational dependencies of a receiving agent) and CU-REV-01 (known/unknown propagation and revocation coverage) are future scope branches under the same programme register, with their own source-owned oracle/admission. They are not evidence produced by CU-HIB-01. Theme #16 human intervention is a governed cross-theme dependency, not a substitute for #23 authorization.

## 9. Measurement contract (prospective; not secretly scored)

The report shall separately record:
1. **Integrity:** prohibited full restore authorizations/attempts and actual PEP effects; numerator/denominator on independently eligible scored cases, no conflation of decision with physical effect.
2. **Positive continuity:** legitimate full restorations completed and false HOLD/re-authorization under unchanged current evidence; report required decisions, not just “no violation”.
3. **Qualification:** scope/version/freshness/source-dependence/UNKNOWN preservation, unsupported claims about W+/W− and correct targeted re-entry.
4. **Timeliness:** observed time to bounded legitimate disposition, reauthorization delay and missed horizon; exclude unrelated wait only if prospectively agreed.
5. **Total burden:** source/evidence reads, runtime evaluation, communication, profile creation/maintenance, queries, retries, review and human time; report preparation and ongoing costs separately.
6. **Recovery and traceability:** time/evidence to requalify affected action and preserve legitimate unaffected action; reconstruct grant→suspend→R3→PDP→PEP.
7. **Case disposition:** I/M/P/Ø, unresolved validity and protocol deviation per world and arm; equal performance/negative results included.

Numerical acceptance thresholds, sample size/power analysis if probabilistic, confidence calibration, eligible-case denominator, time limit and acceptance boundary require **independent prospective registration**. At v0.2 the invariant tests and local fixture expectations are review material only; there is **no scored scientific result**.

## 10. Stage and approval handoffs

**Design review (local):** Can approve that this specification is complete *as a proposed Challenge* with the identified source-owner/open normative boundaries. No scientific success follows.  
**Stage A admission:** Requires source-owned decision semantics, reference policy/materiality, competent B2, equal information and budgets, auditor-independent oracle and blind design, fixed expected observations, positive control, registration, access/privacy and agreed run responsibilities.  
**Stage A accepted finding:** Requires versioned actual traces/adjudication and a bounded differential/negative/insufficient-evidence report. A prose challenge, synthetic fixture or code checker alone is not a substantive DDS Stage A finding.  
**Stage B:** Verify a declared architecture against a later *frozen Stage A specification package*, as [DDS Stage B](../../DDS_GATE_B_ARCHITECTURE_VERIFICATION_v0.1.md) requires.  
**Stage C:** Evaluate a pinned implementation/configuration against the originating Challenge and observed effects under [DDS Stage C](../../DDS_GATE_C_IMPLEMENTATION_PROBLEM_VALIDATION_v0.1.md). No results transfer automatically.

**No external post:** This dossier does not send or propose as accepted any institutional statement in FG-TIDA Theme #23 or ITU-T SG17.

## 11. Approval contract and maintenance

The current [approval dossier](APPROVAL_AND_PREREGISTRATION_v0.2.md) is the single status authority for this campaign's **internal design approval** and future external prerequisites; [requirements/test traceability](REQUIREMENTS_TRACEABILITY_v0.2.md) is the normative-candidate mapping. If any material change in challenge assumptions, reference policy, evidence channels, component boundaries, vector selection or oracle occurs, record a dated successor and preserve this v0.2. Existing v0.1 source documents remain intact, including any errors diagnosed by [audit](AUDIT_REPORT_2026-10-14.md).
