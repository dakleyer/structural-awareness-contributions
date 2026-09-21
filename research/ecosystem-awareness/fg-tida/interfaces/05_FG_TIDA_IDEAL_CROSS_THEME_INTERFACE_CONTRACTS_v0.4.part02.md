→ #13

&nbsp;

- affected decision domains/dependencies;
- qualified system-level determination/residual indeterminacy for the relevant incident scope;
- source-dependence or unresolved-coupling warning;
- specific corroboration/requalification target;
- qualified operating posture relevant to containment consumers;
- where material, a statement that further corroboration/observation is or is not proportionate to the current sensitivity, available response capacity and response window;
- EA scope/coverage/unknowns for the assessment.

&nbsp;

What #13 is expected to do with EA output

#13 may use the assessment to prioritize corroboration, distinguish locally strong but systemically insufficient evidence, refine affected-scope interpretation, select among already-authorized containment options, or determine that more evidence/requalification is needed before expanding containment. EA does not issue containment authority and does not replace the #13 signal lifecycle.

&nbsp;

Validation Profile traceability

Primary: UC-EA-02 and UC-EA-04. External validation: FG-TIDA/use-cases #4. Supports UC-EA-01 when incident/context change affects frame validity.

&nbsp;

5. Provisional contract — Theme #16 Operational Human Oversight

&nbsp;

Interface role

Theme #16 owns human-intervention lifecycle, human authority/decision rights, intervention evidence, bounded mandates where applicable, reconciliation and return to operation. EA treats effective human capacity and the resulting decision as qualified inputs, not as automatic epistemic repair.

&nbsp;

#16 → EA

&nbsp;

Stable profile may declare:
- oversight lifecycle/state semantics;
- reviewer-role and authority vocabulary;
- capacity-state vocabulary;
- evidence-status / decision-status vocabulary;
- return-to-operation semantics.

&nbsp;

Per handoff where material:
- required human role and authority reference;
- effective human capacity: available / binding / unavailable / equivalent;
- useful response/intervention window;
- reviewer information scope / coverage;
- evidence sufficiency or limitations;
- human decision and its scope;
- intervention mandate/validity where used;
- intervention outcome/reconciliation state;
- material change since the decision;
- unknown qualifiers.

&nbsp;

What EA does with it

EA determines whether the human path is an effective current dependency rather than a nominal role; checks whether reviewer scope covers the domain creating the systemic condition; prevents a human approval from retroactively curing contrary evidence unless new evidence actually requalifies that domain; and incorporates capacity into frame/posture assessment. Repeated review/evidence requests are also treated as consumption of finite extended-system capacity, so EA can distinguish a useful escalation from Type-1 escalation that is depleting the very human capacity needed for recovery.

&nbsp;

EA → #16

- domain/dependency creating the systemic concern;
- whether the current oversight evidence frame is sufficient for that domain;
- residual/structural limitations relevant to the intervention;
- specific information or requalification needed for a human decision to affect the domain;
- whether human capacity is itself binding;
- qualified Normal / Containment / potential Regime-Transition posture;
- EA scope/coverage/unknowns.

&nbsp;

What #16 is expected to do with EA output

#16 uses the result to qualify the intervention path, decide whether ordinary escalation remains meaningful, target the correct reviewer/information set, avoid repeated ineffective escalation, preserve scarce human attention when additional review has low decision value, and re-evaluate return to operation. #16 retains human authority and intervention ownership.

&nbsp;

Validation Profile traceability

Primary: UC-EA-03; supporting UC-EA-01.

&nbsp;

6. Provisional contract — Theme #6 Intent/Policy Runtime Conformance

&nbsp;

Interface role

Theme #6 produces the action-side conformance determination and evidence/appraisal semantics. EA never recomputes conformance; it determines how far a locally sound verdict can legitimately support a broader system-level claim.

&nbsp;

#6 → EA

&nbsp;

Stable profile may declare:
- verdict vocabulary and semantics;
- evidence-side rejection / attested-absence semantics;
- issuer-relationship vocabulary;
- policy/reference provenance/version semantics;
- confidence/threshold semantics where used.

&nbsp;

Per handoff where material:
- action-side verdict;
- named/versioned reference evaluated;
- issuing evaluator and relationship to evaluated party;
- action/decision scope examined;
- freshness/as-of;
- confidence/threshold semantics where relevant;
- intents in collision and criticality where material;
- indeterminate with scope;
- attested absence distinctly from indeterminate;
- unknown qualifiers.

&nbsp;

What EA does with it

EA treats the verdict as a source-attributed scoped determination; checks whether its scope covers the system-level proposition under consideration; composes it with authority, attestation, oversight and other states; preserves indeterminate/unknown qualifiers; and detects when a valid verdict is being projected beyond the reference/evaluation boundary. EA also uses the O1/F1 sensitivity profile to avoid requesting a fresh or independent conformance evaluation when that extra evaluation would not materially affect the current decision.

&nbsp;

EA → #6

- whether the existing verdict scope is sufficient for the current higher-level claim;
- affected domain/dependency requiring requalification;
- request for reevaluation under refreshed/current reference when material and decision-relevant;
- explicit indication that reevaluation is not currently justified when its expected decision value is below its burden or remaining response window;
- request for independent evaluation when source dependence is binding;
- requirement to preserve current indeterminate rather than promote it to broader certainty;
- EA scope/coverage/unknowns.

&nbsp;

What #6 is expected to do with EA output

#6 may rerun or refresh the conformance evaluation where the request is within its scope, produce a new scoped verdict, or retain its current verdict unchanged. It is not expected to adopt EA’s system-level conclusion as a new conformance verdict.

&nbsp;

Validation Profile traceability

Primary: UC-EA-02 and UC-EA-04; supporting UC-EA-01.

&nbsp;

7. Provisional contract — Theme #21 Population-Level Evaluation

&nbsp;

Interface role

Theme #21 owns population-level inference: what can be concluded from a population under stated taxonomy/evaluator assumptions. EA uses that qualified population evidence as one source in an operating-system determination; it does not recompute rates or turn a rate directly into authority.

&nbsp;

#21 → EA

&nbsp;

Stable profile may declare:
- taxonomy/reference semantics;
- evaluator-family characterization fields;
- rate/statistical-result semantics;
- sampling-vs-structural classification method;
- pooling/independence assumptions where used.

&nbsp;

Per handoff where material:
- assessment claim;
- defined population;
- observation period;
- taxonomy/policy version;
- per-type rate or other non-composite result;
- evaluator/evaluator-family characteristics;
- independence/diversity information where established;
- sampling uncertainty where applicable;
- residual indeterminacy under the stated observation architecture;
- statement of what the result can/cannot establish;
- unknown qualifiers.

&nbsp;

What EA does with it

EA determines whether the population result materially requalifies a current decision domain; preserves the distinction between sampling uncertainty and structural non-identifiability; checks evaluator/source dependence before treating multiple results as corroboration; and prevents a population statistic from becoming an unscoped ecosystem truth. A new population assessment is requested only when the mission-side sensitivity/consequence profile makes the unresolved hypothesis decision-relevant enough to justify the additional observation/evaluation burden.

&nbsp;

EA → #21 / operational consumer

- the specific system-level hypothesis for which population evidence is requested and why it is material to the current decision;
- where useful, the observation/evaluation budget or stopping condition under which additional population evidence remains worth acquiring;
- whether the returned result requalifies the affected domain;
- remaining material source/evaluator dependence;
- residual state not resolved by the population evidence;
- scope beyond which the result must not be projected;
- EA scope/coverage/unknowns.

&nbsp;

What #21 is expected to do with EA output

#21 may perform or refine a population assessment for the stated claim under its own methodology. Operational action remains with #16/#13/S12-like consumers, not #21.

&nbsp;

Validation Profile traceability

Primary: UC-EA-02 and UC-EA-04.

&nbsp;

8. Provisional contract — Theme #22 Remote Attestation for Agentic AI

&nbsp;

Interface role

Theme #22 owns evidence generation/appraisal for attested runtime/model/policy/interaction state. EA consumes qualified Attestation Results, not raw private evidence by default.

&nbsp;

#22 → EA

&nbsp;

Stable profile may declare:
- attestation/appraisal profile and covered components;
- verifier relationship semantics;
- subject/runtime/interaction binding semantics;
- no-assertion/limitation semantics;
- default freshness/replay policy.

&nbsp;

Per handoff where material:
- Attestation Result;
- attested subject/runtime/interaction/action;
- verifier/issuer;
- model/runtime/policy/reference identifiers/versions where material;
- freshness/replay state;
- verifier/appraisal relationship where known;
- what was actually covered/appraised;
- known exclusions and limitations;
- no-assertion/unknown state.

&nbsp;

What EA does with it

EA determines whether the attested scope covers the proposition being relied upon; distinguishes attestation from behavioral/system truth; checks freshness and source relationship where material; composes the result with other domains; and requests re-attestation or alternative rooting when the current evidence no longer requalifies the affected domain. It should not request re-attestation merely because it can: the request is conditioned on whether the attested property is material to the current sensitivity/risk profile and whether a refreshed result can still change the relying decision.

&nbsp;

EA → #22

- claim/domain for which attestation is currently material;
- insufficiency of current attested scope;
- request for re-attestation due to material state change;
- request for independent/differently rooted evidence where source dependence matters;
- whether the new result materially requalifies the affected system domain;
- EA scope/coverage/unknowns.

&nbsp;

What #22 is expected to do with EA output

#22 may produce a new attestation/appraisal result under an appropriate existing profile. It is not expected to certify EA’s systemic conclusion.

&nbsp;

Validation Profile traceability

Primary: UC-EA-02; supporting UC-EA-04 and future embodied/profile cases.

&nbsp;

9. Provisional contract — Theme #5 Provenance of Authority / #9 fuzzy-authority case

&nbsp;

Interface role

Theme #5 specifies authority origination, grant content, scope, limits, composition, standing/revocation and anchor integrity. #9 provides the difficult case where a clean authority reference may never have existed. EA does not verify or originate the grant; it preserves authority uncertainty as a material input where required.

&nbsp;

#5/#9 → EA

&nbsp;

Stable profile may declare:
- grant/mandate schema and provenance semantics;
- standing/revocation/version semantics;
- delegation/redelegation semantics;
- fuzzy/absent/contested authority-state semantics.

&nbsp;

Per handoff where material:
- principal/grantor and grantee;
- grant/mandate identifier;
- purpose/action scope;
- hard limits/conditions;
- delegation lineage;
- standing/validity/revocation;
- policy/reference linkage/version;
- authority provenance/anchor information;
- explicit fuzzy, absent, contested or unresolved state;
- unknown qualifiers.

&nbsp;

What EA does with it

EA treats authority as a separate epistemic domain; detects when downstream conformance, human approval or incident response is being used as a substitute for unresolved authority; preserves unresolved root/standing state; and identifies when authority uncertainty is binding for the current system determination.

&nbsp;

EA → #5/#9 or authority consumer

- authority uncertainty material to a specific action/domain;
- request to refresh/resolve standing or applicable grant where possible;
- request to narrow action scope to what remains qualified;
- statement that downstream evidence did not repair the unresolved authority root;
- EA scope/coverage/unknowns.

&nbsp;

What #5/#9 is expected to do with EA output

The authority layer may refresh or clarify the authoritative artifact/standing if it has the mechanism and mandate to do so. It is not required to accept EA as a legal/authority decision-maker. If the state cannot be resolved, UNKNOWN remains valid.

&nbsp;

Validation Profile traceability

Primary support for UC-EA-01, UC-EA-03 and UC-EA-04.

&nbsp;

10. Supporting contract — Theme #1 Accountability / action records

&nbsp;

#1 → EA

Actor/action/interaction identity, timestamp, authority reference, policy/verdict references, issuer/freshness/integrity, attestation linkage and actual outcome where recorded.

&nbsp;

What EA does

Uses records as hi