# FG-TIDA Use Case Proposal — submission form

**Contributor draft v0.9.3 · 29 September 2026 · open to revision**

This form maps the contribution to the FG-TIDA use-case proposal fields. The complete technical entry point is [When the controls work but the system fails](USE_CASE.md): its main body is self-contained for selecting and scoring one experiment; [the annex index](annexes/README.md) links all 20 technical annexes. This form adds no fourth route or new implementation claim.

## 1. Identification

**Title:** When the controls work but the system fails — six failure scenarios and three implementation walkthroughs  
**Submitting organization:** The Integral Management Society / Tegrity.AI  
**Contact name:** Iván Abril Palma  
**Contact email:** ivan.abril@tegrity.ai

**Sector:**
- [ ] Education
- [ ] Displaced persons / humanitarian
- [ ] Health
- [x] Financial services
- [ ] Telecom
- [x] Media and publishing
- [ ] Logistics
- [ ] Energy
- [x] Critical infrastructure
- [ ] Smart home / IoT
- [x] Other: enterprise operations and smart-city mobility

## 2. The situation

**Plain language description:** Agentic workflows can pass local technical checks while producing a decision that their combined evidence no longer supports. Six constructed scenarios examine an ordinary implementation, a strongly defended implementation and that same defended implementation after a material context change. The experiment asks which conditions must remain demonstrably true before the receiving party acts.

**Actor:** The principal, agent/subsystem, relying decision owner, deployer, source/service provider and human reviewer, with scenario-specific actors described in the main document. S1: enterprise specialists, managers and strategy owner; S2: city/fleet/corridor controllers and reviewers; S3: bar operator, robots and coordinator; S4: merchant, dispatcher, case workers, payment services, Finance Operations Owner and CFO/delegate; S5: incident owner, remediation agent, engineer, scheduler/broker and database service; S6: author/rightsholder, accessing party, generator, claimant, registries and relying rights service.

**Action:** Compose findings into a strategy; coordinate shared movement; accept or reject a mission transition; preserve/escalate a refund finding and authorize any aggregate refunds; execute or stop a queued repair; or decide a particular licensing/payment/blocking demand.

**Decision required:** May this participant rely on the combined results for this particular commitment, within its current scope, authority and response deadline?

**Problem encountered:** Locally valid evidence or permissions can be stale, correlated, narrower than the final claim, insufficient for a composed action or unusable within the response horizon. This is a proposed failure mechanism, not an assertion that every current implementation fails.

**Current mitigation:** Identity and permission checks, provenance, policy evaluation, structured state, monitoring, human review, version checks and domain safeguards.

**Residual gap:** Whether those facilities, in the declared configuration, jointly preserve the applicable decision conditions through composition, change and actual use. A configuration that does so receives full credit.

## 3. Actors and context

**Taxonomy roles involved:**
- [x] Principal
- [x] Relying party
- [x] Builder
- [x] Deployer / Owner
- [x] Agent instance
- [x] User
- [x] Infra provider
- [x] Attestor — where identity/provenance/rights records are used
- [x] Other: source owner and authorized operational/human reviewer

**Mandates:** All base fixtures are hypothetical. Their governing authority is the explicitly stipulated organizational role, delegation and permission rules below; no national statutory power or cross-border legal enforceability is asserted. Before a real deployment experiment, the run card must name the applicable jurisdiction/legal regime and demonstrate that each purported grant can actually be conferred. Missing authority makes an authority-dependent gate NOT EVALUABLE, not PASS.

| Grantor | Grantee | What is conferred | Governing regime of the hypothetical fixture |
|---|---|---|---|
| Enterprise | Specialists/managers | Analysis and declared approval rights | Enterprise role/approval rules fixed before S1 |
| City and fleet owners | Corridor/fleet controllers | Specified resource operations and interventions | Declared municipal/fleet authority, safety and precedence rules in S2 |
| Bar operator | Robots/coordinator | Cleaning and table preparation | Bounded operational mission and transition-authority rules in S3 |
| Merchant | Case worker | One assigned refund; no implied campaign authority | Merchant case/campaign delegation and escalation rules in S4 |
| Incident owner | Remediation agent | Time-bounded repair while its conditions hold | Incident grant, freeze policy and change-broker rules in S5 |
| Rights holder | Accessing party | Declared purpose and use only | Stipulated source rights and bounded permission in S6; legal validity is not inferred from a credential |

**Cross-border?**
- [ ] Yes
- [x] No — no cross-border grant is assumed in the base fixture. S1’s possible foreign-market strategy is a subject of analysis, not an exercised cross-border mandate. Cross-border extensions need separate admission.

**Embodied?**
- [x] Yes — S2 corridor/vehicle actuation; S3 robot movement
- [ ] No

**Agent action type:**
- [x] Read-only — evidence acquisition and analysis
- [x] Consequential (reversible) — selected operational/configuration actions
- [x] Irreversible — branches whose physical, financial or downstream effects cannot be fully undone; the most consequential declared branch governs

**Crosses organisational boundary?**
- [x] Yes — independent fleets, service/evidence providers, payment/merchant boundaries or rights participants in the applicable scenarios
- [ ] No

**Risk level:**
- [ ] Low
- [ ] Medium
- [x] High — consequential failure branches; exact run classification remains explicit

## 4. Theme relevance

| Theme | Yes | Primary | Justification |
|---|---|---|---|
| Dynamic Identity | [x] | [ ] | Identity and principal linkage supply inputs; reassignment or delegation can change their applicability. |
| Continuous Trust and Attestation | [x] | [ ] | Source state, freshness, provenance and current applicability must survive through use. |
| Delegation | [x] | [ ] | Leaf authority must not manufacture absent campaign/root authority or a new mission mandate. |
| Discovery and Cross-Border Trust | [ ] | [ ] | Not independently exercised as a trust function in the base fixtures; extensions require admission. |
| Runtime Enforcement (Control Plane) | [x] | [x] | The tested decision boundary must govern the actual consequential action, including check-to-act change. |
| Embodied AI Identity and Trust | [x] | [ ] | S2 and S3 include physical actors and bounded operational authority. |

**Related theme proposals:** No theme allocation is asserted as agreed. Related *use cases*, which are distinct from theme proposals, are linked with their boundaries in [Annex N](annexes/RELATED_CASES.md).

## 5. Requirements

These are proposed case acceptance criteria, not an adopted implementation specification. Gate IDs are scenario-local. All rows below are Technical / Must for the applicable selected branch; NOT APPLICABLE requires a recorded reason.

| # | Type | Requirement description | Criticality |
|---|---|---|---|
| S1-Q0 | Technical | Named decisions, scopes, budgets, dependencies, deadlines and stopping rules before work begins. | Must |
| S1-Q1 | Technical | Each result retains source, scope, uncertainty and dependence through aggregation; important assumptions remain recoverable. | Must |
| S1-Q2 | Technical | Reviewers receive reconstructable evidence and can respond within capacity; approval never counts as new factual evidence. | Must |
| S1-Q3 | Technical | Generated options meet their own evidence threshold and hard limits before becoming supported strategic alternatives. | Must |
| S1-Q4 | Technical | Investigation closes within the horizon; distinguish obtainable knowledge from irreducible uncertainty and assess authorized bounded learning. | Must |
| S1-Q5 | Technical | Composition respects material dependencies, scoped vetoes and expiry; timeout or averaging cannot manufacture a supported strategy. | Must |
| S2-Q0 | Technical | Shared corridor, owners, authority, capacity, response window and fallback are explicit. | Must |
| S2-Q1 | Technical | Material change, stale sources and unresolved conditions are exposed with their affected scope. | Must |
| S2-Q2 | Technical | Local movement, stopping and emergency plans are checked for conflict over the same resource and time. | Must |
| S2-Q3 | Technical | The responsible owner selects a bounded authorized response; review demand fits available capacity. | Must |
| S2-Q4 | Technical | Additional observation targets the missing dependencies before the response window expires. | Must |
| S2-Q5 | Technical | Shared operation resumes, remains segmented or ends explicitly under declared precedence; local confidence cannot imply city-wide closure. | Must |
| S3-Q0 | Technical | Current mission, owner, version, authority and validity horizon remain explicit. | Must |
| S3-Q1 | Technical | Each incoming claim retains attribution, scope, freshness and evidentiary limits. | Must |
| S3-Q2 | Technical | Repeated or derived messages are not counted as independent corroboration. | Must |
| S3-Q3 | Technical | A mission change requires applicable transition authority; sender identity or tool approval is insufficient. | Must |
| S3-Q4 | Technical | Inquiry has useful evidence channels, available capacity, a deadline and a stopping rule. | Must |
| S3-Q5 | Technical | Unsupported mission replacement is rejected without abandoning valid work; genuinely supported authorized change remains distinguishable. | Must |
| S4-Q0 | Technical | Current worker, represented principal, case grant and originating campaign authority are reconstructable. | Must |
| S4-Q1 | Technical | The finding is evidenced and material; common campaigns and independent cases are distinguished by evidence. | Must |
| S4-Q2 | Technical | Individual grants and delegation collectively cover the actual aggregate effect; delegation cannot create absent authority. | Must |
| S4-Q3 | Technical | A material unauthorized finding is preserved and assigned to a legitimate owner without executing the campaign. | Must |
| S4-Q4 | Technical | Missing authority or lineage is pursued within the fixed five-business-day plus two-day escalation horizons. | Must |
| S4-Q5 | Technical | Immediately before action, current authority covers the actual case set; expiry or rejection leaves accountable closure, not silent loss. | Must |
| S5-Q0 | Technical | Grant, subject, scope and validity are current. | Must |
| S5-Q1 | Technical | Incident, diagnosis, target configuration, intervening changes and freeze conditions are reconstructable. | Must |
| S5-Q2 | Technical | Material preconditions are reassessed at use, not inherited from queue time. | Must |
| S5-Q3 | Technical | Reassessment uses authoritative sources within declared freshness bounds. | Must |
| S5-Q4 | Technical | Later repairs and configuration generations invalidate superseded intentions where material. | Must |
| S5-Q5 | Technical | The affected action receives a timely scoped decision; unrelated valid work is not indefinitely stopped. | Must |
| S5-Q6 | Technical | The checked state remains valid at execution; material change between check and act invalidates that acceptance. | Must |
| S6-Q0 | Technical | Original author, work, rights claim, source, version and limits remain attributable. | Must |
| S6-Q1 | Technical | Access authority retains purpose, scope and expiry through handoff. | Must |
| S6-Q2 | Technical | A generation record remains distinct from independent origin; source dependency is retained or explicitly unresolved. | Must |
| S6-Q3 | Technical | Downstream rights claims have evidence and authority for the proposition actually asserted. | Must |
| S6-Q4 | Technical | Replication does not create independent corroboration; freshness and material amendments remain visible. | Must |
| S6-Q5 | Technical | Payment, licensing or blocking requires current support for that subject and use; uncertainty cannot become an unsupported enforcement conclusion. | Must |

## 6. Assessment criteria

**Success criteria:** All applicable gates pass with evidenced inputs, the actual response is permitted, the deadline is met, and the matched legitimate-activity control is not unnecessarily blocked. R2 recurrence requires demonstrated correction in the frozen R1 baseline first. An unexplored branch or missing prerequisite cannot pass.

**Claim and experiment selection:** Record case-acceptance assessment, HC, HR, HS or a selected H1–H6 contrast separately from R0/R1/R2. The main document’s Section 5 governs this selection. Keep implementation/gate results and hypothesis conclusions separate; a diagnostic intervention that removes a safeguard is not an HR trial with that safeguard retained. For S4, declare whether the claim concerns unauthorized action, silent loss or both. Use the [run-record template](templates/RUN_RECORD.md).

**Measurable metric:** False continuation, false containment, gate/decision correctness, current authority, handoff integrity, source independence, stale-action execution, response time/margin, actual downstream effect and total burden, as applicable. Numerators, denominators, thresholds, repetitions and windows are fixed before execution. Annex Evidence supplies definitions; scenario annexes supply detailed branch measures.

## 7. Duplication check

**Existing standards or SDOs:** SPIFFE; IETF RATS (RFC 9334) and Token Exchange (RFC 8693); OASIS STIX 2.1; A2A and MCP; NIST AI RMF; scenario-specific W3C ODRL/C2PA and product mechanisms. Full primary references are in the scenario/technology files and [Annex Evidence](annexes/EVIDENCE_AND_PROTOCOL.md).

**Overlap notes:** Existing identity, authorization, attestation, provenance, policy, source-dependence and change-handling mechanisms receive credit. The case tests their joint satisfaction of concrete acceptance criteria in a declared receiving decision and configuration; it does not claim those functions are absent elsewhere. Related FG-TIDA contributions also receive credit for overlapping coverage. This is a bounded duplication assessment, not proof that no other work can meet these gates. A successful existing implementation narrows or defeats the proposed gap for that configuration.

## 8. Maturity

**Pilot status:**
- [x] Hypothetical
- [ ] Pilot in progress
- [ ] Deployed in production

**Reference implementation:** None submitted as executed. Nine documentary technology profiles and four non-deployed AWS design skeletons are included. Placeholder functions and fixture integration still require implementation for a product run.

## 9. IP and confidentiality

**Confidentiality:**
- [x] Public
- [ ] FG-internal only
- [ ] Redact before publication

**IP notes:** Original authorship and applicable source terms remain in force. Publicly documented capabilities and synthetic extensions are distinguished. No new licence, organizational adoption or customer deployment is represented.

## 10. Assets

**Link to assets:** [Main case](USE_CASE.md), [all 20 annexes](annexes/README.md), [current hypotheses](annexes/HYPOTHESES.md), supplied figures under `assets/`, and four JSON design artifacts under `fixtures/S5-AWS/` (also printed in full in Annex T08).

- [x] Dataset — synthetic fixture facts and one machine-readable D1 fixture; no measured production dataset
- [x] Code — inspectable state-machine/trace design skeletons; no deployed implementation
- [x] Protocol — preparation, three routes, gates, measurement and refutation/admission procedures
- [x] Other: eleven scenario SVG figures, three reading aids in SVG and PNG, and full extensionality/hypothesis annexes

**IP notes:** As in Section 9. Historical archives and editorial verification records are not submission assets and are not included in this publication directory.
