# Open-World Agent Encounters: A Uniform Decision Frontier

**Mathematical mini-paper · Structural Awareness Programme · v0.2 · 27 October 2026 (finite resources and verifier chains)**  
**Logical subject:** SA-MATH-OW-01 · **Role:** standalone working mathematical contribution, for author and external mathematical review  
**Lineage:** Iván Abril Palma, *Practical Incompleteness* (L1 / R07), *Given Universe*, and the present Ecosystem Awareness foundational work. This exposition was prepared with AI assistance at the author's request.  
**Maturity:** conditional formal results using standard computability and observation-equivalence arguments; **not** a new proof of the halting theorem, an empirical finding about all smart cities, or an accepted architecture/standard.  
**Reading boundary:** the strong theorem concerns **uniform substantive determination**; the new results concern finite resource/evidence envelopes and computable verifier chains. None denies the ability to send a message, decline a connection, impose a deadline, return UNKNOWN or certify a restricted class. A timeout or malformed packet is **not by itself** a Turing-undecidable input. The [canonical A/B/C/D semantics](../ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md#abcd-canonical) are unchanged.

## Abstract

A robot or software agent in an open smart city can discover peers, perform a terminating yes/no handshake and then execute further decision procedures. Does this make every possible peer interaction decidable? No, provided the admissible world is computationally expressive enough and the question concerns nontrivial **future semantic behaviour**, not merely receipt of a handshake acknowledgement. We construct a fixed, effectively describable family of peer agents, all of which pass the same handshake, such that a sound and complete, terminating procedure deciding whether each peer will eventually fulfil a particular request would decide the diagonal halting problem. No such uniform procedure exists. A second, observation-relative lemma explains why a finite interaction prefix cannot certify eventual non-response without further valid bounds or evidence. The result recovers the operational frontier sought by *Practical Incompleteness* without treating finite strings as a proper class, without asserting that every fixed peer is individually undecidable, and without presuming an exhaustive “Given Universe.” A weaker finite-resource argument shows how deadlines and irrecoverable loss of evidence can cause **situated indeterminacy**, without absolute undecidability. Any finite or effectively orchestrated chain of computable handshake filters is itself a computable composite procedure: it can increase justified coverage without becoming a universal semantic decider. The separate *Projection Mechanism* raises a further question about the semantic constitution of the receiving universe; that stronger question is not inferred merely from timeout or filter incompleteness.

## 1. The problem: a protocol is not an omniscient decision procedure

Consider a mobile agent encountering other agents in a city or connected world. It may execute a sequence:

1. discover a peer and obtain an address or advertised interface;
2. exchange a **handshake** (a peer can reply YES or NO);
3. bind the intended question, permissions and interaction context;
4. request a service or a substantive commitment;
5. attempt to decide whether the required outcome will occur;
6. continue, decline, bound the attempt, or report an unresolved result.

The entire sequence, not only the handshake, is the relevant procedure. A handshake can be universally terminating while the subsequently queried property remains undetermined. “The peer answered YES to HELLO” and “the peer will eventually fulfil request r” are different propositions. Likewise, “I decline this interaction” is a local **admission decision**, not a proof that the peer could not fulfil it.

The older *Given Universe* difficulty appears when an internally declared decision universe is treated as if it covered every relevant future encounter. An open ecosystem does not provide a general trusted **last peer** or a universally exhaustive catalogue of future participant behaviour. Nevertheless, one can formulate precise theorems about its admissible agent class without claiming that any actual city contains literally infinitely many simultaneous agents.

## 2. Formal objects and the meaning of “sufficiently large”

Let **A** be a querying agent and **Π** its effective interaction-and-decision procedure. The procedure may use finite or unbounded computable local calculation, inspect available peer descriptions, carry out handshakes and query admitted peers. Assume no noncomputable oracle is silently supplied.

Let **K** be the **class of admissible peer descriptions**. “Sufficiently large” in this mini-paper means **computationally expressive**, not merely numerous:

**Expressivity hypothesis (H-EXP).** For every index e of a Turing program U_e, a computable compiler can describe an admissible peer P_e that (i) replies to HELLO with the same finite positive handshake transcript and (ii) on receiving a specified request r, simulates U_e(e), emitting a distinguished valid completion receipt exactly if that computation halts.

This is a condition on potential participants and discoverable interfaces, not a claim that all physically deployed peers meet it. It holds for an unrestricted class of suitably programmable agents; it need not hold for a finite, certified allowlist of bounded finite-state devices.

Define the substantive target proposition:

\[
T(P,r)=1 \quad\Longleftrightarrow\quad
P\text{ eventually emits a valid completion receipt for }r.
\]

This is **eventual completion**, not “receipt before an imposed deadline” and not the safety of accepting an interaction. The latter are different questions and may have different decision procedures.

We distinguish three properties of a procedure **Π**:

- **Totality:** Π returns after finite time for every admissible peer.
- **Soundness:** every definitive YES or NO is correct for the declared proposition T.
- **Completeness:** Π returns a definitive YES or NO for every admissible peer, rather than an unresolved result.

The operational result alphabet may include **YES, NO, UNKNOWN**. UNKNOWN is a legitimate reported result, not a third truth value of T. Classical computability here permits execution with **no uniform prior upper time bound**, although every halting run still uses finite time and computation; it does **not** postulate a physically infinite computer. The practical results below impose explicit finite budgets.

## 3. Theorem OW-1 — no uniform infallible interaction decider

**Theorem (uniform substantive decision frontier).** Under H-EXP, no effective procedure Π, including any computable handshake and subsequent subroutines, can be simultaneously **total, sound and complete** for T over all peers in K.

**Proof.** Fix an effective numbering U_0,U_1,... of Turing programs. For an arbitrary index e, use the compiler guaranteed by H-EXP to construct P_e. By construction, the peer gives the same affirmative handshake for every e. After request r it sends a valid completion receipt exactly when U_e(e) halts. Thus

\[
T(P_e,r)=1 \;\Longleftrightarrow\; U_e(e)\downarrow .
\tag{1}
\]

Suppose Π were effective, total, sound and complete. Given e, construct P_e and run Π against that described peer and its interaction interface. Read the definitive Boolean output. By (1) the output is YES exactly when U_e(e) halts. This yields an effective total decider for

\[
K_0=\{e\in\mathbb N:U_e(e)\downarrow\},
\]

contradicting the standard diagonal halting theorem. Therefore Π cannot possess all three properties. \(\square\)

**Scope of the theorem.** The reduction is **uniform across effectively described peers**. It does not claim that a particular fixed P_e has a nonrecursive completion predicate, nor that each encountered agent exhibits undecidability as an intrinsic property. The obstruction concerns a single universal procedure expected to produce the correct substantive binary answer across an expressive open class.

**Corollary OW-1a (unavoidable unresolved cases under soundness).** Any **total, sound** effective procedure with output alphabet {YES, NO, UNKNOWN} must return UNKNOWN for at least one P_e. If a sound procedure is restricted to definitive YES/NO outputs and is allowed not to halt, it must fail to terminate on at least one P_e. A total procedure compelled to answer only YES/NO must make an error on at least one P_e. The alternatives depend on the stated output and termination contract.

This is an existence result within the already-declared admissible agent class. It does **not** require repeatedly extending the universe until the argument works.

## 4. Lemma OW-2 — a finite handshake/transcript cannot certify all future outcomes

A different, more elementary observation concerns a particular agent with only a **finite observed transcript**.

**Lemma (finite-prefix underdetermination).** Assume no trusted upper response-time bound, exhaustive terminal certificate, or other source-qualified evidence decides eventual response. For any finite interaction observation horizon h, there exist two admissible peer behaviours with the **same visible transcript through h** after the same successful handshake, but with different eventual completion values.

**Proof.** Let P^+_h send the completion receipt after h+1 observation steps, and let P^-_h never send it. Arrange both to produce the identical handshake and the identical absence of substantive replies during steps 1,...,h. Then their observed prefixes agree, while T(P^+_h,r)=1 and T(P^-_h,r)=0. No determinate function of that prefix alone can output the correct value of T in both cases. \(\square\)

This lemma is **observation-relative**: access to additional verified code facts, a correct termination proof, a binding timeout specification that changes the question, or a trusted completeness certificate may justify a local result. It is not a separate theorem of Turing undecidability.

## 4A. Resource-bounded determination: the weaker operational frontier (OW-3)

The preceding diagonal result concerns a **uniform effective algorithm**, without any fixed upper bound on the time a successful calculation may take. A physical agent works within a narrower envelope. Let

\[
\rho=(\tau,c,m,b,v,a)
\]

stand for a declared finite **wall-clock deadline**, computation, usable memory, communication, accessible verification evidence and legitimately available escalation/assistance. These are task-relative parameters, not universal physical constants. A field study must specify their concrete units and what the agent can actually see.

Write \(O_A^\rho(w,r)\) for the entire evidence legitimately accessible to the querying agent A, including handshake and subsequent subroutines, while it encounters request r in possible world w under resource envelope \(\rho\). Write \(q(w,r)\in\{0,1\}\) for the **substantive** answer: e.g., whether the peer will ever produce the required completion. A universally correct, definitive decision **from this evidence alone** would require a function \(d_\rho\) satisfying

\[
q(w,r)=d_\rho(O_A^\rho(w,r))
\quad\text{for every admissible }w.
\tag{3}
\]

An agent's justified decisive region is question-, time-, information-, access- and resource-relative. Its operationally unresolved residual need not be recursively undecidable, permanently nonterminating or equivalent to the present corpus's D category.

**Proposition OW-3 (bounded-resource witness).** For any finite \(\rho\), assume the admissible world permits both (i) a peer whose valid positive handshake is followed by completion **after** the last observation permitted by \(\rho\), and (ii) a peer that sends the **same evidence within \(\rho\)** but never completes. Assume further that no accessible trustworthy independent proof or response bound distinguishes those cases. Then no procedure using only \(O_A^\rho\) can be sound and definitive for **eventual completion** on both cases.

**Proof.** Select the admissible worlds \(w_+\) and \(w_-\) in the premise. By construction,

\[
O_A^\rho(w_+,r)=O_A^\rho(w_-,r),\qquad
q(w_+,r)=1,\quad q(w_-,r)=0.
\]

A function of equal observations gives equal answers, which cannot equal both substantive outcomes. The procedure must return an unresolved result on at least one case, acquire new qualified evidence outside the specified envelope, or make an error. \(\square\)

This is OW-2's observation argument **lifted to the complete bounded resource/evidence envelope**, not a new diagonal theorem. It needs neither a universal machine nor an actually infinite set of deployed agents: even **finite-state delayed-response systems** can satisfy its premises. Thus it is a weaker, directly operational **existence claim**, subject to a genuinely unresolved pair of accessible states.

**Timeout is a fact about a clock, not about eternity.** A timeout proves no valid completion was observed **by \(\tau\)**. It does not prove that the peer can never complete. Likewise, a computation quota, exhausted battery or unavailable human can block justified determination if the task depends on it. One may legitimately respond TIMEOUT, DENY or UNKNOWN and terminate. This is **bounded local handling**, not a definitive answer to the unchanged eventual-outcome question.

If the contract instead asks “did the peer complete by \(\tau\)?” and observation and timing are reliable, that **new bounded proposition** is decidable by the clock and validated receipts. Restricted solvability is a useful achievement; it is not a proof of universal semantic coverage of future encounters.

## 4B. Damaged files, malformed frames and lost distinctions (OW-4)

Open-world interaction includes irrecoverable or temporarily inaccessible evidence: truncated files, undecodable formats, missing authority fields, inconsistent source statements and broken communication channels. These events do **not** all mean the same thing:

- A total parser may conclusively reject malformed syntax or a failed checksum. Local protocol validity is **decided**, not mathematically undecidable.
- The underlying **semantic question** may remain indeterminate when the damaged frame lost its decisive information and no qualified recovery path is currently available.
- Conflicting reports require source and authority qualification; their coexistence alone is not permission to invent a single true answer.

**Proposition OW-4 (lossy evidence cannot decide a changed target).** Let \(s\) range over admissible upstream semantic states, \(g_\rho(s)\) be the representation accessible to the receiver **after every available repair/check under \(\rho\)**, and \(q(s)\) the substantive target. Suppose:

\[
\exists s_0,s_1:\quad
g_\rho(s_0)=g_\rho(s_1)
\quad\land\quad
q(s_0)\ne q(s_1).
\tag{4}
\]

Then no sound definitive receiver function depending **only on \(g_\rho\)** can determine q on both cases.

**Proof.** If \(q=d\circ g_\rho\), equal representations would imply equal values of q, contradicting (4). \(\square\)

**Example.** Two genuinely different permissions are encoded in records that differ only in a decisive authorization field. Both incoming records are truncated **before** that field, and the receiver has no independent authenticated copy within \(\rho\). It can decide BAD_FRAME and reject the damaged message; it **cannot** decide whether the underlying permission existed using the damaged bytes alone. An authenticated retransmission, redundancy, independent authority source or verified reconstruction can settle the question. OW-4 applies only while those options do **not** remove the ambiguity.

A corrupt file is therefore **not automatically an undecidable object**. It can be a perfectly decidable corrupt frame containing **insufficient evidence for another decision**.

## 4C. Oracle chains are still one handshake-and-decision procedure (OW-5)

Suppose A is given a preflight verifier \(F_1\) to filter its peer encounters. Add \(F_2\) to verify \(F_1\), then \(F_3\), identity checks, signed protocol tests, policy engines, static analyzers, remote specialist agents and any later subroutines. The resulting interaction process is

\[
\Pi_n=\operatorname{Compose}(A,F_1,\ldots,F_n),
\qquad n<\infty,
\tag{5}
\]

where \(\operatorname{Compose}\) means the **whole operational scheduler**, including messages and handoffs, not an assertion that each component is total or that validation is a simple mathematical function composition.

**Proposition OW-5 (computable-composition frontier).** Assume \(n\) is finite, the scheduler and every \(F_j\) are effective, peer interactions admit effective simulation from their descriptions, and no component receives a genuine noncomputable oracle. Then \(\Pi_n\) is itself an effective, possibly partial procedure. Under H-EXP, it cannot be simultaneously **total, sound and complete** for T over all admissible peers K.

**Proof.** An ordinary universal program can simulate the scheduler, each effective verifier, the querying agent and the described peer exchanges. This simulation reproduces the composite's externally relevant verdict behaviour. If \(\Pi_n\) always terminated with an infallible definitive YES/NO on K, its simulator would be the forbidden OW-1 decider. \(\square\)

The same argument covers a **uniform adaptive** chain whose next step is selected effectively and whose final claimed answer is reached after finitely many effective steps on each input. An infinite serial stack has no completed verdict merely by being called “infinite”; it needs a separately defined finite-time aggregation rule. The claim concerns **any chosen finite length**, not the stronger and generally false assertion that one common input necessarily defeats **each component separately**.

**Corollary OW-5a — filtering does not imply complete semantic separation.** A computable filter can admit a **restricted certified peer class**, return NO to a **local admission-policy** question, or conservatively refuse/return UNKNOWN. Such policies can prevent some failures and sharply enlarge justified coverage. But refusing a peer or timing out does **not** decide its eventual behaviour; filtering everything out yields a terminating refusal policy, **not** a universal T-decider.

In this setting, adding a verifier changes the **composite handshake plus subsequent decision procedure**. It may be valuable; it cannot be promoted to an infallible semantic solver for the same unrestricted expressive task. Extra checks also consume portions of \(\rho\); whether that cost helps or harms a particular deployment is a **measured** question, not a monotonic mathematical law.

**Two meanings of “oracle.”** A software checker, specialist peer, policy service or audit node is an **effective verifier** and is covered by OW-5. A genuine **noncomputable halting oracle** is not: it can decide ordinary halting questions beyond ordinary algorithms, so the theorem's premise would change. Oracle-relative computations have further undecidability results about their **own higher-level** problems, but they are not proof that an ordinary software verification chain accesses supernatural computation.


**Supplementary theorem OW-5b — a perfect general semantic meta-filter is not computable.** Filtering for a narrowly certified protocol is possible; **uniformly classifying arbitrary programmable peers by whether their complete request-response domain is itself decidable** is a different and generally undecidable meta-question. This result requires a **multi-request expressivity hypothesis (H-REQ)**: the admissible peer class contains the effectively compiled family of peers (G_e) defined below. H-EXP alone, which addresses **one fixed request**, does not automatically imply H-REQ. An explicit construction, corresponding to the existing R07-P2 research development, establishes the distinction.

Let \(K_0=\{y:U_y(y)\downarrow\}\). From any program index e, effectively construct a peer \(G_e\), with the same simple successful HELLO exchange in every case, and define its response behaviour to requests:

\[
G_e(x)=
\begin{cases}
\text{send completion}, & x\in 00\Sigma^*,\\
\text{never complete}, & x\in 01\Sigma^*,\\
\text{simulate }U_e(e)\text{, then }U_y(y)
   \text{ and complete iff both halt}, & x=1y.
\end{cases}
\tag{6}
\]

The **request language of successful completion** of this peer is

\[
D_{G_e}=
\begin{cases}
00\Sigma^*, & U_e(e)\uparrow,\\
00\Sigma^*\cup 1K_0, & U_e(e)\downarrow .
\end{cases}
\tag{7}
\]

In the first case \(D_{G_e}\) is decidable; in the second it is undecidable by the many-one reduction \(y\mapsto1y\) from \(K_0\). Any total computable meta-filter that, for every e, correctly announces whether the **whole** request-response domain of \(G_e\) is decidable would thereby decide whether \(U_e(e)\) halts. Contradiction. \(\square\)

This is a **uniform index-level statement under H-REQ** about the property of a program's *complete response language*, not a claim that the outcome for **each fixed request of each peer** is intrinsically unanswerable. Its mathematical antecedent is the R07-P2 index-family construction, ultimately within standard Rice/halting theory. It does not forbid practical admission checks for verified restricted classes; it refutes their unjustified promotion to a perfectly general semantic separator.

## 4D. Operational encounters and testable interpretation

| Encounter after discovery | Legitimate bounded outcome | Incorrect inference to avoid |
| --- | --- | --- |
| HELLO accepted, requested result arrives with valid evidence | Qualified local result under the declared target | All future peer behaviour is settled |
| HELLO accepted, no qualifying answer by \(\tau\) | TIMEOUT; substantive eventual outcome may remain UNKNOWN | It can never answer |
| File corrupted beyond admissible recovery | BAD_FRAME; source meaning remains unresolved if (4) holds | The sender's underlying permission is necessarily false |
| Protocol version incompatible | Incompatible for the negotiated interface | No other interface or relationship is possible |
| Peer verified but receiving task needs independent authority | Await/deny/requalify under the receiving contract | A handshake or a sender's success automatically creates permission |
| Several computable preflight checkers pass | The declared preflight predicates are supported | The full semantic target is universally decided |

A finite fixture may test both delayed-vs-never traces at fixed observation budget, damage a decisive field, restore it through an authorized source, and compare a plain handshake with a longer checker chain under the **same** \(\rho\). The observable quantities are justified definitive answers, safe UNKNOWN, incorrect false closure, response latency, verification/communication cost and legitimacy of continuation—not a physically observed diagonal theorem.

**Limits of existence versus frequency.** OW-3/OW-4 supply **conditional witnesses**, not a measured frequency of timeouts or damaged files in a particular city. A claim that a wandering robot **will actually encounter** one requires additional coverage, availability, reachability or probability assumptions about real interactions. Mere geographical movement and number of peers prove no encounter probability. This distinction preserves the engineering motivation without substituting anecdote for a quantified theorem.

## 5. The agent's actual procedure: what has, and has not, been decided

The proof does **not** prohibit a sensible interaction discipline. It distinguishes the propositions that a discipline answers.

| Observed or produced result | What it establishes | What it does not establish |
| --- | --- | --- |
| HELLO → YES | Handshake accepted under a declared envelope | Eventual fulfilment, global compatibility or safety |
| HELLO → NO | Contact declined under that envelope | Mathematical impossibility of every other interaction |
| Valid signed completion receipt | The specified observed completion occurred, subject to verification | Reliability in all future contexts |
| Timeout at h | No qualifying receipt was observed by h | That a later receipt is impossible (OW-3) |
| Corrupted input / BAD_FRAME | The parser or integrity check rejected the presented record | The underlying semantic target was false or intrinsically undecidable (OW-4) |
| UNKNOWN / deferred / insufficient evidence | Current procedure does not justify a substantive binary answer | That the peer is malicious, incoherent or intrinsically undecidable |
| Local admission DENY | The receiver will not proceed under its current rules | That the peer lacks the ability to fulfil r |

A protocol can decide **whether to attempt interaction under current policy** with finite YES/NO outputs. It cannot thereby acquire a sound, complete decider for **every nontrivial semantic question about all admissible programs**. Changing the question to “did the handshake finish within h?” makes that bounded question decidable, but does not solve the eventual-completion question defined above.

## 6. Open-world encounter versus an artificially closed Given Universe

The relevant quantifiers are

\[
\forall\Pi\in\mathsf{EffectiveDeciders}\;\exists P\in K:
\Pi\text{ fails to give a terminating correct definitive answer to }T(P,r),
\tag{2}
\]

where failure means **an error**, **nontermination**, or **UNKNOWN**, depending on the permitted output contract.

Equation (2) is **not**

\[
\forall P\in K,\;T(P,r)\text{ is undecidable for that fixed peer},
\]

and it is not a probabilistic claim that a particular robot will encounter such a peer tomorrow.

If an exploration policy is **fair and exhaustive with respect to the described family** P_e and evaluates the same substantive question for each member, the existence witness in (2) must eventually be included among its encounters. Under those additional reachability and execution assumptions, a sound finite-return procedure must eventually report an unresolved case; a procedure forced to answer binary must fail correctness somewhere. **Fair exhaustive contact is a hypothesis, not a consequence of mere geographical movement.**

Conversely, a truly closed, finite, correctly inventoried peer set with certified bounded protocols may support total local decisions. This does not invalidate OW-1: that set does not satisfy H-EXP. An arbitrary numerical threshold such as “more than N agents” does **not** suffice. The mathematically relevant meaning of an open smart world is **unbounded admission of sufficiently expressive possible peer behaviours**, without a trustworthy global closure certificate.

The result is therefore useful **without asserting that every possible universe extension creates an undecidable residual**. The obstruction arises in the specified open class and the demanded universal decision task. The **finite-resource** results OW-3/OW-4 additionally show situated indeterminacy in admissible indistinguishable cases even without that unrestricted Turing expressivity; those are distinct premises and a distinct conclusion.

## 7. Relation to L1 and to the current Structural Awareness corpus

**L1 (*Practical Incompleteness*).** The historical source asks where a concrete procedure's effective resolution domain ends. The present theorem preserves the **procedure-relative frontier** and the existential logic, now for a querying agent, its handshake and all subsequent decision subroutines. Its proof deliberately uses a valid diagonal reduction: it does **not** reuse the historical assertion that finite binary strings form a proper class, nor infer an undecidable fixed halting domain merely from a machine being partial. The existing [R07 mathematical review](https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R07_PRACTICAL_INCOMPLETENESS_v0.1.md) already develops the uniform/nonuniform distinction. OW-1 applies that sound distinction to an explicit peer-interaction semantics; neither claim is presented as a novel computability impossibility.

**Given Universe and Ecosystem Awareness.** The current [Foundational Theory v0.5](../ecosystem-awareness/baseline/01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md) distinguishes an open class of potentially relevant states Ω, a bounded represented operational universe U, and an open residual R_U **that is not an exhaustively enumerable set complement**. OW-1 is narrower: it constructs an effective peer family K and a precise undecidable **uniform target property** T. It does not replace Ω, U, R_U or prove an all-purpose theorem about physical reality.

**A/B/C/D.** The [canonical 00M v0.8](../ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md#abcd-canonical) makes A/B/C/D **process-, question-, scope-, capability- and time-relative roles**, not mutually exclusive sets or a total partition:

- **A:** the result actually delivered; it may be a legitimate UNKNOWN or a bounded DENY.
- **B:** the established basis, limits and characterized, assessable reserve (e.g., a verified bound or known verification route).
- **C:** a grounded but uncharacterized exploration avenue.
- **D:** potentially material effects beyond this process's effective evaluation route under current conditions.

OW-1 justifies why **the overall decisive YES/NO function cannot be assumed universally complete** under H-EXP. It does not decree that every timeout belongs in D, that every unspecified peer is C, or that the entire set of hard programs can be enumerated as a populated A/B/C/D record. A missing basis for assigning any role remains **UNKNOWN** rather than a fabricated D classification.

The [current signalling annex 01J](../ecosystem-awareness/baseline/01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md) independently distinguishes discovery/handshake, bounded semantic coupling, receiver qualification and subsequent interaction. This mini-paper establishes a mathematical **limit**, not a mandatory handshake format, shared trust root, agent-citizenship protocol, security policy, MSCA change or new architecture component.


### 7.1 Relation to the projection articles: separate, stronger question

The original 2025 [*Projection Mechanism*](https://www.researchgate.net/publication/393802750_The_Projection_Mechanism_How_Practical_Incompleteness_Infiltrates_Formal_Systems) combined a practical incompleteness/validator-chain claim (§2) and a meta-discriminator hierarchy (§3) with a further **projection** proposal, defined via ZFC Separation (§5), and an identity/bijection between already defined residual collections (§6). The source's strong claims that every gateway computationally dominates downstream components or that an arbitrary countable chain shares one individually unresolved input do **not** follow without stronger assumptions; the specific source-level conditions and counterexamples are recorded in the separate [R08 research dossier](https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R08_PROJECTION_MECHANISM_2025_v0.1.md). OW-5 establishes the **weaker and valid composite-procedure result** instead; it does not borrow those stronger claims.

The author's [fourth revision of *The Projection Mechanism*](https://drive.google.com/file/d/1OrJ2LWz2qBv2sP8_-VNldWpctxZdwcfI/view), particularly §§5–6, distinguishes an **in-frame incompleteness item** missed by a filter from a **projected item** whose semantic placement was not justified when forming the receiving working universe. It also explicitly withdraws blanket claims about all open-world inputs being Turing-complete, and treats any net growth of projected residue as conditional on defined arrival/removal rates (§9). The distinct [*Projected Infinite Paradox*](https://www.researchgate.net/publication/393884759_The_Projected_Infinite_Paradox_Unifying_Constructivism_and_Platonism) examines changing constructive stages/populations and claimed semantic consequences of projection; it is **not** a statement about one late handshake or damaged file. Its editions require separate proof/quantifier control.

**Formal boundary in this paper:** OW-1/OW-3/OW-5 show that one agent's complete interaction procedure need not settle a substantive question; **that alone does not establish projection**. OW-4 identifies an independently checkable **source-to-receiver information-sufficiency obstruction** that may help develop projection claims, but only after the upstream and receiving semantic questions, data mappings, admissible witnesses and authority conditions are specified. Repeating more filters on the **same insufficient representation** cannot recover a distinction erased from every accessible input; an independent qualified source or a repaired representation may.

We therefore record projection as **a distinct next research stage**, not a corollary of a timeout, a corrupt frame, or OW-5. This mini-paper does not establish inevitable misclassification, unconditional accumulation, physical entropy, universal semantic corruption or superiority of a particular architectural response.

## 8. What would count against the applied claim?

The mathematical proof is conditional and can be checked by inspecting the effective compilation e↦P_e and the equivalence (1). Its application to a real smart-city profile must separately establish that the actual admissible agent class can express this construction **and** that the declared substantive decision has the required semantics.

A bounded profile that (i) admits only certified finite-state peers, (ii) imposes a verified maximum completion time as part of its substantive contract, or (iii) restricts the target to finite observable traces, can be legitimately decidable. Authorized independent certificates may also distinguish OW-3's alternatives or repair OW-4's lost decisive fields. That is not a paradox or a counterexample to OW-1; it is a **different hypothesis or decision task**. If the target's claimed semantic strength or H-EXP does not hold, the theorem may not be applied.

Empirical research can then examine rates of clean completion, justified NO, bounded UNKNOWN, damaged-source recovery, false certainty, indefinite waiting, added verifier-chain cost and useful requalification. Such measurements test **operational handling**, not the diagonal theorem. No superiority of Structural/Ecosystem Awareness over conventional tools follows from OW-1.

## 9. Conclusion

A universally terminating handshake does not imply a universally terminating **correct semantic decision** about every possible peer. In a computationally expressive open agent class, a single effective procedure cannot always return an infallible substantive YES/NO after discovery, handshake and any computable sequence of subsequent subroutines. **Every finite effectively composed chain of software verifiers remains one such procedure.** Under weaker finite-resource premises, delayed responses and irrecoverable evidence loss can additionally make specific questions indeterminate relative to the agent's actual observations, despite decidable local protocol outcomes. A sound total procedure must leave some substantive questions unresolved in the expressive case; a forced total binary procedure must sometimes be wrong.

This is the precise existential contribution: **an agentic world need not be assumed exhaustively given for there to be a mathematically unavoidable frontier relative to the agent's uniform decision task**. It establishes the frontier before discussing how it should be represented, classified, projected or managed. An intentionally closed, certified interface or finite-deadline contract is useful and can legitimately decide its **declared limited task**, but cannot by that fact decide arbitrary future peer behaviour.

---

## Sources and review boundaries

1. Iván Abril Palma, *Practical Incompleteness: A Set-Theoretic Framework for Concrete Decision Procedures*, historical manuscript (L1). https://www.researchgate.net/publication/393799525_Practical_Incompleteness_A_Set-Theoretic_Framework_for_Concrete_Decision_Procedures
2. R07, *Practical Incompleteness: Fixed Halting Domains, Uniform Undecidability, Effective Scope and Source-Qualified Continuation* (internal source-specific mathematical review; access follows its existing repository permissions). https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R07_PRACTICAL_INCOMPLETENESS_v0.1.md
3. Structural Awareness, *Ecosystem Awareness — Integrated Foundational Theory v0.5*. https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md
4. Structural Awareness, *00M v0.8 — A/B/C/D Semantics and Mathematical Plausibility*. https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md
5. Structural Awareness, *01J — Ecosystem Signalling: Selective Disclosure and Choreographed Repositioning*. https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md
6. Iván Abril Palma, *The Projection Mechanism: How Practical Incompleteness Infiltrates Formal Systems*, original 2025 edition. https://www.researchgate.net/publication/393802750_The_Projection_Mechanism_How_Practical_Incompleteness_Infiltrates_Formal_Systems
7. Iván Abril Palma, *The Projection Mechanism*, distinct fourth revision, 2026. https://drive.google.com/file/d/1OrJ2LWz2qBv2sP8_-VNldWpctxZdwcfI/view
8. Iván Abril Palma, *The Projected Infinite Paradox: Unifying Constructivism and Platonism*, distinct original/later editions, 2025. https://www.researchgate.net/publication/393884759_The_Projected_Infinite_Paradox_Unifying_Constructivism_and_Platonism
9. R08 source-specific review and conditions. https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R08_PROJECTION_MECHANISM_2025_v0.1.md
10. R09 fourth-revision source-specific review. https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R09_PROJECTION_MECHANISM_V4_v0.1.md
11. R10 edition-controlled source-specific review. https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R10_PROJECTED_INFINITE_PARADOX_v0.1.md

**Change scope:** this is the additive **v0.2 revision of the existing mathematical mini-paper**, preserving its logical identity and public path. It does not edit, supersede or promote the historical sources L1, R07–R10, 00M, Foundational Theory, 01J or frozen architecture artifacts. OW-3/OW-4 are conditional finite-evidence propositions; OW-5/OW-5b apply established computability arguments. Formal machine verification and empirical deployment are not claimed.
