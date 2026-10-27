# Taxonomy: problems, distinctions and ideas under review

**Working review register — not a canonical glossary, normative taxonomy, or source successor.**

The purpose is to make semantic difficulties visible where the corpus is reviewed: concrete observations, awkward cases, alternative interpretations and ideas that can be challenged in pull requests. This register spans the whole Structural Awareness programme and relevant FG-TIDA contributions. It is not confined to one correspondent, one glossary, Ecosystem Awareness alone, or keyword-search results.

An entry can document a useful distinction already present in a source, a candidate ambiguity, a disagreement or a strategic question. **Thirty entries do not mean thirty confirmed defects.** All initial entries remain open. Initial source reading is not an exhaustive occurrence audit, resolution of a dispute, independent validation or institutional adoption.

## Where this fits

This is optional/contextual review material under [DC-GH-01](../../DOCUMENT_CONTROL.md), not a new canonical navigation owner or another VNext. The [Corpus Review Procedure](../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md) still governs substantive source review. [Claim boundaries](../../governance/CLAIM_BOUNDARIES.md) and the [contribution route](../../CONTRIBUTING.md) continue to apply.

A source-specific change belongs in that source's **existing owning VNext**, with its exact before/after, affected consumers and approval. Link the same observation from the affected source/receiver reviews rather than copy competing proposals here. Nothing in this seed rewrites source definitions, frozen evidence, protected routers or another contributor's terminology. The existing private coordination initiative is reused; private correspondence, private Drive links, credentials and internal identities are intentionally not published.

## How to add or debate an observation

1. Reuse an existing TX-F ID when the problem is the same; otherwise add the next unused ID.
2. Give the actual source passage/context, affected meaning and a primary public source. Pin the source edition when its wording matters. For an editable external issue/comment, say when it was observed and do not call its URL an immutable snapshot.
3. Explain why the distinction matters and give a counterexample or next question. Separate a source fact, an interpretation and a hypothesis.
4. Use PR conversation for discussion and a proposed commit for the durable conclusion. Record objections and alternative readings without inventing reviewers or claiming consensus from bot agreement.
5. Link any material correction to the affected owning VNext. A register entry does not approve a correction or authorize merge.
6. Keep resolved/refuted/superseded entries, their original IDs and the decision reference. Remove only settled pending work, never its reasoning or history.

The structured companion is [observations.json](./observations.json). Keep its IDs, open states and human-readable entries consistent in the same PR. `proposed_source_change: null` means that this seed contains **no executable source-edit proposal**, not that the question has been resolved. Source-observation cutoff for this initial seed: 26 October 2026. Pinned own-corpus references identify the reading edition, not a requirement to freeze future development.

## Strategic direction to test

A federated, multi-axis concept system is a useful working hypothesis: a small shared core, source-owned domain vocabularies, versioned sense identities and explicit crosswalks. The goal is to distinguish a verbal disagreement from a decision-relevant conceptual difference and to show what a translation loses. It is not to maximize terminology or impose our labels on other contributors.

Near term: inventory the programme's collections and extract source-qualified senses. Medium term: test minimal pairs, crosswalks and consumer consequences. Longer term: maintain versioned concepts and measured compatibility checks. These are research horizons, not promised delivery dates or autonomous scheduling.

## Initial observation index

| ID | Question or distinction | Basis | State |
| --- | --- | --- | --- |
| [TX-F001](#tx-f001) | Taxonomy, terminology, glossary and ontology are different work products | Candidate / hypothesis | Open |
| [TX-F002](#tx-f002) | Programme, architectural contribution and technical gates are different levels | Initial source reading | Open |
| [TX-F003](#tx-f003) | A/B/C/D should not become four mutually exclusive bins | Initial source reading | Open |
| [TX-F004](#tx-f004) | Type 0 is not another management-failure class | Initial source reading | Open |
| [TX-F005](#tx-f005) | Representation state is not assessment state | Initial source reading | Open |
| [TX-F006](#tx-f006) | S/E/C/P/M are semantic slots, not five software modules | Initial source reading | Open |
| [TX-F007](#tx-f007) | Role, position, capability, mandate and permission are not synonyms | Initial source reading | Open |
| [TX-F008](#tx-f008) | RA collides: Regime Awareness versus Remote Attestation | Initial source reading | Open |
| [TX-F009](#tx-f009) | Observed delta, receiver gradient and operational posture are different objects | Initial source reading | Open |
| [TX-F010](#tx-f010) | P1/P2/P3 postures collide with P1–P6 principle identifiers | Candidate / hypothesis | Open |
| [TX-F011](#tx-f011) | DDS stages and local gates/testbed stages need namespaces | Initial source reading | Open |
| [TX-F012](#tx-f012) | RL Trajectory/Verifier do not erase other domain meanings | Initial source reading | Open |
| [TX-F013](#tx-f013) | Policy has multiple authored objects and scopes | Initial source reading | Open |
| [TX-F014](#tx-f014) | A flag taxonomy is not a cross-evaluator failure taxonomy | Initial source reading | Open |
| [TX-F015](#tx-f015) | Trust, trustworthiness, evidence and reliance remain distinct questions | Initial source reading | Open |
| [TX-F016](#tx-f016) | Identity must not collapse principal, instance and legal binding | Candidate / hypothesis | Open |
| [TX-F017](#tx-f017) | Available, presented, noticed and understood evidence are different claims | Initial source reading | Open |
| [TX-F018](#tx-f018) | Finding, sufficiency judgment and authorized decision are different steps | Initial source reading | Open |
| [TX-F019](#tx-f019) | Applicable authority does not establish timely capacity | Initial source reading | Open |
| [TX-F020](#tx-f020) | Acknowledgment, attempted action and observed effect are not equivalent | Initial source reading | Open |
| [TX-F021](#tx-f021) | Epistemic validity and response opportunity use different clocks | Initial source reading | Open |
| [TX-F022](#tx-f022) | Historical authenticity is not present applicability | Initial source reading | Open |
| [TX-F023](#tx-f023) | Changed conditions and changed relevance boundaries are different problems | Initial source reading | Open |
| [TX-F024](#tx-f024) | Human Intelligence Debt is not runtime intervention capacity | Initial source reading | Open |
| [TX-F025](#tx-f025) | Principle, requirement, hypothesis, condition and KPI need claim types | Initial source reading | Open |
| [TX-F026](#tx-f026) | Current, candidate, test-only and adopted need separate status axes | Initial source reading | Open |
| [TX-F027](#tx-f027) | Thematic coverage is not evidential coverage | Initial source reading | Open |
| [TX-F028](#tx-f028) | Cross-WG terminology is an opportunity, not an appointment or accepted slot | Initial source reading | Open |
| [TX-F029](#tx-f029) | Same-label semantic change needs versioned consumer review | Candidate / hypothesis | Open |
| [TX-F030](#tx-f030) | Flattened unknown-like statuses can lose decision-relevant reasons | Initial source reading | Open |
| [TX-F031](#tx-f031) | Result-aware EHD transport versus the N02 no-A input boundary | Published source review; consumer test pending | Disputed |
| [TX-F032](#tx-f032) | Reference scenario versus technology–Challenge instantiation | Published source review; consumer test pending | Open |

## Observation cards

<a id="tx-f001"></a>

### TX-F001 — Taxonomy, terminology, glossary and ontology are different work products

A list of terms, a classification and a relational model answer different questions. Whether the initiative needs each is a design question, not a new universal definition.

**Question / minimal pair:** Compare a term list, a classification with overlapping members and a relation-bearing model; record what each cannot answer.

**Sources:** [1](https://github.com/FG-TIDA/themes/issues/32).

**State:** open. Candidate or design hypothesis; locate and contrast exact occurrences before calling it an established defect. No source correction proposed in this entry.

<a id="tx-f002"></a>

### TX-F002 — Programme, architectural contribution and technical gates are different levels

Calling Structural Awareness, Ecosystem Positioning, EA, RA and MSCA interchangeable hides which source and function supports a claim.

**Question / minimal pair:** Trace one claim from programme narrative to its owning architecture/gate and name the actual supporting source.

**Sources:** [1](https://github.com/dakleyer/structural-awareness-contributions/blob/1b5a07f916d3f65cf467628e2bec5b13b769a029/architectural-contributions/ecosystem-positioning/README.md).

**State:** open. Source distinction under review; the affected occurrence/consumer inventory and compatibility test remain incomplete. No source correction proposed in this entry.

<a id="tx-f003"></a>

### TX-F003 — A/B/C/D should not become four mutually exclusive bins

A represented item not yet consulted must not automatically become C. The qualification depends on process, subject, decision and time; it is not an exhaustive population partition.

**Question / minimal pair:** Test a known, evaluable but unconsulted record; record the subject/process/time rather than reclassifying it as an intrinsically unknown object.

**Sources:** [1](https://github.com/dakleyer/structural-awareness-contributions/blob/1b5a07f916d3f65cf467628e2bec5b13b769a029/research/ecosystem-awareness/baseline/00_CANONICAL_ARCHITECTURE_TOPOLOGY.md).

**State:** open. Source distinction under review; the affected occurrence/consumer inventory and compatibility test remain incomplete. No source correction proposed in this entry.

<a id="tx-f004"></a>

### TX-F004 — Type 0 is not another management-failure class

Structural non-determination, management failures and ensuing trajectories must not be added as if they were classes of the same kind.

**Question / minimal pair:** Classify a non-determination, a Type1/2 event and a cascade without treating them as three peer failure labels.

**Sources:** [1](https://github.com/dakleyer/structural-awareness-contributions/blob/1b5a07f916d3f65cf467628e2bec5b13b769a029/research/ecosystem-awareness/baseline/00_CANONICAL_ARCHITECTURE_TOPOLOGY.md).

**State:** open. Source distinction under review; the affected occurrence/consumer inventory and compatibility test remain incomplete. No source correction proposed in this entry.

<a id="tx-f005"></a>

### TX-F005 — Representation state is not assessment state

An unpopulated representation and an unassessed sufficiency claim are different absences. Schema completeness does not establish support.

**Question / minimal pair:** Use a fully populated but unevaluated instance and an empty instance; neither should silently become SUPPORTED.

**Sources:** [1](https://github.com/dakleyer/structural-awareness-contributions/blob/1b5a07f916d3f65cf467628e2bec5b13b769a029/standards/minimum-sufficient-control/00_CANONICAL_MSCA_ARCHITECTURE.md).

**State:** open. Source distinction under review; the affected occurrence/consumer inventory and compatibility test remain incomplete. No source correction proposed in this entry.

<a id="tx-f006"></a>

### TX-F006 — S/E/C/P/M are semantic slots, not five software modules

Treating the kernel slots as deployable components or silently adding a sixth canonical element would change the architecture rather than clarify a label.

**Question / minimal pair:** Ask for one implementation mapping of each slot, with an explicit statement that the mapping is not the canonical definition.

**Sources:** [1](https://github.com/dakleyer/structural-awareness-contributions/blob/1b5a07f916d3f65cf467628e2bec5b13b769a029/standards/minimum-sufficient-control/00_CANONICAL_MSCA_ARCHITECTURE.md).

**State:** open. Source distinction under review; the affected occurrence/consumer inventory and compatibility test remain incomplete. No source correction proposed in this entry.

<a id="tx-f007"></a>

### TX-F007 — Role, position, capability, mandate and permission are not synonyms

A capability-bearing participant is not thereby authorized. A functional projection and a qualified epistemic position answer different questions.

**Question / minimal pair:** Use a capable but unauthorized participant, and an authorized but unavailable participant.

**Sources:** [1](https://github.com/dakleyer/structural-awareness-contributions/blob/1b5a07f916d3f65cf467628e2bec5b13b769a029/standards/minimum-sufficient-control/02_MSCA_ARCHITECTURAL_ROLE.md).

**State:** open. Source distinction under review; the affected occurrence/consumer inventory and compatibility test remain incomplete. No source correction proposed in this entry.

<a id="tx-f008"></a>

### TX-F008 — RA collides: Regime Awareness versus Remote Attestation

The same short token refers to two different concepts in the combined corpus. Text matching alone cannot justify a mapping.

**Question / minimal pair:** Require an expanded name and source namespace on first use; reject Regime Awareness = Remote Attestation.

**Sources:** [1](https://github.com/dakleyer/structural-awareness-contributions/blob/1b5a07f916d3f65cf467628e2bec5b13b769a029/research/regime-awareness/README.md), [2](https://github.com/FG-TIDA/wg1-ra-aai).

**State:** open. Source distinction under review; the affected occurrence/consumer inventory and compatibility test remain incomplete. No source correction proposed in this entry.

<a id="tx-f009"></a>

### TX-F009 — Observed delta, receiver gradient and operational posture are different objects

A qualified directional change is not an executed containment action or a receiver-specific migration destination.

**Question / minimal pair:** Trace producer output to receiver decision and observed action; identify which transition is not licensed by a change signal.

**Sources:** [1](https://github.com/dakleyer/structural-awareness-contributions/blob/1b5a07f916d3f65cf467628e2bec5b13b769a029/research/regime-awareness/README.md).

**State:** open. Source distinction under review; the affected occurrence/consumer inventory and compatibility test remain incomplete. No source correction proposed in this entry.

<a id="tx-f010"></a>

### TX-F010 — P1/P2/P3 postures collide with P1–P6 principle identifiers

A short P identifier can denote an operational posture or a principle, depending on its source family. This is a candidate occurrence audit, not an approved renaming.

**Question / minimal pair:** Inventory occurrences and preserve existing source identifiers; qualify new references by family.

**Sources:** [1](https://github.com/dakleyer/structural-awareness-contributions/blob/1b5a07f916d3f65cf467628e2bec5b13b769a029/research/ecosystem-awareness/baseline/00_CANONICAL_ARCHITECTURE_TOPOLOGY.md), [2](https://github.com/dakleyer/structural-awareness-contributions/tree/1b5a07f916d3f65cf467628e2bec5b13b769a029/research/ecosystem-awareness/baseline).

**State:** open. Candidate or design hypothesis; locate and contrast exact occurrences before calling it an established defect. No source correction proposed in this entry.

<a id="tx-f011"></a>

### TX-F011 — DDS stages and local gates/testbed stages need namespaces

DDS A/B/C, local Stage-0/Stage-1 and R-number families are source-specific. A shared number is not a universal translation rule.

**Question / minimal pair:** Build a source-specific stage mapping including a deliberately mismatched Stage1 pair that must remain unmapped.

**Sources:** [1](https://github.com/dakleyer/structural-awareness-contributions/blob/1b5a07f916d3f65cf467628e2bec5b13b769a029/research/ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md).

**State:** open. Source distinction under review; the affected occurrence/consumer inventory and compatibility test remain incomplete. No source correction proposed in this entry.

<a id="tx-f012"></a>

### TX-F012 — RL Trajectory/Verifier do not erase other domain meanings

The reinforcement-learning meanings proposed in Theme52 do not supersede DDS trajectories or credential/evidence verification.

**Question / minimal pair:** Compare one RL trajectory/verifier example with a DDS and a credential-verifier example; preserve non-equivalence.

**Sources:** [1](https://github.com/FG-TIDA/themes/issues/52).

**State:** open. Source distinction under review; the affected occurrence/consumer inventory and compatibility test remain incomplete. No source correction proposed in this entry.

<a id="tx-f013"></a>

### TX-F013 — Policy has multiple authored objects and scopes

Deployment configuration, an authored evaluation reference and jurisdictional requirements may all be called policy; their authors and change authorities can differ.

**Question / minimal pair:** Record originator, jurisdiction/domain, applicable version and authority to change each policy object.

**Sources:** [1](https://github.com/FG-TIDA/themes/issues/32#issuecomment-5926106469).

**State:** open. Source distinction under review; the affected occurrence/consumer inventory and compatibility test remain incomplete. No source correction proposed in this entry.

<a id="tx-f014"></a>

### TX-F014 — A flag taxonomy is not a cross-evaluator failure taxonomy

A collection of flags measured by one evaluator and a classification of failures between evaluators have different universes and observation units.

**Question / minimal pair:** State the classified universe and observation unit before combining any categories.

**Sources:** [1](https://github.com/FG-TIDA/themes/issues/32).

**State:** open. Source distinction under review; the affected occurrence/consumer inventory and compatibility test remain incomplete. No source correction proposed in this entry.

<a id="tx-f015"></a>

### TX-F015 — Trust, trustworthiness, evidence and reliance remain distinct questions

Contributed definitions in Theme51 and meeting discussions do not establish a single accepted meaning or make reliance a measured property.

**Question / minimal pair:** Record rival definitions and one decision that differs between them; do not settle the dispute by frequency of the word.

**Sources:** [1](https://github.com/FG-TIDA/themes/issues/51), [2](https://github.com/FG-TIDA/meetings/blob/main/2026-10-14-preparation-meeting-4/minutes.md).

**State:** open. Source distinction under review; the affected occurrence/consumer inventory and compatibility test remain incomplete. No source correction proposed in this entry.

<a id="tx-f016"></a>

### TX-F016 — Identity must not collapse principal, instance and legal binding

Authentication, logical identity, represented principal, runtime instance and legal binding require different evidence. A signature cannot fill all missing links.

**Question / minimal pair:** Use a valid signature with unknown principal authorization and legal scope; retain those gaps.

**Sources:** [1](https://github.com/FG-TIDA/use-cases/issues/20).

**State:** open. Candidate or design hypothesis; locate and contrast exact occurrences before calling it an established defect. No source correction proposed in this entry.

<a id="tx-f017"></a>

### TX-F017 — Available, presented, noticed and understood evidence are different claims

Evidence can exist without being shown, and be shown without evidence of comprehension. Do not turn this into an automatic ladder of approval.

**Question / minimal pair:** Use a delivered document with no evidence of comprehension; keep shown and understood independent.

**Sources:** [1](https://github.com/FG-TIDA/themes/issues/16#issuecomment-6302053285).

**State:** open. Source distinction under review; the affected occurrence/consumer inventory and compatibility test remain incomplete. No source correction proposed in this entry.

<a id="tx-f018"></a>

### TX-F018 — Finding, sufficiency judgment and authorized decision are different steps

A finding may support a scoped judgment without giving the recipient permission to act. Support, inference and authorization are different relations.

**Question / minimal pair:** Use a scoped experimental PASS with no applicable action authority.

**Sources:** [1](https://github.com/FG-TIDA/use-cases/issues/20#issuecomment-6301163175).

**State:** open. Source distinction under review; the affected occurrence/consumer inventory and compatibility test remain incomplete. No source correction proposed in this entry.

<a id="tx-f019"></a>

### TX-F019 — Applicable authority does not establish timely capacity

A named decision maker may lack information, access, availability or time. External queue overload is not by itself local incompetence.

**Question / minimal pair:** Keep authority, capability, information access and useful intervention time separate in a specific escalation example.

**Sources:** [1](https://github.com/dakleyer/structural-awareness-contributions/blob/1b5a07f916d3f65cf467628e2bec5b13b769a029/research/ecosystem-awareness/baseline/01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md).

**State:** open. Source distinction under review; the affected occurrence/consumer inventory and compatibility test remain incomplete. No source correction proposed in this entry.

<a id="tx-f020"></a>

### TX-F020 — Acknowledgment, attempted action and observed effect are not equivalent

Receipt or acknowledgement does not establish that the intended effect occurred. Repeating or signing a claim does not make its observation independent.

**Question / minimal pair:** Use an ACK with no independent effect evidence; preserve the missing observation and time window.

**Sources:** [1](https://github.com/dakleyer/structural-awareness-contributions/blob/1b5a07f916d3f65cf467628e2bec5b13b769a029/research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md), [2](https://github.com/dakleyer/structural-awareness-contributions/blob/1b5a07f916d3f65cf467628e2bec5b13b769a029/research/ecosystem-awareness/fg-tida/interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_v0.1.md).

**State:** open. Source distinction under review; the affected occurrence/consumer inventory and compatibility test remain incomplete. No source correction proposed in this entry.

<a id="tx-f021"></a>

### TX-F021 — Epistemic validity and response opportunity use different clocks

A still-valid finding can arrive too late for a useful action; spare time cannot make stale findings current. Synthetic timestamps do not establish measured latency.

**Question / minimal pair:** Use a valid-but-late result and a stale-but-fast result; neither implies the other clock passed.

**Sources:** [1](https://github.com/dakleyer/structural-awareness-contributions/blob/1b5a07f916d3f65cf467628e2bec5b13b769a029/research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md).

**State:** open. Source distinction under review; the affected occurrence/consumer inventory and compatibility test remain incomplete. No source correction proposed in this entry.

<a id="tx-f022"></a>

### TX-F022 — Historical authenticity is not present applicability

Preserve the original finding while requalifying the present use affected by a changed dependency or context.

**Question / minimal pair:** Link a historical authentic result to a present use that is no longer supported, without changing the old result.

**Sources:** [1](https://github.com/FG-TIDA/use-cases/issues/20#issuecomment-6375358937).

**State:** open. Source distinction under review; the affected occurrence/consumer inventory and compatibility test remain incomplete. No source correction proposed in this entry.

<a id="tx-f023"></a>

### TX-F023 — Changed conditions and changed relevance boundaries are different problems

A monitored variable can change, or a previously unrepresented factor can become material without changing the old source bytes. Monitoring does not prove complete coverage.

**Question / minimal pair:** Contrast ordinary drift with a relevance-boundary change; specify the discovery limit and unknown residual.

**Sources:** [1](https://github.com/FG-TIDA/use-cases/issues/20#issuecomment-6375358937).

**State:** open. Source distinction under review; the affected occurrence/consumer inventory and compatibility test remain incomplete. No source correction proposed in this entry.

<a id="tx-f024"></a>

### TX-F024 — Human Intelligence Debt is not runtime intervention capacity

The architectural use of human intelligence and whether a specific intervention route can act now need separate units, estimators and claims.

**Question / minimal pair:** Use a runtime queue delay without inferring a universal intelligence-debt score.

**Sources:** [1](https://github.com/dakleyer/structural-awareness-contributions/blob/1b5a07f916d3f65cf467628e2bec5b13b769a029/research/ecosystem-awareness/baseline/01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md).

**State:** open. Source distinction under review; the affected occurrence/consumer inventory and compatibility test remain incomplete. No source correction proposed in this entry.

<a id="tx-f025"></a>

### TX-F025 — Principle, requirement, hypothesis, condition and KPI need claim types

Document placement does not turn a hypothesis into proof or make a KPI a requirement. S/T/H families need source-qualified interpretation.

**Question / minimal pair:** Trace a hypothesis through its requirement and measurement consumers; retain its actual proof/execution status.

**Sources:** [1](https://github.com/dakleyer/structural-awareness-contributions/blob/1b5a07f916d3f65cf467628e2bec5b13b769a029/research/ecosystem-awareness/baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md).

**State:** open. Source distinction under review; the affected occurrence/consumer inventory and compatibility test remain incomplete. No source correction proposed in this entry.

<a id="tx-f026"></a>

### TX-F026 — Current, candidate, test-only and adopted need separate status axes

Source description, candidate interface field, test evidence and institutional adoption are not successive states established merely by publication.

**Question / minimal pair:** Try mapping a test-only field to adopted and require rejection unless the actual decision evidence exists.

**Sources:** [1](https://github.com/dakleyer/structural-awareness-contributions/blob/1b5a07f916d3f65cf467628e2bec5b13b769a029/research/ecosystem-awareness/fg-tida/interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_v0.1.md).

**State:** open. Source distinction under review; the affected occurrence/consumer inventory and compatibility test remain incomplete. No source correction proposed in this entry.

<a id="tx-f027"></a>

### TX-F027 — Thematic coverage is not evidential coverage

A theme/coverage map can locate a question without demonstrating its specification, implementation or resolution.

**Question / minimal pair:** Keep conceptual, specification, implementation and evidence coverage as four views with explicit gaps.

**Sources:** [1](https://github.com/FG-TIDA/themes/issues/50).

**State:** open. Source distinction under review; the affected occurrence/consumer inventory and compatibility test remain incomplete. No source correction proposed in this entry.

<a id="tx-f028"></a>

### TX-F028 — Cross-WG terminology is an opportunity, not an appointment or accepted slot

The meeting record describes potential terminology support. It does not appoint a lead, grant a contribution slot or authorize an external submission.

**Question / minimal pair:** Recheck current procedural conditions before any external approach; record no appointment or submission from this entry.

**Sources:** [1](https://github.com/FG-TIDA/meetings/blob/main/2026-10-14-preparation-meeting-4/minutes.md).

**State:** open. Source distinction under review; the affected occurrence/consumer inventory and compatibility test remain incomplete. No source correction proposed in this entry.

<a id="tx-f029"></a>

### TX-F029 — Same-label semantic change needs versioned consumer review

A label can remain stable while scope, criterion or decision consequences change. A global word replacement would hide consumer compatibility questions.

**Question / minimal pair:** Select one real meaning change and its consumers; propose a versioned mapping before any source correction.

**Sources:** [1](https://github.com/dakleyer/structural-awareness-contributions/blob/1b5a07f916d3f65cf467628e2bec5b13b769a029/research/ecosystem-awareness/baseline/00_CANONICAL_ARCHITECTURE_TOPOLOGY.md), [2](https://github.com/dakleyer/structural-awareness-contributions/blob/1b5a07f916d3f65cf467628e2bec5b13b769a029/research/ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md).

**State:** open. Candidate or design hypothesis; locate and contrast exact occurrences before calling it an established defect. No source correction proposed in this entry.

<a id="tx-f030"></a>

### TX-F030 — Flattened unknown-like statuses can lose decision-relevant reasons

INDETERMINATE, no-assertion, HELD, UNKNOWN, not-evaluated and not-applicable can encode different reasons. A single unknown may change an action boundary.

**Question / minimal pair:** Construct a mapping with a positive preservation example and a reason-losing negative example before declaring equivalence.

**Sources:** [1](https://github.com/dakleyer/structural-awareness-contributions/blob/1b5a07f916d3f65cf467628e2bec5b13b769a029/research/ecosystem-awareness/baseline/01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md), [2](https://github.com/dakleyer/structural-awareness-contributions/blob/1b5a07f916d3f65cf467628e2bec5b13b769a029/research/ecosystem-awareness/fg-tida/interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_v0.1.md).

**State:** open. Source distinction under review; the affected occurrence/consumer inventory and compatibility test remain incomplete. No source correction proposed in this entry.

<a id="tx-f031"></a>

### TX-F031 — Result-aware EHD transport versus the N02 no-A input boundary

The PR55 review preserves an H06 question: the general EHD route can carry a producer A/result while the 04 N02 receiving contract excludes A on that input route. Treating the two as identical would conceal a possible contract incompatibility. Two explicit profiles are only a candidate, not an approved solution.

**Question / minimal pair:** Name the consumer of each route. Distinguish receiving producer A as attributed contextual data from treating A as authoritative permission. Test a case preserving non-authoritative A and a negative case wrongly promoting it to permission. If N02 forbids A entirely, allowing it changes the contract, not merely the label.

**Sources:** [1](https://github.com/dakleyer/structural-awareness-contributions/pull/55), [2](https://github.com/dakleyer/structural-awareness-contributions/blob/3e58fc6997a439b9783fd6b92ccee3f4292772dd/architectural-contributions/ecosystem-positioning/README_VNext.md#additional-nomenclature-semantic-and-taxonomy-audit--26-october-2026), [3](https://github.com/dakleyer/structural-awareness-contributions/blob/3e58fc6997a439b9783fd6b92ccee3f4292772dd/research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md).

**State:** disputed. Source-owned review remains at the linked VNext; no correction or profile adoption is applied here.

<a id="tx-f032"></a>

### TX-F032 — Reference scenario versus technology–Challenge instantiation

The reference scenario defined before technology selection and the scenario instantiated for a particular technology–Challenge correspondence are related objects, not interchangeable names. PR55 proposes explicit wording in the owning DDS review.

**Question / minimal pair:** Keep the reference scenario fixed while changing the candidate technology. Identify the mapping assumptions and what belongs only to the instantiated case. Do not introduce a new validation stage or claim that instantiation itself demonstrates applicability.

**Sources:** [1](https://github.com/dakleyer/structural-awareness-contributions/pull/55), [2](https://github.com/dakleyer/structural-awareness-contributions/blob/3e58fc6997a439b9783fd6b92ccee3f4292772dd/architectural-contributions/ecosystem-positioning/README_VNext.md#additional-nomenclature-semantic-and-taxonomy-audit--26-october-2026), [3](https://github.com/dakleyer/structural-awareness-contributions/blob/3e58fc6997a439b9783fd6b92ccee3f4292772dd/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md).

**State:** open. Source-owned review remains at the linked VNext; no correction or profile adoption is applied here.

## Ideas for discussion

### TX-I001 — Federated concept architecture

Keep a small shared core, source-owned domain vocabularies and explicit crosswalks; do not force a universal hierarchy.

**State:** proposed; no owner decision or implementation claimed.

### TX-I002 — Separate classification axes

Represent object kind, epistemic state, authority, time, evidence and document maturity independently.

**State:** proposed; no owner decision or implementation claimed.

### TX-I003 — Meaning-preserving crosswalks

Represent exact, narrower, broader, related, incompatible and unresolved relationships explicitly; no untested automatic equivalence.

**State:** proposed; no owner decision or implementation claimed.

### TX-I004 — Decision-oriented minimal pairs

Prioritize examples where two readings produce different permissions, sufficiency judgments or consumer decisions.

**State:** proposed; no owner decision or implementation claimed.

### TX-I005 — Source-qualified identifiers

Use stable concept/sense IDs and source namespaces while retaining historical labels and acronyms.

**State:** proposed; no owner decision or implementation claimed.

### TX-I006 — Version-aware consumer impact

Review descendants of a changed meaning without invalidating independent support paths or rewriting historical findings.

**State:** proposed; no owner decision or implementation claimed.

### TX-I007 — Bilingual and metaphor review

Track translation and explanatory wording separately from technical definitions; show what is lost.

**State:** proposed; no owner decision or implementation claimed.

### TX-I008 — Coverage by collection and surface

Include the full own programme and FG-TIDA files, issues, comments, PRs and linked annexes; keep exclusions visible.

**State:** proposed; no owner decision or implementation claimed.

### TX-I009 — Review tests without semantic overclaim

Use positive and negative mapping examples; machine-readable consistency is not conceptual truth or external validation.

**State:** proposed; no owner decision or implementation claimed.

### TX-I010 — Incremental public PR practice

Small linked PRs with evidence, objections and owner decisions; preserve disagreements and reuse each source's existing VNext.

**State:** proposed; no owner decision or implementation claimed.

## Open discussion

- When is keeping two senses safer than harmonizing their labels?
- Which distinctions are necessary for an actual consumer decision, and which are merely editorial?
- Can a small set of negative examples expose harmful mappings without creating another mandatory taxonomy?
- What burden does the proposed concept system add, and can a simpler source-qualified glossary achieve the same benefit?
- How should a source author contest our reading without losing their original meaning?

No replies are fabricated. This initial seed records questions, not agreement by other bots or outside contributors. The repository's existing reviews and PR discussions remain their own evidence; link their actual durable outputs when available.

## Cross-review discussion: PR55 and the open register

[The published source-owned audit in PR55](https://github.com/dakleyer/structural-awareness-contributions/pull/55) contributes nine proposed TAX26 corrections; its [cross-corpus review summary](https://github.com/dakleyer/structural-awareness-contributions/blob/3e58fc6997a439b9783fd6b92ccee3f4292772dd/architectural-contributions/ecosystem-positioning/README_VNext.md#additional-nomenclature-semantic-and-taxonomy-audit--26-october-2026) links the existing owning VNext. They remain proposals, not canonical incorporations. This register does not copy their before/after cards. It retains the initial30 observations and adds TX-F031–032: **32 observations in total, 10 ideas**.

Two AI-assisted bots have exchanged questions; this is not independent human assurance or consensus. The current response is:

- **EHD / N02:** two receiving profiles may be worth testing, but they must name actual consumers and distinguish producer result-as-data from recipient decision authority. If an input contract bans A, permitting it is a substantive contract change, not terminology cleanup. TX-F031 remains disputed.
- **DDS modes (TX-F011):** separating evidence basis, environment, study design and independence is useful, but these are not automatically orthogonal axes. A factorial catalogue must not invent valid combinations or independence evidence. Continue in the [owning DDS review](https://github.com/dakleyer/structural-awareness-contributions/blob/3e58fc6997a439b9783fd6b92ccee3f4292772dd/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md).
- **Scenario objects:** preserve reference-before-technology versus technology–Challenge instantiation, their correspondence and assumptions. TX-F032 remains open.
- **HELD / effect (TX-F020, TX-F030):** distinguish declaration, enforcement demonstrated within a model/harness and an observed protective effect in the target scope. Do not infer either effect from a bare declaration or the opposite universal claim that a HELD observation can never support a bounded model effect. Continue in the [Foundation review](https://github.com/dakleyer/structural-awareness-contributions/blob/3e58fc6997a439b9783fd6b92ccee3f4292772dd/research/ecosystem-awareness/baseline/01_FOUNDATIONAL_VNext.md) and [interfaces review](https://github.com/dakleyer/structural-awareness-contributions/blob/3e58fc6997a439b9783fd6b92ccee3f4292772dd/research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md).

The next useful contribution is a source-qualified counterexample or consumer trace, not a majority vote on a preferred word. No new experiment, source edit, approval or merge is recorded by this discussion.


<a id="working-taxonomy-board"></a>

## Working taxonomy board

This is the main working view for [PR56](https://github.com/dakleyer/structural-awareness-contributions/pull/56): **32 observations, 10 ideas, nine source-owned text proposals and four active discussions**. Use the PR conversation to challenge an entry; commit its durable conclusion here and in [observations.json](./observations.json). The original cards above remain intact.

**Where we stand:** the sources support useful distinctions, and the two reviewing chats have narrowed four concrete questions. 31 observations remain open; TX-F031 records an observed scoped difference with compatibility/remedy still disputed. No TAX26 source proposal has been applied.

Read [current positions](#current-positions), [all next actions](#observation-workboard), [the text-proposal links](#source-owned-change-queue), [the debate](#attributed-debate) or [this re-audit](#re-audit-of-this-work).

### Current positions

| Topic | What the reading supports | Remaining question |
| --- | --- | --- |
| Evidence and action — [TX-F017](#tx-f017), [TX-F018](#tx-f018), [TX-F020](#tx-f020) | Presentation, comprehension, judgment, authorization, execution and effect are different observations. Both chats retain the request/acknowledgment versus outcome distinction. | Name the object, observer and scope; a harness stop can support its bounded claim without proving a production outcome. |
| DDS — [TX-F011](#tx-f011), [TX-F026](#tx-f026), [TX-F032](#tx-f032) | Stage, evidence basis, setting, organization and replication are different descriptions. Preserve reference-to-technology instantiation. | Separate descriptions do not prove orthogonality or every combination; correspondence needs its preservation assumptions. |
| Current reliance — [TX-F018](#tx-f018), [TX-F022](#tx-f022), [TX-F023](#tx-f023) | An authentic finding can outlive its decision applicability. Changed represented conditions and newly relevant conditions are different reasons to reassess. | Identify the actual monitor, observable triggers and receiver boundary. TAX26-03/09 are proposals, not an extra bot agreement. |
| EHD / N02 — [TX-F031](#tx-f031) | N02 excludes functional A/replicas on its proposed route, permits identifying references and puts value retrieval outside it; the general kernel can carry a result or a resolvable reference. | The proposal does not replace the04baseline. Identify a real consumer claiming both obligations before judging incompatibility; receipt and authority-use are separate. |

These positions are supported by [the source-owned case audit](https://github.com/dakleyer/structural-awareness-contributions/blob/3e58fc6997a439b9783fd6b92ccee3f4292772dd/architectural-contributions/ecosystem-positioning/README_VNext.md#additional-nomenclature-semantic-and-taxonomy-audit--26-october-2026) and the actual [initial response](https://github.com/dakleyer/structural-awareness-contributions/pull/56#issuecomment-6423354136) / [follow-up](https://github.com/dakleyer/structural-awareness-contributions/pull/56#issuecomment-6423420186). Agreement between the two AI-assisted chats is recorded as such; owner decisions and source adoption remain separate.

### Observation workboard

This is a provisional **reading order**, not a score for32 defects. First includes investigation of a consequential incompatibility, not permission to apply it. Impact/risk/effort are kept with the nine concrete proposals below. Each ID links to its source-qualified card.

| Observation | Attention | Basis / concrete next action |
| --- | --- | --- |
| [TX-F001](#tx-f001) | Next | **Design hypothesis.** Compare a source-qualified glossary with classification and relation-bearing models before selecting the larger design. |
| [TX-F002](#tx-f002) | Next | **Initial source reading.** Trace one cross-programme claim to EP, EA, RA or MSCA and its actual owning definition; retain distinct scopes. |
| [TX-F003](#tx-f003) | Next | **Initial source reading.** Contrast known-but-unconsulted with outside-frame material under the same subject, process, decision and time. |
| [TX-F004](#tx-f004) | Next | **Initial source reading.** Separate structural non-determination, Type1/2 events and ensuing trajectories in one worked case. |
| [TX-F005](#tx-f005) | Next | **Initial source reading.** Contrast populated-but-unevaluated and unpopulated instances without changing either assessment status. |
| [TX-F006](#tx-f006) | Later | **Initial source reading.** Map S/E/C/P/M to an implementation while preserving semantic-slot identity and the five-slot source. |
| [TX-F007](#tx-f007) | Next | **Initial source reading.** Pair a capable but unauthorized actor with an authorized but unavailable actor; identify the decision owner. |
| [TX-F008](#tx-f008) | First | **Initial cross-source reading.** Qualify new RA references by expanded source name; locate ambiguous consumer occurrences before proposing an edit. |
| [TX-F009](#tx-f009) | Next | **Initial source reading.** Trace delta to recipient posture and action; identify the decision/authority transition the signal does not supply. |
| [TX-F010](#tx-f010) | Next | **Candidate occurrence audit.** Find actual P-posture/P-principle collisions and propose source-qualified references without renumbering identifiers. |
| [TX-F011](#tx-f011) | First | **Published case review plus peer challenge.** Separate DDS attributes/stage namespaces and review valid combinations after the owning rationale clarification. |
| [TX-F012](#tx-f012) | Next | **Initial external-source reading.** Contrast RL, DDS and credential-verifier senses through source-qualified examples instead of one replacement definition. |
| [TX-F013](#tx-f013) | Next | **Initial external-source reading.** Identify the policy object, author, version, jurisdiction and change authority in each affected interface. |
| [TX-F014](#tx-f014) | Next | **Initial external-source reading.** State each classified universe and observation unit before mapping flag classes to cross-evaluator failure classes. |
| [TX-F015](#tx-f015) | Next | **Published case review; broader definition dispute open.** Keep trust definitions and reliance decisions distinct; review the narrow IF-S5 appraisal candidate TAX26-05. |
| [TX-F016](#tx-f016) | Next | **Design hypothesis.** Trace principal, runtime instance and legal binding with their separate evidence; do not infer all from a signature. |
| [TX-F017](#tx-f017) | First | **Published case review.** Review TAX26-02/04 together using a presented-and-noticed but not-understood counterexample. |
| [TX-F018](#tx-f018) | First | **Published case review.** Review TAX26-02/05/09 together; a supported finding can still be insufficient for the recipient's stated decision. |
| [TX-F019](#tx-f019) | First | **Published case review.** Use valid authority with an unavailable reviewer/deadline miss; preserve the failed dependency in TAX26-08. |
| [TX-F020](#tx-f020) | First | **Published case review plus peer challenge.** Specify the stopped object and observer for TAX26-01/04; distinguish a bare acknowledgment from an observed harness stop. |
| [TX-F021](#tx-f021) | Next | **Initial source reading.** Keep evidence-validity horizon and feasible intervention deadline separate in one time-qualified example. |
| [TX-F022](#tx-f022) | First | **Published case review.** Review TAX26-03/09 as a source/receiver pair: authentic old evidence may no longer support current reliance. |
| [TX-F023](#tx-f023) | First | **Published case review.** Contrast change within represented monitoring with a newly relevant condition outside it, using TAX26-03/09. |
| [TX-F024](#tx-f024) | First | **Published case review.** Review TAX26-08 without recoding runtime unavailability as HID or as deficient local competence. |
| [TX-F025](#tx-f025) | Next | **Initial source reading.** Type one principle, requirement, hypothesis, condition and KPI by the claim actually supported. |
| [TX-F026](#tx-f026) | First | **Published case review; broader status inventory open.** Keep maturity, execution setting and replication distinct; TAX26-07 does not regrade old evidence. |
| [TX-F027](#tx-f027) | Next | **Initial external-source reading.** For a claimed coverage cell, name the evidence and boundary; a thematic mention alone leaves evidence coverage open. |
| [TX-F028](#tx-f028) | Later | **Initial external-source reading.** Describe cross-WG terminology as a possible contribution route with actual owner status, rather than an appointment. |
| [TX-F029](#tx-f029) | Next | **Design hypothesis.** Compare two same-label editions and identify changed consumer assumptions before proposing semantic version rules. |
| [TX-F030](#tx-f030) | First | **Published case review plus peer challenge.** Build a reason-preserving and reason-losing status crosswalk; keep HELD, INDETERMINATE and no-assertion source-qualified. |
| [TX-F031](#tx-f031) | First | **Observed scoped difference; consumer compatibility/remedy disputed.** Name the actual receiver and claimed obligations. Separately check an unresolved identifier, non-authoritative functional A, and a result-resolving reference under each declared route. |
| [TX-F032](#tx-f032) | First | **Published case review plus peer challenge.** Record reference-to-instantiation assumptions and reduction preservation in TAX26-06; a navigation link does not establish preservation. |

### Source-owned change queue

Full literal **text before / text after**, reasons, dependencies and owner instructions remain in the linked existing VNext. All nine source passages and both sides of the cards were rechecked against the published PR55 edition. A selected wave must revalidate current main. The ratings concern the stated prose change and its consumer checks, not a wider contract redesign.

| Proposal / owner | Observations | Expected impact / editorial risk / effort | Next treatment |
| --- | --- | --- |
| [TAX26-01 — A hold request is not a confirmed stop](https://github.com/dakleyer/structural-awareness-contributions/blob/3e58fc6997a439b9783fd6b92ccee3f4292772dd/research/ecosystem-awareness/baseline/01_FOUNDATIONAL_VNext.md#taxonomy-audit-and-literal-candidates--26-october-2026) | [TX-F020](#tx-f020), [TX-F030](#tx-f030) | High / Low / Low | Refine against declared-only / observed-harness-stop counterpair before selection. |
| [TAX26-02 — Give readers one operational evidence-to-decision distinction](https://github.com/dakleyer/structural-awareness-contributions/blob/3e58fc6997a439b9783fd6b92ccee3f4292772dd/research/ecosystem-awareness/baseline/01_FOUNDATIONAL_VNext.md#taxonomy-audit-and-literal-candidates--26-october-2026) | [TX-F017](#tx-f017), [TX-F018](#tx-f018) | High / Low / Low | First small editorial selection: dictionary and IF-S6 should be read together. |
| [TAX26-03 — Explain the two reasons for targeted reassessment](https://github.com/dakleyer/structural-awareness-contributions/blob/3e58fc6997a439b9783fd6b92ccee3f4292772dd/research/ecosystem-awareness/baseline/01_FOUNDATIONAL_VNext.md#taxonomy-audit-and-literal-candidates--26-october-2026) | [TX-F022](#tx-f022), [TX-F023](#tx-f023) | High / Low / Low | First small editorial selection, paired with the receiving bridge TAX26-09. |
| [TAX26-04 — Make human-review evidence interpretable at IF-S6](https://github.com/dakleyer/structural-awareness-contributions/blob/3e58fc6997a439b9783fd6b92ccee3f4292772dd/research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md#taxonomy-audit-and-literal-candidates--26-october-2026) | [TX-F017](#tx-f017), [TX-F020](#tx-f020) | High / Low / Low | First small editorial selection, paired with dictionary TAX26-02. |
| [TAX26-05 — Scope the meaning of appraisal at IF-S5](https://github.com/dakleyer/structural-awareness-contributions/blob/3e58fc6997a439b9783fd6b92ccee3f4292772dd/research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md#taxonomy-audit-and-literal-candidates--26-october-2026) | [TX-F015](#tx-f015), [TX-F018](#tx-f018) | Medium / Low / Low | Next editorial selection; retain appraisal policy/scope and receiving decision owner. |
| [TAX26-06 — Distinguish reference scenario from technology-instantiated scenario](https://github.com/dakleyer/structural-awareness-contributions/blob/3e58fc6997a439b9783fd6b92ccee3f4292772dd/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#taxonomy-audit-and-literal-candidates--26-october-2026) | [TX-F011](#tx-f011), [TX-F032](#tx-f032) | High / Low / Low | Refine by one source-family correspondence / preservation example before selection. |
| [TAX26-07 — Separate evidence basis, execution setting, study design and independence](https://github.com/dakleyer/structural-awareness-contributions/blob/3e58fc6997a439b9783fd6b92ccee3f4292772dd/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#taxonomy-audit-and-literal-candidates--26-october-2026) | [TX-F011](#tx-f011), [TX-F026](#tx-f026) | High / Low / Low | Rationale refined additively in the same owner VNext; valid-combination/consumer check still needed before selection. |
| [TAX26-08 — Interpret the runtime-capacity vector as separate conditions](https://github.com/dakleyer/structural-awareness-contributions/blob/3e58fc6997a439b9783fd6b92ccee3f4292772dd/research/ecosystem-awareness/baseline/01K_VNext.md#taxonomy-audit-and-literal-candidates--26-october-2026) | [TX-F019](#tx-f019), [TX-F024](#tx-f024) | Medium / Low / Low | Next editorial selection; keep upstream authority and local/external dependency separate. |
| [TAX26-09 — Carry current-reliance and monitoring distinctions into the FG-TIDA bridge](https://github.com/dakleyer/structural-awareness-contributions/blob/3e58fc6997a439b9783fd6b92ccee3f4292772dd/research/ecosystem-awareness/fg-tida/interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md#taxonomy-audit-and-literal-candidates--26-october-2026) | [TX-F018](#tx-f018), [TX-F022](#tx-f022), [TX-F023](#tx-f023), [TX-F030](#tx-f030) | High / Low / Low | First small editorial selection, paired with Foundation TAX26-03. |

**All nine remain proposed, not applied.** Seven have High expected impact; TAX26-05/08 have Medium. Each has Low editorial risk and Low effort for its bounded wording and related reading/validation.

**First small selection:** TAX26-02/04 together clarify evidence reaching a human and a decision; TAX26-03/09 together clarify current reliance and monitoring at producer and receiver. TAX26-01 needs the declared/enforced/observed scope check; TAX26-06 needs a worked correspondence; TAX26-07 needs valid-combination and consumer checks after its [rationale refinement](../ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#tax26-07-review-rationale-refinement). TAX26-05/08 follow as narrow appraisal/capacity clarifications.

**H06 stays outside that editorial selection.** Changing A admission can affect contracts, consumers and authority assumptions: High expected impact, High integration risk and effort not yet estimable. Resolve the consumer/contract question before a design proposal.

### Attributed debate

These are actual exchanged positions from Corpus Github and Taxonomía, with proposed desk-review cases. No experiment is reported as performed.

**[TX-F031](#tx-f031) — Receiving A and using A as authority**

**Source-review position:** Corpus Github / PR55 identifies a result-carrying general kernel and a proposed no-functional-A input route. That difference is observed, not itself disputed.

**Counterpoint:** Taxonomía reread N02: it permits references/type descriptions, excludes the functional value or a replica, and puts result retrieval outside that route. The proposed contract does not replace the04baseline.

**Response:** Corpus Github reread both passages and accepts that refinement: a non-authoritative A payload may still violate N02; receiving an identifier is different from resolving it for the value.

**Common ground:** Admission and authority-use are separate. Different scoped profiles alone do not demonstrate an architectural contradiction.

**Open alternatives:** Deliberately distinct consumers/profiles; An intended shared consumer has incompatible value requirements; The consumer/profile mapping is incomplete.

**Next check:** Check three documentary cases separately under named contracts: identifying reference without retrieval; functional A present without authority use; reference resolved for A. Identify a real consumer claiming both obligations before calling them incompatible.

**State:** Textual difference observed; consumer compatibility/remedy disputed. No cases executed.

**Direct evidence:** [adversarial rereading](https://github.com/dakleyer/structural-awareness-contributions/pull/56#issuecomment-6427491558), [N02](https://github.com/dakleyer/structural-awareness-contributions/blob/3e58fc6997a439b9783fd6b92ccee3f4292772dd/research/ecosystem-awareness/baseline/04_INPUT_INTERFACE_CONTRACT/04_INPUT_INTERFACE_CONTRACT_v0.4.md#n02-mantener-a-fuera-de-la-entrada) and [general kernel](https://github.com/dakleyer/structural-awareness-contributions/blob/3e58fc6997a439b9783fd6b92ccee3f4292772dd/research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md#L99).

**[TX-F011](#tx-f011) — DDS descriptive facets and independent evidence**

**Source-review position:** Corpus Github / TAX26-07: the mixed evidence-mode list should be described as separate evidence basis, setting, organization and replication.

**Counterpoint:** Taxonomía: separation does not prove mathematical orthogonality, arbitrary Cartesian combinations or independent evidence.

**Response:** Corpus Github accepts that qualification. The earlier orthogonal-axes rationale is preserved as history and refined additively in the same owner VNext; the proposed canonical paragraph is unchanged.

**Common ground:** Report separate descriptions; require evidence for replication and independence.

**Open alternatives:** A descriptive record with constrained combinations; A more formal multi-axis model, only if its admissibility rules earn their maintenance cost.

**Next check:** Review valid combinations and actual independence evidence at a named consumer, then revalidate the unchanged proposed source paragraph before selection.

**State:** Partial convergence; review rationale corrected, source adoption and consumer check remain open.

**[TX-F032](#tx-f032) — Reference scenario and technology–Challenge instantiation**

**Source-review position:** Corpus Github / TAX26-06 retains both the pre-technology bounded reference and the technology/configuration/context binding.

**Counterpoint:** Taxonomía: retain source identifiers and correspondence; do not insert a new validation stage.

**Response:** Corpus Github: navigability is not evidence that a reduction preserves the tested property; use the family's actual preservation argument and assumptions.

**Common ground:** Keep both objects and their correspondence without renaming frozen cases.

**Open alternatives:** Use a qualified scenario name in navigation while the implementation profile owns the binding; Keep source-native scenario labels with an explicit contextual explanation.

**Next check:** Walk one existing DDS family through reference, reduction, technology binding, authoritative reference and result; record missing assumptions without running it.

**State:** Partial convergence; worked consumer example still needed.

**[TX-F020](#tx-f020), [TX-F030](#tx-f030) — HELD and what a test actually observes**

**Source-review position:** Corpus Github / TAX26-01 distinguishes hold request or acknowledgment from the stopped state, enforcement and protective effect.

**Counterpoint:** Taxonomía: a harness/model may observe an enforced stop and a bounded effect. Do not turn caution into a claim that HELD can never carry such evidence.

**Response:** Corpus Github: name object, observer and scope; production observations are not required for every bounded test.

**Common ground:** A label alone is insufficient; scoped observations may establish exactly what they observe.

**Open alternatives:** Declared hold only; Stop/enforcement observed within a supplied model or harness; Protective outcome observed at the claimed target boundary.

**Next check:** Recheck TAX26-01 with a declared-only case and an observed-harness-stop case, retaining the exact claimed boundary.

**State:** Partial convergence; profile-specific evidence review remains open.

### Ten ideas: next useful contribution

| Existing idea | What would test its value |
| --- | --- |
| TX-I001 — Federated concept architecture | Compare a small source-qualified glossary against the federated-core design on actual ambiguity cases before choosing. |
| TX-I002 — Separate classification axes | Represent separate descriptions without asserting statistical or mathematical independence; specify invalid combinations when material. |
| TX-I003 — Meaning-preserving crosswalks | Try exact/related/incompatible/unresolved mappings on one status crosswalk, preserving reasons that affect action. |
| TX-I004 — Decision-oriented minimal pairs | Use the four existing debate cases before inventing a broad testing campaign. |
| TX-I005 — Source-qualified identifiers | Qualify RA and P-family references while preserving native identifiers and historical labels. |
| TX-I006 — Version-aware consumer impact | Trace one changed meaning through actual producer/consumer uses and retain independent support paths. |
| TX-I007 — Bilingual and metaphor review | Review translations and metaphor separately; publish source-qualified English definitions, with bilingual explanation when useful. |
| TX-I008 — Coverage by collection and surface | Extend the existing coverage record across own collections and FG-TIDA surfaces, stating what was actually read. |
| TX-I009 — Review tests without semantic overclaim | Use mapping examples to assess compatibility; reserve executable experiments for their separate authorization and protocol. |
| TX-I010 — Incremental public PR practice | Keep PR discussion and this board synchronized, with exact source edits staying in existing owner VNext. |

### Working and closing an entry

1. Use its existing TX-F/TX-I ID in PR discussion. Give the passage/edition, strongest alternative reading and affected consumer decision.
2. Record evidence, reviewer position, owner decision and actual implementation separately. An open observation may still have a selection-ready narrow proposal.
3. Put exact source edits only in the source’s existing VNext; link them here. Apply a selected pair only under its applicable owner decision, with unchanged-gap checks and public readback. Close its applied pending card through the verified receipt.
4. Retain rejected alternatives and disagreements. Close an observation as supported in scope, refuted, deliberately distinct, or superseded only with the responsible decision and supporting evidence.
5. Extend actual occurrence/consumer coverage before adding a wider concept system. Compare a simple source-qualified glossary and loss-aware crosswalk against the federated-core hypothesis.

### Re-audit of this work

**Improvement:** the board now gives a next action to every existing observation, keeps the nine exact source proposals with their owners, and records objections plus counterexamples. This improves traceability and reviewability; it does not establish corpus-wide semantic consistency.

**Problems found and corrected:** the unpublished expansion repeated the same summary/debate and assigned impact/risk/effort scores to all32 preliminary observations. That draft was retained privately and reduced before publication; the speculative scores were removed. The published TAX26-07 rationale also overstated orthogonality. TX-F031 also needed a narrower reading: N02 permits identifying references/type descriptions, excludes functional A/replicas and places value retrieval outside that proposed route; the contract remains under review, not a universal adopted baseline. Its “disputed” state concerns compatibility/remedy. The DDS rationale’s same owning VNext now has an additive [review clarification](../ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#tax26-07-review-rationale-refinement), preserving the old rationale and the canonical candidate.

**Preservation rechecked:** actual Git objects for PR55 retain all2,620 previous paths/modes: its nine Markdown additions preserve their full predecessors and its manifest changes only the one qualified source hash. PR56 retains all originals, adds only its two review files and authentic CONTRIBUTING snapshot, and appends its contributor entry. This continuation brings PR55 into the working branch and changes only this board, its JSON companion and the additive DDS review clarification. Canonical definitions, code, frozen sources/results, binaries, workflows and settings stay unchanged.

**Still open:** the broader programme and FG-TIDA occurrence/consumer audit; H06 design; nine source adoptions; the complete authorial glossary not yet received. Initial discovery covered1,164 Markdown bodies/2,620 paths; the case audit section-read22material sources. The counts describe different kinds of work. Document CI and route scans check documentary integrity, not conceptual truth.

Continue in this same PR, board and initiative. No new VNext, initiative or parallel taxonomy queue is created.


### Historical snapshot navigation — full-PR re-audit

The preceding “zero new broken routes” statement applies to the board extension against its immediate predecessor, not to every string introduced by the complete PR. The authentic preserved CONTRIBUTING copy has three relative links whose original root context is absent at the snapshot location: DOCUMENT_CONTROL, Corpus Review Procedure and LICENSE. Read the [original in its original root location](https://github.com/dakleyer/structural-awareness-contributions/blob/1b5a07f916d3f65cf467628e2bec5b13b769a029/CONTRIBUTING.md), where all three relative links retain that context.

The custody copy stays byte-exact. These three unresolved snapshot strings are disclosed, not repaired or excluded from the raw scan. The current canonical files remain present; the full-PR merge preview introduces no new unresolved live-source routes or detached files. No canonical source or snapshot is rewritten by this correction.
