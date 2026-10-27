# Mathematical Utility Classes of Metasyntactic Information

**Part II — From representation to decision value in open and changing ecosystems**  
**Structural Awareness Programme · SA-MATH-UTILITY-01 · Research note v0.1 · 27 October 2026**

**Scientific status:** mathematical class-level construction with conditional theorems, general proof obligations and executable finite checks; **not** empirical validation, an adopted agentic protocol, or proof of universal efficiency. Intellectual lineage: Iván Abril Palma's original mathematical programme; source-specific R-reviews; [the open, unmerged PR #60](https://github.com/dakleyer/structural-awareness-contributions/pull/60). Research integration prepared with AI assistance at the owner's request.

**Dependency:** [Part I — Metasyntactic Architecture for Open Ecosystems](../A_APRIME_OPEN_SEMANTIC_TRANSFER_BETWEEN_AGENT_ECOSYSTEMS_v0.1.md), consolidated v1.0. The first part proves typed expressive extension and limited integrity/resilience results, but not universal operational superiority. **This paper starts only where the representational theorem ends.**

## Abstract

The ability to formulate an open-domain semantic question is distinct from the ability to improve a decision. A constant metasyntactic tag stating that the universe is open may be essential to interpret the scope of a report, yet may add **no discriminating information** about which possible world is actual. This paper identifies a broader, nontrivial family of decision and verification problems in which a **qualified meta-observation, proof certificate, partial relation, validity-window statement or additional authorized observation** changes the receiver's informational partition or compatible-world set. It proves exact criteria for (1) detecting representation insufficiency without solving the hidden question; (2) restoring decision sufficiency with selected, eligible additional distinctions; (3) strictly decreasing attainable decision loss for some tasks; (4) improving robust decisions using qualified restrictions on possible states **without identifying the actual state**; and (5) accounting for information, verification and design costs.

The mathematical class is **not** defined by A/B/C/D, a social or economic model, a particular agent brand, or a hard-coded list of modules. Its members are independently specified questions, observations, admissible sources, context transformations, actions and losses. It includes changed-operation interfaces, finite proof/metaproof certificates, version-sensitive transfer, anonymous relational information, selective acquisition and qualified resource-limited decisions. Positive examples and mandatory strong-baseline counterexamples are specified separately. Only a **task-relative, source-qualified and priced** claim can establish strict practical utility.

## 1. Scope: one abstract class, several independent scientific mechanisms

Take a nonempty state class \(W\), which may be very large or open and need not be globally enumerable. An agent or other process has:

\[
o:W\longrightarrow O,\qquad
r:W\longrightarrow R,
\tag{1}
\]

where o is the **available object-level observation** and r the independently declared **receiving question**. The object-level observation could be an execution receipt, a syntactic proof result, a measurement, a source statement or a partial interface. A **metasyntactic source record** is denoted

\[
m:W\longrightarrow M,
\tag{2}
\]

where m may describe *qualified scope, provenance, validity, interpretability, an abstract relation, a certified constraint or a demonstrable limitation of the observation*. Its value must be **actually obtainable through a specified source and admissibility contract**; merely postulating an informative m would be a disguised oracle.

Other elements include an admissible action set \(\mathcal A\), loss \(\ell:\mathcal A\times R\to[0,\infty)\) (or a declared partial order of acceptable outcomes), time/resource budget \(\rho\), source rights/authority \(\alpha\), and a current question/context profile \(\kappa\).

**The meta-information utility class \(\mathcal C_{\rm MU}\)** consists of all tuples

\[
\mathcal C_{\rm MU}=
\{(W,o,r,\mathcal M,\alpha,\rho,\mathcal A,\ell):
\text{a qualified metalevel question or source can be evaluated}\},
\tag{3}
\]

with the following *research gates*: a meaningful task r exists independently of proposed signals; the admissibility/interpretation of every m is specified; a source-only baseline does not quietly receive the same m; and an independent referee can evaluate model truth on its finite tests. Merely satisfying (3) **does not guarantee positive gain**. Instead, theorems below characterize **positive subfamilies** of \(\mathcal C_{\rm MU}\).

A metalevel process can legitimately report "o cannot support r" **without learning the true r(w)**. This *certificate utility* is distinct from a *world-discriminating* m that helps determine the actual r. Keeping these two types separate is central.

## 2. The general mathematical frontier: task-relative sufficiency

**Theorem MU-1 (fiber sufficiency and metacertifiable insufficiency).** A deterministic r-answer exists as a function \(h:O\to R\) of observation o alone **if and only if** every observation fiber is r-homogeneous:

\[
\boxed{
o(w)=o(w')
\Longrightarrow r(w)=r(w').
}
\tag{4}
\]

If two admissible worlds w,w′ with equal o but different r can be exhibited and their r-values are independently justified **for the declared model**, a metaprocess can construct a finite **insufficiency certificate** carrying that pair. It need not identify the actual world.

**Proof.** If \(r=h\circ o\), equal o-values force equal r-values. Conversely, homogeneous fibers permit \(h(y)=r(w)\) for any representative w in the nonempty fiber \(o^{-1}(y)\); this is well-defined. For the negative case, a verified pair with equal o but different r immediately contradicts factorization, so a finite checker can validate a certificate on a **finite decidable test model**. This does not produce the actual hidden answer. \(\square\)

**Historical provenance.** The factorization condition is ordinary mathematics, present in the author's *Given Universe* §4 and [00M v0.8 §4](../../ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md), and as F1 in [PR #60's mathematical core](https://github.com/dakleyer/structural-awareness-contributions/blob/research/mathematical-lineage-agentic-reduction-20261026/research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/mathematical-lineage-social-agentic-v0.1/02_FORMAL_CORE_AND_PROOFS.md). The certificate *construction* is metalevel; its logical content is a standard consequence, not a newly discovered Gödel theorem.

**A broad problem class already appears:** a representation sufficient for an old r can become insufficient for a **new question, allowed transition, receiving party or validity condition**. The old output need not have become false. Its qualification is now inadequate for the new use.

## 3. The positive class: meta-evidence that separates the still-relevant ambiguity

Suppose a qualified m is available and relevant to the same task. The enriched observation is \(y=(o,m)\). Define the **unresolved, task-conflicting observation pairs**

\[
U_{r\mid o}
=
\bigl\{\{w,w'\}:
o(w)=o(w'),\
r(w)\ne r(w')
\bigr\}.
\tag{5}
\]

This definition has meaning whether W is finite or infinite; a **finite test** uses a declared \(\widehat W\subseteq W\) without pretending to enumerate the whole open universe.

**Theorem MU-2 (necessary and sufficient meta-refinement).** The enriched observation \(y=(o,m)\) is sufficient to compute r on the declared model **if and only if**

\[
\forall\{w,w'\}\in U_{r\mid o}:
\quad m(w)\ne m(w').
\tag{6}
\]

**Proof.** If one conflicting o-pair remains equal under m, both observations y are equal but r differs, so factorization fails. If every conflicting o-pair is separated, then equality of y implies equality of r, so the fiber theorem MU-1 yields an exact decoder. \(\square\)

**This is not a universal acquisition algorithm.** MU-2 identifies what a *known qualified signal* would need to distinguish. A source may have no rights, no instrumentation, no adequate proof, or no feasible cost to supply that signal. Theorem MU-2 makes no assertion of availability or truth from mere syntax.

**Corollary MU-2a (source-qualified minimum additional distinctions).** On a finite declared model \(\widehat W\), given separately qualified supplementary candidates \(Q_j\) and additive costs \(c_j\), a set \(H\) suffices for target r in combination with **already available o** if and only if each pair in \(U_{r\mid o}\) is separated by some \(Q_j\) with \(j\in H\). The min-cost feasible H is exactly a weighted **set-cover** instance on the conflicting pairs, when the stated additive/independence and eligibility hypotheses hold:

\[
\min_{H\subseteq J_{\rm eligible}}\sum_{j\in H}c_j
\quad\text{subject to}\quad
U_{r\mid o}=
\bigcup_{j\in H}\{\{w,w'\}\in U_{r\mid o}:Q_j(w)\ne Q_j(w')\}.
\tag{7}
\]

**Proof.** Directly apply (6) to the vector \(m_H=(Q_j)_{j\in H}\). \(\square\)

This draws on the [R03 review §14.2](https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R03_PRIMALIDAD_Y_LOGICA_v0.1.md), which proves the bounded pair-separation version **as a reviewer development**, not a theorem of the original historical bunch operator. The [PR #59 re-audit](https://github.com/dakleyer/structural-awareness-contributions/pull/59) correctly warns that the **PR #60 D3 Q-alone problem** cannot be used as an *incremental* selection algorithm without first subtracting what **o already distinguishes**. Equation (7) incorporates that correction explicitly.

## 4. Strict utility for an entire class, not one preferred product

**Theorem MU-3 (two-world strict gain for a discriminating qualified signal).** Suppose two admissible worlds \(w_0,w_1\) have the same o, different binary r, and a qualified obtainable m distinguishes them. Give those two worlds probability \(1/2\) each, and choose a binary receiving decision with 0–1 misclassification loss. Then

\[
\boxed{
R^*_o=\frac12,\qquad
R^*_{(o,m)}=0.
}
\tag{8}
\]

**Proof.** An o-only decision must produce the same label in both worlds and errs on one equiprobable world. Using m, the two worlds are distinguished and their known independently defined correct r-labels can be assigned, giving zero errors. \(\square\)

**Scope of the class-level statement:** it holds for **every** admitted pair of worlds with these three properties, rather than merely for a robot or for A/B/C/D. A large/open real ecosystem can contain many such pairs without the agent exhaustively locating them. It is a mathematical **existence of a utility-positive class**, not a prevalence, population-frequency or net-profit theorem for all real systems.

The extra m must be **source-qualified and feasible**; setting \(m=r\) by fiat without an independent measurement/inference basis would hide an oracle inside the assumptions. Natural sources include a verified current version, a signed change of scope, an authenticated proof-status/countermodel, a source-owner release bit, or an interpretable relation already known by a qualified source but lost in the baseline's message.

**Negative control MU-N1.** If \(m=g\circ o\) on W—or it is just a **constant OPEN** flag already entailed by common model assumptions—then the enriched signal has the **same fibers** as o. It cannot yield the strict improvement (8) for an otherwise fixed task with the same prior, actions and costs.

**Negative control MU-N2.** If an existing conventional controller already has a recoverable copy of m and the same task/action/evidence contract, it can tie. The theorem establishes an **information requirement**, not a brand monopoly or intrinsically superior processor.

## 5. Utility without identifying the actual state: robust qualified constraints

A more general and operationally important phenomenon is that *m need not identify a world or a hidden individual*. It may **rule out some states** in the current receiver decision without making the remaining alternatives distinguishable.

Let

\[
C_o=\{w\in W:o(w)=o\},\qquad
C_{o,m}=\{w\in W:o(w)=o,\ m(w)=m\}\subseteq C_o.
\tag{9}
\]

For a common action set \(\mathcal A\) and loss \(\ell(a,w)\), define the *worst-case attainable loss*

\[
V(C)=\inf_{a\in\mathcal A}\sup_{w\in C}\ell(a,w).
\tag{10}
\]

**Theorem MU-4 (qualified partial information weakly improves robust attainable loss).** For any nonempty \(C_{o,m}\subseteq C_o\),

\[
\boxed{V(C_{o,m})\le V(C_o).}
\tag{11}
\]

**Proof.** For each action a, a supremum of loss over the smaller set cannot exceed the supremum over the larger. Taking the infimum over the *same admissible actions* preserves the inequality. \(\square\)

This theorem is a **logical decision-information statement**, not an algorithm for discovering the actual w, not a claim that an arbitrary false certificate may safely restrict \(C_o\), and not a theorem that an implementation automatically minimizes V. **Qualified source evidence** must justify the exclusion of every removed possibility under the declared model.

**Strict witness that does not identify the hidden state.** Let \(W=\{w_0,w_1,w_2\}\), with the same object observation o in all three. Let actions be EXECUTE and HOLD; losses are

| State | EXECUTE loss | HOLD loss |
| --- | ---: | ---: |
| \(w_0\) | 0 | 2 |
| \(w_1\) | 0 | 2 |
| \(w_2\) | 10 | 2 |

Without additional evidence, \(C_o=W\), hence \(V(C_o)=2\) (HOLD beats the worst-case EXECUTE loss 10). A correctly verified **anonymous exclusion certificate** may rule out \(w_2\), leaving \(C_{o,m}=\{w_0,w_1\}\). Then \(V(C_{o,m})=0\), because EXECUTE is safe for *both* remaining states. Thus

\[
\boxed{V(C_o)-V(C_{o,m})=2>0}
\tag{12}
\]

although the receiving process **still cannot identify whether the actual state is \(w_0\) or \(w_1\)**.

This is a general proof pattern: **a source-qualified, task-relevant partial constraint can change an optimal action even when full identification remains impossible**. It is applicable to any domain satisfying the risk/action/certificate premises. A false or expired certificate can reverse the conclusion; this must be checked separately.

**Novelty boundary:** (11) is a standard monotonicity property of minimax decision making. The research contribution sought here is the **qualified meta-to-receiver architecture** that carries the constraint, its scope and its limits, not a new theorem of minimax theory.

## 6. A general class of changing semantic windows

A receiving task may use a past observation only while its **interpretation and source evidence remain valid for the target context**. In a changing system, the distinction is not merely a fixed number of seconds.

Let \(c=(\text{task},\text{scope},\text{version},\text{authority},t)\) be a declared receiving context. Let \(o_c\) be the currently received raw observation and \(v_c\) an **independently verifiable source qualification**, e.g. a version-bound validity certificate. A semantic window is a subset of contexts

\[
\mathcal W(e,r)=
\{c:\text{source evidence e legitimately supports target r in c}\}.
\tag{13}
\]

The window is **defined relative to evidence e, question r and contextual validity**; it is not an assumption of time-invariant semantic equivalence. The historical [Semantic Window and Good Enough Early Warning](../../ecosystem-awareness/baseline/ARTICLE_03_SEMANTIC_WINDOW_AND_GOOD_ENOUGH_EARLY_WARNING.md) and [Regime Awareness programme](../../regime-awareness/PROGRAMME_CONTEXT.md) develop **independent, more application-oriented semantic-window and early-warning research hypotheses**. They are antecedents to this mathematical question, not proven by (13).

**Theorem MU-5 (context-dependent sufficiency).** Suppose two contexts \(c_0,c_1\) yield the same raw observation o but different legitimate receiver outputs \(r(c_0)\ne r(c_1)\) due to scope, source version, interpretation or authority changes. Then **no raw-o-only decoder** is sufficient across both contexts (MU-1). If a legitimate meta qualification \(v\) distinguishes them, \(r\) may become a function of \((o,v)\); if it does, the paired representation is sufficient **for that declared context class**.

**Proof.** The first part is MU-1's equal-observation/different-target counterexample. The positive part is MU-2's fiber condition applied to v; it is conditional because some changes require additional measurements beyond a context label. \(\square\)

**Negative controls.** If r is invariant across the changed version/scope, no new useful distinction follows. A stale validity flag from an unauthenticated replica does not qualify as v. A version-bound receipt does not itself grant a source-owner permission. An implementation may already monitor these conditions with conventional timestamp/version/policy constructs and tie the metasyntactic alternative.

This mathematical family is broad: any producer/receiver context shift, policy version change, task operation expansion, semantic drift or time-of-check/time-of-use mismatch can instantiate its hypotheses **when** the change is material to an independently stated decision.

## 7. General anonymous relationships: useful structure without names

R03's independently developed [§14.4 quotient-without-a-named-class example](https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R03_PRIMALIDAD_Y_LOGICA_v0.1.md) gives a useful abstraction principle. One can represent a relationship/equivalence class without selecting a privileged individual representative or naming every member.

Let a group \(G\) act on a state space W with quotient \(\pi:W\to W/G\). For a target r:

**Theorem MU-6 (anonymous relational sufficiency).** There exists \(\bar r\) such that \(r=\bar r\circ\pi\) **if and only if** \(r(gw)=r(w)\) for every \(g\in G,w\in W\).

**Proof.** Factorization implies the function is constant on orbits. Conversely, G-invariance makes the map \(\bar r([w])=r(w)\) well-defined. \(\square\)

**Interpretation.** A process can make a **quotient-invariant** decision from relational structure **without naming an individual in an otherwise symmetric class**, when the relation itself is source-qualified and the receiving target is invariant. It does **not** follow that every anonymous relational description is sufficient, that a non-invariant task has an answer, or that the observer may identify a representative without an additional marker.

The [R04 §14.3–14.5 perspective review](https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R04_ALGEBRA_POSICIONAMIENTOS_v0.1.md) proves the same orbit-invariance criterion and a **typed partial transfer** relation with an independent authorization/domain condition. These results support a **class of anonymous, relational and source-sensitive receiving questions**, not the ontological claim that a particular unobserved agent exists.

## 8. Resource price, copying and design selection

A receiver supplied with additional m can always ignore it **in the mathematical free-information model**. But acquiring, verifying, computing, transmitting and selecting the appropriate supplementary evidence has cost.

Let \(R_o^*\) and \(R_{o,m}^*\) be the optimal task-specific expected losses, or use V for the robust analogue. In common declared units, define

\[
\boxed{
\Delta_{\rm net}
=
R_o^*-R_{o,m}^*
-
C_{\rm acquire}
-
C_{\rm verify}
-
C_{\rm transmit}
-
C_{\rm compute}
-
C_{\rm design}.
}
\tag{14}
\]

**Theorem MU-7 (strict net value under an explicit resource envelope).** A metasyntactic route has strict **positive net task value** relative to the declared baseline **if and only if** its gross task improvement exceeds the **additional** qualified costs of that route under the agreed accounting convention. If the sum is zero it ties; if it is negative, the extra processing is not justified on that metric.

**Proof.** Rearrangement of (14) by the specified definition of net loss; no empirical cost magnitude is implied. \(\square\)

This is an **accounting criterion**, not a general algorithmic or economic theorem. R12's [proof-sharing cost review, as mapped in PR #60](https://github.com/dakleyer/structural-awareness-contributions/blob/research/mathematical-lineage-agentic-reduction-20261026/research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/mathematical-lineage-social-agentic-v0.1/01_ORIGINAL_SOURCE_LINEAGE.md) offers a related *conditional arithmetic* for reusable verification. It is not a demonstrated physical energy saving or proof of universal communication compression.

**Selection/designer versus copied execution.** A conventional universal programme can compile a successful metasyntactic controller and reproduce **the same eventual execution**. That does not answer how its particular design was selected, sourced, verified or adapted after the receiving question changed. Any differential comparison must either provide the **same completed design to both parties** (then a tie may be inevitable) or include **legitimate design discovery and adaptation cost on both sides**. A conventional system that successfully performs the same meta-selection is **functionally a metasyntactic solver for this task**, regardless of coding notation.

**Strong incumbent comparison.** Do not compare with an incompetent controller that throws away already available o, omits source validity, or lacks safe abstention. The correct competitor may use modern abstract interpretation, symbolic model checking, policy engines, proof certificates, versioning or active information acquisition. If it represents equivalent m under the same rights and budget, it may equal or beat the present implementation. **The mathematical utility class does not belong exclusively to one software brand or architecture diagram.**

## 9. A unified problem-family theorem, and its limits

Define a **positive metasyntactic-utility problem** to be any tuple from (3) satisfying at least one of the following independently checkable routes:

- **Route A — certification of inadequacy:** a finite proof/model witness exhibits an o-fiber in which r varies, giving an accurate **meta-certificate of insufficiency**; the downstream use of that certificate must be judged separately.
- **Route B — qualified discrimination:** a legitimately available m distinguishes r-conflicting o-fiber states so that the receiver can perform an otherwise unavailable correct task-specific decision (MU-2/MU-3).
- **Route C — anonymous constraint refinement:** a valid source constraint shrinks the receiving compatible-world set in a decision-relevant way, possibly improving robust action **without identifying the true state** (MU-4).
- **Route D — changing context:** a task, operation, version, meaning or source permission changes such that old o no longer suffices, but qualified context/evidence can restore a needed distinction (MU-5).
- **Route E — relational invariant:** the target depends only on a qualified invariant/quotient, not on individual named members (MU-6).

These are **structural conditions on classes of problems**, not a list of product use cases or A/B/C/D statuses. They can overlap, but each requires its own explicit observation, target and qualification proof.

**Theorem MU-8 (nonempty broad positive class).** Routes B and C each contain a nonempty family of problems with **strict gross decision improvement** for some declared task, prior or robust loss, **without requiring global identification** of the open ecosystem.

**Proof.** MU-3 supplies, for *any qualified separating two-world instance*, a strict \(1/2\to0\) expected-loss improvement. MU-4's three-world example supplies a strict \(2\to0\) minimax improvement while \(w_0,w_1\) remain indistinguishable under the meta-certificate. Adding arbitrary irrelevant states/objects outside the receiving decision's qualified domain, without altering the established task and source-validity premises, embeds these examples into arbitrarily large model ecosystems. Therefore the class is not defined by a particular finite toy system or by a specific label vocabulary. \(\square\)

**Important size qualification:** embedding a finite witness in a large domain does **not** show that the witnessing decision remains correct after **new relevant admissible states** are introduced. If new states change the task or invalidate source premises, the old decision must be requalified. The claim is structural nonemptiness for arbitrarily large **appropriately scoped** models, not universal benefit in every open world.

**Theorem MU-9 (no-free-information converse).** If every eligible metasyntactic message is already recoverable from the source o together with the same public task/model knowledge, and the receiver's permitted actions and inference capabilities are identical, no strict extra Bayes/minimax decision power is obtained **solely by re-encoding that information**. If re-encoding costs extra, its net benefit on the frozen task can be negative.

**Proof.** The enriched and original signals induce identical information fibers/compatible state sets. Both decision spaces can simulate each other's policies, giving identical optimum task loss with no extra cost. Add positive overhead and net loss increases. \(\square\)

This is why **Part I's structural/open-boundary claim** must be distinguished from **Part II's demonstrated class of decision-positive qualified meta-information**. The mere correctness of an OPEN message does not make every meta-operation worth executing.

## 10. Experimental and independent-review programme

A valid research campaign must be independently specified **before** testing a candidate meta-programme. It should be capable of both confirming and falsifying the proposed differential.

| Family | Frozen problem and proof target | Critical negative control |
| --- | --- | --- |
| Changed operation / task | Same initial observation, new allowed transformation; check fiber congruence and required probes | Old observation still sufficient; extra query irrelevant |
| Source→receiver qualification | Independently typed transfer, version, purpose, source rights and target | Strong qualified policy/ABAC incumbent ties |
| Meta proof and contradiction | Object-level evidence versus host-level proof/under-determination certificate | Invalid/stale proofs or host adopts object contradiction |
| Context/semantic window | Evidence changes validity under version, clock or regime; target frozen | Window change does not change r; cache/authority unverified |
| Anonymous relational target | Equivalence invariant under declared group/permutation, no canonical member identity | Non-invariant target needs a distinguished member |
| Active information acquisition | Choose cheapest eligible sources to separate unresolved r-pairs **after including o** | Q-alone set cover falsely declares insufficiency or overspends |
| Robust partial constraints | Anonymous qualified m excludes decision-relevant possibilities | False certificate removes actual world; wrong safe action |
| Cost/design accounting | Matched full evidence and rights, including search, verification, design and rollback | Copied identical design ties; meta overhead loses |

The companion [finite executable research harness](../fixtures/METASYNTACTIC_UTILITY_CLASSES_v0.1.mjs) checks deterministic factorization over an exhaustive family of small Boolean observation maps, pair separation with prior o, strict task-value examples, anonymous robust constraints, changing validity, invariant quotient examples and negative baselines. It is **bounded symbolic evidence**, not a real multi-agent deployment or a proof of historical article originalities.

The still-open [PR #60 study](https://github.com/dakleyer/structural-awareness-contributions/pull/60) and its [PR #59 correction](https://github.com/dakleyer/structural-awareness-contributions/pull/59) are specifically relevant prior internal work. We reuse F1 and D1–D7 only in their mathematics; we do **not** copy the ACC/social reduction, its agent product configuration, or a mandatory B/C/D role partition.

## 11. Conclusion and separate evidential burden

Part I establishes that an effective programme can communicate correct typed claims about limitations and an open semantic frontier in a language which a strictly closed representation does not possess. That is a **representational and integrity** contribution.

Part II establishes a stronger **mathematical applicability result**, still conditional: there is a structurally defined, broad class of decision problems in which qualified meta-information **either reveals that the original observation is insufficient, restores missing task-relevant distinctions, restricts compatible worlds without identifying them, or preserves validity across context changes**. Within nonempty subfamilies, strict **gross** decision improvements follow from general fiber/refinement and robust minimax theorems—not from a particular implementation or privileged model name.

Positive **net** utility after compute, communication, verification, authority and design costs is not implied. Neither is superiority over a capable implementation that already solves the same meta-question. Those outcomes require an independently frozen receiver task and a fair experiment. This is the appropriate mathematical starting point for the next applied study, rather than declaring that all metasyntactic architectures must outperform all syntactic architectures in every open ecosystem.

## Sources, derivation and priority

**Original author's ideas:** *Given Universe*, *Primalidad y Lógica* (syntactic distinction and positioning), *Formalización del Meta Sistema* (meta-level and object-level separation), *Practical Incompleteness* (uniform determination frontier), *Projection Mechanism* (source/recipient representation), *Projected Infinite Paradox* (local/global question change). The original historical manuscript's ontological or prime-number completeness claims are **not imported as established theorems**.

**Later source-specific mathematical reviews:** [R03](https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R03_PRIMALIDAD_Y_LOGICA_v0.1.md) for finite labels and decision pair-cover; [R04](https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R04_ALGEBRA_POSICIONAMIENTOS_v0.1.md) for partial interpretation and invariant quotient; [R05](https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R05_FORMALIZACION_META_SISTEMA_v0.1.md) for bounded meta-certificates; [R07](https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R07_PRACTICAL_INCOMPLETENESS_v0.1.md) for uniform rather than fixed-program undecidability.

**Still-unmerged bridge:** [PR #60 mathematical lineage](https://github.com/dakleyer/structural-awareness-contributions/pull/60); [PR #59 re-audit](https://github.com/dakleyer/structural-awareness-contributions/pull/59) for its supplementary-Q caution. Source terms **S (standard), R (reviewer reconstruction), D (conditional derived result), H (experimental hypothesis)** should be maintained when promoting any downstream claim. The present MU theorems are principally **standard mathematical theorems specialized to a qualified metasyntactic decision problem**; their integration and applied utility are a research proposal.

**Open proof/applicability obligations:** independent source-by-source proof review; formal check of every claimed metadata source; correctness of changing-context/rights interpretation; measured implementation costs; matched strong baselines; systematic failure tests when the meta-certificate is wrong or unavailable; and the genuine prevalence of MU-positive cases in observed open ecosystems.
