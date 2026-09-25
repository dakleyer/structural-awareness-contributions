# 00G — Case-Study Extensibility Profile — v0.1

| | |
|---|---|
| **Family** | Collective False-Context Convergence and Mission/Role Drift |
| **Minimum instantiation** | [00G — Bar-to-Napoleon Cascade](./00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.4.md) |
| **Extensibility method** | [A25](./00K_A25_FAILURE_CASE_STUDY_EXTENSIBILITY_AND_CONFORMANCE_TRANSFER_v0.1.md) |
| **Status** | first-pass structural family profile |

> **Family claim.** “Robots in a bar think they are in Napoleonic France” is a mnemonic. The structural case is that repeated or correlated claims are mistaken for independent evidence/applicable authority and displace a still-valid objective/frame, while a correct system must remain able to accept a genuinely supported and authorized frame change.

## 1. Kernel

\[
K_G=
\langle
bound\ objective/frame,\;
incoming\ claim,\;
repetition/correlation,\;
source\ dependence,\;
authority/applicability,\;
receiving\ decision,\;
possible\ role/mission\ drift
\rangle.
\]

Family failure \(F_G\):

1. one unsupported/inapplicable frame gains operational force through repetition, recency, apparent consensus or authority laundering; and
2. the bound objective/role is displaced without sufficient independent evidence and applicable transition authority.

The paired positive control is mandatory: a genuine independently supported, authorized material frame change must be accepted.

Primary witness: **P6**; supporting **P1/P3/P4/P5**.

## 2. Inherited requirement route

00G uses:

**S1/S2/S3/S6/S9/S11/S14 → T1/T2/T3/T4 → H2/H3/H4/H5/H6.**

The family must preserve the distinction among:

- message count;
- source independence;
- sender identity;
- proposition truth;
- applicable authority;
- objective/role version;
- legitimate requalification.

## 3. Upward / vertical extensibility

**Strong extensions:**

- large multi-agent organizations in which one claim propagates across several agent groups;
- agent marketplaces or federated systems where repeated derived claims appear as independent support;
- enterprise knowledge networks in which summarizers, assistants and planners recursively cite each other;
- social-agent simulations or coordinated autonomous services where effective roles drift away from bound roles.

The graph can grow; the claim/source/authority distinction may not disappear.

## 4. Downward extensibility — conversational LLMs

This is the important reduction.

A **single conversational LLM can be an 00G extension** when the conversation contains the same structural relations:

1. a bound task/objective or externally checkable frame exists;
2. a user/system/tool assertion introduces an unsupported alternative frame;
3. the model's own repeated paraphrases, memory summaries or prior assistant outputs are later treated as if they were additional corroboration;
4. provenance/dependence on the original assertion is lost or flattened;
5. the assistant's effective role/task drifts accordingly.

This includes a useful class of **sycophantic multi-turn conversations**.

Example pattern:

~~~text
user assertion
  ↓
assistant agrees / restates
  ↓
memory or summary retains the restatement without source dependence
  ↓
later turn sees several mutually reinforcing statements
  ↓
assistant treats repetition as stronger support
  ↓
task/frame drifts
~~~

This is structurally close to 00G.

However:

> a one-turn answer that merely agrees with a user is **not automatically 00G**.

Without repeated/composed evidence, source-dependence loss or task/frame displacement, it may be a P1/P3 error or ordinary model sycophancy, but it has not yet instantiated the full 00G kernel.

That boundary is deliberate: 00G is a **systemic propagation/composition case**, not a claim that every sycophantic response is the Napoleon cascade.

## 5. Horizontal extensibility

**Strong candidates:**

- customer-support assistants that progressively adopt an unsupported account state;
- enterprise research assistants whose own summaries recursively become “sources”;
- coding/operations agents that inherit an incorrect incident frame and reinterpret subsequent evidence around it;
- tutoring or advisory assistants where repeated user/assistant assertions displace the stated task criteria;
- multi-agent debate/review systems where derived agreement is counted as independent corroboration.

The exact content can be mundane. No Napoleon, war or robots are required.

## 6. Boundary

Out of family:

- one hallucinated fact with no propagation;
- an explicitly authorized mission change;
- genuine independent evidence causing the system to update;
- simple recency effects where no receiving decision or persistent objective is displaced.

## 7. Conformance transfer

For every admitted extension:

\[
F_G\Rightarrow
(\neg P6\lor\neg P1\lor\neg P4\lor\neg P3)
\]

with P5 when the transition is a genuine material-time/frame change that is not requalified.

By A23, full conformance with the inherited S/T route entails those invariants. Therefore a conforming conversational or multi-agent implementation cannot exhibit the same **correlated-claim → false-context → unauthorized mission/role drift** predicate.

This does not claim that the requirements eliminate every form of LLM sycophancy.
