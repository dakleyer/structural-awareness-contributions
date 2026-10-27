# Open-World Agent Encounters: A Uniform Decision Frontier

**Mathematical mini-paper · Structural Awareness Programme · v0.4 · 27 October 2026 (non-closure under repeated execution; set-query sanity checks)**  
**Logical subject:** SA-MATH-OW-01 · **Role:** standalone working mathematical contribution, for author and external mathematical review  
**Stable-path notice:** the filename retains its original v0.1 suffix to preserve inbound references; the current **document edition is v0.4**, recorded in Git history. No second active edition or independent VNext is implied.  
**Lineage:** Iván Abril Palma, *Practical Incompleteness* (L1 / R07), *Given Universe*, and the present Ecosystem Awareness foundational work. This exposition was prepared with AI assistance at the author's request.  
**Maturity:** conditional formal results using standard computability and observation-equivalence arguments; **not** a new proof of the halting theorem, an empirical finding about all smart cities, or an accepted architecture/standard.  
**Reading boundary:** the strong theorem concerns **uniform substantive determination**; the new results concern finite resource/evidence envelopes and computable verifier chains. None denies the ability to send a message, decline a connection, impose a deadline, return UNKNOWN or certify a restricted class. A timeout or malformed packet is **not by itself** a Turing-undecidable input. The [canonical A/B/C/D semantics](../ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md#abcd-canonical) are unchanged.

## Abstract

A robot or software agent in an open smart city can discover peers, perform a terminating yes/no handshake and then execute further decision procedures. Does this make every possible peer interaction decidable? No, provided the admissible world is computationally expressive enough and the question concerns nontrivial **future semantic behaviour**, not merely receipt of a handshake acknowledgement. We construct a fixed, effectively describable family of peer agents, all of which pass the same handshake, such that a sound and complete, terminating procedure deciding whether each peer will eventually fulfil a particular request would decide the diagonal halting problem. No such uniform procedure exists. A second, observation-relative lemma explains why a finite interaction prefix cannot certify eventual non-response without further valid bounds or evidence. The result recovers the operational frontier sought by *Practical Incompleteness* without treating finite strings as a proper class, without asserting that every fixed peer is individually undecidable, and without presuming an exhaustive “Given Universe.” A weaker finite-resource argument shows how deadlines and irrecoverable loss of evidence can cause **situated indeterminacy**, without absolute undecidability. Any finite or effectively orchestrated chain of computable handshake filters is itself a computable composite procedure: it can increase justified coverage without becoming a universal semantic decider. An additional non-closure result distinguishes the classical mathematical existence of a semantic set from an effective exact membership test or a justified certificate of global exhaustiveness. A further extension distinguishes **a finite closed run result** from **a globally complete reusable procedure**, proves an eventual unresolved encounter under exhaustive repeated evaluation, and gives specific guards for some/all, fixed-time and nearest-neighbor queries. The separate *Projection Mechanism* raises a further question about the semantic constitution of the receiving universe; that stronger question does not follow merely from timeout, non-closure or filter incompleteness.

## 1. The problem: a protocol is not an omniscient decision procedure

Consider a mobile agent encountering other agents in a city or connected world. It may execute a sequence:

1. discover a peer and obtain an address or advertised interface;
2. exchange a **handshake** (a peer can reply YES or NO);
3. bind the intended question, permissions and interaction context;
4. request a service or a substantive commitment;
5. attempt to decide whether the required outcome will occur;
6. continue, decline, bound the attempt, or report an unresolved result.

The entire sequence, not only the handshake, is the relevant procedure. A handshake can be universally terminating while the subsequently queried property remains undetermined. “The peer answered YES to HELLO” and “the peer will eventually fulfil request r” are different propositions. Likewise, “I decline this interaction” is a local **admission decision**, not a proof that the peer could not fulfil it.

The older *Given Universe* difficulty appears when an internally declared decision universe is treated as if it covered every relevant future encounter. **Mathematically specifying a set of all desired peers does not supply an executable membership test or a certificate that discovery is complete.** Nor does success on one finite execution imply a universally complete future-query procedure. An open ecosystem does not provide a general trusted **last peer** or a universally exhaustive catalogue of future participant behaviour. Nevertheless, one can formulate precise theorems about its admissible agent class without claiming that any actual city contains literally infinitely many simultaneous agents.

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

### 6.1. Effective non-closure: what the concept means

The question is **not** whether classical mathematics can define a set. For the compiled peer family \(P_e\) under H-EXP, the two *semantic* sets

\[
Y_T=\{e\in\mathbb N:T(P_e,r)=1\},\qquad
N_T=\{e\in\mathbb N:T(P_e,r)=0\}
\tag{8}
\]

exist as complementary subsets of the index universe. **Global effective semantic closure** would require an executable, total, sound and complete YES/NO membership procedure for these sets, without silently changing the target \(T\). The existence of a set-theoretic description does **not** imply that such a procedure exists.

A crucial distinction is the set of cases for which the *chosen agent itself* actually emits a definitive verdict:

\[
S_\Pi=\{e:\Pi(P_e,r)\text{ terminates with YES or NO}\}.
\tag{9}
\]

This is **not** the same as either class in (8). If \(\Pi\) is computable, total and allowed to return YES/NO/UNKNOWN, then \(S_\Pi\) **is decidable** simply by executing \(\Pi\). A program that always answers UNKNOWN has \(S_\Pi=\varnothing\), a perfectly decidable set, without having solved the semantic question. If \(\Pi\) is partial, its definitive-response domain is recursively enumerable but need not be undecidable. Therefore this article **does not claim** that every agent's own output domain is intrinsically undecidable.

### 6.2. Theorem OW-6 — the semantic classes cannot be exactly closed by a program

**Theorem OW-6 (no global executable semantic partition).** Under H-EXP, no total computable classifier can decide exact membership in \(Y_T\) or \(N_T\) for every compiled peer. The positive class is recursively enumerable on this family; the negative class is not. Thus both semantic sets exist mathematically, but their exact, exhaustive two-sided classification **cannot be operationally computed**.

**Proof.** OW-1's construction gives:

\[
Y_T=\{e:U_e(e)\downarrow\}=K_0,\qquad
N_T=\mathbb N\setminus K_0.
\tag{10}
\]

The diagonal halting set \(K_0\) is recursively enumerable by simulation but not decidable. Were \(N_T\) also recursively enumerable, we could enumerate both classes in parallel and decide every index by waiting until it appeared in exactly one list. This would decide \(K_0\), a contradiction. A total exact membership test for either class would also decide its complement. \(\square\)

**Interpretation.** A process may enumerate witnessed successful responses. That is **not** a finite certificate that the entire universe has been classified, nor a general procedure for certifying every negative case. A bounded certified subset may be fully decidable; the theorem prohibits promoting that local classification into exact coverage of the original expressive class.

**Corollary OW-6a (meta-description is not runtime closure).** Defining “the set of all peers whose future behaviour has property \(T\)” is a legitimate mathematical construction. It is **not** a computable program that can recognize all members, correctly eliminate all nonmembers, and certify the absence of an unresolved residue. Any requirement that an operative agent **close that whole set** must supply an effective decision/coverage method. The original set definition is insufficient.

**Corollary OW-6b (unavoidable bounded unresolved result under soundness).** A sound, total, computable YES/NO/UNKNOWN procedure for \(T\) must return UNKNOWN on at least one compiled peer; a sound binary procedure allowed to diverge must leave some case without a terminating verdict; a total forced-binary procedure must err somewhere. This is a **logical statement about task contracts**. It predicts neither a literal software crash nor a particular deployment frequency. A watchdog can turn a long run into TIMEOUT, which still does not prove negative eventual completion.

**Separate meta-property:** classifying whether a peer's *entire request-response language* is decidable requires the extra multi-request expressivity H-REQ of OW-5b. Classifying a total agent's *own* YES/NO/UNKNOWN outputs can be easy. These are not interchangeable claims.

### 6.3. Lemma OW-7 — no globally exhaustive inventory from an open prefix

There is a separate *discovery* boundary. Let \(h\) be a finite history of peer discovery, handshakes and verifications, and \(S(h)\) the finite recognized population. Assume an **open-prefix condition (H-OPEN)**: in the absence of a trustworthy upper bound or authenticated terminal certificate, there are two admissible worlds yielding **the same history \(h\)**, one containing exactly \(S(h)\), the other containing \(S(h)\) plus a relevant but still undiscovered peer \(p_\star\).

**Lemma OW-7 (finite-prefix inventory non-closure).** Under H-OPEN, no sound function of \(h\) alone can definitively certify that every relevant peer has been discovered in both worlds.

**Proof.** The history is identical, but the proposition “\(S(h)\) is exhaustive” is true in one world and false in the other. Any function of the same history produces the same answer in both, so its definitive global closure certification cannot be correct in both. \(\square\)

This lemma is **observational**, not a second Turing theorem. An independently justified, finite inventory bound or authentic complete-scan certificate can permit **local closure within that specific domain and time**. Without one, “all encountered so far” is warranted; “all that exist or may become relevant” is not.

### 6.4. Corollary OW-8 — a closure agent is itself part of the procedure

Suppose another agent \(G\) is ordered to classify all peers first, allowing A to interact only with those deemed resolvable. If \(G\), A and their scheduler are computable, **the composite remains one effective procedure** (OW-5). If the composite is required to solve the **unchanged substantive YES/NO target** correctly for every peer in the expressive class, OW-1/OW-6 forbid it. If \(G\) claims to identify perfectly, from arbitrary peer code, whether that peer's **entire request domain** is decidable, OW-5b applies under H-REQ.

A conservative \(G\) may instead produce a **safe, restricted allowlist** that A can handle; it may reject all untrusted peers by policy or report UNKNOWN. Such a finite or decidable whitelist is legitimate. What cannot be inferred is that this restricted set **exhausts all agents which could in principle be handled** or that rejected agents have been semantically disproved. Moving an unsupported global “all peers such that ...” demand into a stronger handshake does not manufacture the absent evidence.

### 6.5. NC-1 — an open-world operational sanity condition

**Proposed design consequence, not an adopted system requirement:** an agent working against an open ecosystem should **not** be instructed to return a globally exhaustive **“ALL agents satisfying \(P\)”**, **“no other relevant agent exists”**, or **“the entire ecosystem has been closed”** result unless it possesses a **valid closure contract**: declared question, peer population/scope, snapshot or validity interval, observation/compute budget, credible source/authority and an effective completeness witness.

The working discipline is **open-by-default, closed-by-evidence**. It does not prohibit universal quantifiers in mathematics or correctly closed, certified **local** workloads. Two valid instructions are “find all qualifying peers in this certified finite registry at time \(t\)” and “return the qualifying peers found so far, with incomplete/OPEN coverage”. What is unsound is treating the latter as the former without proof.

The output contract must keep distinct **YES/NO** for supported substance, **UNKNOWN/INDETERMINATE** for unresolved semantics, **TIMEOUT** for a deadline, **BAD_FRAME** for invalid bytes, **DENY/OUT_OF_SCOPE** for local admission, and **OPEN/NOT_CERTIFIED_CLOSED** for uncertified population coverage. These refer to different propositions. A malformed file can be correctly rejected while its lost authorization field remains semantically unresolved. An UNKNOWN is **not** a proof of intrinsic Turing undecidability or automatically an item in canonical epistemic D.

**Failure signatures depend on the specified task.** Under the full H-EXP semantic contract, a forced total binary classifier must **make an error on some input**; a partial one may hang; a sound total three-valued classifier must abstain sometimes. Under bounded resources, timeout or explicit insufficiency may occur. A literal runtime exception is possible in practice but **is not mathematically forced**.

### 6.6. Concrete smart-city interpretation and limitations

A roaming robot successfully handshakes with twenty service agents and verifies their twenty specific results. It can report **twenty locally complete checked interactions**, but not a complete city-wide population. A newly encountered agent then answers HELLO=YES, supplies a corrupted authorization record and misses the service deadline. The robot may correctly state **HELLO accepted**, **BAD_FRAME**, **TIMEOUT by \(\tau\)**; without independent qualified evidence it cannot infer the missing permission or eventual completion. A second software validator inspecting the *same damaged record* cannot restore information absent from that record alone. It may, however, obtain a different verified source or repair the transmission. A defensible report is **twenty local successes, one substantive UNKNOWN, global inventory OPEN**.

The results concern **effective epistemic and operational non-closure**, not topology or an impossibility of defining mathematical sets. H-EXP is an expressivity premise and H-OPEN an observational possible-world premise; neither follows from merely counting physical devices. Neither theorem guarantees that a robot follows a route that actually encounters the witness. These results are **prior to** and independent of the stronger proposed *Projection Mechanism*, and do not silently modify current A/B/C/D semantics.

### 6.7. Closed finite run results versus an open reusable procedure

Three objects must remain distinct: a finite **run record** \(L_r\) of actual peer encounters; a finite **confirmed-result set** \(M_r\) supported by evidence obtained in that run; and the **general procedure** \(\mathcal Q\) intended to return correct answers across future possible encounters.

For the finite processed and observed candidate population \(E_r\), an appropriately bounded three-way classifier can record

\[
E_r=M_r\;\dot\cup\;F_r\;\dot\cup\;I_r,
\tag{11}
\]

where \(M_r\) contains witnessed matching cases, \(F_r\) witnessed nonmatching cases, and \(I_r\) **observed but substantively indeterminate** cases. A timeout or corrupted message is a separately recorded diagnostic, **not a proof** of nonmembership. This is only a partition of the **observed processed log**, not a global partition of the ecosystem.

The finite set \(M_r\) may be perfectly determined, contain **no** indeterminate elements, and be legitimate as an exact set of witnessed positive results from that run. Nevertheless, a result contract must separately say whether there are unresolved *observed* candidates and whether the broader *population coverage* remains OPEN. A clean finite collection is not an assertion that there are no outside or undecided cases.

Therefore the literal claim **“every set contains indeterminate elements” is false**: a certified finite list, a trivial total predicate and the empty set are counterexamples. The correct programming statement is that a **reusable, universally sound and complete** semantic set-query over the expressive H-EXP class cannot silently produce globally definitive results for **every possible input**. The result **type and procedure contract** must accommodate an indeterminate or open-coverage outcome, even if a given run contains none.

### 6.8. Theorem OW-9 — eventual INDETERMINATE under exhaustive repeated execution

The stronger claim “after sufficiently many executions, an indeterminate necessarily appears” needs an **encounter completeness** hypothesis; OW-1 alone does not give that recurrence.

Let \(C\) be a **total computable and sound** evaluator of the fixed semantic target \(T(P_e,r)\) over H-EXP peers, returning YES, NO, or INDETERMINATE. Let \(e_0,e_1,\ldots\) be an **effectively generated exhaustive traversal** of the indices of that family, meaning each natural index appears at some finite position. Every evaluation terminates.

**Theorem OW-9 (existential finite encounter position).** Under those conditions,

\[
\exists k<\infty:\quad C(P_{e_k},r)=\mathrm{INDETERMINATE}.
\tag{12}
\]

**Proof.** OW-1a implies at least one index \(e^\star\) where the total sound evaluator cannot return a justified definitive YES/NO. By exhaustive traversal, \(e^\star=e_k\) for some finite \(k\). Therefore the \(k\)-th execution returns INDETERMINATE. \(\square\)

The correct quantifier pattern is **for each evaluator and each exhaustive traversal, there exists some finite encounter index**. There is **no uniform finite number of runs** that follows for every evaluator and every possible encounter schedule. Repeating one easy interaction, following an unrepresentative route or staying inside a certified finite whitelist need never reach the constructed witness. Without totality, a sound binary procedure may hang instead of returning INDETERMINATE; a forced-total binary semantic procedure may be wrong instead of admitting uncertainty.

This is a conditional consequence of standard diagonalization, **not** a theorem that every fixed peer or every actual street encounter contains an indeterminate element.

### 6.9. OW-9b — optional probability statement, never a substitute for proof

If a stochastic encounter process **independently justifies** a lower bound \(p>0\) on the conditional probability that the next evaluation is indeterminate **given that none has occurred so far**, then

\[
\Pr(\text{no INDETERMINATE in }n\text{ runs})
\le (1-p)^n,
\quad
\Pr(\exists j\le n:I_j)\ge 1-(1-p)^n.
\tag{13}
\]

The multiplication rule proves this without independence, provided the conditional lower bound genuinely holds for every relevant history. The likelihood approaches one as \(n\to\infty\), but **no fixed finite n is guaranteed** when \(p<1\). Neither L1 nor the number of devices in a smart city provides such a \(p\); it must come from a declared population, encounter policy and measured or justified assumptions.

### 6.10. Theorem OW-10 — 17 seconds bounds a run, not its semantic universe

“Find all P-matching agents **in 17 seconds**” combines two distinct possible completeness claims: **coverage** of the relevant population and **determination** of predicate \(P\) for each relevant candidate. A 17-second deadline alone proves neither.

For the finite log \(E_{17}\), the witnessed set \(M_{17}\), witnessed negatives \(F_{17}\) and observed unresolved cases \(I_{17}\) may be reported precisely, subject to the evidence/measurement contract. But

\[
M_{17}=\{x\in\Omega_{\mathrm{relevant}}:P(x)\}
\tag{14}
\]

is an **additional global assertion** requiring a qualifying coverage/exclusion witness and enough sound semantic information. Even with all observed candidates classified, an unseen possible match invalidates the equality. Even with a certified complete finite population, an observed indeterminate predicate may invalidate it.

**Proposition OW-10 (two-axis set non-closure).** If two admissible worlds yield identical available run evidence but differ either (i) by a relevant undiscovered matching agent or (ii) by the truth of \(P\) for a relevant observed indeterminate agent, then no function of that run evidence can certify an **exact global matching set** correctly in both worlds.

**Proof.** The observation is the same, forcing the same reported set, while the true target set differs. \(\square\)

A certified finite and fully covered candidate population together with a justified membership decision for every relevant candidate is a **sufficient** closure condition; another valid certificate may establish that all unobserved candidates are nonmatches. The sufficient form is not claimed to be the **only** possible legitimate certificate. If the query is explicitly changed to “verified matching receipts **contained in this authenticated 17-second log**”, that narrower finite-log task may be decidable and locally closed, with **world coverage still OPEN**.

“Find **some** matching peer” is safer only when the returned witness is legitimate. No witness found before timeout is **not** proof that none exists.

### 6.11. Lemma OW-11 — nearest observed is not necessarily globally nearest

Suppose the observed record \(h\) contains an eligible peer at qualified distance \(d>0\). Assume two possible worlds are compatible with the same \(h\): in one no closer eligible peer exists, while in the other an **unseen** eligible peer at distance \(d'<d\) exists. The agent has no trusted closer-exclusion certificate or complete-radius scan.

**Lemma OW-11 (nearest-neighbor non-closure).** No procedure using only \(h\) can conclusively certify that the nearest **observed** qualified peer is **globally nearest** in both worlds.

**Proof.** Identical observations lead to identical output, but the globally nearest peer differs between the worlds. \(\square\)

A robot **can** compute the nearest **among observed and qualified peers**. It can also determine a true **global** nearest peer when a trusted scoped registry, complete spatial scan or bound reliably excludes closer eligible candidates. With no observed matches, “no qualified neighbor **observed**” is not “no qualified neighbor **exists**.” Merely replacing ALL by ONE, SOME, FIRST or NEAREST does **not** settle coverage or missing semantic evidence.

### 6.12. NC-2 — programming-level sanity checks for collection-producing instructions

**NC-2 is a proposed programming/research constraint, not an adopted runtime standard.** Any agentic query returning a collection or selected peer should carry a result contract which distinguishes (a) run-local witnessed elements, (b) substantive indeterminate observed cases, (c) population completeness, (d) semantic completeness and (e) execution/diagnostic status. Default **global result-set completeness is OPEN** until justified by qualified evidence.

| Instruction | Correctly qualified result | Invalid silent assumption |
| --- | --- | --- |
| Find **all** peers satisfying P | Witnessed matches with explicit scope, unresolved cases and coverage; claim ALL only under an effective completeness witness | A sample is the whole ecosystem |
| Find **some** peers satisfying P | One or more **witnessed** matches or no witness found within budget | Empty result proves no match exists |
| Search for **17 seconds** | Log-scoped matches, negatives, indeterminates and TIMEOUT/BUDGET state | Ending a loop certifies all relevant predicates and peers |
| Find the **nearest** eligible peer | Nearest observed qualified candidate; global nearest only when closer alternatives are excluded | No unseen closer peer exists |
| Add a handshake/metafilter | Better local qualification, refusal or honest UNKNOWN | Computable meta-checks decide all future semantics |
| Construct the set “all inputs on which this procedure decides” | Mathematical description or scoped executed output | Definition yields a universal decision or completeness oracle |

At minimum, an executable API should preserve the **target question, declared scope and snapshot, computation/time/evidence budget, provenance, witnessed matches/nonmatches, indeterminate observed cases, population coverage, semantic completeness, global-result qualification and separate diagnostics**. A finite set of confirmed positives need **not contain** a literal INDETERMINATE element: uncertainty belongs in the **typed result envelope**, not necessarily inside its verified match set.

**Example — legitimate open-world set query response:**

~~~json
{
  "target_predicate": "will_eventually_complete",
  "scope": "city-zone-A",
  "budget_seconds": 17,
  "witnessed_matches": ["agent-01"],
  "witnessed_nonmatches": [],
  "unresolved_observed": ["agent-02"],
  "diagnostics": {"agent-02": ["TIMEOUT", "BAD_FRAME"]},
  "population_coverage": "OPEN",
  "semantic_completeness": "INCOMPLETE_ON_OBSERVED",
  "global_result_set": "OPEN"
}
~~~

The witnessed matching member is assumed to have a qualified independent completion receipt; HELLO=YES alone is not proof of eventual successful fulfilment. The unresolved list counts **observed** cases only; it neither enumerates nor estimates all unknown outside peers.

**Executable research sanity checks:** [OW non-closure set-query and nearest-neighbor contract fixture](./fixtures/OW_NONCLOSURE_CONTRACT_CHECKS_v0.1.mjs) (15 bounded internal assertions). The fixture exercises valid local subsets, certified finite inventory closure, timeouts, damaged records, missing/incompatible population certificates, unknown semantics despite complete inventory, and global-nearest versus observed-nearest distinctions. Run from repository root with the command below:

~~~sh
node research/structural-awareness/fixtures/OW_NONCLOSURE_CONTRACT_CHECKS_v0.1.mjs
~~~

The fixture's trusted-inventory input is assumed to come from an **externally authenticated/qualified certifier**. Its affirmative/negative semantic judgments are also **mocked as already qualified**; the fixture does **not** independently verify their receipts or provenance. The script does **not** verify that authority, invent a global oracle or machine-check any infinite theorem; it validates only declared *contract invariants* in finite constructed inputs.

**Failure-mode boundary:** if forced into a total correct binary global semantic contract under H-EXP, a computable program must err somewhere. A partial program may hang; a sound total three-outcome program must preserve an INDETERMINATE case. A timeout or exception can be **an operational event**, but is not mathematically forced in every run. Silent promotion of UNKNOWN to YES/NO creates false closure. Endless waiting for an unprovable universal enumeration can squander resources. Neither a specific Type-1 nor Type-2 EA diagnosis follows without the Foundation's separate operational/causal conditions.

## 7. Relation to L1 and to the current Structural Awareness corpus

**L1 (*Practical Incompleteness*).** The historical source asks where a concrete procedure's effective resolution domain ends. The **OW-6–OW-11** continuation distinguishes mathematically defined semantic membership from effective global closure, a **closed finite execution record** from a **universally exhaustive reusable query**, and the conditional appearance of an indeterminate under effective exhaustive traversal. NC-2 adds explicit set-valued API checks. The present theorem preserves the **procedure-relative frontier** and the existential logic, now for a querying agent, its handshake and all subsequent decision subroutines. Its proof deliberately uses a valid diagonal reduction: it does **not** reuse the historical assertion that finite binary strings form a proper class, nor infer an undecidable fixed halting domain merely from a machine being partial. The existing [R07 mathematical review](https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R07_PRACTICAL_INCOMPLETENESS_v0.1.md) already develops the uniform/nonuniform distinction. OW-1 applies that sound distinction to an explicit peer-interaction semantics; neither claim is presented as a novel computability impossibility.

**Given Universe and Ecosystem Awareness.** The current [Foundational Theory v0.5](../ecosystem-awareness/baseline/01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md) distinguishes an open class of potentially relevant states Ω, a bounded represented operational universe U, and an open residual R_U **that is not an exhaustively enumerable set complement**. OW-1 is narrower: it constructs an effective peer family K and a precise undecidable **uniform target property** T. It does not replace Ω, U, R_U or prove an all-purpose theorem about physical reality.

**A/B/C/D.** The [canonical 00M v0.8](../ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md#abcd-canonical) makes A/B/C/D **process-, question-, scope-, capability- and time-relative roles**, not mutually exclusive sets or a total partition:

- **A:** the result actually delivered; it may be a legitimate UNKNOWN or a bounded DENY.
- **B:** the established basis, limits and characterized, assessable reserve (e.g., a verified bound or known verification route).
- **C:** a grounded but uncharacterized exploration avenue.
- **D:** potentially material effects beyond this process's effective evaluation route under current conditions.

OW-1 justifies why **the overall decisive YES/NO function cannot be assumed universally complete** under H-EXP. It does not decree that every timeout belongs in D, that every unspecified peer is C, or that the entire set of hard programs can be enumerated as a populated A/B/C/D record. A missing basis for assigning any role remains **UNKNOWN** rather than a fabricated D classification.

The [current signalling annex 01J](../ecosystem-awareness/baseline/01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md) independently distinguishes discovery/handshake, bounded semantic coupling, receiver qualification and subsequent interaction. This mini-paper establishes a mathematical **limit**, not a mandatory handshake format, shared trust root, agent-citizenship protocol, security policy, MSCA change or new architecture component.


### Mathematical continuation: meaning transfer through A/A′

[**From A to A′: Open Meaning and Semantic Transfer Between Agent Ecosystems**](./A_APRIME_OPEN_SEMANTIC_TRANSFER_BETWEEN_AGENT_ECOSYSTEMS_v0.1.md) develops the next, distinct mathematical question before projection. In that note **A** denotes the intended **procedure and independently defined semantic task**, **A′** its **open non-determination frontier**, and finite run records are separate. TR-1/TR-2 show why raw traces or falsely closed result sets cannot generally reconstruct/export the semantic target; TR-3 gives the conditional source-to-receiver soundness criterion for transporting the pair without false closure. This is **not** a modification of canonical 00M A/B/C/D nor a claim of automatic cross-ecosystem compatibility.

### 7.1 Relation to the projection articles: separate, stronger question

The original 2025 [*Projection Mechanism*](https://www.researchgate.net/publication/393802750_The_Projection_Mechanism_How_Practical_Incompleteness_Infiltrates_Formal_Systems) combined a practical incompleteness/validator-chain claim (§2) and a meta-discriminator hierarchy (§3) with a further **projection** proposal, defined via ZFC Separation (§5), and an identity/bijection between already defined residual collections (§6). The source's strong claims that every gateway computationally dominates downstream components or that an arbitrary countable chain shares one individually unresolved input do **not** follow without stronger assumptions; the specific source-level conditions and counterexamples are recorded in the separate [R08 research dossier](https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R08_PROJECTION_MECHANISM_2025_v0.1.md). OW-5 establishes the **weaker and valid composite-procedure result** instead; it does not borrow those stronger claims.

The author's [fourth revision of *The Projection Mechanism*](https://drive.google.com/file/d/1OrJ2LWz2qBv2sP8_-VNldWpctxZdwcfI/view), particularly §§5–6, distinguishes an **in-frame incompleteness item** missed by a filter from a **projected item** whose semantic placement was not justified when forming the receiving working universe. It also explicitly withdraws blanket claims about all open-world inputs being Turing-complete, and treats any net growth of projected residue as conditional on defined arrival/removal rates (§9). The distinct [*Projected Infinite Paradox*](https://www.researchgate.net/publication/393884759_The_Projected_Infinite_Paradox_Unifying_Constructivism_and_Platonism) examines changing constructive stages/populations and claimed semantic consequences of projection; it is **not** a statement about one late handshake or damaged file. Its editions require separate proof/quantifier control.

**Formal boundary in this paper:** OW-1/OW-3/OW-5 and OW-6–OW-11 establish limits on effective determination, repeated execution, and global closure for an agent's interaction procedure; **none of that alone establishes projection**. OW-4 identifies an independently checkable **source-to-receiver information-sufficiency obstruction** that may help develop projection claims, but only after the upstream and receiving semantic questions, data mappings, admissible witnesses and authority conditions are specified. Repeating more filters on the **same insufficient representation** cannot recover a distinction erased from every accessible input; an independent qualified source or a repaired representation may.

We therefore record projection as **a distinct next research stage**, not a corollary of a timeout, a corrupt frame, or OW-5. This mini-paper does not establish inevitable misclassification, unconditional accumulation, physical entropy, universal semantic corruption or superiority of a particular architectural response.

## 8. What would count against the applied claim?

The mathematical proof is conditional and can be checked by inspecting the effective compilation e↦P_e and the equivalence (1). Its application to a real smart-city profile must separately establish that the actual admissible agent class can express this construction **and** that the declared substantive decision has the required semantics.

A bounded profile that (i) admits only certified finite-state peers, (ii) imposes a verified maximum completion time as part of its substantive contract, or (iii) restricts the target to finite observable traces, can be legitimately decidable. Authorized independent certificates may also distinguish OW-3's alternatives or repair OW-4's lost decisive fields. That is not a paradox or a counterexample to OW-1; it is a **different hypothesis or decision task**. If the target's claimed semantic strength or H-EXP does not hold, the theorem may not be applied.

Empirical research can then examine rates of clean completion, justified NO, bounded UNKNOWN, damaged-source recovery, false certainty, indefinite waiting, added verifier-chain cost and useful requalification. Such measurements test **operational handling**, not the diagonal theorem. No superiority of Structural/Ecosystem Awareness over conventional tools follows from OW-1.

## 9. Conclusion

A universally terminating handshake does not imply a universally terminating **correct semantic decision** about every possible peer. In a computationally expressive open agent class, a single effective procedure cannot always return an infallible substantive YES/NO after discovery, handshake and any computable sequence of subsequent subroutines. **Every finite effectively composed chain of software verifiers remains one such procedure.** Under weaker finite-resource premises, delayed responses and irrecoverable evidence loss can additionally make specific questions indeterminate relative to the agent's actual observations, despite decidable local protocol outcomes. A sound total procedure must leave some substantive questions unresolved in the expressive case; a forced total binary procedure must sometimes be wrong.

This is the precise existential contribution: **an agentic world need not be assumed exhaustively given for there to be a mathematically unavoidable frontier relative to the agent's uniform decision task**. It establishes the frontier and the limits of **effective global closure** before discussing how they should be represented, classified, projected or managed. A succession of successful closed finite runs does not turn the reusable query into an exhaustive global classifier; under **effective exhaustive exploration** a sound total three-outcome evaluator eventually encounters an indeterminate, with no uniform finite bound on the number of runs. **The operative constraint is to work open-by-default and close only where a defined question, finite domain, legitimate evidence and completeness witness justify doing so.** An intentionally closed, certified interface or finite-deadline contract is useful and can legitimately decide its **declared limited task**, but cannot by that fact decide arbitrary future peer behaviour.

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

**Change scope:** this is the additive **v0.4 revision of the existing mathematical mini-paper**, preserving its logical identity and public path. It does not edit, supersede or promote the historical sources L1, R07–R10, 00M, Foundational Theory, 01J or frozen architecture artifacts. OW-3/OW-4 and OW-7/OW-10/OW-11 are conditional finite-evidence and coverage propositions; OW-5/OW-5b/OW-6/OW-8 use standard computability/composition; OW-9 requires a genuinely exhaustive computable traversal; OW-9b requires an independently supported encounter-probability lower bound. NC-1 and NC-2 are **proposed operational disciplines, not adopted requirements**. The executable fixture checks bounded contract invariants only. These additions make no topological closure claim and no declaration of a complete operational ABCD classifier. Formal machine verification and empirical deployment are not claimed.
