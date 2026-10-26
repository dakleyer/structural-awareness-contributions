# 02 — Formal core: dynamic sufficiency, bounded distinctions and explicit proof obligations

**Stage A mathematical development.** Every theorem is conditional on its displayed hypotheses. Nothing here treats A/B/C/D as an objective exhaustive partition of the ecosystem. Core lineage: [G, R01/S01, R03, R04, R05, R07, R10, R20](./01_ORIGINAL_SOURCE_LINEAGE.md).

## 0. Types, scope, epistemic separation

Let \(\mathcal S=(X,\Sigma,o,r,V)\) be a **declared finite, bounded model**:

- \(X\ne\varnothing\) a finite set of candidate system states compatible with a *specified source qualification*; **not** “all real ecosystem states”.
- \(o:X\to O\) a current observable interface (“A-like” functional contracts/outputs only *after* separate 00M qualification). Its fiber relation \(E_o=\{(x,y):o(x)=o(y)\}\).
- \(\Sigma=\{f_a:X\to X:a\in A_{\mathrm{act}}\}\) a finite **declared** signature of eligible deterministic total unary transitions. Partial/stochastic/open actions are **not** covered without additional typing (§7).
- \(r:X\to R\) an independently defined receiver/mission decision question. It may include reward thresholds, safety categories, feasible reallocation, *not subjective suffering*.
- \(Q_j:X\to V_j\) a **separately characterized**, available, permitted source observation for a specific recipient/purpose. *The variable name \(Q\) does not convert unknown EA C/D into accessible evidence*.
- \(\kappa\) a qualification record: owner, source root, declared semantics, time/version, allowed use, cost, evidence quality, and authenticated closure assumptions.

**Two distinct mathematical levels:**

1. *Model-relative truth:* claims over \(X,\Sigma,o,r\), with exact finite proofs.
2. *Actual-world entitlement:* whether the real ecosystem fits these chosen maps, states and permissions. The first does **not** prove the second. Absence of a valid \(\kappa\) yields UNKNOWN.

Canonical EA meanings remain in [00M v0.8](../../../../00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md) and [00N v0.7](../../../../00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.7_RESEARCH_NOTE.md).

## 1. Preliminary fact: factorization is only a diagnostic (S)

**Lemma F1 (known):** There exists \(h:O\to R\) on the image of \(o\) with \(r=h\circ o\) iff

\[
xE_oy\Longrightarrow r(x)=r(y).
\tag{F1}
\]

**Proof:** If \(r=h\circ o\), equal observables imply equal \(r\). Conversely define \(h(z)\) as the common \(r\)-value of any \(x\) with \(o(x)=z\). This is independent of the representative by the displayed implication. □

**Meaning:** equal reports sometimes hide mission-relevant differences. This **does not** establish a new information theorem, and it can fail to motivate extra information if \(r\) is already constant. A large hidden state space, \(K>M\), or a pigeonhole argument says merely that *some states share an observation*; **it does not prove different receiving decisions, applicable permissions, improvement, or a profitable transition**.

## 2. Dynamic theorem: sufficiency can expire when the contract of use changes (S + D)

A quotient implementation under \(\Sigma\) would supply \(\bar f_a:O\to O\) for every eligible operation, satisfying \(o\circ f_a=\bar f_a\circ o\), plus \(\bar r:O\to R\) with \(r=\bar r\circ o\).

**Theorem D1 — exact deterministic interface adequacy.** Such quotient maps on the image of \(o\) exist **if and only if**:

\[
\boxed{E_o\subseteq\ker r
\quad\text{and}\quad
\forall f\in\Sigma,\ xE_oy\Longrightarrow f(x)E_of(y).}
\tag{D1}
\]

**Proof:** The first term is Lemma F1. For \(\bar f\) to be independent of the representative of observed \(o(x)\), all states sharing an observation must have the same observed successor under \(f\). Conversely when congruence holds, define \(\bar f(o(x))=o(f(x))\); independence follows, and the diagrams commute. □

**Corollary D1a — finite-trace adequacy.** Under D1, any finite word \(w=f_{a_n}\circ\cdots\circ f_{a_1}\) has a quotient map \(\bar w\), and \(r(w(x))=\bar r(\bar w(o(x)))\). **Proof:** inductively commute \(o\) past each \(f_{a_i}\), then factor \(r\). □

**Corollary D1b — signature expansion.** If the actual operations and receiving question remain the same except for added eligible operations, the set of equivalences supporting exact quotients may *shrink*, never grow. This is the elementary inclusion \(\mathrm{Cong}(\Sigma_{\rm old}\cup\{f\})\subseteq\mathrm{Cong}(\Sigma_{\rm old})\), not a claim that every expansion necessarily breaks sufficiency.

**Complete 4-state witness [R01 review §6 P2]:**

\[
X=\{0,1,2,3\},\quad o(x)=x\bmod2,\quad r(x)=o(x),\quad s(x)=x+1\bmod4.
\]

For old signature \(\Sigma_0=\{s\}\), parity congruence holds; \(s\) flips the observed bit. Add \(f\) defined as:

| x | o(x) | f(x) | o(f(x)) |
|---:|---:|---:|---:|
| 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 |
| 2 | 0 | 0 | 0 |
| 3 | 1 | 3 | 1 |

Now \(o(0)=o(2)=0\) but \(o(f(0))=1\ne0=o(f(2))\). No deterministic \(\bar f\) on the old parity quotient exists. **The original A-interface remains correct for s; its interpretation no longer suffices for the expanded signature**. This is the more precise research point than K>M.

**Necessary caution:** a sound conventional *set-valued* transition \(f^\#(E)=\{o(f(x)):o(x)=E\}\) remains available. In this example \(f^\#(E)=\{E,O\}\). If conservative HOLD is sufficient for the mission, there may be **no benefit** in refining the interface. Exact quotient failure alone does not establish actual failure, mission loss or EA superiority.

## 3. Existing finite partition-refinement algorithm (S)

Let \(R_0\) be an observation equivalence and \(\Sigma\) finite total deterministic unary operations. Iterate:

\[
R_{k+1}=R_k\cap
\bigcap_{f\in\Sigma}
\{(x,y):(f(x),f(y))\in R_k\}.
\tag{D2}
\]

**Theorem D2:** the iteration stops at a greatest \(\Sigma\)-stable equivalence \(R_\infty\subseteq R_0\). Every stable equivalence \(S\subseteq R_0\) is contained in \(R_\infty\). There are at most \(|X|-|X/R_0|\) *strict* refinement steps.

**Proof:** \(R_0\) is an equivalence. The preimage of an equivalence under \((f,f)\) is an equivalence; intersections preserve equivalence. Each iteration refines, adding at least one block on a strict step. Finite partitions of X have at most \(|X|\) nonempty blocks, hence termination bound. The fixed point is stable under each \(f\). If S is a stable sub-equivalence of \(R_0\), inductively S lies in every \(R_k\); thus S lies in \(R_\infty\). □

**Interpretation:** the algorithm finds the coarsest *state distinction required by declared operations*, not the least new evidence available from vendors. A refinement can be mathematically required but **unimplementable** because no eligible Q exposes it. For a new signature \(\Sigma_1\), regenerate \(R_\infty\) and produce a concrete witness pair where the old quotient breaks. For very large state sets the algorithm is a finite specification, not a claim of tractable enumeration.

**Proof obligation PO-DYN:** externally verify that real contracts can be given such well-typed transitions, and that the new mission/op differs in a way not repaired by existing strong observability. If all validated transitions respect the old quotient, the claimed dynamic-insufficiency episode does not occur.

## 4. R03: receiver-dependent *minimum* supplementary distinctions (S + R)

Fix a finite, independently sampled \(\widehat X\subseteq X\), a receiving target \(r\), eligible queries \(J_\kappa\), and \(g_H(x)=(Q_j(x))_{j\in H}\).

Define the **receiving-conflicting pairs**:

\[
U_r=\{\{x,y\}\subseteq\widehat X:x\ne y,\ r(x)\ne r(y)\},
\]

and the coverage contributed by a query:

\[
C_j=\{\{x,y\}\in U_r:Q_j(x)\ne Q_j(y)\}.
\]

**Theorem D3 (standard finite pair-separation equivalence):**

\[
r=h\circ g_H\text{ on }\widehat X\quad\Longleftrightarrow\quad
U_r=\bigcup_{j\in H} C_j.
\tag{D3}
\]

**Proof:** If a conflicting pair is not separated by any \(Q_j\) in H, its vector \(g_H\) coincides but its target does not; no h exists. If all conflicting pairs are separated, identical vectors cannot hide different targets; define h consistently on each vector. □

Under *additive independent costs* \(c_j\ge0\), choose \(H\subseteq J_\kappa\) minimizing \(\sum_{j\in H}c_j\) subject to (D3): the familiar **weighted set-cover problem**. For dynamic mission horizon h, replace \(r\) by the finite vector \(r_h(x)=(r(w(x)))_{w\in\Sigma^{\le h}}\) if this trace family is authorized and computable.

**Boundary:** D3 does not prove that each Q is available, true, safe, private, legally disclosable or sufficient outside \(\widehat X\). A source query may be a costed observation of a particular B-profile *only after 00M qualification*; none can be invented from C or D. If \(\bigcup_{j\in J_\kappa}C_j\ne U_r\), the exact target is **unachievable by this query menu**, not “solved by oracle.” Cost additivity fails with batch discounts, shared proof work and correlated permissions: use general \(C(H,\kappa)\) and re-check.

## 5. R04: safe domain and transfer of qualified source claims (S + R)

Given source observation \(o\), receiving target \(r\), define its maximal *observation-saturated* target-adequate subdomain:

\[
D^{\rm sat}_{o,r}=\bigcup\{o^{-1}(y):\ |\{r(x):o(x)=y\}|=1\}.
\tag{D4}
\]

**Lemma D4:** this is the largest union of **complete fibers** of o on which r factors through o. Proof: included fibers are target-homogeneous; any admissible union cannot contain a heterogeneous fiber. □

For participant \(i\to j\), translation \(t_{ij}:D_{ij}\rightharpoonup X_j\) must have a **saturated domain** on the declared equivalence and preserve target outputs; a qualified observation square must commute. Two translations compose on:

\[
D_{\rm raw}=\{x\in D_{ij}:t_{ij}(x)\in D_{jk}\}.
\]

The *permitted* domain is smaller: \(D_{\rm eligible}=\{x\in D_{\rm raw}:W_{\rm origin}(x,\text{purpose},t,\text{recipient})=1\}\).

**Lemma D5:** on a domain where both typed squares commute and every map is defined, their composition commutes; **no grant of access or delegation follows from this equality**. Proof: associativity of well-typed partial composition on its common domain. □

Here mathematical **definedness**, semantic adequacy and institutional **authority** are three different predicates. A proposed A→B resource transfer may be *feasible in a global resource ledger* but not in the currently authorized action graph.

## 6. R05: a finite second-order certificate, not omniscience (S + R)

Let \(\Gamma_\kappa\) be a qualified propositional frame over a finite explicitly enumerated model universe X, and \(p\) a question. With \(\mathcal M_\kappa=\{x\in X:x\models\Gamma_\kappa\}\), return:

\[
\mathrm{Meta}_{\Gamma_\kappa}(p)=
\begin{cases}
\text{INCONSISTENT\_FRAME},&\mathcal M_\kappa=\varnothing;\\
\text{ENTAILED},&\forall x\in\mathcal M_\kappa,\ p(x)=1;\\
\text{REFUTED},&\forall x\in\mathcal M_\kappa,\ p(x)=0;\\
\text{UNDERDETERMINED},&\exists x,y\in\mathcal M_\kappa,\ p(x)=1,\ p(y)=0.
\end{cases}
\tag{D5}
\]

**Lemma D6:** for nonempty finite \(\mathcal M_\kappa\), two actual opposite-valued satisfying models are an exact witness for UNDERDETERMINED. The proof is ordinary exhaustion of the two truth-value possibilities. □

Outside a trustworthy, qualified, finite frame, return separate **UNKNOWN**, including uncharacterized source methods, expired credentials, C/D or system-open prefixes. A meta-certificate about \(\Gamma_\kappa\) does not determine actual \(p\), authorize transfer, or change the canonical A of the original agent. We call this a *bounded metaprotocol* rather than a mathematical oracle.

## 7. Open-world, non-closure and local/global limits

**R20 finite-prefix lemma:** if k distinct entities have been observed but an authenticated END signal or trusted upper bound is missing, worlds of size k and k+1 share that prefix. Therefore no universally sound claim “all entities enumerated” follows merely from it. However, authenticated finite scoped completion **is possible**.

**R10 stage-population example:** for \(1\le i\le k\),

\[
p_i^{(k)}=\frac{i}{k}(1-2^{-k}).
\tag{D6}
\]

For each fixed i, \(p_i^{(k)}\to0\); yet \(\max_i p_i^{(k)}\to1\). Moreover for a threshold 1/4, the fraction of stage-k items above it tends to 3/4. **Proof:** for fixed i, \(i/k\to0\); maximum is at i=k; the threshold inequality is \(i/k>1/[4(1-2^{-k})]\), asymptotic frequency 1−1/4. □

The individual-level “safe” fact does **not** factor through an aggregate new-vendor tail question. This can motivate *which* additional aggregate observables to request. It is not proof that such metrics exist or matter in a specific deployment.

**Beyond finite deterministic X:** partial operations require domain saturation and definedness witnesses (R01 P3); nondeterministic systems need simulation/bisimulation conditions; stochastic systems need probability-kernel compatibility; nonstationary vendor signatures require versioned requalification. Arbitrary evolving \(X_t\) cannot be handled by asserting (D1) on one chosen finite \(X\). **Any universal open-world claim is H/open.**

## 8. The only legitimate advantage statements

Let \(\mathcal I_A\) be the information from currently qualified A, and \(\mathcal I_{A,Q}\supseteq\mathcal I_A\) a *legitimate refinement* accessible at no cost to an optimizer allowed to ignore it. Then its **minimum expected loss** satisfies:

\[
\inf_{\delta\in\mathcal D_{A,Q}}\mathbb E[L(\delta,X)]
\le
\inf_{\delta\in\mathcal D_A}\mathbb E[L(\delta,X)].
\tag{D7}
\]

Proof: every A-only policy can be run in the enriched policy class by ignoring Q. □

This **weak** inequality is general decision theory. It says nothing about **strict** improvement, positive net return, rights, source truth, realizability or unique advantage of agentic architecture. Adding \(C_{\rm acquisition}+C_{\rm coordination}+C_{\rm transformation}\) can reverse the net result. A strict difference requires a concrete independent prior/loss and a pair of states requiring different optimal choices, sufficient legitimate discriminating evidence, and an economically feasible transition; still **not** a novel mathematical theorem.

## 9. Requested negative countermodels (must pass)

| Countermodel | Mathematical implication |
|---|---|
| Arbitrarily complex hidden vendor interior, but \(r=h\circ o\) and all transitions respect \(\ker o\) | No BCD need for this declared mission; complexity does not force a failure |
| Expanded signature breaks exact congruence, but a conservative set-valued abstraction makes the correct safe choice | No unique benefit of our protocol |
| Eligible Q changes raw bits but \(r\) is constant on each original A fiber | Extra information yields zero decision value |
| Q separates mission pairs but its use is forbidden, unverified, stale or outside scope | No legitimate information gain or automatic action |
| Reallocation conserves total raw resources but exceeds change/coordination budget | Nominal global optimum unreachable; no free metamorphosis |
| Unlimited state population without a verified finite-frame closure | No sound global “all cases resolved” certificate |
| Competent incumbent computes the same partition, with same queries, rights and cost | Expected **tie**; evidence against superiority assertion |

**Research thesis remaining open:** whether the conjunction of the above familiar mathematical operations can be implemented as an accurate, cost-effective, rights-qualified *composable metaprotocol* across multiple independent vendors, and how often it adds value over the strongest existing control. That is what [05](./05_INDEPENDENT_VALIDATION_PROTOCOL.md) is designed to try to refute.