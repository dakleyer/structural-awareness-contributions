# 03 — Bounded second-order metaprotocol: algorithms, authority and costs

**Stage A design, not an implemented oracle.** All calculations are relative to a declared finite model and qualified sources. Original-source provenance for every imported algorithm is in [01](./01_ORIGINAL_SOURCE_LINEAGE.md); mathematical correctness conditions in [02](./02_FORMAL_CORE_AND_PROOFS.md).

## 1. What exactly is the “oracle”?

A **meta-protocol** \(\mathfrak M\) is a *procedure* (possibly distributed; not necessarily another AI agent) that receives a versioned question about a particular ecosystem configuration and returns:

\[
\mathfrak M(\kappa,o,\Sigma_0,\Sigma_1,r,Q,\mathcal A,B)
\longrightarrow
(\text{certificate},\text{eligible inquiries},\text{proposal},\text{decision status}).
\]

Inputs:

| Input | Meaning and origin |
|---|---|
| \(\kappa\) | Signed scopes, owners, timestamps/expiry, source roots, claims, rights, proof status and declared model boundary (00M/00N; R04, R18, R20) |
| \(o\) | Present functional contract/output; **not** an omniscient internal-world observation (*Given Universe*) |
| \(\Sigma_0,\Sigma_1,r\) | Current/changed allowed operations and independently defined recipient mission target (R01) |
| \(Q=\{Q_j\}\) | Characterized, eligible partial questions/evidence routes (R03, R05); unavailable questions are **not invented** |
| \(\mathcal A\) | Current authorized action, transfer, adaptation and metamorphosis relations for each participant (R04; ACC) |
| \(B\) | Explicit inquiry, coordination, transformation, money, latency and rollback budgets, in **typed** units (R12; ACC) |

Outputs always include an **evidence scope** and **expiry condition**. A certificate may say “in this stated model, the present interface is adequate”; or “pair x/y witnesses a failure under new operation”; or “query j distinguishes the relevant pair”; or **UNKNOWN** because the frame or source qualification is inadequate. It never says “what C/D really contains.”

**Important:** if an existing conventional source already supplies equal evidence and coordination, the meta-protocol has **no special epistemic privilege**. Agentic systems may be cheaper to reconfigure, but that is an experiment, not a theorem.

## 2. Algorithms reused exactly, with their source status

| Step | Mathematical object | Provenance | Exact use and non-claim |
|---|---|---|---|
| P0 | Source/permission/version validation | R04 §14.5; R18 §1.3; 00M/00N | Reject invalid inference, not just invalid syntax; *policy is externally specified* |
| P1 | Equivalence & congruence check | R01/S01 review §6 P1–P2; standard quotient algebra | Test if old A retains operational sufficiency after changed task |
| P2 | Greatest stable refinement (D2) | R01/S01 §6 P4; standard partition refinement | Construct the needed state distinctions *within finite scope* |
| P3 | Conditional mission-conflicting-pair cover (D3-A given current A; D3 for Q-only) | R03 review §14.2; ordinary conditional pair separation; [02 §4.1](./02_FORMAL_CORE_AND_PROOFS.md) | Select minimum eligible **supplementary** sources for conflicts left unresolved by the already qualified receiver observation; no C/D sampling |
| P4 | Saturated safe domain & typed commuting map | R04 review §14.3–14.5 | Prevent “meaning transfer” and “rights transfer” from being conflated |
| P5 | Finite second-order certificate | R05 review §14.3–14.5 | Report entailed/refuted/underdetermined/inconsistent *in frame*; UNKNOWN otherwise |
| P6 | Conflicting report joint atoms | R18 review §1.2–1.4; existing partition mathematics | Preserve both signed sources and no false world contradiction |
| P7 | Open-prefix closure check | R11 §9, R13 §3.1, R20 §1.2 | A finite empty search is not universal absence; return UNKNOWN if no authenticated closure |
| P8 | Local/global population monitor | R10 third original and review §§3–6 | Requalify “global good” when composition/population changes |
| P9 | Query/verification reuse economics | R12 compiled original §proof cost, review §§2–4 | Measure actual reusable proof benefit after verification overhead |
| P10 | Recipient obligation queue and strong comparator | R09 review §§4–6; ACC pilot | Create a task queue for **specific** downstream obligations, not a universal controller |

**Distinct transformations:** a source's initial historical intuition is **not** proof that the reviewer’s P1–P10 operations already appear as complete algorithms in it. The formal algorithm versions are a **later explicit integration**. In particular: R03 original \(\oplus\ne\) XOR; R05 original not an executable frame truth oracle; R12 entropy hypotheses not physical operating-cost formulas.

## 3. Complete protocol specification, with authorization gates

The following is pseudocode, not a deployed service:

~~~text
META_REQUALIFY(signed_inputs, changed_mission, budget):
  00. VERIFY_ORIGIN_AND_SCOPE
      Verify each issuer, claim semantics, original purpose, receiving purpose,
      clock/version, expiry, revocation, evidence access and permitted transformations.
      If unknown source, expired frame or forbidden use:
          return UNKNOWN(reason, source_ids, allowed_next_steps=[]).

  01. TYPE_AND_FREEZE_FRAME
      Freeze bounded X_hat, o, old/new Sigma, mission target r, allowed Q,
      authorized action graph A, and independent cost units / commitments.
      Reject incorrectly typed or internally contradictory premises;
      return INCONSISTENT_FRAME where the finite frame has zero models.

  02. CHECK_CONGRUENCE_AND_MISSION
      Check fiber sufficiency for r (F1), operational congruence (D1).
      If both pass for NEW Sigma and accepted bounded scope:
          return QUALIFIED_ADEQUATE(scope, certificate, expiry, audit).

  03. WITNESS_LOST_DISTINCTION
      Find a concrete pair (x,y) equal under current o that:
          (a) yields different r; OR
          (b) yields different new-operation observable successors.
      Also compute a sound set-valued conventional fallback.
      If no witness and no complete model:
          return UNKNOWN(no_exhaustive_coverage, audited_prefix).

  04. COMPUTE_REQUIRED_REFINEMENT
      Refine old partition under declared new operations;
      form the conditional pair universe U_(r|o) still ambiguous under
      current qualified A=o, or U_(r_h|o) for an authorised finite horizon.
      U_r applies ONLY if the receiving question has no reusable A observation.
      This gives the proof obligation, NOT access to missing answers.

  05. FIND_ELIGIBLE_EVIDENCE
      For every characterized Q_j, verify rights, source, meaning, cost and scope.
      Cover ONLY the receiver's unresolved U_(r|o) pairs with eligible Q;
      use joint (o,Q), not Q alone, for the resulting sufficiency test.
      Solve minimum-cost query cover where additive / independent;
      otherwise solve an explicitly typed joint-cost optimization.
      If impossible, cost-over-budget or unsafe:
          return HOLD_OR_INQUIRE(reason, uncovered_witnesses).

  06. CHECK_TRANSLATION_AND_CONFLICTS
      Check saturated eligibility domain, commuting question maps,
      signed conflicting evidence and no transitive authority inference.
      Re-evaluate recipient permissions. Preserve disagreements and UNKNOWN.

  07. META_CERTIFY_WITHOUT_REIFYING_TRUTH
      Enumerate only qualified finite candidate frame models when available.
      Return ENTAILED / REFUTED / UNDERDETERMINED / INCONSISTENT_FRAME;
      return UNKNOWN outside the model, open prefixes or uncharacterized methods.

  08. SOLVE_AUTHORIZED_RECONFIGURATION
      Enumerate or search ONLY already allowed actor transforms/transfers.
      Enforce finite ledger resource conservation and transition budgets.
      Compare mission benefit to acquisition, verification, coordination,
      transformation, monitoring, rollback and human-consent costs.
      Include strongest conventional policy and no-change comparator.
      If no feasible net-positive candidate, recommend HOLD/no-change.

  09. ISSUE_SCOPED_PROPOSAL
      Output: witness, evidence ids, declared mission, provenance, rights,
      model/algorithm version, uncertainty, eligible transitions, cost ledger,
      expiry/requalification triggers, independent referee comparison.
      Actuation: NEVER; requires separately authenticated owner/governance approval.
~~~

**27 October correction reception:** The prior P3/Q-only adaptation mistakenly charged Q with distinguishing pairs that the current A observation already separates. [02 §4.1](./02_FORMAL_CORE_AND_PROOFS.md) preserves D3 and proves the conditional receiver version D3-A, including the four-state false-unattainability counterexample. P3 and stages 04–05 above now use the **conditional** problem. This is an arithmetic/interface repair in Stage A research, not evidence that a real-world source Q exists or is cheaply verifiable. Cost of existing A remains part of the full comparison ledger.

**Why not “a magic oracle”?** At every step, knowledge is bounded by observations, a finite declared model and existing actor rights. The output is a *proposal or certificate relative to input conditions*. The protocol can reveal that a better known state arrangement is feasible **in its model**, but cannot conjure unobserved resources, forge information or bypass source controls.

## 4. Mission-relative allocation and metamorphosis

Let \(N\) participating actors have roles \(a_i\in\mathcal A_i\), resource allocations \(z_i\in\mathbb R_{\ge0}^d\), and resource stock \(R\in\mathbb R_{\ge0}^d\). Define:

\[
\mathcal F(\kappa)=\left\{(a,z):
a_i\in\mathcal A_i,\ \sum_i z_i\le R,\
\operatorname{rights}_\kappa(a,z)=1,\
\operatorname{transitionCost}(a,z)\le B_{\rm trans}\right\}.
\tag{P1}
\]

An independent mission value \(U(a,z;\omega)\) is set by the receiving task, with an uncertain environment \(\omega\); all claimed optima require a declared \(\omega\)-model, loss function or robust criterion. The candidate problem is:

\[
(a^\*,z^\*)\in\arg\max_{(a,z)\in\mathcal F(\kappa)}
\left(\mathbb E[U(a,z;\omega)\mid I]
- C_{\rm query}-C_{\rm coordination}-C_{\rm transition}-C_{\rm monitoring}\right).
\tag{P2}
\]

This optimum is a **conditional decision benchmark**, not evidence that a real future state is known. Distinguish a *nominal feasible stock* \(\sum_i z_i\le R\) from the **fully reachable and authorized set** \(\mathcal F(\kappa)\). The latter may be empty.

**Metamorphosis:** a change of role/configuration is legitimate **only when contained in \(\mathcal A_i\)** or its separately approved governance transition. The protocol does not “give” the agent new powers. “Solidarity” (one agent giving resources, deactivating or changing role for another's mission) can be explicitly programmed in non-agentic systems too. The proposed difference is **potential coordination and implementation cost**, subject to empirical comparison.

## 5. Distinguish primary and second-order “frustration”

Use **mission gap** in the agentic model, not “suffering.” Let \(U_{\rm ref}\) be the utility of an *independently feasible, authorized* reference design under the same real resource and time boundary, and \(U_{\rm run}\) realized utility:

\[
G_1=[U_{\rm ref}-U_{\rm run}]_+.
\tag{P3}
\]

This is **operational opportunity loss**. It is not “experienced pain”; a simulation can measure it.

An admissible partial source might reveal a **nearer but currently unreachable** configuration \(a^\dagger\) with higher mission value. A separate diagnostic is:

\[
G_{\rm disclosed}=[U(a^\dagger)-U_{\rm current}]_+
\quad\text{with}\quad a^\dagger\notin\mathcal F(\kappa)
\tag{P4}
\]

and an *explanation of the blocking constraint*: permission, cost, information, role or timing. **Do not add \(G_{\rm disclosed}\) to \(G_1\)**; they can overlap or reference incomparable baselines. Additional evidence can **increase awareness** of an unavailable optimum without decreasing realized mission gap. A separate second-order metric could be a new *avoidable gap after an authorized redesign*, but that remains H/open until defined and tested.

A realistic falsifier: better Q yields a precise promising but unauthorized allocation; the protocol correctly abstains, performance does not improve and coordination costs rise. This is **not** a successful resource-reduction result.

## 6. Cost accounting: usable arithmetic, non-universal advantage

R12 review gives a simple reuse *identity*. With initial work \(C_A\), independently checked questions j costing \(c_j\), shared validation of reused checks \(v_j\), reuse indicator \(r_j\in\{0,1\}\), and fixed integration overhead h:

\[
C_{\rm sep}=C_A+\sum_j c_j,
\]

\[
C_{\rm shared}=C_A+\sum_j[(1-r_j)c_j+r_jv_j]+h,
\]

\[
\Delta C=C_{\rm sep}-C_{\rm shared}
=\sum_{r_j=1}(c_j-v_j)-h.
\tag{P5}
\]

The *numerical example* in R12 originally discusses 7+5(1−.4)=10 arbitrary units. P5 is ordinary arithmetic but valuable as a **measurable operational audit**: reuse pays iff \(\sum(c_j-v_j)>h\). Verification may cost more than independent assessment; then reuse is negative. Cross-owner licensing, translation, dynamic invalidation, attestation, privacy and consent are extra line items.

For the meta-protocol compare:

\[
\Delta V_{\rm net}
=V_{\rm decision}(A,Q)-V_{\rm decision}(A)
-C_{\rm Q}-C_{\rm verify}-C_{\rm orchestrate}
-C_{\rm transition}-C_{\rm risk}.
\tag{P6}
\]

Report units separately: **seconds, compute, money, labor, policy risk, mission utility**, and only combine through a declared valuation model. Do **not** equate Shannon bits, abstract \(\Omega\), token usage, physics exergy and monetary expense.

The hypothesis that an agentic system's \(C_{\rm transition}\) is lower than a city's or a monolith's is **not a theorem** and may be false for high-assurance production AI. Benchmark matched complexity, governance, security and rollback.

## 7. Computational limits and implementation choices

| Operation | General bounded upper/lower observation |
|---|---|
| Check congruence on explicit finite X with an existing partition | Straight pair-based check is \(O(|\Sigma||X|^2)\), ignoring function-evaluation cost |
| Naive iterative refinement | At most \(|X|-|X/R_0|\) strict iterations, so a simple \(O(|\Sigma||X|^3)\) upper bound; more efficient algorithms exist |
| Minimum additive-cost pair-separating query set | Weighted set cover is NP-hard in general; exact search can require exponential time; any approximation guarantee must state its assumptions |
| Partial translation/rights witness | Depends on availability of authentic source grants; arithmetic complexity does **not** settle institutional validity |
| Complete propositional finite meta-certificate | Finite/exhaustive relative to X but exponential if X is implicitly a large Boolean assignment set |
| Resource allocation/reconfiguration | Often combinatorial/nonconvex; no assumed polynomial global optimizer or built-in actuator |
| Open prefixes/new vendors | Requalification is event-driven; global closure not inferred from finite tests |

**Alternatives and strong incumbents to test:** abstract interpretation/set-valued monitors, distributed policy engines, BDI/coordination protocols with existing contracts, constraint/MILP scheduling, formal methods with proof-carrying data, belief-state POMDP/Bayes decision systems, standard rights-aware orchestration. A bespoke meta-protocol may be less cost-effective than a strong ordinary implementation of the **same** mathematics.

## 8. Concrete machine-checkable artifacts expected at Stage B

For each finite case, save: exact state and transition generator seed; signed simulated source ledger; owner/role rights; canonical mission target and independent full-information referee; actual Q menus and costs; partition before/after; witness pair(s); eligible-query cover and uncovered pairs; certificate; feasible reallocation and budget; strong incumbent action; full provenance; expiration triggers; rejection reasons. Every result must be regenerated from *independent*, unfriendly counterexamples, not just from a fixture built to reproduce A/B/C/D.

**Promotion threshold:** correct mathematical proofs do not suffice to claim agentic advantage. It must survive independent R1/R2/R3 technology comparisons and UC21 companion falsification with protected judge and independent scoring; see [05](./05_INDEPENDENT_VALIDATION_PROTOCOL.md).