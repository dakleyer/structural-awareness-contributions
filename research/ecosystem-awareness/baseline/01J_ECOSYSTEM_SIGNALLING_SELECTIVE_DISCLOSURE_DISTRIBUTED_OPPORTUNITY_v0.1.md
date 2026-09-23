# Annex 01J — Ecosystem Signalling: Selective Disclosure, Distributed Opportunity and Choreographed Repositioning

**Status:** additive public working annex, v0.1, 23 September 2026. This document is outside the controlled/frozen v0.4 release baseline and outside the EA core. It does not define a mandatory wire protocol, common ecosystem contract, common MSCA, common trust root, common objective, central gradient service, consensus mechanism, adopted FG-TIDA architecture or ITU-T deliverable.

## 1. Purpose

Ecosystem signalling allows independently governed participants to expose selected portions of their local state so that other participants can improve their own ecosystem positioning.

The minimum substrate is deliberately weak:

- no common orchestrator is required;
- no common objective is required;
- no common Agentic Citizenship Contract (ACC) is required;
- no common MSCA is required;
- no global state is required;
- no participant is required to disclose its complete internal state;
- a participant may emit nothing unless an applicable participation profile, law, policy or authority condition requires disclosure.

The architectural purpose is not to coordinate agents directly. It is to make selected local conditions externally interpretable so that receivers can update their own evidence, opportunity assessment, admissibility assessment and local repositioning.

The basic transformation is:

> local qualified position -> selective projection -> signal -> receiver qualification -> local opportunity assessment -> admissibility/authority check -> local repositioning -> optional re-signalling

This is choreography, not orchestration.

## 2. Relationship to EA, MSCA, ACC and authority

The four elements carried or referenced in signalling are not equivalent layers.

### 2.1 Epistemic position

EA qualifies what the participant can responsibly rely on for a declared decision, scope and time. The signal may expose a bounded projection of:

- A — sufficiently determined;
- B — recognized but unresolved;
- C — potentially obtainable within current capability/resources;
- D — structural residual beyond the current represented/capability boundary;
- provenance/source dependence;
- freshness;
- residual uncertainty;
- revalidation conditions.

The four positions remain non-fungible. Confidence or determination in one domain does not erase uncertainty in another.

### 2.2 MSCA

MSCA represents and assesses the participant-local control-sufficiency landscape under an applicable Objective Envelope and operating frame.

A signal may expose only the MSCA dimensions material to the receiving interaction, for example:

- Objective Envelope reference or relevant objective/constraint delta;
- operating environment assumptions;
- coordination scope;
- intervention mechanisms;
- enabling means;
- response capacity;
- resource burden;
- assessment status;
- profile/version/delta.

The receiver must not infer a common or ecosystem-wide MSCA from one participant's projection.

### 2.3 Agentic Citizenship Contract / participation profile

ACC is a separate participation/governance layer. It does not define the opportunity landscape and does not erase opportunities merely because they are inadmissible for a particular participant.

Its role relative to local repositioning is therefore:

> opportunity may exist -> ACC determines whether that candidate transition is admissible for this participant

A signal may expose only the ACC/profile elements material to the interaction:

- participation-profile ID/version;
- membership/domain;
- role eligibility;
- relevant permissions;
- obligations;
- prohibitions;
- autonomy bounds;
- non-compensable constraints;
- validity, expiry, suspension, revocation or supersession.

The ACC projection may be empty, minimal, progressively disclosed or mandatory according to the applicable profile.

### 2.4 Authority / delegation

ACC eligibility does not itself establish that the participant currently holds authority to act.

Where material, signalling may therefore carry or reference:

- principal;
- authority source;
- delegated role/capability;
- grant/delegation chain;
- scope and limits;
- validity/expiry/revocation;
- proof or verification reference;
- trust-anchor reference.

The receiver evaluates those references against its own legitimate trust and verification logic. A sender's self-declaration does not create authority.

## 3. Signal as bounded local projection

Let participant i maintain a richer local state L_i(t).

A signal from i to j is a selective projection:

**S_i->j(t) = pi_i->j(L_i(t))**

where the disclosure function pi may depend on:

- recipient;
- purpose;
- trust;
- expected decision value;
- privacy;
- commercial sensitivity;
- adversarial exposure;
- cost;
- regulation;
- applicable ACC;
- previous signalling history;
- incentives;
- local strategy.

The architecture therefore treats signalling as selective disclosure, not transparency.

A participant may disclose:

- a single fact;
- a qualified epistemic state;
- an MSCA delta;
- an ACC/profile reference;
- authority/delegation evidence;
- several of these together;
- or nothing.

## 4. Minimum extensible signal semantics

The architecture defines semantics, not a mandatory transport.

A minimum extensible signal may contain or reference:

### Epistemic projection
- receiving decision / scope;
- A/B/C/D position by material domain;
- provenance / source dependence;
- inherited uncertainty;
- freshness;
- residual;
- revalidation condition.

### MSCA projection
- relevant Objective Envelope reference;
- relevant control/capability dimension;
- availability / burden;
- current sufficiency/assessment status;
- profile/reference/version/delta.

### ACC projection
- applicable participation-profile reference/version;
- relevant admissibility constraint;
- relevant role eligibility;
- relevant obligation/prohibition;
- validity/expiry/revocation state.

### Authority projection
- principal;
- authority/grant reference;
- delegation chain;
- scope/limits;
- validity;
- proof/verification reference.

### Optional contextual qualifiers
- current posture;
- available response capacity;
- declared local objective;
- dependency condition;
- signalling incentive;
- requested corroboration;
- privacy/disclosure class.

No field is universally mandatory at the architecture level. Domain profiles may impose mandatory disclosure.

## 5. Ecosystem signalling and the opportunity gradient

The gradient is not a globally calculated vector and there is no central gradient owner.

Each participant computes a local ordering over candidate epistemic or control actions using:

- its own MSCA;
- its own epistemic position;
- owner-defined objectives and constraints;
- received signals;
- resource burden;
- useful response horizon;
- privacy and authority limits.

Conceptually:

**G_i(d,t) = G(MSCA_i, EPI_i, Sigma_i, Objective_i, burden_i, horizon_i)**

where Sigma_i is the set of received signals that survive local qualification.

The result is an ordering of candidate actions, not necessarily a numeric differentiable gradient.

Candidate actions may include:

- observe/re-observe a source;
- request or verify a handoff;
- widen, narrow or redirect the Semantic Window;
- acquire additional evidence;
- increase/decrease warning sensitivity;
- add or remove containment capability;
- prepare migration;
- offer or acquire a capability;
- seek a new role or authority;
- cooperate;
- compete;
- wait;
- decline an opportunity;
- re-signal a bounded state.

Signals expose portions of the ecosystem opportunity surface that the receiver may not directly observe.

## 6. Collective gradient as choreography

The ecosystem does not follow one gradient. It produces an evolving field of locally computed gradients.

A typical sequence is:

1. Participant A detects a local gap, risk or opportunity.
2. A repositions locally.
3. A may signal part of that state or movement.
4. Participant B receives or observes the signal and requalifies it.
5. B's local opportunity surface changes.
6. B may reposition differently from A because its objective, ACC, MSCA, authority or evidence differ.
7. B may emit another bounded signal.
8. Other participants update independently.

The aggregate pattern is choreography produced by interacting local optimizations.

No convergence, equilibrium, social optimum or global optimum is assumed.

## 7. ACC as an admissibility constraint, not an opportunity suppressor

A useful architectural separation is:

- **opportunity:** does this candidate move appear beneficial, useful or information-improving?
- **feasibility:** does the participant have or plausibly obtain the required means/capability?
- **admissibility:** does the applicable ACC/profile permit this participant to occupy the role or execute the transition?
- **authority:** does the participant actually hold the mandate/grant needed to act now?

A candidate move may therefore be:

- attractive;
- technically feasible;
- epistemically supported;
- but inadmissible under the ACC.

That opportunity remains visible in the landscape. The participant may instead discover a secondary opportunity to seek membership, qualification, delegation or another legitimate authority path.

ACC therefore constrains the participant's reachable region; it does not redefine the external opportunity surface as nonexistent.

## 8. Trust, partial disclosure and strategic signalling

Signalling may be cooperative, competitive, opportunistic, defensive, regulated or adversarial.

Participants may:

- reveal information progressively as trust increases;
- withhold fields from unknown or untrusted peers;
- disclose only fields required by regulation;
- emit decoy or deceptive signals;
- receive without contributing;
- selectively corroborate;
- challenge a signal;
- refuse a handshake;
- terminate an interaction.

A receiver may update trust when a received claim is compatible with independently held information, including information the receiver did not previously disclose. Such compatibility may increase local confidence in the sender, but it does not prove truthfulness of unrelated claims and must not become a universal reputation score.

Repeated forwarding, correlated reports or many identities controlled by one source must not be treated as independent corroboration.

## 9. Handshake, continuation and termination

A minimal interaction may progress through:

### Discovery / handshake
Participants exchange enough bounded state to determine whether further interaction is worth considering.

### Qualification
Each side evaluates semantic compatibility, provenance, epistemic state, ACC/profile compatibility where relevant, authority/delegation evidence and MSCA/capability relevance.

### Continuation
A participant may disclose more, request evidence, propose work, accept a role, change its Semantic Window or reposition.

### Termination
A participant may stop because:

- compatibility is too low;
- authority is not established;
- ACC conditions conflict;
- trust is insufficient;
- expected value is negative;
- disclosure cost is too high;
- the useful response horizon has expired.

No global controller is required to approve continuation or termination.

## 10. Regulated signalling profiles

The minimum ecosystem architecture permits zero disclosure.

A regulated or institutionally governed domain may define a signalling profile that requires specific disclosures, for example:

- identity or principal class;
- current authority source;
- participation-profile version;
- incident state;
- revocation state;
- provenance;
- minimum freshness;
- response capacity;
- audit reference.

Those obligations come from the legitimate participation/governance layer, not from EA itself.

Thus:

> open signalling architecture + optional domain signalling profiles

## 11. Transport neutrality

The architecture is deliberately protocol-neutral.

A conforming implementation could use, among others:

- A2A messaging;
- JSON or CBOR envelopes;
- signed messages;
- verifiable credentials;
- capability/delegation tokens;
- OAuth-style references;
- DID-based proofs;
- event streams;
- APIs;
- P2P channels;
- distributed ledgers/blockchains;
- shared databases;
- human-readable declarations.

A blockchain or ledger can be useful for immutable lineage, authority history, revocation or shared verification in some domains, but it is not required and does not substitute for semantic qualification.

## 12. Failure mode: collective false-context convergence

A key failure mode occurs when participants propagate an unsupported frame until the group begins treating repetition as corroboration.

The risk is especially material where:

- agents share narrative context;
- source dependence is lost;
- uncertainty is collapsed;
- received claims are treated as facts;
- the original mission/objective becomes displaced;
- subsequent actions provide self-confirming evidence for the false frame.

Qualified signalling should make this failure harder by preserving:

- decision scope;
- provenance;
- source dependence;
- A/B/C/D qualification;
- independent corroboration;
- ACC/admissibility boundaries;
- authority/delegation status;
- local MSCA differences;
- revalidation triggers.

It does not make hallucination, context drift or collective error impossible.

## 13. Testable hypothesis

A candidate hypothesis is:

> Under matched resource and communication budgets, independently governed agents using bounded ecosystem signalling that preserves provenance, source dependence, epistemic qualification, selective MSCA/ACC projections and authority references will show lower rates of collective false-context convergence and unjustified mission displacement than agents exchanging unqualified narrative state or syntactically valid but semantically unbounded messages.

Candidate measures include:

- false-frame adoption rate;
- time to recover the original mission frame;
- number of independent evidence paths required before requalification;
- source-dependence error;
- unsupported authority acceptance;
- inadmissible-action proposal rate;
- mission displacement rate;
- residual-preservation rate;
- signalling/verification burden;
- useful response margin.

A negative or no-difference result counts against the hypothesis.

## 14. Relationship to existing corpus

Read this annex with:

- [01H — Participant-Local Ecosystem Positioning & Decision-Scoped Epistemic Opportunity](./01H_PARTICIPANT_LOCAL_ECOSYSTEM_POSITIONING_AND_DECISION_SCOPED_EPISTEMIC_OPPORTUNITY_v0.1.md);
- [01I — Agentic Citizenship Contract](./01I_AGENTIC_CITIZENSHIP_CONTRACT_HUMAN_GOVERNED_PARTICIPATION_PROFILE_v0.1.md);
- [Article II — Minimum Control Architecture / Multi-Optima](./ARTICLE_02_MINIMUM_CONTROL_ARCHITECTURE_MULTI_OPTIMA.md);
- [Article IV — Ecosystem Signalling Without Required Cooperation](./ARTICLE_04_ECOSYSTEM_SIGNALLING_WITHOUT_REQUIRED_COOPERATION.part01.md);
- [04 — General Functional Interfaces & Agentic Security](./04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md).

This annex is a working reconciliation and extension of those mechanisms. It does not redefine the frozen architecture or assert that the proposed gradient, ACC/MSCA coupling or signalling strategy has been empirically validated.
