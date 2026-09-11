sp;

Interface role

Theme #6 produces the action-side conformance determination and evidence/appraisal semantics. EA never recomputes conformance; it determines how far a locally sound verdict can legitimately support a broader system-level claim.

&nbsp;

#6 → EA

&nbsp;

Stable profile may declare:

\- verdict vocabulary and semantics;

\- evidence-side rejection / attested-absence semantics;

\- issuer-relationship vocabulary;

\- policy/reference provenance/version semantics;

\- confidence/threshold semantics where used.

&nbsp;

Per handoff where material:

\- action-side verdict;

\- named/versioned reference evaluated;

\- issuing evaluator and relationship to evaluated party;

\- action/decision scope examined;

\- freshness/as-of;

\- confidence/threshold semantics where relevant;

\- intents in collision and criticality where material;

\- indeterminate with scope;

\- attested absence distinctly from indeterminate;

\- unknown qualifiers.

&nbsp;

What EA does with it

EA treats the verdict as a source-attributed scoped determination; checks whether its scope covers the system-level proposition under consideration; composes it with authority, attestation, oversight and other states; preserves indeterminate/unknown qualifiers; and detects when a valid verdict is being projected beyond the reference/evaluation boundary. EA also uses the O1/F1 sensitivity profile to avoid requesting a fresh or independent conformance evaluation when that extra evaluation would not materially affect the current decision.

&nbsp;

EA → #6

&nbsp;

\- whether the existing verdict scope is sufficient for the current higher-level claim;

\- affected domain/dependency requiring requalification;

\- request for reevaluation under refreshed/current reference when material and decision-relevant;

\- explicit indication that reevaluation is not currently justified when its expected decision value is below its burden or remaining response window;

\- request for independent evaluation when source dependence is binding;

\- requirement to preserve current indeterminate rather than promote it to broader certainty;

\- EA scope/coverage/unknowns.

&nbsp;

What #6 is expected to do with EA output

#6 may rerun or refresh the conformance evaluation where the request is within its scope, produce a new scoped verdict, or retain its current verdict unchanged. It is not expected to adopt EA’s system-level conclusion as a new conformance verdict.

&nbsp;

Validation Profile traceability

Primary: UC-EA-02 and UC-EA-04; supporting UC-EA-01.

&nbsp;

7\. Provisional contract — Theme #21 Population-Level Evaluation

&nbsp;

Interface role

Theme #21 owns population-level inference: what can be concluded from a population under stated taxonomy/evaluator assumptions. EA uses that qualified population evidence as one source in an operating-system determination; it does not recompute rates or turn a rate directly into authority.

&nbsp;

#21 → EA

&nbsp;

Stable profile may declare:

\- taxonomy/reference semantics;

\- evaluator-family characterization fields;

\- rate/statistical-result semantics;

\- sampling-vs-structural classification method;

\- pooling/independence assumptions where used.

&nbsp;

Per handoff where material:

\- assessment claim;

\- defined population;

\- observation period;

\- taxonomy/policy version;

\- per-type rate or other non-composite result;

\- evaluator/evaluator-family characteristics;

\- independence/diversity information where established;

\- sampling uncertainty where applicable;

\- residual indeterminacy under the stated observation architecture;

\- statement of what the result can/cannot establish;

\- unknown qualifiers.

&nbsp;

What EA does with it

EA determines whether the population result materially requalifies a current decision domain; preserves the distinction between sampling uncertainty and structural non-identifiability; checks evaluator/source dependence before treating multiple results as corroboration; and prevents a population statistic from becoming an unscoped ecosystem truth. A new population assessment is requested only when the mission-side sensitivity/consequence profile makes the unresolved hypothesis decision-relevant enough to justify the additional observation/evaluation burden.

&nbsp;

EA → #21 / operational consumer

&nbsp;

\- the specific system-level hypothesis for which population evidence is requested and why it is material to the current decision;

\- where useful, the observation/evaluation budget or stopping condition under which additional population evidence remains worth acquiring;

\- whether the returned result requalifies the affected domain;

\- remaining material source/evaluator dependence;

\- residual state not resolved by the population evidence;

\- scope beyond which the result must not be projected;

\- EA scope/coverage/unknowns.

&nbsp;

What #21 is expected to do with EA output

#21 may perform or refine a population assessment for the stated claim under its own methodology. Operational action remains with #16/#13/S12-like consumers, not #21.

&nbsp;

Validation Profile traceability

Primary: UC-EA-02 and UC-EA-04.

&nbsp;

8\. Provisional contract — Theme #22 Remote Attestation for Agentic AI

&nbsp;

Interface role

Theme #22 owns evidence generation/appraisal for attested runtime/model/policy/interaction state. EA consumes qualified Attestation Results, not raw private evidence by default.

&nbsp;

#22 → EA

&nbsp;

Stable profile may declare:

\- attestation/appraisal profile and covered components;

\- verifier relationship semantics;

\- subject/runtime/interaction binding semantics;

\- no-assertion/limitation semantics;

\- default freshness/replay policy.

&nbsp;

Per handoff where material:

\- Attestation Result;

\- attested subject/runtime/interaction/action;

\- verifier/issuer;

\- model/runtime/policy/reference identifiers/versions where material;

\- freshness/replay state;

\- verifier/appraisal relationship where known;

\- what was actually covered/appraised;

\- known exclusions and limitations;

\- no-assertion/unknown state.

&nbsp;

What EA does with it

EA determines whether the attested scope covers the proposition being relied upon; distinguishes attestation from behavioral/system truth; checks freshness and source relationship where material; composes the result with other domains; and requests re-attestation or alternative rooting when the current evidence no longer requalifies the affected domain. It should not request re-attestation merely because it can: the request is conditioned on whether the attested property is material to the current sensitivity/risk profile and whether a refreshed result can still change the relying decision.

&nbsp;

EA → #22

&nbsp;

\- claim/domain for which attestation is currently material;

\- insufficiency of current attested scope;

\- request for re-attestation due to material state change;

\- request for independent/differently rooted evidence where source dependence matters;

\- whether the new result materially requalifies the affected system domain;

\- EA scope/coverage/unknowns.

&nbsp;

What #22 is expected to do with EA output

#22 may produce a new attestation/appraisal result under an appropriate existing profile. It is not expected to certify EA’s systemic conclusion.

&nbsp;

Validation Profile traceability

Primary: UC-EA-02; supporting UC-EA-04 and future embodied/profile cases.

&nbsp;

9\. Provisional contract — Theme #5 Provenance of Authority / #9 fuzzy-authority case

&nbsp;

Interface role

Theme #5 specifies authority origination, grant content, scope, limits, composition, standing/revocation and anchor integrity. #9 provides the difficult case where a clean authority reference may never have existed. EA does not verify or originate the grant; it preserves authority uncertainty as a material input where required.

&nbsp;

#5/#9 → EA

&nbsp;

Stable profile may declare:

\- grant/mandate schema and provenance semantics;

\- standing/revocation/version semantics;

\- delegation/redelegation semantics;

\- fuzzy/absent/contested authority-state semantics.

&nbsp;

Per handoff where material:

\- principal/grantor and grantee;

\- grant/mandate identifier;

\- purpose/action scope;

\- hard limits/conditions;

\- delegation lineage;

\- standing/validity/revocation;

\- policy/reference linkage/version;

\- authority provenance/anchor information;

\- explicit fuzzy, absent, contested or unresolved state;

\- unknown qualifiers.

&nbsp;

What EA does with it

EA treats authority as a separate epistemic domain; detects when downstream conformance, human approval or incident response is being used as a substitute for unresolved authority; preserves unresolved root/standing state; and identifies when authority uncertainty is binding for the current system determination.

&nbsp;

EA → #5/#9 or authority consumer

&nbsp;

\- authority uncertainty material to a specific action/domain;

\- request to refresh/resolve standing or applicable grant where possible;

\- request to narrow action scope to what remains qualified;

\- statement that downstream evidence did not repair the unresolved authority root;

\- EA scope/coverage/unknowns.

&nbsp;

What #5/#9 is expected to do with EA output

The authority layer may refresh or clarify the authoritative artifact/standing if it has the mechanism and mandate to do so. It is not required to accept EA as a legal/authority decision-maker. If the state cannot be resolved, UNKNOWN remains valid.

&nbsp;

Validation Profile traceability

Primary support for UC-EA-01, UC-EA-03 and UC-EA-04.

&nbsp;

10\. Supporting contract — Theme #1 Accountability / action records

&nbsp;

#1 → EA

Actor/action/interaction identity, timestamp, authority reference, policy/verdict references, issuer/freshness/integrity, attestation linkage and actual outcome where recorded.

&nbsp;

What EA does

Uses records as historical/outcome evidence for F9 revalidation and for checking whether current claims align with prior action state; does not treat the record as proof that every carried claim was substantively true.

&nbsp;

EA → #1

Optional bounded EA statement for later reconstruction: assessed scope, management condition/structural markers, posture, requalification decision and material residual/inherited-indeterminacy markers.

&nbsp;

What #1 does

Preserves the EA statement as one attributable record artifact where relevant; it does not turn EA output into liability or legal responsibility.

&nbsp;

Validation Profiles

Supports UC-EA-01/03 and downstream Value Advantage/repair tests.

&nbsp;

11\. Supporting contract — Theme #10 / enforcement-containment plane

&nbsp;

#10/S12-like plane → EA

Available response capabilities, required authority, effective reach, latency/actionability window, reversibility/rollback, execution outcome, residual exposure, migration/reconfiguration readiness and unknown execution state.

&nbsp;

What EA does

Uses response capability to determine whether the current operating frame remains actionable and whether a bounded containment path exists versus a need to qualify migration/regime transition. Response reach, reversibility and remaining time also bound how much further observation/determination effort is rational before control options expire.

&nbsp;

EA → enforcement plane

Qualified posture, affected scope/domain, targeted scope/autonomy reduction request, request to invoke an already-defined containment mechanism, migration/requalification preparation request and success/revalidation criteria.

&nbsp;

What enforcement plane does

Owns authorization and execution. EA does not directly block, revoke, quarantine or migrate.

&nbsp;

Validation Profiles

Primary support for UC-EA-01 and UC-EA-02.

&nbsp;

12\. Supporting contract — Theme #19 Privacy / minimum disclosure

&nbsp;

#19 → EA

Disclosure policy, recipient/purpose, permitted/forbidden attributes, retention/linkability constraints, selective-disclosure capabilities and privacy-risk constraints.

&nbsp;

What EA does

Computes the minimum semantic information needed for the receiving decision; accepts coarser privacy-preserving representations; and leaves unavailable qualifiers UNKNOWN rather than forcing disclosure or inventing values.

&nbsp;

EA → #19

Minimum required semantic fields for a particular handoff, acceptable abstraction/coarsening, and the epistemic consequence of non-disclosure.

&nbsp;

What #19 does

Applies privacy/minimum-disclosure controls; it does not decide the epistemic conclusion.

&nbsp;

Validation Profiles

Supports UC-EA-02 and interoperability/privacy aspects of Challenge 6.

&nbsp;

13\. Supporting contract — Theme #18 Multi-objective / operator-drift evaluation

&nbsp;

#18 → EA

Declared/effective operator or drift result, observation/evaluation scope, evaluator/method, applicable reference/version, confidence/limitations and source relationship where available.

&nbsp;

What EA does

Treats the result as one scoped external assessment; determines whether operator/drift evidence is material to the current decision domain or operating-frame assumption; and avoids promoting one evaluation channel to global certainty.

&nbsp;

EA → #18

Specific unresolved system hypothesis requiring operator/drift evaluation, target scope/domain, and whether the resulting evidence materially changed the system-level qualification.

&nbsp;

What #18 does

Performs or refines its own evaluation; it does not adopt EA as the operator classifier.

&nbsp;

Validation Profiles

Potential external fixture for UC-EA-01 and UC-EA-04.

&nbsp;

14\. Efficiency and deployment expectations

&nbsp;

\- Profile + handoff delta should avoid repeating stable semantics on every hot-path message.

\- Risk/sensitivity calibration should not become a universal Theme metadata tax: mission-side sensitivity/consequence and awareness budgets normally stay in O1/F1, while Themes expose only the capacity/cost facts they actually own.

\- Decision-scope projection should keep state proportional to the receiving decision scope rather than path length.

\- A producer may adopt fields incrementally; conformance is honest declaration, not complete population.

\- Fields are conditional on material decision relevance.

\- An implementation may begin in shadow mode: EA emits assessments without gating the existing control path, enabling comparison, overhead measurement and field-utility pruning.

\- Before a production profile is proposed, measure envelope overhead (bytes and encode/decode latency) under representative chains with and without profile caching and scope projection.

\- Separately measure awareness overhead and value: retrieval/tool calls, compute/tokens, latency, bandwidth/privacy burden, human-review time, and whether additional observation actually changed a decision or preserved an option.

&nbsp;

15\. Use Case contract sufficiency audit

&nbsp;

The cross-Theme contracts are not intended to replace ordinary EA operational inputs. The frozen parent Case Study supplies mission, principal preferences/objectives and T0–T2 facts; O1 supplies mission/orchestration context, including the v0.2 ecosystem-sensitivity/consequence/reversibility and finite-capacity basis; and O4 supplies ordinary state/retrieval availability and, where available, observation burden. A new Theme contract is justified only for a state actually owned by that Theme.

&nbsp;

UC-EA-01 — Action-time operating-frame requalification. Required external state is available from the parent Case Study/O1 plus #5/#9 authority, #6 policy/conformance where used, #13 or another qualified context/incident signal, #16 effective human capacity, and #10/S12 response capability. O1/F1 supplies the sensitivity/consequence and observation-capacity basis needed to distinguish a material change requiring wider/fresher W(d,t) from a low-sensitivity change where broad requalification would be wasteful. EA can produce frame qualification, posture/posture qualifier and the specific requalification target. Result: contract set sufficient for the frozen and v0.2 sensitivity branches.

&nbsp;

UC-EA-02 — Bounded determination under incomplete/conflicting/partially scoped evidence. Qualified external evidence can be supplied by #6, #13, #21 and #22; O4 provides availability and burden of potentially obtainable evidence and #19 constrains disclosure where applicable. Scope/coverage, UNKNOWN, provenance, freshness when material and dependency/source relationship are expressible without requiring full histories. The same contract can test Type-1 over-observation/resource depletion and Type-2 under-observation/hidden exposure against a fixed awareness budget. Result: contract set sufficient for Type-1, Type-2, structural-residual, risk/resource and privacy/interoperability branches.

&nbsp;

UC-EA-03 — Human oversight under bounded effective capacity and non-curative approval. #16 supplies role/authority reference, effective capacity, information coverage, decision scope and reconciliation/outcome state; #5/#9 supplies authority standing; #6/#22 may supply decision-relevant evidence; #1 can supply historical outcome records. EA can test whether human intervention actually requalifies the affected domain, whether capacity is binding, and whether repeated escalation/evidence requests deplete the extended human-agent system's future capacity. Result: contract set sufficient without EA owning HITL.

&nbsp;

UC-EA-04 — Scope-indexed composition of locally valid determinations. The parent Case Study/O1 supplies the relevant principal objectives/preferences and sensitivity/consequence profile; #5/#9 supplies authority domains; #6 supplies policy/conformance determinations; #13/#21/#18 may supply additional scoped assessments; source/dependency/correlation qualifiers support the independence and no