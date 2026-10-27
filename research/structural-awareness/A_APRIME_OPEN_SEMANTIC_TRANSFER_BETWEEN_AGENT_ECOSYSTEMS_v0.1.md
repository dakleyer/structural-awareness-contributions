# From A to A′: Open Meaning and Semantic Transfer Between Agent Ecosystems

**Structural Awareness Programme · Mathematical Contributions · Working research companion v0.2 · 27 October 2026**  
**Stable-path notice:** retained v0.1 filename for existing inbound links; **the current document edition is v0.2**, recorded by the GitHub revision.  
**Logical subject:** SA-MATH-TR-01 · **Relationship:** mathematical continuation of [OW-1–OW-11, effective non-closure and repeated runs](./OPEN_WORLD_AGENTIC_INTERACTION_INDETERMINACY_L1_EXTENSION_v0.1.md).  
**Status:** conditional mathematical construction, intended for mathematical review. AI-assisted authoring at the research owner's request; not independently formalized in a proof assistant and not an adopted protocol or A/B/C/D definition.  
**Scientific lineage:** Iván Abril Palma, *Practical Incompleteness* (L1); *The Projection Mechanism* (2025 and distinct 2026 fourth revision); *The Projected Infinite Paradox*; [00M mathematical plausibility and canonical A/B/C/D](../ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md#abcd-canonical).

## Abstract

A finite agent execution can deliver exact local results without settling the semantic task to which its procedure refers in an open world. When a source ecosystem sends only execution traces to a receiving ecosystem, the receiver may acquire extensive data without enough information to reconstruct the **general question** that those executions were intended to address. When it instead sends a run-local result as a **globally closed set**, it exports an unsupported exhaustiveness claim. The proposed semantic carrier separates **A, the procedure and its declared task**, from **A′, its open non-determination frontier**. A/A′ is not a sum of extensional sets and does not require enumeration of unknown agents. We prove a trace-only nonfactorization result, a false-closure transfer result, and a conditional soundness statement for semantic transfer through a qualified correspondence between the source and receiver's questions. A further result identifies the **weak information dominance** of a signal preserving witnessed boundary information over a reduced signal that discards it, without giving either machine the power to compute A′. The B/C/D distinctions are treated as **partial, process-relative abstractions of the open frontier**, each retaining its own primed non-closure rather than forming a mandatory exhaustive partition. The receiver can thereby preserve **meaning and honest incompleteness** without being given a purported universal semantic oracle or a completed list of every unknown case.

## 1. Names and mathematical objects

Use \(\mathcal E_S\) for the **source ecosystem** and \(\mathcal E_R\) for the **receiving ecosystem**. Do not call these ecosystems “A” and “B”: those labels would collide with the A/A′ mathematical pair, as well as the adopted A/B/C/D process-relative vocabulary of 00M.

In **this note only**, define:

\[
A_{\mathrm{proc}}=(\Pi,q,\rho,\sigma)
\tag{1}
\]

as **A**, the executable **procedure together with its intended semantic task**. \(\Pi\) is the instruction and its effective subroutines (“execute this N times,” “search for 17 seconds,” “find the nearest eligible neighbor”), \(q\) is the declared **semantic question**, \(\rho\) describes available time, computation, communication and verification resources, and \(\sigma\) declares the relevant predicate, metric, scope, time and interpretation. An instruction merely saying “run N times” without identifying **what it intends to determine** is not yet a complete semantic specification.

For any finite source execution sequence \(r\), distinguish:

\[
L_{S,r}:=\operatorname{Trace}_{\mathcal E_S}(A_{\mathrm{proc}},r),
\qquad
M_{S,r}:=\operatorname{QualifiedMatches}(L_{S,r}).
\tag{2}
\]

The finite trace \(L_{S,r}\) and the witnessed result set \(M_{S,r}\) are **products of executing A**. They **are not A**. A particular run's qualified output may be exactly determined, even though A's intended task refers to an open world.

Define **\(A'_S\)** as the **open semantic frontier** relative to \(\mathcal E_S\) and \(A_{\mathrm{proc}}\): the continuing applicability and generalization obligations of \(q\) **not established by the finite execution record**, together with the fact that no global semantic/inventory closure is available under the original L1/OW-1/OW-6 hypotheses. A′ is a **semantic boundary specification**, not an enumerated collection of all unknown objects, nor merely the list of observed INDETERMINATE status values. Its source-side extension cannot generally be computed as a closed inventory.

The **proposed semantic carrier** is:

\[
\boxed{
\mathfrak M_S(A)=A_{\mathrm{proc}}\;\widehat{\oplus}\;A'_S
}
\tag{3}
\]

where \(\widehat{\oplus}\) means **typed coupling**, not numerical addition, ordinary union or literal set complement.

A carries the **instruction, question and interpretation**. A′ carries the essential **non-closure qualification**: the procedures and executions do not exhaust the semantic question's reach. Neither component is usefully replaced by an accumulated bag of old run data.

## 2. Theorem TR-1 — the run history is not the meaning of the procedure

Let \(W_S\) be a class of admissible possible source-world situations. A finite history is an observation map

\[
H_r:W_S\longrightarrow\mathcal H_r,
\]

and the semantic target of A is independently defined as

\[
q_S:W_S\longrightarrow Y.
\]

Assume that the open-world situation contains two admissible worlds whose **entire available run history** is indistinguishable, while the correct semantic answer differs:

\[
\exists w_0,w_1\in W_S:
\quad H_r(w_0)=H_r(w_1),
\qquad q_S(w_0)\ne q_S(w_1).
\tag{4}
\]

**Theorem TR-1 (trace-only nonfactorization).** No function of the finite run history alone recovers the intended semantic answer for both worlds:

\[
\boxed{\nexists f:\mathcal H_r\to Y
\quad\text{such that}\quad q_S=f\circ H_r.}
\tag{5}
\]

**Proof.** Equal histories force equal values from f; the target differs in (4). \(\square\)

This is **the established 00M §4 task-sufficiency/factorization condition applied to finite source executions**, not a new general Turing theorem. OW-1 and OW-6 separately prove a stronger **effective uniform frontier** for the expressive peer family. TR-1 explains why accumulating arbitrarily many **particular finite** execution records, without an appropriate semantic rule and scope, does not authorize a global claim about unseen or future contexts.

Transferring a huge record may be expensive yet leave precisely the missing distinction unresolved. The mathematics proves **semantic insufficiency under (4)**; it does not claim that code is always smaller than its logs or prove an unconditional byte/information ratio.

## 3. Proposition TR-2 — a false closed set exports a semantic error

Let the source return a finite collection of correctly **witnessed** positive cases \(M_{S,r}\). Now suppose it transmits the **stronger** statement

\[
M_{S,r}
=
\{x\in\Omega_S^{\mathrm{relevant}}:P_S(x)\}
\tag{6}
\]

as if its actual execution had certified **all and only** the matches in the open source world.

Under the open-world alternative of OW-7/OW-10, two possible source worlds can yield the **same transmitted finite record** while differing in unobserved, but relevant, matches.

**Proposition TR-2 (false-closure transfer).** In such a pair of worlds, the globally exhaustive claim (6) is false in at least one, even though every individual record in \(M_{S,r}\) is correct. A receiver that uses (6) as a premise imports an **unsupported scope/exhaustiveness commitment**.

**Proof.** The export is identical, but the correct global set differs. It cannot be equal to the same finite set in both worlds. \(\square\)

The transmitted failure is **not necessarily an exception or corrupt byte sequence**. It is the unjustified assertion that the *scope of what has been determined* coincides with the *scope of what the procedure means to determine*. Better transport reliability does not repair that confusion.

## 4. Theorem TR-3 — qualified transfer of A with A′

The required cross-ecosystem object is **not** the closed result set and **not** the unqualified run history. Transmit the semantic pair \(\mathfrak M_S(A)\), then interpret it **for the receiving ecosystem**.

A receiving ecosystem need not share the source's eligible population, metric, authority, context or available evidence. Let \(W_R\) be its admissible worlds, \(q_R:W_R\to Y\) its **independently fixed recipient question**, and let

\[
\mu:D_\mu\subseteq W_R\longrightarrow W_S
\]

be a **qualified, partial source–receiver interpretation**. For a shared answer type \(Y\), preservation of the relevant question requires:

\[
\forall v\in D_\mu,\qquad
q_R(v)=q_S(\mu(v)).
\tag{7}
\]

If answer types differ, (7) must be replaced by a correspondingly qualified value translation. Mere identical protocol labels or the name “nearest” is not evidence that (7) holds.

Let \(C_S\) be a **sound source evaluator**: it may return a correctly qualified definitive value from Y or INDETERMINATE, but never a false definitive value. Define a receiver interpretation:

\[
C_R(v)=
\begin{cases}
C_S(\mu(v)),
  & v\in D_\mu\text{ and the source/interpretation evidence is valid},\\
\mathrm{INDETERMINATE},&\text{otherwise}.
\end{cases}
\tag{8}
\]

**Theorem TR-3 (soundness of qualified semantic transfer).** Under the source soundness assumption and (7), every **definitive** \(C_R\) output is sound for \(q_R\). Cases without a qualified correspondence remain open rather than being converted into fictitious definitive answers.

**Proof.** If \(C_R(v)=b\in Y\), then by (8) the qualified branch applies, and \(b=C_S(\mu(v))=q_S(\mu(v))=q_R(v)\). Otherwise the evaluator issues no definitive semantic claim. \(\square\)

The **semantic meaning is transferred without *false closure***, not as a promise that every substantive question becomes decidable in the receiver. The latter is exactly what L1/OW-1 forbids for the unrestricted expressive class.

It is also wrong to transplant source A′ as a literal unchanging bag of unknown objects. Instead:

\[
\boxed{
(A_{\mathrm{proc}},A'_S)
\ \xrightarrow[\text{qualified }\mu]{\text{semantic transfer}}\
(A_{\mathrm{proc},R},A'_R)
}
\tag{9}
\]

where \(A'_R\) is **requalified** for the receiving ecosystem's own scope, capabilities, agent population and unanswered target obligations. What can travel is the **semantic commitment and its open frontier**, not a completed inventory of all future unknowns.

The receiver can understand the source's declared intended question even when no \(\mu\) is available; what it cannot do without (7) is claim that it has **correctly applied or decided** that question in its different ecosystem.

## 5. The example: a nearest observed neighbor versus *the* nearest neighbor

Let \(S_r\) be the finite set of source-observed qualified neighbor candidates in execution r. The source can correctly return:

\[
\widehat x_r\in
\operatorname*{argmin}_{x\in S_r\cap\operatorname{Eligible}_S}
d_S(a,x).
\tag{10}
\]

The output is **nearest within the observed eligible population**. It does not establish the concept **the nearest eligible neighbor in the whole relevant open ecosystem**, whose predicate is:

\[
\operatorname{Nearest}_S(x)
\iff \operatorname{Eligible}_S(x)\land
\forall y\in\Omega_S^{\mathrm{relevant}}
\bigl(\operatorname{Eligible}_S(y)\Rightarrow
d_S(a,x)\le d_S(a,y)\bigr).
\tag{11}
\]

The **universal comparison** in (11) is not exhausted by finite run records under the open encounter condition. Two worlds may have identical observed nearest-neighbor results while one has a closer eligible but unobserved neighbor. Thus the source output can be locally correct while an unqualified globally nearest claim is wrong.

**A** specifies **which question is being pursued, with which metric and eligibility semantics, using which procedure and budget**. **A′** records that the **universal comparison required by the target has not been exhausted**, independently of how many successfully observed nearest neighbors were reported. Their combination is precisely what gives the receiver an interpretable distinction between an observed witness and the **general meaning** being pursued.

The receiving ecosystem \(\mathcal E_R\) may have different notions of distance, eligibility, time and authority. It must interpret those semantics and requalify the open frontier; merely transferring coordinates and a ranked list does not prove the same global nearest-neighbor relation in the recipient.

## 6. Why A′ matters for generalization and abstraction

A trace explains **what happened in a finite execution**. A procedure with a declared question explains **what operation the agent intends to perform**. The open frontier A′ explains **why the delivered history is not a certificate that the intended question has been exhausted**.

The semantically consequential information in A′ is **not a computable list of every unknown**. It is the **generalization obligation left open** by the procedure's target, particularly when the target quantifies over agents or possible contexts not yet known to the source. This is why **A′ matters when moving to a higher abstraction layer or to another ecosystem**: it prevents a legitimate observed A-result from silently becoming a global truth claim.

This establishes a precise form of **construction–meaning asymmetry**:

\[
\boxed{
\text{finite constructed output}
\not\Rightarrow
\text{globally sufficient semantic representation}
}
\tag{12}
\]

and a positive, but **conditional**, counterpart:

\[
\boxed{
\text{procedural target A + open frontier A′ + qualified correspondence}
\Rightarrow
\text{sound qualified transfer of the intended task}.
}
\tag{13}
\]

The first follows from TR-1 when (4) holds; the second is TR-3. Neither implies that semantic content is *physically created by unknown objects*, that an actual city contains infinitely many unobserved peers, or that any transfer architecture outperforms an existing competent method. The distinction between **description of meaning** and **successful determination of all instances** is an essential part of the mathematics, not a retreat from L1.

### 6.1. A machine cannot compute the complete A′, but can witness its boundary during A

Fix the procedure/semantic task \(A_{\mathrm{proc}}=(\Pi,q,\rho,\sigma)\) defined in §1. Running it yields **finite outputs and a finite execution/evidence record**. It can produce a verified match, a justified refusal, a timeout, a contradictory report, a damaged input, or an explicit INDETERMINATE. These are **run-level products of A**. A machine that executes A does not thereby enumerate, decide or reach the whole unclosed \(A'_S\).

Nevertheless, an execution may encounter a **finite witnessed manifestation of its open boundary**. The machine can recognize, for example, that a particular received authorization record cannot justify a definitive answer, or that the comparison with unseen eligible neighbors remains open. Calling this observation a **qualified indicator of A′** does not mean the machine has evaluated all of A′.

Define \(Z_{S,r}\) as a **finite qualified boundary record** for run r. It can include *observed unresolved questions, explicit limits of evidence, known B/C/D-related claims, undecided role assignments, and open-coverage or non-closure qualifiers*. In particular:

\[
Z_{S,r}\text{ is finite and observable},\qquad
Z_{S,r}\ne A'_S.
\tag{14}
\]

Even \(Z_{S,r}=\varnothing\) does not imply \(A'_S=\varnothing\). This distinction is essential: **A′ supplies the open semantic scope; \(Z_{S,r}\) supplies only the boundary evidence actually available in a run.**

The machine's ability to state an indetermination is not an ability to determine the hidden substantive truth. An unanswered request can be *recognized as unanswered*, while its eventual success remains indeterminate.

### 6.2. Two ways to transmit one execution: loss by erasure

Compare two **deliberately defined signalling policies** over identical source runs and the same source question:

\[
X(w)=
\bigl(A_{\mathrm{proc}},M_{S,r}(w)\bigr)
\tag{15}
\]

and

\[
Y(w)=
\bigl(A_{\mathrm{proc}},M_{S,r}(w),
        Z_{S,r}(w),\mathrm{OPEN}(A'_S)\bigr).
\tag{16}
\]

Here X is the **reduced A-only representation**: it keeps the procedure and established results but **drops the observed residual qualifiers**. Y is the **A/A′-aware representation**: it keeps X and additionally preserves the observed boundary record and the open semantic obligation. The symbol \(\mathrm{OPEN}(A'_S)\) is a **finite truthful non-closure declaration**, **not an encoding of every indeterminate element**.

There is a simple, computable **forgetting map**

\[
g:Y\longrightarrow X,\qquad
g(A,M,Z,\mathrm{OPEN})=(A,M).
\tag{17}
\]

Consequently \(X=g\circ Y\). This is the exact limited sense in which a source can perform an **information-losing projection** by exporting X after discarding source-qualified indeterminate signals. This use of *projection* means a forgetting/representation map; it does not assert every theorem in the separate 2025/2026 *Projection Mechanism* papers.

Not every system described colloquially as “A-only” will actually erase the boundary. The theorem compares the **specified erasing policy X** with the **retaining policy Y**. If an existing sender already preserves Z, its signal is not this X baseline, whatever its product branding.

### 6.3. Theorem TR-4 — weak informational dominance of A/A′-aware transfer

Let \(W\) be any fixed class of source-world/run situations, and let \(X:W\to\mathcal X\), \(Y:W\to\mathcal Y\) be the reduced and extended messages (15)–(16). Fix any legitimate **receiving decision task** \(t:W\to\mathcal T\), a common available action set \(\mathcal A\), and any task-specific loss \(\ell(a,t(w))\). Compare the **best attainable receiver decisions** under the **same feasible actions and decision-processing assumptions**, before charging any additional acquisition, communication or deployment cost for Y.

**Theorem TR-4 (weak informational dominance).** If \(X=g\circ Y\), then for any receiver policy \(d_X:\mathcal X\to\mathcal A\) there exists a richer-message policy \(d_Y:\mathcal Y\to\mathcal A\) yielding exactly the same actions and losses in every admissible world. Thus the optimal attainable expected or worst-case loss with Y cannot exceed that with X:

\[
\boxed{
\inf_{d_Y}\mathbb E[\ell(d_Y(Y(W)),t(W))]
\ \le\
\inf_{d_X}\mathbb E[\ell(d_X(X(W)),t(W))]
}
\tag{18}
\]

and, likewise, for the corresponding infimum worst-case risk whenever those quantities are defined.

**Proof.** For any \(d_X\), set \(d_Y=d_X\circ g\). By (17), \(d_Y(Y(w))=d_X(X(w))\) **for every w**. Hence every policy achievable using X is also achievable using Y, by ignoring its extra fields. The optimal loss under Y is weakly no larger. \(\square\)

This is a simple **deterministic garbling / information-refinement** instance of the established Blackwell comparison of experiments: a richer observation can reproduce the poorer one by deletion. The elementary proof above is sufficient for this case; no claim of discovering a new statistical theorem is made. See David Blackwell, *Equivalent Comparisons of Experiments*, *Annals of Mathematical Statistics* 24(2), 1953, 265–272, DOI [10.1214/aoms/1177729032](https://doi.org/10.1214/aoms/1177729032).

**Meaning of weak.** Equality is allowed. If the supplementary boundary signal is irrelevant to the receiving task, or the receiver already knows it, the receiver may gain **nothing**. The theorem establishes **greater or equal attainable decision information**, not that every actual enhanced algorithm automatically makes better choices, spends fewer bytes, reduces latency or enjoys lower net operating cost. These latter claims require a matched resource/communication model and measurements.

**Strict informational gain requires a witness.** If two admissible situations have \(X(w_0)=X(w_1)\) but different qualified additional signals \(Y(w_0)\ne Y(w_1)\), Y preserves a distinction lost by X. Strict *decision* improvement occurs only for a task that **depends on that distinction** and for which Y supports a better receiver action.

### 6.4. Proposition TR-5 — a finite strict-gain witness without deciding A′

Consider two source worlds with the **same procedure A** and the **same two confirmed positive receipts**. In \(w_0\), the finite encountered peer population consists exactly of those two witnessed cases. In \(w_1\), the source encountered an **additional third peer with an unresolved authorization question**, but the X channel discards the third peer's unresolved status. Both source ecosystems still have **globally OPEN population/semantic coverage**.

The reduced payload is identical:

\[
X(w_0)=X(w_1)=(A,\{\mathrm{receipt}_1,\mathrm{receipt}_2\}).
\tag{19}
\]

The extended payload preserves the distinction:

\[
Y(w_0)=(X,\mathrm{observed\ unresolved}=0,\mathrm{OPEN}),\quad
Y(w_1)=(X,\mathrm{observed\ unresolved}=1,\mathrm{OPEN}).
\tag{20}
\]

Define the **independently specified, run-scoped receiving task** \(t(w)\): *did the source finish this particular run with no substantively unresolved encountered peer?* Its answer is YES in \(w_0\) and NO in \(w_1\). For a uniform two-world prior, 0–1 loss and binary receiver actions, any X-only decision must give the **same answer** in both worlds, with a minimum expected error of \(1/2\). Y permits **zero error for this run-scoped meta-question**, because the source provided the trustworthy qualified indicator.

\[
\boxed{
R_X^*(t)=1/2,\qquad R_Y^*(t)=0 .
}
\tag{21}
\]

This is an **illustrative finite construction**, not a field measurement. Y does **not** determine whether the third peer's authorization was truly valid, whether it will eventually complete, or what all unseen peers will do. It improves the ability to **recognize that a currently known decision remains unresolved** and therefore prevents certain false local closures. This is the precise **strict differential witness** compatible with weak informational dominance.

The extra reported information may be tiny (a verified unresolved-count/indicator, subject identity and scope), while the raw execution archive could be large. The construction does not assert a universal compression ratio; it shows **task-relevant information preservation**, not merely higher byte volume.

### 6.5. B/C/D as partial abstractions of A′; B′/C′/D′ as non-closed role frontiers

The open A′ is **not exhaustively divisible into three fully decided subsets**. The current Structural Awareness [00M §1](../ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md#abcd-canonical) supplies a **useful process-relative qualification vocabulary**, with no claim to exhaustively partition a universe.

For any positioning profile \(p=(\mathrm{actor},\mathrm{question},\mathrm{scope},\mathrm{capability},\mathrm{time})\), qualifying an **observed, suitably defined aspect x** may support one or more declarations concerning:

- **B:** characterized evaluation basis and a defensibly assessable reserve beyond the currently delivered functional result;
- **C:** grounded exploration opportunity for which that evaluation basis is not characterized;
- **D:** potentially material condition beyond this process's effective route to evaluation for its particular relevant effect;
- **UNKNOWN / UNQUALIFIED:** even the scope, evidential basis or role assignment is not sufficiently established.

These roles apply **to aspects and functional claims**, not by magically sorting every physical agent into one and only one category. A program may correctly observe and report **one B reserve**, another C lead, or a witnessed D-type evaluation barrier **within a finite run**, yet that says nothing about having listed every possible B, C or D aspect of the open ecosystem.

For each role \(j\in\{B,C,D\}\), write \(\kappa_{j,p}\) for the **partial, evidence-qualified role-assertion function**, defined only on the aspects for which the predicate, scope and proof basis are established. The local **primed notation**

\[
B'_p,\qquad C'_p,\qquad D'_p
\tag{22}
\]

denotes the **unclosed applicability and exhaustion obligation of those partial role characterizations**, respectively. The primes are **meta-level boundary qualifiers**, not newly defined canonical epistemic categories, literal complements \(\Omega\setminus B\), or collections that can be enumerated by the executing agent. They do **not** assert that a particular unseen B-, C- or D-item has been found or that every named role's extensional class is necessarily nonempty.

**Lemma TR-6 (no total role inventory from an open prefix).** Fix any role \(j\in\{B,C,D\}\). If admissible source worlds allow the **same finite role-evidence history** with and without an additional unseen relevant aspect qualifying for j, then no function of that history alone can correctly certify an exhaustive global inventory of j in both worlds.

**Proof.** Both histories are identical, but the proposition “the known j-role claims exhaust all relevant j-role aspects” has different truth values. This is OW-7's indistinguishability proof applied to j-qualified claims. \(\square\)

This is **not** a theorem saying that every B/C boundary is intrinsically undecidable: specific B/C/D assignments may be clear and correctly justified. Rather, **making the role map total and exhaustive over an open domain is an extra global decision/coverage demand**. Under a sufficiently expressive role-decision problem that encodes OW-1's target, a claimed sound total boundary oracle would contradict OW-1; that expressivity connection must be stated for the role-decision task. A program should never be forced to place **all** unqualified open material into B, C or D, or to treat an insufficiently established role as D by default.

**Operational interpretation.** B is a witnessed **reserve of exploitation that can be characterized**, not a certificate of the largest reserve that will ever exist. B′ is the unclosed boundary of **what further reserves could become characterized**. C′ and D′ play the corresponding role for their respective evaluability frontiers. The useful current B/C/D assertions can be transferred as **finite, qualified representatives of A′-related epistemic structure**, while B′/C′/D′ preserve their non-exhaustiveness.

A/B/C/D remains the **owner-adopted vocabulary of 00M**; this source's A/A′/B′/C′/D′ notation is a **candidate mathematical lens**, not an amendment of that normative semantic definition.

### 6.6. What the weak dominance result does—and does not—establish

**Established mathematical consequence:** given equal access to the same source execution and a Y signal that recoverably includes X, the receiver's **set of possible informed policies is no smaller under Y**. Y can preserve qualifying evidence of encountered indeterminates that X deliberately erases; an independent downstream task may strictly benefit, as TR-5 demonstrates.

**Not established by the weak theorem:** a total program for A′; an effective enumeration of all B′/C′/D′; an exact role partition; automatic semantic compatibility between two unrelated ecosystems; a universal lower bitrate; smaller latency; inevitable improvement of every recipient action; or net cost superiority. Transmission costs, access restrictions, interpretation rights and finite processing budgets may change the engineering comparison.

**Core proposition:** an A/A′-aware agent may perform no more computation on the unknown world than an A-only agent, but it can communicate **more of what was legitimately learned—including the limits of what was learned—without compressing an open decision into an unjustified closed result**. This is the **weak informational superiority** that precedes any empirical claim of superior performance.

## 7. Relationship to the established A/B/C/D vocabulary

This note deliberately reserves \(A_{\mathrm{proc}}\) for **the procedure**, to avoid conflating it with the adopted **00M A**, which means **the result actually delivered by a functional process**. A source execution's finite results may be canonical **A** for that execution; its known evaluation basis and reserve may be **B**; a grounded route to explore uncharacterized questions may be **C**; and effects beyond effective evaluation may be **D**, subject to the canonical source's process/question/time conditions. **A′ is a pre-taxonomic description of the unclosed semantic obligation, not a declaration that all A′ is D**. UNKNOWN remains appropriate when even the role assignment lacks justification.

The source's open frontier and the receiving ecosystem's open frontier need not coincide: **ABCD roles are assigned again relative to the receiving process**, not inherited by sharing a label. This is consistent with the current [01J signalling/semantic coupling](../ecosystem-awareness/baseline/01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md), which preserves compatibility limits and does not promote handshake success to global semantic equivalence.

## 8. Position before the Projection Mechanism

TR-1–TR-3 establish the **pre-projection transfer limit and conditional soundness**; TR-4–TR-6 add the **weak informational dominance**, a finite strict-gain witness, and non-total B/C/D role-boundary structure. Together they build the **pre-projection** result: why transferring only executions is semantically insufficient, why closed-result export can convey a false generalization, and how A/A′ plus a legitimate interpretation can transmit the **intended task and its open reach** without claiming to decide everything.

The separate [2025 *Projection Mechanism*](https://www.researchgate.net/publication/393802750_The_Projection_Mechanism_How_Practical_Incompleteness_Infiltrates_Formal_Systems) and [2026 fourth revision](https://drive.google.com/file/d/1OrJ2LWz2qBv2sP8_-VNldWpctxZdwcfI/view) ask what happens when an unqualified representation is imported and operated upon as if it carried sufficient meaning. The *Projected Infinite Paradox* provides a historical motivation for distinguishing named finite constructions and population-level or limiting questions, but its broader ontological claims are not assumed as theorems here.

The next, distinct research question is **projection under an unqualified import of a source result**, not whether the receiver has a way to preserve the A/A′ distinction.

## Source and proof boundary

- [OW-1–OW-11 mathematical source article](./OPEN_WORLD_AGENTIC_INTERACTION_INDETERMINACY_L1_EXTENSION_v0.1.md), including non-closure, bounded indeterminacy and executable set-query sanity checks.
- [00M v0.8 §4 — source/recipient factorization and incomplete summaries](../ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md), from which the TR-1 argument is transferred.
- [00M v0.8 §1 — canonical A/B/C/D terminology](../ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md#abcd-canonical), unaffected by this note.
- [01J current signalling annex](../ecosystem-awareness/baseline/01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md) for the architecture's existing qualification of source-to-recipient meaning.
- [Original *Projected Infinite Paradox* published route](https://www.researchgate.net/publication/393884759_The_Projected_Infinite_Paradox_Unifying_Constructivism_and_Platonism) — historical interpretation, not imported universal proof.

**Documentary disposition:** working mathematical companion, not a replacement for L1, 00M, 01J, any frozen original, or an implementation mandate. TR-1/TR-2 are elementary nonfactorization/indistinguishability consequences; TR-3 is a conditional soundness preservation proof. TR-4 is an instance of standard information refinement/Blackwell garbling; TR-5 is a finite strict-gain witness only for its independently declared receiving task; TR-6 is an open-prefix role-inventory lemma. No total A′ evaluator, exhaustively partitioning B/C/D oracle, automatic ecosystem compatibility or empirical net superiority is claimed.
