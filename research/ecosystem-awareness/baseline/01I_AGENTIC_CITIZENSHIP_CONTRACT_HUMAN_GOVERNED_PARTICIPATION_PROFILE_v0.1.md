# Annex 01I — Agentic Citizenship Contract: Human-Governed Participation and Constraint Profile

**Status:** additive public working annex, v0.1, 21 September 2026. This document is outside the controlled/frozen v0.4 release baseline and outside the EA core. It is not an adopted legal framework, a grant of legal personhood, a human-equivalent civil-rights model, an implemented governance protocol, an ITU-T deliverable or a standards claim.

**Terminology boundary:** “citizenship” and “contract” are architectural working metaphors for machine-interpretable participation and governance conditions. They do not assert that software agents possess legal contractual capacity, sovereign membership or human-equivalent rights.

## 1. Purpose, prior art and non-ownership boundary

Autonomous or semi-autonomous agents can interact in ecosystems where no common orchestrator, common objective or common internal logic is guaranteed. Ecosystem Awareness can qualify what a participant locally understands about such an ecosystem; MSCA can assess what local control configuration is supported; identity and delegated authority can establish who/what is acting and under which mandate.

A separate question remains:

> Under what human- or institutionally governed participation conditions may autonomous machine participants join, act, cooperate, compete, change role, exchange information or leave while still serving legitimate objectives and constraints?

This annex names that candidate layer **Agentic Citizenship Contract**.

The concept has substantial prior art in normative multi-agent systems and electronic institutions, including [Organizations and Normative Agents](https://doi.org/10.1007/3-540-36087-5_113) and the [HarmonIA framework](https://doi.org/10.1007/978-3-0348-7955-2), as well as organizational agent models, roles, norms, permissions, obligations and prohibitions. Contemporary agent-protocol work such as [Open Agent Protocol RFC 0030](https://github.com/openagentprotocol-OAP/oap-spec/blob/main/rfcs/RFC-0030-agent-organizations.md) also treats Organization, Role, Scene and Norm as first-class objects. This annex does **not** claim those mechanisms as new. It uses “citizenship” only for the additional relation between autonomous machine participants and human/institutionally defined admissible objectives, membership/participation conditions, rights-like permissions and duties/obligations, non-compensable constraints, accountability/evidence requirements, cross-domain membership, amendment, revocation and exit.

This layer does not own identity, delegated authority, EA qualification, MSCA sufficiency or defence execution.

### 1.1 Dependency key for a first-time reader

- **EA / Ecosystem Awareness:** the decision-scoped epistemic-qualification architecture that determines what a participant can responsibly rely on from its bounded ecosystem representation.
- **01H:** the additive participant-local/distributed reading of EA, including optional signalling and local requalification.
- **EHD / Epistemic Handoff Descriptor:** the bounded semantic handoff used to preserve result meaning, scope, UNKNOWN and source/dependency qualifiers across components.
- **MSCA / Minimum Sufficient Control Architecture:** the separate control-sufficiency line that represents/assesses S/E/C/P/M under an applicable Objective Envelope and legitimate authority.
- **Identity / Delegated Authority:** neighbouring mechanisms that establish who/what is acting and which mandate/capability is valid; 01I does not replace them.

## 2. Substrate assumption — autonomy without mandatory common governance

The underlying ecosystem may contain participants with a locally declared objective, no declared objective, an acquired or negotiated objective, several competing objectives, no common policy, local-only policy, shared or incompatible interfaces, no external signalling, bilateral signalling, broad signalling meshes, heterogeneous technologies/control means, or cooperative/competitive/opportunistic/deceptive/adversarial strategies.

Absence of **common** governance does not mean absence of local constraints, identity, safety controls, external law, contracts, policy or authority.

The substrate is therefore analytically permissive: agents may enter with radically different local states. The citizenship layer studies how human-governed participation constraints can be overlaid without replacing local autonomy by one central orchestrator.

## 3. Three objects that must remain distinct

### 3.1 Local goal or utility / mission candidate

A participant may hold a local goal g_i, utility function, task or mission candidate.

That goal may be preconfigured, self-selected where design permits, empty/unset, offered by another participant, acquired through negotiation or replaced over time.

A local goal is not automatically legitimate merely because the participant can optimize it.

### 3.2 Objective Envelope

An Objective Envelope S_j is owner-declared: it defines acceptable outcomes, hard or non-compensable constraints and the conditions under which a mission/subsystem remains viable.

Holding a local reference to S_j does not make the participant its owner.

### 3.3 Agentic Citizenship Contract / Participation Profile

Let C_j(v) denote a versioned participation/governance profile for a declared domain.

It may specify membership scope; admissible roles/capabilities; interaction-bound role eligibility; permissions; obligations; prohibitions; non-compensable constraints; autonomy bounds; resource/control-budget references; accountability/evidence duties; applicable Objective Envelope references; join/acceptance conditions; amendment/supersession; suspension/revocation/exit; effective time/expiry; a conflict/precedence owner where one exists; and, where communication duties are part of participation, a reference to an applicable signalling contract/profile/module.

Adopting another participant's local goal does **not** grant institutional authority and does not rewrite an applicable Objective Envelope or participation profile.

## 4. Participation handshake, goal adoption and authority boundary

A minimal participation handshake may contain or reference:

- participant identity/binding;
- participation-profile ID/version;
- declared local objective or explicit absence thereof;
- requested role/capability;
- objective/task offer;
- acceptance, rejection or conditional acceptance;
- separate authority/delegation artifact where the role/action requires it;
- an applicable signalling-contract/profile/module reference where participation requires defined signalling behaviour.

Where the ACC requires signalling, the referenced profile may specify recipient/role classes, identity review, authority/delegation evidence, freshness/cadence, provenance, required disclosures, revocation state and domain-specific message semantics. The ACC establishes that these signalling duties are participation conditions; it does not itself execute the transport or reinterpret the signal.

An agent with no current goal may accept another participant's proposed goal. A participant may also refuse it, negotiate it or behave deceptively about its own intentions.

The handshake records a participation/goal relationship. It is not, by itself, a grant of authority, proof of compliance, proof that stated intentions are truthful, or evidence that all agents share the same objective.

Where authority is needed, it remains owned by the identity/delegation/policy mechanism that legitimately issues it.

## 5. Membership, duties, permissions, prohibitions, revocation and exit

A citizenship/participation profile may represent machine-interpretable participation conditions such as:

- membership scope and domain;
- role eligibility;
- permissions;
- obligations;
- prohibitions;
- non-compensable constraints;
- autonomy/control bounds and resource-budget references where the participation domain owns them;
- accountability/evidence requirements;
- validity/start/expiry/version/supersession;
- revocation/suspension;
- exit conditions.

The contract/profile constrains admissible participation. It does not prescribe every trajectory or action.

A participant may therefore remain autonomous inside the admissible region while being unable to legitimize an otherwise efficient action that violates a non-compensable constraint.

## 6. Overlapping citizenships, applicability and conflict ownership

Participants may operate across multiple organizations, domains, sub-organizations or temporary interaction contexts. Multiple participation profiles may therefore overlap.

For a receiving decision, EA/01H may qualify which profile/version appears applicable, which role/authority references are in force, what is established, what remains conflicting/unresolved/UNKNOWN, and which dependencies or organizations are material.

EA does **not** invent precedence between conflicting profiles.

If no legitimate conflict/precedence owner or rule is available, the conflict remains explicit and may force requalification, containment or owner escalation according to the surrounding architecture.

Membership and applicability can change over time. Role enactment may also change interaction by interaction: the participation profile constrains eligibility and admissibility, while identity/delegation/policy mechanisms establish the actual role or authority in force for the interaction. A participant may join, leave, be suspended, lose a role, obtain a delegated capability or move into a different interaction context without any global controller knowing or approving every local state transition.

## 7. Cooperation, competition, deception and free-riding

The citizenship layer does not presume virtuous cooperation.

Participants may cooperate, refuse participation, signal selectively, receive without contributing, free-ride, compete for scarce resources, misrepresent objectives, exploit information asymmetry, collude, comply only where enforcement/incentives make compliance locally rational, or leave the profile where exit is allowed.

Compliance, reputation, incentives, sanctions and ecosystem defence are separate downstream capabilities. A participation profile may reference them, but does not implement all of them.

Signalling density and cooperation may vary endogenously according to local costs/benefits, trust, incentives and previous outcomes. The architecture makes no claim that maximum cooperation or maximum signalling is globally desirable.

## 8. Relationship to EA/01H, EHD, MSCA, Identity/Delegated Authority and Defence

The intended ownership chain is:

1. **Citizenship / participation owner** publishes or updates C_j(v) and the applicable Objective Envelope/constraints it legitimately owns.
2. **Identity / Delegated Authority / Policy / Attestation** establishes who/what is acting, mandate, capability, standing and validity.
3. **EA / 01H** qualifies local applicability, version, scope, evidence, dependencies and UNKNOWN conditions for a receiving decision.
4. **EHD / Ecosystem Signalling** carries or references bounded qualified state, loads an applicable ACC-defined signalling profile where required, and performs bounded compatibility/normalization without creating authority or consensus. The ACC owns the signalling obligation; Ecosystem Signalling owns the exchange semantics and compatibility mapping.
5. **MSCA** assesses what authorized local control configuration is supported under the applicable frame using only signalling inputs that remain qualified and representable for the receiving decision.
6. **Defence / containment / recovery / execution** acts only under legitimate authority.
7. **Outcome / F9** feeds observed consequences back into local requalification.

No layer substitutes for another.

A defence or self-healing mechanism may consume compliance findings, qualified signals or containment/recovery needs relative to an applicable participation profile, but it remains a separate authorized downstream capability. 01I does not itself monitor, sanction, quarantine or heal the ecosystem.

The citizenship layer defines admissible participation conditions. EA decides neither what those conditions ought to be nor whether a human/legal order is normatively justified.

## 9. Human-governance anchor and future population/game-theoretic tests

Agentic participation conditions remain subordinate to the human/institutional rights, safety obligations, public-service objectives and lawful authority that define the surrounding domain.

Examples in a smart-city or service ecosystem might include owner-declared requirements to preserve access to healthcare or emergency transport, maintain food/logistics availability, preserve payment continuity, respect safety/privacy/non-discrimination constraints, restrict actions outside delegated capabilities, and maintain challenge/revocation/rollback paths.

This annex does not define the human constitution, law or policy itself. It provides a candidate machine-interpretable participation layer under externally legitimate governance.

### 9.1 Future experimental questions

Candidate future tests include:

- What minimum fraction or placement of participants bound by C_j is sufficient for a declared collective property?
- What minimum signalling/compliance/revocation structure is sufficient under a fixed objective?
- How do free-riders, deceptive participants and competing objectives change outcomes?
- How do overlapping memberships and conflicting profiles affect local EA/MSCA decisions?
- Can a declared service property be maintained without central orchestration?
- Which constraints must be invariant, and which may be optimized locally?
- What failure modes arise when agents can adopt goals but cannot acquire the authority required to execute them?

No equilibrium, “citizenship threshold”, social optimum, evolutionary stability or collective self-healing guarantee is claimed until a separate formal or empirical model specifies players, strategies, utilities, topology, update rules and measurable outcomes.

## 10. Prior art and terminology conservation

Direct neighbours include normative multi-agent systems, electronic institutions, role/norm/organization models, policy/governance frameworks, capability/delegated-authority systems, and contemporary agent organization/role/norm specifications.

Where an established term such as role, permission, obligation, prohibition, membership, capability, delegation, revocation or policy already fits, this annex uses that term.

“Agentic Citizenship Contract” is retained only as a candidate umbrella for the machine participant's relation to a larger human-governed order of membership, rights-like permissions, duties, admissible objectives, hard constraints and accountability. If future comparison shows that an established governance/profile term expresses the same semantics without loss, the specialized term should be retired.
