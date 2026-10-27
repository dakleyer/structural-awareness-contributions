# Open-World Agent Encounters: A Uniform Decision Frontier

**Mathematical mini-paper · Structural Awareness Programme · v0.1 · 27 October 2026**  
**Logical subject:** SA-MATH-OW-01 · **Role:** standalone working mathematical contribution, for author and external mathematical review  
**Lineage:** Iván Abril Palma, *Practical Incompleteness* (L1 / R07), *Given Universe*, and the present Ecosystem Awareness foundational work. This exposition was prepared with AI assistance at the author's request.  
**Maturity:** conditional formal results using standard computability arguments; **not** a new proof of the halting theorem, an empirical finding about all smart cities, or an accepted architecture/standard.  
**Reading boundary:** the theorem below concerns **uniform substantive determination**, not the ability to send a message, reject a connection, impose a deadline, or record UNKNOWN. The [canonical A/B/C/D semantics](../ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md#abcd-canonical) are unchanged.

## Abstract

A robot or software agent in an open smart city can discover peers, perform a terminating yes/no handshake and then execute further decision procedures. Does this make every possible peer interaction decidable? No, provided the admissible world is computationally expressive enough and the question concerns nontrivial **future semantic behaviour**, not merely receipt of a handshake acknowledgement. We construct a fixed, effectively describable family of peer agents, all of which pass the same handshake, such that a sound and complete, terminating procedure deciding whether each peer will eventually fulfil a particular request would decide the diagonal halting problem. No such uniform procedure exists. A second, observation-relative lemma explains why a finite interaction prefix cannot certify eventual non-response without further valid bounds or evidence. The result recovers the operational frontier sought by *Practical Incompleteness* without treating finite strings as a proper class, without asserting that every fixed peer is individually undecidable, and without presuming an exhaustive “Given Universe.” It motivates, but does not validate, the separate agentic handling of situated indeterminacy.

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

The operational result alphabet may include **YES, NO, UNKNOWN**. UNKNOWN is a legitimate reported result, not a third truth value of T.

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

**Corollary OW-1a (unavoidable unresolved cases under soundness).** Any **total, sound** effective procedure with output alphabet {YES, NO, UNKNOWN} must return UNKNOWN for at least one P_e. A sound effective procedure permitted to run without a bound must instead leave some cases without a terminating definitive answer. A total procedure compelled to answer only YES/NO must make an error on at least one P_e.

This is an existence result within the already-declared admissible agent class. It does **not** require repeatedly extending the universe until the argument works.

## 4. Lemma OW-2 — a finite handshake/transcript cannot certify all future outcomes

A different, more elementary observation concerns a particular agent with only a **finite observed transcript**.

**Lemma (finite-prefix underdetermination).** Assume no trusted upper response-time bound, exhaustive terminal certificate, or other source-qualified evidence decides eventual response. For any finite interaction observation horizon h, there exist two admissible peer behaviours with the **same visible transcript through h** after the same successful handshake, but with different eventual completion values.

**Proof.** Let P^+_h send the completion receipt after h+1 observation steps, and let P^-_h never send it. Arrange both to produce the identical handshake and the identical absence of substantive replies during steps 1,...,h. Then their observed prefixes agree, while T(P^+_h,r)=1 and T(P^-_h,r)=0. No determinate function of that prefix alone can output the correct value of T in both cases. \(\square\)

This lemma is **observation-relative**: access to additional verified code facts, a correct termination proof, a binding timeout specification that changes the question, or a trusted completeness certificate may justify a local result. It is not a separate theorem of Turing undecidability.

## 5. The agent's actual procedure: what has, and has not, been decided

The proof does **not** prohibit a sensible interaction discipline. It distinguishes the propositions that a discipline answers.

| Observed or produced result | What it establishes | What it does not establish |
| --- | --- | --- |
| HELLO → YES | Handshake accepted under a declared envelope | Eventual fulfilment, global compatibility or safety |
| HELLO → NO | Contact declined under that envelope | Mathematical impossibility of every other interaction |
| Valid signed completion receipt | The specified observed completion occurred, subject to verification | Reliability in all future contexts |
| Timeout at h | No qualifying receipt was observed by h | That a later receipt is impossible |
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

The result is therefore useful **without asserting that every possible universe extension creates an undecidable residual**. The obstruction arises in the specified open class and the demanded universal decision task.

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

## 8. What would count against the applied claim?

The mathematical proof is conditional and can be checked by inspecting the effective compilation e↦P_e and the equivalence (1). Its application to a real smart-city profile must separately establish that the actual admissible agent class can express this construction **and** that the declared substantive decision has the required semantics.

A bounded profile that (i) admits only certified finite-state peers, (ii) imposes a verified maximum completion time as part of its substantive contract, or (iii) restricts the target to finite observable traces, can be legitimately decidable. That is not a paradox or a counterexample to OW-1; it is a **different hypothesis or decision task**. If the target's claimed semantic strength or H-EXP does not hold, the theorem may not be applied.

Empirical research can then examine rates of clean completion, justified NO, bounded UNKNOWN, false certainty, indefinite waiting and useful requalification. Such measurements test **operational handling**, not the diagonal theorem. No superiority of Structural/Ecosystem Awareness over conventional tools follows from OW-1.

## 9. Conclusion

A universally terminating handshake does not imply a universally terminating **correct semantic decision** about every possible peer. In a computationally expressive open agent class, a single effective procedure cannot always return an infallible substantive YES/NO after discovery, handshake and any computable sequence of subsequent subroutines. A sound procedure must leave some questions unresolved; a forced binary procedure must sometimes be wrong.

This is the precise existential contribution: **an agentic world need not be assumed exhaustively given for there to be a mathematically unavoidable frontier relative to the agent's uniform decision task**. It establishes the frontier before discussing how it should be represented, classified, projected or managed.

---

## Sources and review boundaries

1. Iván Abril Palma, *Practical Incompleteness: A Set-Theoretic Framework for Concrete Decision Procedures*, historical manuscript (L1). https://www.researchgate.net/publication/393799525_Practical_Incompleteness_A_Set-Theoretic_Framework_for_Concrete_Decision_Procedures
2. R07, *Practical Incompleteness: Fixed Halting Domains, Uniform Undecidability, Effective Scope and Source-Qualified Continuation* (internal source-specific mathematical review; access follows its existing repository permissions). https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R07_PRACTICAL_INCOMPLETENESS_v0.1.md
3. Structural Awareness, *Ecosystem Awareness — Integrated Foundational Theory v0.5*. https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md
4. Structural Awareness, *00M v0.8 — A/B/C/D Semantics and Mathematical Plausibility*. https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md
5. Structural Awareness, *01J — Ecosystem Signalling: Selective Disclosure and Choreographed Repositioning*. https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md

**Change scope:** this is a new additive mathematical contribution. It does not edit, supersede or promote L1, R07, 00M, Foundational Theory, 01J or frozen architecture artifacts.
