# Structural Awareness — Meta-Existence, Evaluability and Context-Restriction Calculus

**SA-MATH-METAEX-01 · Mathematical working annex v0.1 · 27 October 2026**

**Status:** candidate source-qualified mathematical synthesis; definitions, scoped propositions, existence constructions and explicit countermodels. It does **not** amend the adopted 00M A/B/C/D meanings, decide unrepresented world facts, certify universal runtime superiority, or run an agent/social simulation. All new SA-E statements below are scoped mathematical constructions, many being familiar logic/decision-theory results applied to Structural Awareness. This is **not** a theorem proving physical infinity or a new super-Turing class of machines.

**Sources and continuity:** [Part I v1.0](./A_APRIME_OPEN_SEMANTIC_TRANSFER_BETWEEN_AGENT_ECOSYSTEMS_v0.1.md); [Part II v0.3](./METASYNTACTIC_UTILITY_CLASS_THEOREMS_v0.1.md), including Shannon/R11/R12/R14/R16/Semantic Window; [SA-V1–SA-V7 two-phase note](./SA_META_VALUE_AND_CONTEXT_SYNTAX_REQUALIFICATION_TWO_PHASE_v0.1.md); original mathematical R03 and [00M canonical definitions](../ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md#abcd-canonical); [01 Foundation](../ecosystem-awareness/baseline/01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md) and [01A-A01 FH-C/FH-E](../ecosystem-awareness/baseline/01A_A01_MISSION_DRIFT_CAUSAL_PRIORITY_AND_EPISTEMIC_ECONOMY_HYPOTHESES_v0.1_RESEARCH_NOTE.md) as **recorded hypotheses**, and the [open PR #56 taxonomy workboard](https://github.com/dakleyer/structural-awareness-contributions/pull/56). The new subject is a generic Structural Awareness **mathematical question**, not an incorporation of Ecosystem Awareness requirements or a social-model claim.

## Abstract

A non-delivered result, a still unexplored yet **assessable reserve**, a plausible exploration route, an effect beyond a process's present evaluation capabilities, a mathematically undecidable statement and an unrepresented external entity are **different types of conditions**. Calling all of them "indeterminate" erases the most interesting possible utility of metasyntax: **one may prove or refute a useful property about a population of not-yet-individuated candidates**, or prove the irrelevance of a range, before determining all those candidates.

We separate four axes—**representation**, **evaluability**, **logical/modal truth status**, and **access/verification cost**—and derive a two-sided calculus. A proof of **target-specific existence** may justify an exploration that was not worthwhile under an uninformative prior; a proof of **target-specific absence/impossibility** may safely suppress or shrink a search without enumerating all candidates. Strengthening a constraint shrinks its admissible solution region and, relative to a fixed model universe, enlarges its mathematical exterior; relaxing it does the reverse. None of these set relations yields an effective inventory of the exterior. The value and cost consequences are proved only under declared task, access, search/reachability, evidence and resource assumptions. A multi-source extension can combine independently valid constraints but cannot manufacture source truth or independent confirmation.

This note refines the previously stated two-phase architecture: **Phase I, meta-characterize whether a property exists/is possible/is excluded and whether it is relevant to the new target; Phase II, use that characterization to contract, expand or redesign the syntactic observation/search context when a sound effective construction exists.** The generic open-domain tag A′ is the **space of non-exhausted semantic obligations**, not a bucket in which every constituent is intrinsically undecidable.

## 1. Terminology and the source-owned A/B/C/D boundary

Keep the following **typed** objects separate.

| Kind | Notation | Interpretation |
| --- | --- | --- |
| Open model domain | \(\Omega\) | Mathematically declared semantics; need not be enumerable, nor the set of literally everything in reality |
| Program's admitted representation | \(U_{P,c,t}\) | Typed syntactic frame admitted by process P in context c at time t; its interpretation may be partial |
| Functional result | \(A_{P,c,t}\) | What P **actually establishes and delivers** under that question and profile (consistent with canonical 00M **A**) |
| Open representational residual | \(A'_{P,c,t}\) | **Meta-level obligation concerning scope and facts not exhausted by the present delivery/representation**; not a computable set difference |
| Admissible semantic candidate set | \(S_\Gamma\) | **Mathematical interpretation** of constraints Γ on a fixed \(\Omega\); need not be computably enumerable |
| Exterior of a constraint set | \(R_\Gamma=\Omega\setminus S_\Gamma\) | **Extensional mathematical complement** for reasoning about constraint inclusion, not a list available to P and **not identical by definition to A′** |
| Target property | \(P_c(x)\) | Independently specified, context-scoped question about x; avoid confusing this predicate with the program P |
| Qualification profile | \(\kappa=(c,q,t,\rho,\text{source},\text{rights})\) | Question, time, resources, provenance and authority determining valid interpretation |

**Key correction.** "Undetermined relative to the actual A delivery" does **not** mean "undeterminable in principle". [00M §1](../ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md#abcd-canonical) already reserves distinct process-relative meanings: B is a **characterized and assessable exploitation reserve** including the basis/limits of A; C a **grounded but not characterized exploration frontier**; D a **potentially material effect beyond the process's presently effective evaluation route**. B need not have been exploited; its further evaluation may still cost resources. C is **not** literally a class of 50%-decidable objects; D is **not** equivalent to mathematical absolute uncomputability. Nor are B/C/D exhaustive, mutually exclusive bags of A′ objects. They are **qualified roles/aspects relative to the source process** and need not partition the semantic exterior.

**Proposed generic term:** *open representational residual* for A′; reserve *indeterminate relative to (P,q,κ)* for a question not yet established under those conditions; *mathematically undecidable* only when a proof for the defined formal task exists. Avoid rewriting all legacy source uses of "residual non-fungible indeterminacy" by string replacement: historical expressions can continue to denote a **non-substitutable limit of effective determination**, with a versioned crosswalk of scopes. This is a **review proposal** for the [PR #56 taxonomy workboard](https://github.com/dakleyer/structural-awareness-contributions/pull/56), not a new adopted glossary.

## 2. Four independently qualified axes

**Axis R — status of representation.** Already delivered by P; typed and admitted but unevaluated; outside U / not encoded; the source's representational frame itself not exhaustively characterized. These statuses do not establish the truth of any hidden proposition.

**Axis E — status of effective evaluability.** Assessable by a characterized method within the declared capability/budget; grounded avenue for exploration whose evaluation basis remains uncharacterized; no presently effective evaluation route; formally proved uncomputable **only if such a theorem applies**. An item may be **not delivered** but **assessable**, which explains B's role in 00M.

**Axis L — logical/modal status of a target-specific existence proposition.** Let \(E_{c,w}\) abbreviate

\[
E_{c,w}:\quad \exists x\in\Omega_w\ P_c(w,x).
\tag{1}
\]

For one specified world/model w, **EXISTS** means a valid argument establishes \(E_{c,w}\); **ABSENT-IN-w** means a valid argument establishes \(\neg E_{c,w}\). For a specified admissible model class \(\mathcal W_c\), **POSSIBLE** means \(\exists w\in\mathcal W_c:E_{c,w}\), whereas **IMPOSSIBLE-IN-CLASS** means \(\forall w\in\mathcal W_c:\neg E_{c,w}\). **UNRESOLVED** means neither relevant proof has been qualified. **POSSIBLE** does not imply present-world existence; **ABSENT-IN-w** does not imply impossibility in *other* admissible contexts. Within one fixed world, "does not exist" and "is impossible in this fixed world" may denote the same extensional fact; treating them as globally distinct categories without a modal/context scope is a logical error.

**Axis C — epistemic/operational cost.** Provenance of a certificate; time and cost to obtain, discover, validate, transmit or exploit it; reachability and allowed action. **A short proof message is not evidence of cheap discovery**. No probability or Shannon entropy may be inferred from the labels EXISTS, POSSIBLE, IMPOSSIBLE or UNRESOLVED without a separate distribution model.

The four axes are **not assumed statistically independent**, nor does every Cartesian combination make sense. Their purpose is to prevent a semantic relation or cost from being silently inferred from a different facet. Inconsistent proof sources require an attributed **INCONSISTENT-SOURCE** report rather than unqualified adoption of both \(\varphi\) and \(\neg\varphi\).

## 3. SA-E1 — constraint reversal under a fixed semantic universe

Fix \(\Omega\) and two well-typed constraint conjunctions \(\Gamma_1,\Gamma_2\) such that

\[
\forall x\in\Omega:\quad \Gamma_2(x)\Rightarrow\Gamma_1(x).
\tag{2}
\]

Then

\[
\boxed{
S_{\Gamma_2}\subseteq S_{\Gamma_1},
\qquad
R_{\Gamma_1}\subseteq R_{\Gamma_2}.
}
\tag{3}
\]

**Proof.** Any x satisfying \(\Gamma_2\) satisfies \(\Gamma_1\), giving the first inclusion. Taking complements **relative to the same \(\Omega\)** reverses inclusion. \(\square\)

Thus **adding constraints** generally shrinks the admissible set S and grows its mathematical exterior; **removing constraints** relaxes S and shrinks that exterior. This gives a precise version of the suggested "A and A′ move in opposite directions" *when A is expressly defined as an admissible region S within one fixed \(\Omega\)*. It does **not** prove that canonical 00M A (a delivered functional result) changes by the same inclusion: results may have different datatypes, and changing the task or ambient interpretation invalidates the simple complement argument.

Crucially, \(R_\Gamma\) is a legitimate **mathematical set** even when **no effective algorithm can enumerate or decide its members**. Nor does (3) mean the process gained access to the members newly admitted by relaxed constraints. The **open A′** can carry the appropriately qualified proposition about (3) without being identified with all of \(R_\Gamma\).

**Different-kind residual caveat:** a residual that records "this question remains open after the procedure" need not be antitone with the set of candidate states; loosening constraints could generate **new unresolved questions** even as the extensional exterior \(R_\Gamma\) shrinks. We do not transfer the set monotonicity to all notions of epistemic uncertainty.

## 4. Two candidate source-hypothesis routes: targeted existence and certified exclusion

We distinguish two *candidate mathematical mechanisms*, using temporary labels **SA-H∃** and **SA-H¬** so that they cannot be confused with the established **FH-C/FH-E** foundational hypotheses or any H1–H6.

**SA-H∃ — existence-guided exploration.** A correct, **task-specific** assertion \(\exists x\,P_c(x)\), even when it does not identify x, can improve whether it is worth exploring or which target type to investigate. **General frame openness** \(\exists x\notin U\) does not justify a stronger assertion \(\exists x\,P_c(x)\) without a separate theorem/source premise. A proved existence also does not guarantee a physical search method can reach x.

**SA-H¬ — exclusion-guided context reduction.** A correct, **task-specific** statement \(\forall x\in S\setminus T:\neg P_c(x)\) can justify removing all that region from a search for \(P_c\). A stronger \(\forall x\in S:\neg P_c(x)\) can correctly terminate the search **within S** without checking every member, provided a short valid proof exists. A claim of **global nonexistence** requires the proof's range to be all relevant \(\Omega\), not just a finite frame that happened to be inspected.

These are *hypothesis families of practical applicability* with conditional mathematical propositions below, **not a redefinition of B/C/D**. Both can hold for the same open domain and question under changed admissibility profiles; neither is guaranteed for every task.

## 5. SA-E2 — existence knowledge can strictly change the rational choice to explore

Fix a target property P, a specified context and a **declared Bayesian action problem**. Let the unobserved fact \(E\in\{0,1\}\) mean \(\exists x\,P(x)\). Before receiving a sound target-specific certificate, the agent has probability \(p=\Pr(E=1)\in(0,1)\). Suppose that, conditional on \(E=1\), its specified finite exploration policy discovers a usable witness with probability \(\alpha\in(0,1]\); with \(E=0\), no witness is discoverable. A successful discovery has benefit V>0 and choosing SEARCH costs C>0. Choosing NO-SEARCH has utility 0. Assume those benefits/costs apply under the same authority and resource profile.

Without the certificate:

\[
\mathbb E[U(\mathrm{SEARCH})]=p\alpha V-C.
\tag{4}
\]

With a **valid actual-world certificate** proving \(E=1\), under the same reachability model:

\[
\mathbb E[U(\mathrm{SEARCH})\mid E=1]=\alpha V-C.
\tag{5}
\]

**Theorem SA-E2 (strict existence-guided decision gain).** If

\[
\boxed{p\alpha V<C<\alpha V,}
\tag{6}
\]

then the optimal unqualified choice is NO-SEARCH whereas after receiving the legitimate existence certificate the optimal choice is SEARCH, yielding strictly positive conditional value \(\alpha V-C\) relative to refusing the search for that certified case. The certificate may be nonconstructive and does **not** identify the location or method of reaching x.

**Proof.** The inequalities make (4) strictly negative and (5) strictly positive; compare both with the zero utility of NO-SEARCH. \(\square\)

This establishes that **knowing a property of a not-yet-individuated population can justify resource allocation even before identification**. The decisive premise is **target-specific existence** plus a qualified search-success model, not "the open universe contains something". If the evidence costs \(C_M\), the net conditional benefit is \(\alpha V-C-C_M\) if that cost is charged for this receiving case. Without an effective search policy, or if \(\alpha=0\), the result says nothing about actually locating x.

No theorem requires that search always occurs: if \(C\ge\alpha V\), a known existing target can still be uneconomical to search for. There is also no universal claim that uncertainty without a certificate must rationally prohibit exploration; a different p or C can justify searching anyway. This is a **nonempty strict-value parameter class** rather than a universal prescription.

## 6. SA-E3 — a qualified negative certificate can shrink a search without identifying the excluded individuals

Let S be the admissible candidate region in a **fixed declared question** and \(T\subseteq S\) a restricted region. Suppose a legitimate metatheorem/verified source establishes

\[
\forall x\in S\setminus T:\quad \neg P_c(x).
\tag{7}
\]

**Theorem SA-E3 (safe existential pruning).**

\[
\boxed{
\exists x\in S\,P_c(x)
\quad\Longleftrightarrow\quad
\exists x\in T\,P_c(x).
}
\tag{8}
\]

**Proof.** If a witness lies in S, the certified negative claim excludes its membership in \(S\setminus T\), hence it lies in T. The reverse implication follows from \(T\subseteq S\). \(\square\)

The proof is a **meta-property of the candidate set and question**, not identification of every excluded object. It does not justify shrinking the scope for **other questions** Q whose truth may depend on excluded elements. It does not justify changing **global \(\Omega\)** conclusions if the excluded region outside S has not been assessed.

**Finite work corollary, scoped.** For a finite candidate enumeration of size \(|S|=N\), and \(|T|=n\), the specified exhaustive black-box check of P on S uses N predicate calls in a worst-case negative instance. If a valid certificate of (7) can be **verified** with additional cost v in the same comparison units, then testing only T costs at most v+n predicate-call units. It is cheaper **than that exact all-S exhaustive strategy** whenever

\[
\boxed{v+n<N,}
\tag{9}
\]

for unit-cost tests and a correct certificate. This is **not** a universal asymptotic advantage over *any* algorithm with access to the full formula: such an algorithm may verify the same theorem and reach the same conclusion. It is likewise not a guarantee that generating the proof costs v; its discovery and upkeep may dominate the saving.

**Complete exclusion corollary.** If a justified theorem proves \(\forall x\in S:\neg P_c(x)\), a global P-search **within S** can end legitimately without enumerating S. If only a possible but unproved absence is claimed, pruning is unsound. If the intended question is about all of \(\Omega\), the certificate must also cover \(\Omega\setminus S\).

## 7. SA-E4 — formal work asymmetry exists, but discovery and verification are different

The preceding corollary is an exact **relative work comparison**. There is also a broad *proof-size versus black-box search* separation for negative assertions.

**Theorem SA-E4 (black-box negative certification lower bound).** Let \(P:[N]\to\{0,1\}\) be an arbitrary black-box Boolean predicate. Any deterministic procedure that always correctly certifies \(P(x)=0\) **for every \(x\in[N]\)** in the all-zero case must make at least N point queries in the worst case.

**Proof.** If the procedure terminates after fewer than N negative answers, choose an unqueried index y. The all-zero predicate and the predicate equal to 1 **only at y** produce identical answers to every executed query; hence the procedure would erroneously certify the latter as all-zero. \(\square\)

If an independently available, source-qualified **mathematical proof** establishes the same universal negative statement for a structured predicate family and can be checked in cost \(v(N)\ll N\), the proof-bearing route can be asymptotically cheaper **than the black-box enumeration interface**. For example, the typed formula

\[
P_N(x):=\bigl(x\in[N]\ \land\ x\text{ odd}\ \land\ x\text{ even}\bigr)
\]

has a constant-size contradiction argument independent of N; including the representation of N in binary yields at most \(O(\log N)\) description overhead, while the unrestricted black-box family above has an \(\Omega(N)\) lower bound on universal negative checking. **This comparison uses different available structure:** the proof route is given **the predicate formula and a valid checker**, while the black-box route sees only membership answers. If the ordinary comparator also has the formula and checker, it can obtain the identical advantage. The paper therefore establishes an **existence of an information/verification interface asymmetry**, not a new non-Turing complexity lower bound for all syntactic code.

**Amortized qualified reuse (R12).** If a valid global certificate costs s once to obtain, v to requalify per user, and h to integrate across k recipients, versus c for each complete fresh check, the total certificate route wins only if

\[
\boxed{k(c-v)>s+h.}
\tag{10}
\]

This **includes certificate production** and is compatible with the earlier [Part II SA-U5](./METASYNTACTIC_UTILITY_CLASS_THEOREMS_v0.1.md#8-primitiva-entrópica-r12-metasyntactic-utility-without-new-shannon-information). More generally, certificate generation may be uncomputable, unavailable, wrong, out of scope, expired or costly. Saying "for an open/infinite domain a universal negative proof would be asymptotically cheaper" is **not** a theorem without a family of valid, accessible proofs and a comparison resource model.

**Positive/negative logical asymmetry (R11).** For a c.e. language, a **positive existence witness** may have finite decidable checking, while total negative membership may be unavailable by computation. A **negative metaproof** can sometimes exist through a stronger mathematical theory or structural contradiction, but not for all inputs of a halting-complete language through a uniform effective meta-rule. This is exactly why we distinguish possible, absent, impossible, and unresolved statuses.

## 8. SA-E5 — sound multi-source qualification without inventing a shared A′

Let \(\mathcal W\) be a declared admissible **possible-world/model class** for the same question. Qualified sources i may provide sound constraints \(C_i\subseteq\mathcal W\) compatible with the actual world w*. If each source's scope/semantic interpretation is valid and \(w^*\in C_i\), then

\[
w^*\in \bigcap_i C_i
\qquad\text{and}\qquad
\bigcap_i C_i\subseteq C_j .
\tag{11}
\]

**Proposition SA-E5 (sound source conjunction).** The joint constraints preserve the true world and may reduce the compatible alternatives; they do **not** automatically reveal a new individual constituent, nor create additional statistically independent information when sources copy the same upstream proof.

**Proof.** Elementary conjunction and set inclusion. \(\square\)

The possible decision gain from such qualification follows the existing **Blackwell/robust refinement** mathematics in Part II when it changes a target-relevant compatible-state set; source eligibility and receiver rights must be preserved. An asserted common A′ across several agents is **not** automatically a shared population inventory: the agents' questions, times, capability and denotation maps may differ. A typed correspondence to a common question is an additional premise. This gives a **candidate rationale** for multi-source confluence, not a demonstrated multi-agent advantage.

## 9. SA-E6 — context change permits both contraction and expansion, never free relevance

Let the context c change the question \(P_c\), valid source roles, permissible actions, observation functions and risk. A previously optimal admitted set \(S_{\Gamma,c_0}\) can become insufficient for \(c_1\). SA-E1 tells us how constraints move an **admissible region under fixed \(\Omega\)**; SA-E3 tells us how a **target-specific negative certificate** can safely reduce an existential search; SA-E2 tells us how **target-specific positive existence** can justify an expansion/exploration previously not worthwhile.

These results should be read alongside [SA-V1–SA-V7](./SA_META_VALUE_AND_CONTEXT_SYNTAX_REQUALIFICATION_TWO_PHASE_v0.1.md), not as a competing theory:

\[
\underbrace{\text{change of target, relevance or constraints}}_{\text{context}}
\;\Longrightarrow\;
\underbrace{\text{qualified existence/exclusion and scope diagnosis}}_{\text{metasyntactic Phase I}}
\;\Longrightarrow\;
\underbrace{\text{admissible contraction, expansion or recompiled syntax}}_{\text{Phase II if constructible}}.
\tag{12}
\]

A correct **shrinking** of context is not always better: it may discard variance-reducing observations or other valuable properties for a different question. The original *Semantic Window* theorem supplies an explicit **bias–variance threshold** for the current-regime mean; more history can help when correctly scoped and qualified. Likewise [Shannon conditional task information](./METASYNTACTIC_UTILITY_CLASS_THEOREMS_v0.1.md#5-theorem-sa-u2-strong-decision-relevant-information-gain-in-the-shannon-sense) applies only under a declared joint law. [R14 coverage and support-aware KL](./METASYNTACTIC_UTILITY_CLASS_THEOREMS_v0.1.md#6-distorsión-entrópica-coverage-kl-direction-and-decision-relevance) show that the *size* of a represented region cannot tell us by itself how relevant it is. The [R16 computational-description gap](./METASYNTACTIC_UTILITY_CLASS_THEOREMS_v0.1.md#7-computational-exergy-coding-potential-and-semantic-value-are-different-quantities) is also distinct from the **cost of discovering an applicable proof**.

**No-context-change negative control:** if the receiving question remains exactly and effectively sufficient in the current scope, all useful qualifications are already known, and no future action needs wider reach, additional metareasoning may have zero task value while consuming extra resources. This is consistent with every theorem above. Even when context changes, **positive utility requires a target-specific property and a legitimate source or proof**; generic open-universe existence alone is not sufficient.

## 10. Taxonomy crosswalk and relationship to prior hypotheses

The [PR #56 taxonomy review](https://github.com/dakleyer/structural-awareness-contributions/pull/56) already contains:

- **TX-F003:** A/B/C/D do not form mutually exclusive bins.
- **TX-F005:** representation state and assessment state differ.
- **TX-F023:** changed conditions and changed relevance boundaries differ.
- **TX-F030:** flattened UNKNOWN-like statuses can erase distinct reasons.

This note proposes **one additional cross-cutting distinction for review**: *existence/modal status of the residual is not identical to its assessability or intrinsic computability*. It does not imply an accepted 00M renaming or source update. The source's adopted A/B/C/D semantics remain in [00M v0.8](../ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md#abcd-canonical); no historic theorem numbers or canonical definitions are erased.

The [01 Foundation §1.0](../ecosystem-awareness/baseline/01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md) and [FH-C/FH-E](../ecosystem-awareness/baseline/01A_A01_MISSION_DRIFT_CAUSAL_PRIORITY_AND_EPISTEMIC_ECONOMY_HYPOTHESES_v0.1_RESEARCH_NOTE.md) already assert as **application-specific hypotheses** (i) epistemic limitation awareness may be causally more protective than extra domain data, and (ii) qualified scope information may cost less computationally than broad new data for the same mission-reliance question. SA-H∃ and SA-H¬ are **generic mathematical mechanism hypotheses**, not newly adopted FH or H1–H6 and not a measured revalidation of FH-C/FH-E. This theory may later help state their physical applicability conditions, but **that later study is not a premise of the current math**.

## 11. Theorems, countermodels and honest limitations

| Claim | Exact mathematical result | Essential limitation |
| --- | --- | --- |
| **SA-E1** | Constraint strengthening reverses inclusion of an extensional complement under **fixed \(\Omega\)** | Not automatically monotone for delivered A or open epistemic A′; no effective complement enumerator |
| **SA-E2** | Positive, target-specific existence changes an optimal explore/no-explore decision for \(p\alpha V<C<\alpha V\) | Requires a valid actual-world certificate, a reachable search policy, a utility model and source-cost accounting |
| **SA-E3** | A certified negative outside T proves search over S has same existential answer as search over T | Scope/task specific; certificate validity and costs not free; no unrelated target conclusions |
| **SA-E4** | \(\Omega(N)\) black-box absence-check lower bound; structured proof checking **can** be asymptotically cheaper under different source access | No lower bound against an equally informed theorem prover; source proof discovery cost may dominate |
| **SA-E5** | Intersecting sound source constraints can shrink compatible alternatives without identifying their constituents | Not independent evidence by message count; no shared A′ without typed semantic alignment |
| **SA-E6** | Two-phase changing-context calculus can **expand or contract** search after justified meta-relevance findings | The transition to effective new syntax requires legitimate admissible Q and effective h, as in SA-V6 |

**Not established:** automatic net superiority over any equally informed competitor, actual-world gold/peer/existence from generic ND, intrinsic mathematical indecidability of all of A′, a complete B/C/D partition, numeric entropy for uncounted open residuals, uniformly cheap proof generation or global asymptotically sublinear meta-reasoning. Mathematical utility is **task-relative, evidence-relative and budget-relative**, with **separate source/verification/discovery effort**.

## 12. Conclusion

The correct taxonomic statement is not "all of A′ is indeterminate" in the sense of intrinsically uncomputable or irrelevant. It is:

> **A′ represents the non-exhausted semantic reach of a specified process. Within that reach, certain predicates, relations, existence assertions, exclusions and evaluation routes may already be characterized—even though the relevant individuals or all substantive answers have not been produced by A.**

From this formulation the two candidate uses become mathematically precise:

\[
\boxed{
\begin{aligned}
&\text{a proved, target-specific existence condition}
&&\Rightarrow\text{possible strict exploration decision value (SA-E2)},\\
&\text{a proved, target-specific negative restriction}
&&\Rightarrow\text{sound contextual pruning (SA-E3)},\\
&\text{a qualified, cheaper certificate}
&&\Rightarrow\text{potential lower work under its declared cost model (SA-E4/R12)}.
\end{aligned}
}
\tag{13}
\]

These conditions can justify **widening or narrowing a syntactic context** when the relevant question changes. They need not establish every element of the residual, and no oracle has been added. The underlying physical agents may eventually test the hypotheses, but this annex remains at the level of **mathematical construction and explicit limits**.
