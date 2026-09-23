# ACC Lineage, Identity & Authority Binding Profile

**Status:** canonical MSCA extension profile, v0.1, 23 September 2026.

**Architectural role:** this profile defines the minimum lineage, identity, authority, validity and mutation semantics required to load an Agentic Citizenship Contract (ACC) as a normative extension of an MSCA instance. It does not define a universal identity provider, IAM product, legal contract, credential format, PKI, federation protocol or authorization server.

**Parent architecture:** [Minimum Sufficient Control Architecture — Canonical Architecture](./00_CANONICAL_MSCA_ARCHITECTURE.md)

**ACC source profile:** [Agentic Citizenship Contract / Human-Governed Participation Profile](../../research/ecosystem-awareness/baseline/01I_AGENTIC_CITIZENSHIP_CONTRACT_HUMAN_GOVERNED_PARTICIPATION_PROFILE_v0.1.md)

## 1. Purpose

An ACC can constrain participation, roles, signalling, permissions, prohibitions, autonomy and other governance conditions. Before those constraints can modify an active MSCA representation, the participant must be able to answer a smaller prior question:

> **What ACC lineage is this contract part of, who or what is bound by it, which authority issued or approved it, which parts may change without breaking that lineage, and is the current instance still valid?**

This profile supplies that architectural binding.

It intentionally does **not** prescribe how an organization creates its constitution, IAM system, trust framework, legal authority or approval workflow. Those remain external systems. MSCA only requires enough references and qualified state to know which ACC it is loading and the limits of relying on it.

## 2. ACC lineage is the stable identity of the contract family

An ACC instance is not defined only by its current permissions or fields.

It belongs to an **ACC lineage**: a traceable family of contract/profile instances anchored in a root governance/issuance authority and a declared participation domain.

Conceptually:

~~~text
ACC Root / Lineage Authority
        ↓
ACC lineage identifier
        ↓
issued / approved ACC instance v1
        ↓
authorized successor v2
        ↓
authorized successor v3
        ...
~~~

Two participants can belong to the same ACC lineage while holding different:

- versions;
- roles;
- permissions;
- obligations;
- delegated capabilities;
- autonomy limits;
- signalling duties;
- effective periods.

“Same citizenship” therefore does **not** mean “identical ACC”.

Conversely, two agents can communicate through Ecosystem Signalling while belonging to completely different ACC lineages, incompatible participation domains, or no common ACC at all. Ecosystem Signalling does not require shared citizenship.

## 3. Minimum ACC lineage binding

A loadable ACC profile SHOULD expose or reference enough information to establish the following objects.

| Object | Meaning |
|---|---|
| **ACC_Lineage_ID** | Stable identifier for the contract/profile family whose continuity is being asserted. |
| **ACC_Root / Lineage Authority** | Governance/issuance authority that anchors the lineage. This is an architectural trust/authority reference, not necessarily one cryptographic key or one server. |
| **ACC_Instance_ID** | Identifier of the specific current ACC instance. |
| **Parent_ACC_ID** | Previous instance from which the current instance derives, where lineage is versioned through successor records. |
| **Subject binding** | Identity or actor binding for the participant to which the ACC applies. |
| **Domain / membership scope** | Organization, ecosystem, service, role-domain or participation context in which the ACC is meaningful. |
| **Issuer / approver reference** | Authority that issued, approved or attested the current instance. |
| **Authority evidence reference** | External evidence used to establish the issuer/approver mandate where required. |
| **Version** | Version or revision of the ACC instance/profile. |
| **Effective-from / validity** | When the instance becomes applicable. |
| **Expiry / revalidation condition** | When the instance ceases to be current or must be checked again. |
| **Status** | ACTIVE, SUSPENDED, REVOKED, SUPERSEDED, EXPIRED, or equivalent profile-defined state. |
| **Mutation envelope** | Which fields or classes of change the subject may alter, propose, accept or delegate without breaking the lineage. |
| **Approval route reference** | Which authority/process must approve changes outside the subject's currently delegated mutation rights. |
| **MSCA extension-profile reference** | Mapping used to load the ACC constraints into the MSCA S/E/C/P/M boundary. |
| **Signalling-profile reference** | Optional signalling contract/module required by this ACC. |
| **Conflict / precedence owner reference** | Legitimate owner/rule for conflicts with overlapping ACCs, if one exists. |
| **Proof / status reference** | Optional cryptographic, registry, attestation, credential-status or other verification reference. |

The profile may carry these values directly or reference external authoritative objects. MSCA does not require one universal storage format.

## 4. Root, authority and identity are distinct

The architecture distinguishes three questions.

### 4.1 Who/what is the participant?

This is the **subject identity/binding** question.

The ACC does not need to implement identity proofing itself. It may rely on an external identity/federation/attestation mechanism and retain a qualified reference.

### 4.2 Who may issue or approve this ACC?

This is the **lineage authority** question.

The participant's identity does not prove that it may issue, amend or approve its own ACC.

The root/lineage authority may be an organization, institution, delegated governance role, policy authority, multisignature body, federation, service owner or other legitimate external owner.

### 4.3 What may this participant do under the current ACC?

This is the **contract/admissibility** question.

The ACC may define permissions, prohibitions, role eligibility and mutation rights, but those do not automatically create a runtime authority token or execution permit. Where action requires a separate delegated authority or permit, the external authority mechanism remains authoritative.

Therefore:

~~~text
identity ≠ ACC membership ≠ ACC mutation authority ≠ runtime action authority
~~~

They may be linked, but they are not interchangeable.

## 5. Mutation envelope — what may change without breaking lineage

The **mutation envelope** defines the maximum set of ACC changes that may occur while preserving the current lineage relationship and the participant's authority to make or request those changes.

A profile may divide fields into four classes.

### 5.1 Self-mutable within delegated bounds

The participant may change the value within an explicitly delegated range.

Examples may include:

- selecting among pre-authorized operating preferences;
- narrowing its own autonomy;
- choosing an allowed signalling cadence;
- accepting an optional role already inside its eligibility envelope;
- selecting among pre-approved resource limits.

Self-mutable does not mean untracked. Where material, the successor state remains versioned and attributable.

### 5.2 Delegated successor issuance

The participant or a delegated local authority may create/approve a successor ACC instance **within explicitly delegated issuance rights**.

The successor retains:

- ACC_Lineage_ID;
- traceable parent/version relation;
- subject binding;
- current authority evidence;
- the non-modifiable lineage constraints.

### 5.3 Approval-required mutation

The participant may identify or request the change, but another legitimate authority must approve/issue the successor ACC.

Examples can include:

- broader role eligibility;
- increased autonomy;
- new resource/control budget;
- additional delegation rights;
- a different signalling obligation;
- extension of validity;
- modification of non-compensable participation constraints where the governing system permits such amendment.

The participant's local reasoning, opportunity gradient or MSCA assessment may justify requesting the change. They do not approve it.

### 5.4 Lineage-breaking change

Some changes cannot be represented as a valid mutation of the current lineage.

Examples may include, depending on the governing profile:

- changing the root/lineage authority;
- moving to an unrelated governance domain;
- replacing immutable lineage constraints;
- assuming membership that the current lineage cannot grant;
- acquiring authority that no valid delegation path can derive from the current root.

Such a change requires an **external issuance, join, migration or governance process**. That process is outside this profile.

A new ACC may later be loaded, but the previous system must not fabricate continuity merely because the new ACC is operationally convenient.

## 6. Change lifecycle

An ACC change may originate from many sources:

- explicit human/institutional instruction;
- policy update;
- expiry/revocation;
- role change;
- authority change;
- MSCA control gap;
- Regime Awareness change;
- Ecosystem Signalling;
- a Decision-Scoped Epistemic Opportunity / gradient indicating that a different role, capability or participation state would be useful.

The canonical internal sequence is:

~~~text
change opportunity / requirement
→ identify current ACC lineage and instance
→ verify current subject binding
→ verify lineage authority / issuer / status
→ classify requested change against mutation envelope
→ SELF-DELEGATED | APPROVAL_REQUIRED | LINEAGE_BREAKING
→ if permitted, obtain required approval/evidence
→ issue/accept successor ACC instance
→ verify version, parent, validity and status
→ MSCA normative-extension compatibility check
→ load new ACC extension
→ invalidate only dependent prior MSCA/ACC claims
~~~

The gradient may therefore lead to:

~~~text
opportunity
→ request ACC modification
→ authority decision
→ approved successor ACC
→ compatibility/reload
→ new control/admissibility possibilities
~~~

The gradient never becomes the approval authority.

## 7. Lineage continuity rule

An ACC successor belongs to the same lineage only if continuity can be established under the governing profile.

At minimum, the receiver SHOULD be able to determine:

- the claimed ACC_Lineage_ID;
- predecessor/parent relation or other recognized continuity mechanism;
- the authority that issued/approved the successor;
- that the issuing authority was itself authorized for that type of change;
- that immutable lineage constraints were not silently rewritten;
- the effective time and supersession relation;
- whether prior revocation/suspension state affects the successor.

If material continuity cannot be established, the new ACC remains:

- **UNRESOLVED_LINEAGE**, or
- **NEW / EXTERNAL_LINEAGE**

according to the applicable profile.

It must not be silently treated as a valid successor.

## 8. ACC loading into MSCA

ACC is loaded into MSCA only after two different questions are answered:

1. **Lineage/authority validity:** is this a current, attributable ACC instance whose issuance/change path is sufficiently established?
2. **MSCA extension compatibility:** can its material constraints be bound into the current MSCA extension model without redefining S/E/C/P/M?

Conceptually:

~~~text
ACC instance
→ lineage / identity / authority qualification
→ validity / status qualification
→ mutation / approval lineage verified
→ MSCA normative-extension compatibility
→ COMPATIBLE | BOUNDED_COMPATIBLE | INCOMPATIBLE
→ load / bounded load / reject
~~~

A contract can therefore be authentic but MSCA-incompatible, or MSCA-compatible but not currently valid/authorized.

These states must remain distinct.

## 9. ACC and Ecosystem Signalling across organizations

Ecosystem Signalling does not require:

- the same ACC_Lineage_ID;
- the same issuer;
- the same organization;
- compatible role systems;
- common authority roots;
- common objectives.

A participant may signal to a participant from another organization or ecosystem.

The receiver may use the sender's ACC lineage/profile reference as one bounded input when deciding:

- whether the sender's claimed role is meaningful;
- what signalling obligations the sender claims to be under;
- which authority references should be verified;
- which fields can be relied on;
- whether a specialised signalling profile can be loaded.

A foreign ACC is not automatically imported into the receiver's MSCA.

Cross-lineage interaction is therefore:

~~~text
foreign signal
→ sender ACC/authority references where material
→ signalling compatibility qualification
→ receiver-local trust / epistemic qualification
→ bounded use
~~~

not:

~~~text
foreign ACC
→ automatic local citizenship
~~~

## 10. Overlapping ACCs

A participant may simultaneously hold ACCs from multiple organizations, domains or roles.

Examples:

- employer organization;
- regulated industry domain;
- city/service participation profile;
- temporary project or transaction role.

The architecture does not invent global precedence.

Each ACC retains:

- its lineage;
- its domain/scope;
- its authority root;
- its validity;
- its mutation envelope.

Where profiles overlap, a legitimate conflict/precedence owner or rule may determine which constraint applies. If no such owner/rule can be established, the conflict remains explicit and may render the relevant MSCA assessment UNRESOLVED or force targeted requalification.

## 11. Protocol-neutral compatibility with IAM and credential systems

This profile defines semantics, not a security protocol.

Existing identity/access/credential standards can carry different parts of the binding without becoming the definition of ACC.

| Existing mechanism | Useful ACC binding | What it does not establish by itself |
|---|---|---|
| **NIST SP 800-63-4 family** | Identity proofing, authentication, federation and assertions can support subject/issuer assurance and federation references. | ACC membership, mutation rights, MSCA sufficiency or application-specific governance. |
| **OpenID Connect** | Authenticated subject identity and claims from an identity layer. | Contract lineage or authorization semantics beyond the claims/profile actually issued. |
| **OAuth 2.0 / current security BCP** | Scoped access authorization and protected-resource access patterns. | Institutional citizenship/participation lineage or general ACC governance. |
| **OAuth 2.0 Token Exchange (RFC 8693)** | Delegation/impersonation token relationships can represent actor/subject delegation paths where appropriate. | The legitimacy of the governing ACC lineage or all role/contract semantics. |
| **W3C Verifiable Credentials Data Model 2.0** | Issuer/holder/verifier model, extensible signed claims, validity/status references and revocation/suspension mechanisms can carry ACC-related assertions. | The business/governance logic that decides whether an ACC change is allowed or how conflicting ACCs are resolved. |

Protocol compatibility is therefore an adapter/profile problem.

An implementation may use one or several of these mechanisms, or another qualified mechanism, provided the ACC lineage semantics remain reconstructible.

Current reference anchors:

- NIST SP 800-63-4: https://csrc.nist.gov/pubs/sp/800/63/4/final
- OpenID Connect Core 1.0: https://openid.net/specs/openid-connect-core-1_0.html
- OAuth 2.0: https://www.rfc-editor.org/rfc/rfc6749
- OAuth 2.0 Security BCP: https://www.rfc-editor.org/rfc/rfc9700
- OAuth 2.0 Token Exchange: https://www.rfc-editor.org/rfc/rfc8693
- W3C Verifiable Credentials Data Model 2.0: https://www.w3.org/TR/vc-data-model-2.0/

These references establish interoperability neighbours, not endorsement of ACC by those standards bodies.

## 12. Minimum internal ACC-lineage state

For an implementation that only needs the minimum internal kernel, a compact ACC lineage state can be represented conceptually as:

~~~text
ACCLineageBinding {
  lineage_id
  instance_id
  parent_id?
  subject_ref
  root_authority_ref
  issuer_or_approver_ref
  domain_scope
  version
  effective_from
  expires_or_revalidate
  status
  mutation_envelope_ref
  approval_route_ref
  msca_extension_profile_ref
  signalling_profile_ref?
  proof_or_status_ref?
}
~~~

This is an architectural example, not a mandatory wire schema.

The important property is reconstructibility of lineage and mutation authority, not field naming.

## 13. What this profile does not own

This profile does not define:

- how a state, company, DAO, city or institution decides who may become a participant;
- the legal validity of a contract;
- identity-proofing algorithms;
- authentication protocols;
- PKI or key-management design;
- OAuth/OIDC/VC token formats;
- organizational approval workflow implementation;
- policy-authoring systems;
- sanctions/enforcement;
- cryptographic consensus;
- universal trust roots;
- how a completely new ACC lineage is created.

Those may be external systems referenced by the profile.

The MSCA/ACC architecture needs only enough qualified information to preserve **who/what, which lineage, under whose authority, within which mutation limits, and for what validity period**.

## 14. Conformance / falsification conditions

The lineage profile fails its architectural purpose if an implementation:

- cannot distinguish subject identity from mutation authority;
- cannot identify the ACC lineage/root relevant to the current instance;
- cannot distinguish a successor from an unrelated ACC;
- allows a participant to exceed its mutation envelope without an external authority path;
- treats an expired/revoked/suspended ACC as current;
- rewrites history instead of preserving parent/version lineage;
- converts a signalling relationship into shared citizenship automatically;
- imports a foreign ACC into local MSCA without extension compatibility qualification;
- treats possession of an ACC as a runtime action permit;
- cannot represent an unresolved lineage/authority question explicitly.

## 15. Canonical thesis

ACC lineage is the minimum continuity mechanism that prevents a participation contract from becoming a mutable, self-declared blob.

The participant may discover opportunities, request broader roles, change preferences, narrow autonomy or seek new capabilities. Its current ACC may explicitly permit some of those changes and require approval for others.

What preserves continuity is not that every field stays fixed. It is that:

> **the root/lineage, subject binding, authority path, mutation envelope, validity and successor relation remain reconstructible.**

Once that lineage is qualified, the ACC can be loaded as a normative MSCA extension.

If the lineage cannot support the proposed change, the system does not manufacture a new citizenship. A new issuance/join/migration process must occur outside this profile.
