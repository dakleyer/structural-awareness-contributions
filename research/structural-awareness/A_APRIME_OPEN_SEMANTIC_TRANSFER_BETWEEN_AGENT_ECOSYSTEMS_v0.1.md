# Metasyntactic Architecture for Open Ecosystems

**Part I — Open meaning, non-oracular representation, resilience, and transfer**  
**Structural Awareness Programme · SA-MATH-TR-01 · Consolidated mathematical article v1.0 · 27 October 2026**

**Disposition:** working mathematical research for independent review; not an adopted runtime or engineering standard, not a claimed physical-world universal and not an amendment to the canonical A/B/C/D definitions. Authorship/intellectual lineage: Iván Abril Palma and the historical mathematical research programme; editorial and mathematical reconstruction prepared with AI assistance at the research owner's request.

**Version integrity:** this stable document path retains its historical v0.1 filename for existing inbound links. The complete previous **v0.8 working derivations (TR-1–TR-22, 39 section-6 subsections)** are preserved [unabridged in a non-active historical research snapshot](./archive/2026-10-27_A_APRIME_FULL_WORKING_DERIVATIONS_v0.8.md); only relative link paths were rebased after moving the source one directory deeper. The original pre-consolidation text is also recoverable [at its historical Git revision](https://github.com/dakleyer/structural-awareness-contributions/blob/b4fe76bfad902f4662871ece97a15ba47de40e23/research/structural-awareness/A_APRIME_OPEN_SEMANTIC_TRANSFER_BETWEEN_AGENT_ECOSYSTEMS_v0.1.md). The owner's locally supplied [uncommitted v0.9 addendum](#appendix-a--universal-openness-and-typed-no-explosion-revision) has been reconciled in this article rather than represented as a previously merged commit. **This v1.0 is the active, consolidated reader edition.** Its independent Part II on utility is linked in §11.

## Abstract

An agent can execute a finite programme successfully while lacking grounds to declare that its outputs exhaust the semantic question for which it was designed. A closed-domain interface treats the finite admitted frame as its entire language of meaningful claims; an open-aware interface can additionally communicate an **unclosed frontier** relative to its procedure, target and observation scope, without naming or deciding its missing members. This distinction is not a new halting oracle and is not equivalent to adding unknown cases to a list.

We formalize the architecture as **object-level effective computation plus executable metasyntactic reporting**. We prove: a uniform semantic separator cannot exist under a specified Turing-expressive peer family; inside-domain expressions cannot express a property changing only outside their interpreted domain; an additional finite meta-constructor can produce typed outside-domain questions without deciding them; transfer of a supposedly complete output may be semantically invalid; correctly typed meta-certificates can diagnose inconsistencies and limitations of an object calculus without inheriting its contradictory assertions; and an open report preserves qualified observed information with **weak information dominance** relative to an interface which erases its extra fields. The strict improvement established against the expressly closed comparator is **expressivity of true open-boundary claims**, not a universal gain in execution speed or Bayes risk.

The universal openness principle is explicitly **quantified over admissible finite frames**, not over a privileged subclass such as robots or communicating peers. Its instantiation permits the report that a finite frame has an exterior **within the declared open model**; it does not entail that a peer exists, that it is detectable or that sensors are defective. A precise class-level mathematical study of **when these operators become useful for a receiving task**, independently of A/B/C/D and any social-model reduction, is developed separately in Part II.

## 1. Problem, contribution and theorem boundaries

Our question is not whether any ordinary computer can print a word such as UNKNOWN. It can. The question is whether an **interpreted, typed and executable reporting programme** can preserve a semantic relation **not expressible in a narrower closed-domain programme** while the actual task execution remains computable and finite.

Two architectures are compared **by their external claim languages**, not by vendor, label, historical implementation style or physical computational power. The chosen closed comparator is **deliberately narrow as a mathematical architecture class**: its externally interpreted variables/quantifiers range only over a frame admitted by an initial closure procedure. An actual conventional implementation that already communicates equivalent outside-domain semantics is **not** in this strictly closed class. It can be information-isomorphic to the open architecture.

The results are four different kinds of statement:

| Mathematical level | Precise claim | What is not implied |
| --- | --- | --- |
| **Computability boundary** | No total computable, correct, binary semantic decider exists over the H-EXP expressive family. | Every individual fixed programme is undecidable; every bad packet is undecidable. |
| **Representational expressivity** | A typed metalanguage can express qualified outside-domain claims that the strictly closed object language cannot express. | An external object is identified or physically detected. |
| **Resilience / integrity** | Correctly qualified meta-reports can preserve unknowns, non-closure and object-level contradictions without promoting false object conclusions. | Every software error, contradiction or unsafe action is automatically prevented. |
| **Practical decision value** | An enriched observation permits at least the decisions possible with a recoverable poorer observation; strict value needs a task-dependent separating fact. | Strict improvement for every task, or positive benefit after communication/design costs. |

These must remain distinct throughout the article. We use the author's original [*Primalidad y Lógica*](https://docs.google.com/document/d/19oVzuvEbNBq0-Mj59_3QwIeuft-lkdfd8GEyewZgIHU/edit), [*Formalización del Meta Sistema*](https://docs.google.com/document/d/1cKahUwPzTnMLJSZ6dO1syFl7PocXpSH2LC158tUYsCk/edit), [*Practical Incompleteness*](https://docs.google.com/document/d/1yaJk27YQfr_lNNjcHCwROD2hWwt2Y0uuLTDkrrBvwdI/edit), [*The Projection Mechanism*](https://drive.google.com/file/d/1OrJ2LWz2qBv2sP8_-VNldWpctxZdwcfI/view), and [*Projected Infinite Paradox*](https://drive.google.com/file/d/1Q5RkZeWGCHDdTLem131iEk8I2Aavof1t/view) as **intellectual antecedents**. Claims repaired, proved or specialized in later R-reviews are expressly labelled as those later developments; the original historical papers are not silently rewritten as modern theorems.

## 2. Types and notation: avoid the three different As

Let \(\Omega\) be a **modelled, open semantic domain**. It is not assumed to be an effectively enumerable database or the set-theoretic collection of absolutely everything. Let \(W\) denote admissible possible worlds/context states when observation sufficiency is under analysis.

A finite run \(r\) of an entire effective programme \(\mathcal P\) has history \(h_r\). Define:

| Symbol | Type and exact meaning |
| --- | --- |
| \(\mathcal P\) | The entire **effective programme**: initializer, operation, verification and reporting handoff. |
| \(A_{\rm proc}\) | Earlier development's local shorthand for the **procedure plus its intended semantic question**; here we normally say \((\mathcal P,q)\). |
| \(U_r\) | Finite **syntactically admitted frame** of the initializer on run r, with a partial denotation \(\operatorname{den}_r:U_r\rightharpoonup\Omega\). |
| \(A_{\rm scope}\) | The admitted working scope constructed by a closure-stage K in the two-machine comparator; typically represented by \(U_r\), but not equated with all of \(\Omega\). |
| \(A_1\) | A particular in-scope result of the downstream operator D, **when D is a selecting operation**, so \(A_1\subseteq A_{\rm scope}\). |
| \(A_r\) | Finite **qualified output and observed results of the entire composed run**. It may include recorded substantive unknowns and diagnostic events. |
| \(A'_r\) | A **semantic open-frontier qualification** of \((\mathcal P,q)\) relative to \(h_r\); neither a computable list of unknown individuals nor literally \(U_r\setminus A_r\). |
| \(q\) | Independently stated question (meaning of "nearest", "permitted", "valid", etc.), possibly not decidable for all admissible states. |
| \(\rho,\sigma,\kappa\) | Resource profile; scope/time interpretation; and evidence, permissions and authority qualification respectively. |

**Taxonomic separation.** In the adopted [00M v0.8](../ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md#abcd-canonical), **A** means the *functional result actually delivered by a process*. That canonical A is not the procedural \(A_{\rm proc}\), the admitted frame \(A_{\rm scope}\), or the carrier label A/A′ of the present local mathematics. This notation is provisional to this article. We do **not** redefine canonical B/C/D, nor require a particular B/C/D categorization in the architectural results.

**Semantic status taxonomy.** A finite execution may report a **qualified positive**, a **qualified negative**, an **observed semantic UNKNOWN**, a **TIMEOUT**, a **BAD_FRAME**, an authorization refusal, a scope incompatibility or a partial result. TIMEOUT and BAD_FRAME are *diagnostics*, not proofs about eventual semantic truth. An **unobserved external alternative** is a distinct concept, not an UNKNOWN record magically already contained inside \(A_r\). An **uncertified census** is not an observed missing agent. Conflating these produces false closure.

A central nonidentity is:

\[
\boxed{
A'_r \ne U_r\setminus A_r
\quad\text{and}\quad
\operatorname{QualifiedRunResult}(r)\ne
\operatorname{GlobalMeaning}(\mathcal P,q).
}
\tag{1}
\]

The pair \((A_r,A'_r)\) denotes **finite justified results plus an open semantic obligation**, not a partition into two sets whose every member has been classified.

## 3. Foundation I: computability, effective non-closure and repeated runs

Use [SA-MATH-OW-01](./OPEN_WORLD_AGENTIC_INTERACTION_INDETERMINACY_L1_EXTENSION_v0.1.md) as the exact mathematical dependency. Its H-EXP hypothesis effectively produces for each Turing index e an admissible peer \(P_e\), successful on the same handshake, whose later fixed substantive receipt occurs **if and only if** the diagonal machine \(U_e(e)\) halts. Thus the semantic set of receipt-positive encounters has the halting-set degree.

**F1 — uniform semantic nondecision.** No *total computable binary* classifier can be both sound and complete for all \(T(P_e,q)\) under H-EXP. A sound **total three-valued** evaluator must return a substantive UNKNOWN on some peer index. A sound *partial binary* evaluator may diverge; a forced-total binary evaluator must err somewhere. These are logically different failure modes. Adding a finite/adaptively effective chain of "validators" composes to another effective programme and cannot defeat this uniform theorem.

This is **not** the claim that a given agent's own YES/NO-output domain must be undecidable. For a **total** three-output wrapper, its own YES-or-NO locus is decidable simply by running it. The semantic halting-hard set being pursued is different from that program's self-reported decision-domain set.

A stronger question, "from the code of a peer, is its entire response language decidable?", needs the separate **H-REQ multi-request expressivity hypothesis** of OW-5b/R07, not merely H-EXP.

**F2 — open-prefix non-closure.** If two admissible worlds produce identical finite discovery histories, but one contains a further relevant unseen member, no **function of that history alone** can correctly certify the claim "all relevant peers have been found" in both. This is an observation-indistinguishability lemma, not a proof that every physical city is infinite or every sensor broken.

**F3 — repeated execution.** For a sound total three-valued evaluator over the H-EXP family and an **effective exhaustive traversal of all indices**, there exists a finite encounter index at which UNKNOWN occurs. There is **no fixed universal bound N** shared by every evaluator and schedule, and a real-world exploration that samples only easy peers may never meet the witness.

Together, F1–F3 justify a **type for non-closure** and tests against false "ALL"/"NEAREST"/"no further peers" claims. They do **not** give any real agent knowledge of the identity of all unresolved elements, nor evidence that an unseen individual must be another agent.

## 4. Foundation II: universal openness versus task-specific exterior

The author's historical ND/*boundary* programme is naturally formulated at the **model level** as a principle over all finite representational frames, **not** as the object-level assertion "another compatible agent exists".

Let \(\operatorname{FinAdm}(\Omega)\) be the admitted family of **finite** representational frames, each denoting finitely many constituents of a stipulated \(\Omega\). The **H-ND-UNIVERSAL** principle is

\[
\boxed{
\forall F\in\operatorname{FinAdm}(\Omega)\
\exists x\in\Omega:
x\notin\operatorname{im}(\operatorname{den}_F).
}
\tag{2}
\]

The leading quantifier is **universal in the choice of finite frame**; each instance concludes that something is beyond that frame. No particular kind of x has been assumed. The admitted-frame family must therefore be typed in the scientific model; writing one finite expression for an infinite domain is **not** by itself a member with finite denotation.

**Theorem 4.1 — genuine model-theoretic openness.** If \(\Omega\) has infinitely many distinct constituents and every admissible F denotes only finitely many, (2) follows by elementary cardinality. Alternatively, (2) may be an explicit axiom of an open model. **Finite code length alone is not sufficient:** the short formula \(x=x\) or a finite recognizer could denote all of an infinite \(\Omega\). Our theorem concerns finite **denotation/coverage** frames, not every finite sentence or programme encoding an infinite set. It is not a theorem of classical logic for every physically finite environment; a completely represented finite domain is a counterexample.

**Proof.** For any F, the finite denotation image cannot exhaust an infinite \(\Omega\). Choose any constituent outside the image. No uniform effective choice procedure is inferred. \(\square\)

Notice the essential distinctions:
- **H-ND-UNIVERSAL:** each finite frame has something beyond it in the *declared* \(\Omega\), with **no claim that it is a peer, accessible, or communicable**.
- **H-OPEN:** the observed history is compatible with another possible world containing an unseen **task-relevant** item. This is epistemic *possibility*, not actual physical existence.
- **H-OUT(q):** an independent source/axiom guarantees an **actual q-relevant** outside-U constituent for the interpreted problem.
- **H-REACH(q):** the actual exploration method will eventually encounter arbitrarily many q-relevant constituents; stronger than mere population unboundedness.
- **H-DETECT(q,t):** with verified conditions, the initializer has an obligation to detect a specified q-relevant kind of thing by a specific deadline.

Neither H-ND-UNIVERSAL nor OW-1 implies H-OUT(agents), H-REACH(agents), or H-DETECT. In particular, **semantic undecidability of a question about an encoded peer** does not imply a physical agent lies outside U.

**Theorem 4.2 — no unjustified specialization.** H-ND-UNIVERSAL and finite U imply \(\exists x\in\Omega: x\notin\operatorname{im}(\operatorname{den}_U)\). They do not imply an unobserved agent, new communication channel or defective sensor.

**Proof.** Take \(\Omega=\mathbb N\) and finite U. Interpret the predicates Agent, Communicable and Observable as empty. (2) holds but no external member satisfies those predicates. A second model can make some member an agent without changing U. Thus the premise alone does not decide the agent-specific question. \(\square\)

This is the corrected interpretation of the historical **ND** intuition and the essential content of the supplied local v0.9 textual correction, incorporated here as a first-class theorem rather than as an unmerged file claim.

## 5. Two programmes: closed syntax and an actual metasyntactic extension

Fix the **same object-level effective kernel** \(\mathcal P=V\circ D\circ K\), or any appropriately composed finite/adaptive effective sequence, and the same run trace \(h_r\).

The strictly **closure-first comparator** first uses K to create an admitted scope U/A, then D/V operates inside it. It may **correctly recognize and transmit all its observed in-U uncertainties**. Its external claim language \(L_U\) nevertheless restricts meaningful operands and quantifiers **to the U-reduct**. The source's initial closure is treated as the limit of that language, so it lacks a symbol for the semantically relevant **outside** of U.

The **open-metasyntactic programme** runs exactly the same kernel but applies an additional finite report constructor **Reflect** with a strictly richer typed language \(L_+\):

~~~text
ObjectReport ::= Result(witness) | ObservedStatus(status,evidence)
               | InsideOperation(term,term)

MetaReport   ::= Embed(ObjectReport)
               | UniversalFrameOpenness(model_ref,frame_ref,provenance)
               | OpenFrontier(program_ref,question_ref,scope)
               | OutsideQuestion(predicate_ref,scope,UNDETERMINED)
               | QualifiedExterior(axiom_ref,frame_ref,conclusion)
               | ObjectInconsistency(theory_id,proof_1,proof_2)
               | EvidenceScopeChange(source_ref,version,validity)
~~~

These are **actual finite typed data constructors**, not metaphorical annotations. A programme that prints them and verifies their applicable premises has a distinct output contract and executes additional instructions. An ordinary Turing-complete implementation can compile both kernel and reflector, so the **computational power remains the same**. The additional expressive ability is **relative to the narrower claim language**, not super-Turing computation.

**Theorem 5.1 — relative nondefinability (TR-15/TR-20).** Suppose two full models have identical U-reducts and identical recorded in-U execution, but disagree on some well-defined outside-U property \(\chi\). No term or sentence constructed solely from the typed operators and U-relativized quantifiers of \(L_U\) can distinguish these worlds. The enlarged \(L_+\) can *formulate* the outside question.

**Proof.** All atomic interpreted \(L_U\) statements agree; all permitted compositions and U-bound quantifications preserve agreement by induction on syntax. But the outside-domain formula \(\exists x[\operatorname{Outside}_U(x)\land\chi(x)]\) differs between worlds. It therefore cannot be represented by any \(L_U\) sentence on that class. An \(L_+\) constructor can encode the formula, with status UNDETERMINED if its truth is unavailable. \(\square\)

This also proves why merely computing **the complement inside U**, \(U\setminus A_r\), gives no genuine extension: that complement remains unchanged in both models, while an outside-U property can change.

**Theorem 5.2 — executable metasyntax (TR-16).** For finite, well-typed descriptions of the kernel, target, scope and observed history, a programme can **construct** an encoded UniversalFrameOpenness/OpenFrontier/OutsideQuestion AST and serialize it in finite time.

**Proof.** It copies finite references, constructs a bounded number of typed nodes and sends them through an effective serializer. It does not compute the truth of a universal open-world proposition or inspect all unknown entities. \(\square\)

**Theorem 5.3 — no universal semantic novelty labeler (TR-17).** There is no total computable procedure that always decides whether every total computable function \(F_e\) is extensionally identical to the zero function Z, where

\[
F_e(n)=\mathbf1\{U_e(e)\text{ halts within }n\text{ steps}\},
\qquad Z(n)=0.
\tag{3}
\]

**Proof.** \((\forall n:F_e(n)=Z(n))\iff U_e(e)\uparrow\). Such an equivalence checker would decide the diagonal halting problem. \(\square\)

A machine can always create new **syntactic** labels or a catch-all UNKNOWN. It cannot thereby decide whether a new observed pattern constitutes a genuinely new **semantic behaviour category**. Hence A′ must not be represented as an indefinitely growing list of perfectly classified UNKNOWN, UNKNOWN-OF-UNKNOWN, etc.

## 6. Resilience: contradictions, meta-certificates and a failed initializer

### 6.1. Russell and Gödel: the error belongs to the theory being analysed

In a classical object calculus that admits naive unrestricted comprehension, positing \(R=\{x:x\notin x\}\) produces \(R\in R\iff R\notin R\). **Explosion** in that calculus is a consequence relation: if \(T\vdash p\) and \(T\vdash\neg p\), then \(T\vdash\varphi\) for every \(\varphi\) of the *same object language*. It does not make a coffee cup, paper sheet or different inference calculus explode. Importantly, a larger unbounded **universal quantifier alone** does not insulate the host metatheory; **typed proof quotation and inference-rule separation** do.

**Theorem 6.1 — typed non-propagation of an object-theory contradiction (TR-18/TR-25).** Let Check_T be a sound decidable checker of **finite proof objects** for the explicitly identified object calculus T. If it verifies a proof of \(p\) and a proof of \(\neg p\) from T, a host can emit one attributed metalevel certificate INCONSISTENT_OBJECT_THEORY(T,p,proofs) without deriving arbitrary unrelated host claims, **provided the host does not accept an unrestricted reflection rule "T proves p, therefore the host asserts p".**

**Proof.** The finite certificates establish only \(T\vdash p\) and \(T\vdash\neg p\). The host's metatheory can represent these as data and derive Inconsistent(T). A rule which concludes an arbitrary host q from this data is **not supplied** by the typing; classical explosion is not invoked within the host, whose own premises have not become contradictory. \(\square\)

This is **local syntactic integrity**, not a universal proof of the host's consistency. The source's historical no-explosion aspiration is respected as *lineage*; its unverified claims of absolute global immunity to Russell/Gödel are **not** used as axioms. See the [R05 theorem/fixture review](https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R05_FORMALIZACION_META_SISTEMA_v0.1.md).

Likewise, Gödel coding and particular proof verifications can be effective while the **subject theory** satisfies an incompleteness theorem. This does not make its metalanguage complete or omniscient. For conventional logical definitions see the [Stanford Encyclopedia entry on Russell's paradox](https://plato.stanford.edu/entries/russell-paradox/) and [Gödel's incompleteness theorems](https://plato.stanford.edu/entries/goedel-incompleteness/).

### 6.2. The agent initializes and detects no peers

Let \(U^{\rm peer}_r=\varnothing\): the initializer found no **peer meeting its detection interface**. The meta-level instantiates H-ND-UNIVERSAL for the whole admitted finite representation \(U_r\), not for the population of peers.

The resulting knowledge is:

\[
\operatorname{FoundPeers}(r)=0,\quad
\operatorname{GeneralExteriorOfFiniteU}=\mathrm{TRUE}
\quad\text{(in the declared open model)},\quad
\operatorname{OutsidePeerExists}=\mathrm{UNDETERMINED}.
\tag{4}
\]

No other agent, detectability or communication possibility has been inferred.

**Theorem 6.2 — scoped initializer audit (TR-22/TR-24).** In a model satisfying H-ND-UNIVERSAL, a finite U cannot truthfully claim to **exhaust all of \(\Omega\)**. This does **not** imply a physical sensing or filtering defect. A separate H-OUT(peers) certificate is needed to claim another peer exists; a **verified, applicable H-DETECT(peers,t)** obligation and a failure by its deadline are needed to diagnose a contract breach.

**Proof.** Instantiation of (2) refutes the proposition \( \operatorname{im}(\operatorname{den}_{U_r})=\Omega\). The empty-Agent countermodel in Theorem 4.2 refutes an inferred peer's existence. Detection-contract failure follows only when a separate contract entails a nonempty detection under conditions actually met and the required output is absent. \(\square\)

The agent **may** generate a task to reconsider modalities, type assumptions or the representational scope of sensing/inference/communication. It is **not** logically compelled to find another peer, to construct a specific protocol or to reprogram a sensor.

### 6.3. What resilience has actually been shown

A reporting architecture that retains typed unknowns and refuses unsupported full-coverage assertions can **avoid the specific representational error of false closure**. A proof-checker with an isolated meta-report can **avoid the particular cross-language inference error of promoting an object-level contradiction into host conclusions**. Both require **sound and qualified evidence/premises**. Neither shows zero runtime bugs, guaranteed timely completion, successful self-repair, immunity to contradictory source reports or universal reliability in actual robot fleets.

## 7. Meaning transfer and the distinct informational orders

Let \(H_r:W\to\mathcal H_r\) be the history available from a finite run, and \(q:W\to Q\) the independently declared target. If two admissible worlds have the same H but different target values, no decoder **of the trace alone** reconstructs q across those worlds:

\[
H_r(w_0)=H_r(w_1),\quad q(w_0)\ne q(w_1)
\Longrightarrow
\nexists f:\ q=f\circ H_r.
\tag{5}
\]

This is the **standard fiber/factorization criterion** (Given Universe; 00M §4), not a proof that no finite encoding ever suffices for a finite task. It explains why sending millions of accurate run records cannot **by itself** establish a conclusion that depends on unobserved alternatives.

When a source ecosystem \(\mathcal E_S\) and receiving ecosystem \(\mathcal E_R\) have different states, meaning must be carried via an independently justified **partial interpretation** \(\mu:D_\mu\subseteq W_R\to W_S\) such that

\[
q_R(v)=q_S(\mu(v))\qquad(v\in D_\mu).
\tag{6}
\]

If a source evaluator returns only sound definitive results or UNKNOWN and the interpretation/authority checks genuinely apply, then the receiver can reuse a definitive source result soundly on \(D_\mu\) and preserve UNKNOWN outside it. A **mapping of object meanings** never grants legal authorization merely by composition; provenance, purpose, validity and source-owner rights remain distinct [R04 §14.5](https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R04_ALGEBRA_POSICIONAMIENTOS_v0.1.md).

**Theorem 7.1 — strict semantic expressivity (TR-10/TR-15).** The open metasyntactic interface can express a properly interpreted outside-U question (and, when the model premise justifies it, the fact that an exterior exists) that the **definitionally U-restricted** interface cannot express. This is a *typed-language inclusion theorem*, not an omniscient object detector.

**Theorem 7.2 — weak decision-information dominance (TR-4).** For any world-dependent closed report X and enriched report Y satisfying \(X=g\circ Y\) by a valid **forgetful decoder**, every receiver decision rule using X can be implemented using Y. Under identical admissible actions and no charge for the extra information:

\[
\inf_{d_Y}\mathbb E[\ell(d_Y(Y),q)]
\ \le\
\inf_{d_X}\mathbb E[\ell(d_X(X),q)].
\tag{7}
\]

**Proof.** Given any \(d_X\), choose \(d_Y=d_X\circ g\). The enriched rule exactly reproduces every old action; optimizing over more choices cannot increase minimum loss. \(\square\)

This theorem is **weak, with equality permitted**. The extra flag H-ND-UNIVERSAL, if constant and already derivable from common knowledge, may **not distinguish any further possible-world pair**. A message containing only "OPEN" need not lower loss for an independently fixed decision problem. **Observed, source-qualified, world-varying evidence** can create strict decision improvement; the broader mathematical conditions are Part II's subject.

**Theorem 7.3 — representation equivalence (TR-7).** Two deterministic interfaces \(Y,Z\) are information-isomorphic on an admissible world class W exactly when they induce identical observation fibers: \(Y(w)=Y(w')\iff Z(w)=Z(w')\). Equivalently, each signal is a function of the other on their images. **Effective** equivalence also requires computable, authorized, feasible decoding under the resource profile.

**Theorem 7.4 — maximality only relative to given qualified information (TR-9).** If an enriched report Y permits exact reconstruction of the fixed bundle E of *actually available, qualified* source information, then every derived \(Z=h(E)\) is a function of Y. This is **relative faithfulness/maximality under a fixed E**, not a theorem that Y encodes every future or unknown fact. Under H-EXP there is no globally maximal total sound semantic decider: another correctly answered fixed case can be hardcoded nonuniformly into any such decider's UNKNOWN locus (TR-8). Gödel/Turing do **not** imply that every further correct refinement causes inconsistency.

## 8. Programme reality: meta-operations are executable syntax

The **abstract model** and any **physical realization** have different types. An abstract metalanguage can quantify over unbounded model domains to *define questions* without receiving an actual-world truth oracle. A bounded embodied agent realizes its objects with finite strings, instructions, clocks, storage, verification and communication. A human mathematician is similarly physically bounded when carrying out particular proofs, although the mathematical theorem may quantify beyond the human's finite notes.

**Compiler theorem (TR-19).** An ordinary universal machine can compile or simulate an effective kernel P and effective metareporter M into one conventional programme with the same specified observable behaviour on terminating inputs. The model's **relative syntactic expressivity** derives from *different interpreted output languages and permitted operations*, not a super-Turing processor.

**Design-versus-copy distinction.** Creating a context-appropriate meta-description, choosing a valid source, proving an inadequacy, selecting a safe response, compiling a programme and running the final binary are **different activities**. A conventional system given the correct already-selected binary can reproduce execution. This says nothing about the effort, provenance and uncertainty of **discovering which binary is appropriate** in a new context. Conversely, a conventional programme that itself performs the same metareasoning is functionally an open-aware/metasyntactic implementation, however it is named. An execution-only benchmark cannot establish an advantage in design or choice; the full cost of acquisition, verification and discovery must be represented.

## 9. Optional classification of the open frontier (not the architecture's definition)

An open meta-report may preserve **particular qualified relational claims** about reserve, exploration, incompatibility, likely material effects and unknown evaluability, without requiring an exhaustive map. The programme's adopted A/B/C/D terms [00M v0.8](../ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md#abcd-canonical) are **one possible process-relative taxonomy**, not the necessary grammar for the present metasyntactic theory or its proposed utility proof. The optional labels B′/C′/D′ are **open-boundary qualifiers of partial role assertions**, not enumerated complementary sets.

A precise **negative requirement** is that no agent must decide every B/C, C/D or "UNKNOWN-of-UNKNOWN" semantic boundary merely to report that its generalization obligation remains open. A finite new syntactic label is not a universal semantic type classifier; Theorem 5.3 supplies the corresponding computability counterexample.

## 10. Research integrity, proof map and executable evidence

The article's claims are deliberately no stronger than their sources and proofs. The historical ResearchGate/Google Drive mathematical originals motivate the framework; [R03](https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R03_PRIMALIDAD_Y_LOGICA_v0.1.md) proves the specified subset-label count \(2^m-1\), not physical inhabitants of an exterior; [R05](https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R05_FORMALIZACION_META_SISTEMA_v0.1.md) gives particular finite underdetermination certificates, not a universal truth oracle. The [PR #60 mathematical source programme](https://github.com/dakleyer/structural-awareness-contributions/pull/60) remains **open and unmerged**, with its D3 supplementary-observation selection criticized by the [PR #59 re-audit](https://github.com/dakleyer/structural-awareness-contributions/pull/59): existing information must be included before declaring supplementary evidence minimal.

| Consolidated result | Previous derivation provenance | Status |
| --- | --- | --- |
| F1 / F2 / F3: uniform limit, open-prefix ambiguity, exhaustive encounter | [OW-1, OW-5, OW-6, OW-7, OW-9](./OPEN_WORLD_AGENTIC_INTERACTION_INDETERMINACY_L1_EXTENSION_v0.1.md) | Standard computability + explicitly conditional traversal/discovery |
| 4.1–4.2: universal frame openness and no peer-specialization | Historical ND; **owner-supplied local v0.9 revision**; elementary cardinality and countermodel | Correct for stated model / premises; not verified for physical \(\Omega\) |
| 5.1–5.3: restricted language and typed effective constructor; novelty limit | Historical R03 + [v0.8 archive, TR-15–TR-17](./archive/2026-10-27_A_APRIME_FULL_WORKING_DERIVATIONS_v0.8.md) | Language-relative proof; constructor; standard halting reduction |
| 6.1–6.3: typed meta-certificate / local resilience | Historical R05, R05 review + [v0.8 TR-18](./archive/2026-10-27_A_APRIME_FULL_WORKING_DERIVATIONS_v0.8.md) | Conditional finite-proof integrity, not universal resilience |
| 6.2: empty peer initializer | [v0.8 TR-22](./archive/2026-10-27_A_APRIME_FULL_WORKING_DERIVATIONS_v0.8.md) corrected by local v0.9 supplied draft | General exterior only; no automatic peer/fault inference |
| 7.1–7.4: transfer, strict language expressivity, weak information order, relative faithfulness | Historical *Given Universe*, 00M, R04 + [v0.8 TR-1–TR-14](./archive/2026-10-27_A_APRIME_FULL_WORKING_DERIVATIONS_v0.8.md) | Mostly elementary factorization/refinement with typed assumptions |
| 8: compiler and design distinction | [v0.8 TR-19](./archive/2026-10-27_A_APRIME_FULL_WORKING_DERIVATIONS_v0.8.md) | Ordinary universal simulation; design utility remains task/cost-dependent |

**Finite research fixtures previously authored and retained**, for independently reproducible *bounded model checks* rather than proof of the unbounded theorems:

- [A/A′ weak information dominance](./fixtures/A_APRIME_WEAK_INFORMATION_DOMINANCE_v0.1.mjs), witnessed two-world decision refinement;
- [four-state changed-operation and strict-gain comparison](./fixtures/A_APRIME_STRICT_VALUE_FOUR_STATE_v0.1.mjs);
- [composed K/D execution with open residual](./fixtures/OPEN_ECOSYSTEM_COMPOSITION_AND_RESIDUAL_v0.1.mjs);
- [metasyntactic AST emitter and restricted type checker](./fixtures/METASYNTACTIC_OPEN_FRONTIER_PROGRAM_v0.1.mjs);
- [external-U and deadline-contract tests](./fixtures/EXTERNAL_U_METASYNTACTIC_DIAGNOSTICS_v0.1.mjs).
- [universal finite-frame principle and typed object/meta contradiction isolation](./fixtures/UNIVERSAL_FRAME_OPENNESS_AND_TYPED_META_REPORT_v0.1.mjs): 128 finite frames checked inside the stipulated infinite-natural-number model, with 522 finite assertions.

The historical external-U fixture remains a qualified H-OUT/H-DETECT specialization. The newly published universal-frame fixture tests the **type-neutral ND separation** on 128 explicitly chosen finite frames, with object-level contradictions isolated from host-level reports. Its 522 assertions are **finite constructed checks**, not an independent machine proof of ND for every possible frame, a physical-world measurement, or a GitHub CI result. The separate owner-supplied v0.9 draft and its earlier local executable companion remain distinct historical source material; no claim is made that those exact files were previously committed.

## 11. Conclusion — end of Part I and exact handoff to utility

The architecture's **established mathematical content** is:

1. A real, executable metasyntactic programme can communicate **a question and its open frontier** beyond a strictly U-closed claim language, without an oracle and without identifying the exterior.
2. A typed meta-checker can preserve a contradiction or insufficiency as **a claim about the analysed system** without silently importing a false object-level conclusion. This supplies specified resilience/integrity protections, not universal fault prevention.
3. In an explicitly infinite open model, the **universal finite-frame ND principle** correctly entails that each finite representation has a non-specified exterior. It does **not** entail other peers, communications or an initializer fault.
4. A recoverably enriched report is **weakly at least as decision-informative** as its erasure; a constant OPEN tag may yield no strict world-discrimination, and equivalent conventional representations can tie.

The article **does not claim** absolute semantic truth, a global noncomputable oracle, unbounded cost-free meta-execution, complete physical agent discovery or superiority over every ordinary software system. Nor does it claim the historical *Primalidad y Lógica* prime/composite cycle thesis is a proved completeness theorem for arbitrary logics.

The next scientific task is therefore **utility**, not repetition of an already established representational contrast: identify a **nontrivial class of receiving questions** in which additional *qualified, task-relevant meta-information* changes achievable decisions, and identify the **cost/rights conditions** under which that information is worth acquiring and transmitting. This is the independent [Part II — Mathematical Utility Classes of Metasyntactic Information](./METASYNTACTIC_UTILITY_CLASS_THEOREMS_v0.1.md). It is grounded in original *Given Universe* and source-review results R01/R03/R04/R05, and in the still-unmerged PR #60, while deliberately **not** copying A/B/C/D, the social ACC model or a particular agentic product implementation.

---

## Appendix A — Universal openness and typed no-explosion revision

The owner-supplied local **v0.9 draft**, written after the public v0.8 working edition, corrects the example of an agent that detects no peers. This v1.0 incorporates its three substantive results: (i) H-ND-UNIVERSAL quantified over every finite frame rather than the predicate Agent(x); (ii) **non-entailment of existence/detectability/communicability of particular peers** from that premise alone; and (iii) **typed isolation of object-calculus contradiction** in the meta-calculus. The original local draft was **not previously committed** and is not described as such. Full working predecessor formulas remain accessible through the archived v0.8 source.

The logically complete bounded output for an empty-peer run is therefore:

~~~text
object_run:
  detected_peers: []
  meaning: "no peer detected under this run's interface"
meta_run:
  frame_principle: "all admissible finite frames leave an exterior"
  frame_principle_basis: "proved for declared infinite model / explicit axiom"
  current_frame_exhaustive_of_Omega: false  # under applicable ND
  another_peer_exists: UNDETERMINED
  communication_possible: UNDETERMINED
  sensor_defect: NOT_ESTABLISHED
  suggested_followup: REVIEW_REPRESENTATIONAL_SCOPE
~~~

This is a model-relative **finite report**, not an actual-world measurement or a universal sensor-repair decision.
