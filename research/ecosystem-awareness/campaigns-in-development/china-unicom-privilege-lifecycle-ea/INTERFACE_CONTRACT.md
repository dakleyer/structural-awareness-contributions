# China Unicom Theme #23 ↔ EA — candidate interface contract v0.1


> **SOURCE + PURPOSE RECONCILIATION (14 October v0.3):** Use this v0.1 EHD/PDP/PEP proposal only alongside [the complete context-first R1/R2/R3 Challenge](THIRD_PARTY_CHALLENGE_DOSSIER_R123_v0.3.md). The [09:49 source-owner reply](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6165603429) now supports **declaring a restore condition at suspension, verifying it at activation, then fresh intent derivation**. The interface is a potential way to express decision-relative qualifications; **it is not the primary Challenge target, a mandatory China Unicom protocol, nor an EA privilege engine**. Original v0.1 interface text preserved.


**Local owner:** DDS-A-CU-PLM-EA-01. **Status:** source-preserving design; no normative acceptance, stable external schema or endpoint implementation.  
**Primary basis:** [Ying Wang / #23, 14 October](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6164646309); [EA general interfaces v0.5](../../baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md); [00M canonical semantics](../../baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md).

## 1. Boundary of ownership

| Producer / function | Owns the native meaning and decision | May provide to EA / PDP | Cannot be inferred from EA |
|---|---|---|---|
| Identity / authorization issuer (EA IF-S1 / IF-S2) | Identity, principal binding, original grant, mandate, scope, standing, delegation and revocation | Current grant/intent/status, validity time, policy reference, grantor evidence, declared restore predicate | Issuance, renewal, delegation, revocation or legal standing |
| Policy/intent owner + PDP (EA IF-S4) | Risk policy, NACL and privilege admission/reassessment decision | Named current policy, intended action, local verdict, assurance required for that action | An automatic grant from a qualified context signal |
| Runtime/attestation source (EA IF-S3) | Native execution, current credentials, rotation, attested claims and telemetry | Versioned, scoped attestation/result, as-of, source limits | Universal proof of safety from a technical pass |
| Domain dependency/criticality owner | Actual service relationship, observed status, domain-specific significance | Qualified, current dependency/criticality change; graph view or privacy-preserving evidence reference | All unobserved edges, system completeness, authority over foreign services |
| EA/EHD (F1–F9; especially F3/F4/F5/F6/F7/F8) | Scoped qualification and composition; determination limits and re-entry direction | Qualified operating posture, material-change flag, bounded unknown, source lineage and requalification request | Permission, enforcement instruction, privileged override or complete world model |
| PEP | Execution or refusal of the source-authorized action | Observed enforcement receipt and effects | Legitimacy of a decision solely from executing it |
| Human oversight (FG-TIDA Theme #16) | Named human review, bounded escalation/decision path | Decision/approval provenance where source rules require it | A restoration merely because a person agreed to resume the task |

**Rule:** Source-native verdicts and permissions remain source-owned. The same signal may travel via the existing network; no mandatory transport, centralized control plane, new issuer, common database or complete graph is specified here.

## 2. Proposal for a minimal interoperable handoff

The EA [Epistemic Handoff Descriptor (EHD)](../../baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md) is a **semantic metadata contract**, not a second decision engine or mandatory serialized wire format. For a material handoff, retain its six core semantic elements:

1. Producer epistemic profile/reference and version (or inline semantic equivalent).
2. Subject, proposition and affected decision scope.
3. Producer/issuer identity and source ownership.
4. Native functional result **or a resolvable, scope-bound result reference**.
5. Determination/qualification state of the producer for this result.
6. Material unknown-qualifier declaration (including UNKNOWN when the producer cannot establish a relevant bound).

**Conditional fields only when material to the receiving decision**: freshness/as-of and expiry; original authorization/grant reference; purpose; suspension and restore-condition reference/version; credential/NACL policy epoch; dependency edge/change reference, criticality and affected segment; observed vs inferred status; evidence/attestation source; correlation/lineage; coverage and unobserved segments; latency/horizon; privacy disclosure limit; targeted re-entry/return reference. None is claimed mandatory for every message or actor.

The handoff may be a stable producer profile plus a small decision-instance delta; it must not ship all raw private telemetry just to make an EA assessment possible.

## 3. Proposed producer→consumer path

~~~text
G (grant/intent owner) ────────────────┐
P (policy/NACL/current authorization) ├────────────► PDP
T (token rotation/runtime attestation)┘               │
D_A (domain A state) ───────────┐                     │
D_B (domain B scoped changes) ──┼─► optional EA/EHD ─┤
                uncertainty ──┘                     │
                                           PDP decision / scope / basis
                                                    │
                                      ┌─────────────┴──────────────┐
                                      ▼                            ▼
                                  PEP receipt                 #16 oversight
                                      │                            │
                                      └──── event/requalification ─┘
~~~

EA may return a **targeted review request** identifying one material assumption and the competent receiving source. The PDP decides under its authorized local policy; #16 handles human intervention rather than EA synthesizing approval. Where reactivation is blocked, the review path must have an accountable owner, a declared deadline where possible and an explicit unresolved disposition.

## 4. Restoration decision record (candidate, not an issued schema)

| Field group | Minimum content for the bounded experiment | Status / evidence ownership |
|---|---|---|
| Decision correlation | decision_ref, action, resource, decision_time, requested effect | Trial owner; cannot substitute network message ID for semantic decision identity |
| Mandate | grant_ref, principal/grantor, grantee, scope/purpose, issuer, standing, revocation, validity | Authorization owner |
| Suspend/restore | suspend_event_ref, original restore predicate if source declared it, predicate/version and validity | Privilege lifecycle owner |
| Current authorization | policy_ref/version, relevant NACL snapshot, token/credential rotation/freshness, local outcome | PDP/policy/credential owners |
| Context | affected dependency edge and its version, changed service criticality and source, evidence age, propagation scope | Domain owners; not full graph by default |
| Epistemic envelope | EHD producer profile/version, actual native result or resolvable reference, determination, material qualifiers/UNKNOWN, source dependence | EA or native qualifier with same semantic obligations |
| Decision | permitted/restricted/hold/deny and **why**; scope/expiry of any grant; policy/decision version | PDP alone |
| Follow-up | reauthorization needed, proper human-owner path if applicable, re-entry condition, horizon and actual enforcement receipt | PDP/oversight/PEP respectively |

This table is the **proposed evaluation record**, not a draft NACL syntax or a new universal authorization token. Fields can be absent when genuinely irrelevant, but any absent field material to the decision remains explicit as UNKNOWN. A reference that cannot be resolved at decision time cannot silently count as its purported result.

## 5. Two orthogonal outcome axes (do not collapse)

**Axis A — source-native privilege disposition:** full restored / restricted restored / held for re-authorization / denied or revoked / no timely closure. The exact vocabulary and admissibility remain with #23's future agreed policy.

**Axis B — evidence/qualification for that disposition:** sufficient for the declared action and scope / bounded-partial / unresolved or not verifiable / contradicted or stale. It includes who established what, on which reference/version and from which dependent sources.

A source may say **revocation unverifiable** when downstream paths cannot be checked even if direct privileges are revoked. The proposed future revocation branch must preserve the distinction between (i) known revoked coverage, (ii) known live privilege remnants and (iii) unknown path coverage; these can coexist. Do not force the source-proposed three labels into a logically exclusive global completeness score without its authors' approval.

## 6. Confidence and residual indeterminacy

Ying proposes assessing several evidence sources with confidence levels and risk-specific thresholds. This campaign accepts those as **source-proposed PDP logic**, but not a calibrated independent score or a mandate to sum scores. A confidence label without its generating method, scope, source dependence, freshness and measured population is not automatically comparable across domains.

- **A** is the producer's delivered functional result, including an appropriately produced confidence measure if that is its task.
- **B** preserves assessable basis and limitations (including documented probability intervals if justified).
- **C** is a grounded exploration frontier not yet characterized enough to score.
- **D** is the residual whose relevant effect cannot effectively be evaluated by this process under current access, methods, authority and time.

A change indicator related to D may justify requalification while D remains unquantified. Multiple re-emissions of one observation do not establish independent corroboration. The PDP may have a legitimate bounded fallback despite partial uncertainty, but that fallback must be authorized rather than fabricated by EA.

## 7. Cross-domain adversarial checks

| Input condition | Contract test |
|---|---|
| Valid unchanged context | Correctly qualified full restoration remains reachable |
| New material dependency with scoped evidence | Scope and affected resource preserved; no old verdict reused as current |
| Incomplete remote visibility | UNKNOWN and affected segment preserved, with targeted review; no invented full coverage |
| Conflicting source epochs | Identify conflicting policy/graph/credential reference rather than choose the favorable one silently |
| Shared parent source reissued by three observers | Preserve dependence; do not count as three independent confirmations |
| No authority for restricted observation | Do not restore observation rights as a convenient fallback |
| Human says “resume task” but restore condition fails | Human trigger is not a substitute for PDP's current authorization criteria |
| Secret or inaccessible graph facts | No claims about unseen facts merely because the hidden evaluator knows them |

## 8. Change control and limits

This proposal does not update EA's canonical IF-S interfaces, add O7/IF-S14, create an external data-sharing obligation, overwrite any China Unicom work item or presume that #23 has adopted EHD. Only after external clarification should a stage-A successor attempt normative “shall” requirements. Security-sensitive source details should be substituted with owner-approved synthetic fixtures; no confidential NACLs, grants, customer topology or telemetry are required for the first challenge.
