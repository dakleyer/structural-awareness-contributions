# H-01 — Why the proposed coordination mechanisms succeed or fail

**Source-owned scientific reception, 1 November 2026.** Companion to [H01_STRATEGIC_CHOICE_PROTOCOL.md](H01_STRATEGIC_CHOICE_PROTOCOL.md), [strategic_choice.py](strategic_choice.py) and the author source [bounded_traps.py](bounded_traps.py).

**Reproducible result:** [GitHub Actions #41292908144, PASS](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/41292908144). The CI computes this diagnosis from the **actual 180 H-01 source results** with [h01_failure_diagnostics.py](h01_failure_diagnostics.py), rejects inconsistent labels or actor payoff vectors, and runs **11 additional negative tests** beyond the original 34 H-01 tests and 21 frozen bounded-traps tests. The machine-readable diagnostic is retained in the H-01 artifact.

## 1. The invalid aggregation: "114 successful coordinations" is not "114 rational traps resolved"

The 180 configurations in the predeclared grid have two independent outcome axes:

1. **Strategic state:** Is the initial state a *strict rational trap* with all unilateral alternatives physically feasible, a weak equilibrium, a state with profitable unilateral escape, or simply a configuration without a Pareto-superior target?
2. **Proposed joint response:** Does the exact joint net payoff *strictly* improve each actor's position, given setup resources, explicit PASS governance and zero transfers in this particular sweep?

The cross-classification **must never be silently merged**:

| Initial strategic mechanism | Joint proposal admitted | Joint proposal rejected | Total |
|---|---:|---:|---:|
| **Genuine strict rational trap** | **24** | **15** | **39** |
| Profitable unilateral escape already exists | 66 | 6 | 72 |
| Weak equilibrium (indifferent individual deviation) | 24 | 3 | 27 |
| No strictly Pareto-superior joint target | 0 | 42 | 42 |
| **Total** | **114** | **66** | **180** |

**Actual strategically relevant positive subset:** 24 configurations, not 114. A further 15 have a genuine trap but **the specified remedy is not acceptable**. The 90 other admitted configurations do *not* demonstrate resolution of a strict rational trap: 66 already have profitable unilateral escape; 24 have a weak initial equilibrium.

The correct research claim is an **existence-plus-conditional-remedy demonstration**, not an average success rate or a performance statistic about populations.

## 2. Exact analytical phase boundaries, recovered from the source engine

Within the specified *symmetric two-actor* grid, the source computes each actor's payoff using:

- b0 = 3: initial actor payoff, fixed in the experiment.
- r: standalone return if that actor starts the activity.
- c: individual investment cost.
- s: pairwise complementarity received if **both** act.
- k: burden in that actor's own payoff units from arranging the joint transition.
- e = 1: unilateral inactive exposure to the other actor moving. It affects the off-diagonal payoffs, but not the initial move's private return or the joint profile's payoff.

The outcomes in actor i's own units are:

    u_i(00) = 3
    u_i(10) = 3 + r - c          [actor A moves alone]
    u_i(01) = 3 - e              [actor A stays while B moves]
    u_i(11) = 3 + r - c + s

A's own deviation gain from 00 is **D = r-c**. Each actor's gross joint gain is **J = r-c+s**. Its *strict private surplus after the joint arrangement* is **N = r-c+s-k**. The application of cost occurs **only** at the proposed coordinated transition, not to every unilateral possibility; it therefore does not change whether (0,0) is Nash.

| Threshold | Exact conclusion within this source model |
|---|---|
| D < 0 and J > 0 | **Strict Pareto-inferior Nash / rational trap**. Both unilateral moves are materially feasible but individually harmful |
| D > 0 | **Profitable unilateral escape**, so (0,0) is not Nash; calling a proposed joint agreement a "trap remedy" is incorrect |
| D = 0 and J > 0 | Weak Nash / indifference, not a strict refusal |
| J <= 0 | No Pareto-superior joint candidate exists to recover |
| N > 0 | Each actor strictly gains from the specific post-burden joint proposal (conditional on the other source gates) |
| N = 0 | Gross benefit is entirely consumed by burden; with the manifest's **strict improvement requirement**, the actor can rationally decline |
| N < 0 | Coordination makes each actor worse off than remaining; declining is materially rational |

**Exact condition for a remediable strict trap in this source grid:**

    r < c  AND  s > c-r  AND  k < s-(c-r)

This is a **conditional sufficient characterization in the explicitly symmetric finite game**, not a claim that all social systems follow this additive payoff law.

## 3. The 66 rejections: four distinct reasons, not one failure rate

The new diagnostic derives the failure reason for each individual parameter tuple, rather than trusting stored status labels.

| Failure mechanism | Count | Why the proposal fails |
|---|---:|---|
| **J < 0** | **30** | The joint alternative itself *harms* each actor even before coordination |
| **J = 0** | **12** | The joint alternative offers no positive gross improvement |
| **J > 0 and N = 0** | **12** | Coordination uses exactly the available surplus; strict gain is lost |
| **J > 0 and N < 0** | **12** | The burden exceeds the gross surplus; the proposal reduces private payoff |
| **Total** | **66** | |

Consequently **42 of the 66** should never have been called a recoverable coordination opportunity: there was no gross Pareto improvement. **24 of 66** had a genuine gross improvement but the specific costed remedy failed; of these, **15** were strict strategic traps, **3** weak equilibria and **6** situations with a profitable unilateral escape.

The **strict-positive-benefit** rule itself matters: twelve rejections have N=0 with gross positive J. If the actors agreed to **non-loss** rather than strict gain, those marginal proposals would become individually acceptable under the same physical/governance assumptions. Importantly, a weak non-loss rule would also accept **four** zero-gross-gain situations with no Pareto improvement at all. These distinctions must remain visible; weakening acceptance cannot be rebranded as creating economic value.

## 4. Holding other parameters fixed: which assumption actually causes failure?

### 4.1 Coordination burden k is a direct mechanism in this toy

Within each burden group the **same sixty** return/investment/complementarity triples are evaluated. Thus the burden comparison is matched, not an average over unrelated mixes.

| Each actor's coordination burden k | Joint candidates admitted / 60 | Genuine strict traps / 60 | Strict traps with admissible remedy |
|---|---:|---:|---:|
| 0 | 46 | 13 | **13** |
| 1 | 40 | 13 | **8** |
| 3 | 28 | 13 | **3** |

**Exact counterfactual:** for **18 of 60** fixed (r,c,s) configurations, increasing only burden from 0 to 3 destroys an otherwise admissible joint proposal. **Ten of these eighteen** are genuine strict-trap remedies lost purely from that burden change. The Nash classification stays the same throughout these paired comparisons.

Example: r=0, c=3, s=4 gives D=−3 and J=+1. At k=0 the strict Nash trap is remediable (net gain +1); at k=1 the actor breaks even and strictly refuses (N=0); at k=3 the net loss is −2. **All three have exactly the same strategic trap**, different coordinated acceptance. The mechanism is **cost of making the move together**, not a discovery of new opportunities.

### 4.2 Pairwise complementarity s is necessary to create a strict inferior Nash here

| Complementarity s | Joint proposals admitted /45 | Strict traps /45 | Strict traps with admissible remedy |
|---|---:|---:|---:|
| 0 | 13 | **0** | 0 |
| 2 | 25 | 6 | 2 |
| 4 | 35 | 15 | 8 |
| 6 | 41 | 18 | 14 |

At s=0, the **13 admitted outcomes already have profitable unilateral escape**; none resolves a strict strategic trap. This establishes that pairwise complementarity is **structurally necessary for a strict inferior equilibrium under this particular additive model**. Stronger complementarity expands the parameter region in which acting alone loses but acting together gains. It does not make every arrangement worth its coordination burden.

### 4.3 Assumptions held fixed in the 180-cell result

- All agents are **symmetric** (same returns, costs, synergies and burden). Real asymmetric valuations, credit ownership and changing bargaining power are studied in separate named cases, *not* in these 180 counts.
- The source's **strict gain** requirement is ON. A rational actor at zero net improvement need not accept; weaker participation rules have different implications.
- The current and joint endpoints are materially feasible, and **physical target+setup costs 4 units against budget 10** in every sweep cell. Thus **zero** of the 66 rejections comes from physical resource exhaustion.
- Governance and both consents are explicitly **PASS in every grid cell**. Thus **zero** of the 66 rejections is caused by missing legal authority or consent. The 22 named scenarios independently test these gates, including FAIL/UNKNOWN.
- The grid samples **3 × 5 × 4 × 3 discrete values**, each exactly once. Those counts are **not statistically weighted social frequencies** and should not be expressed as an average expected success rate.
- Information-instrument cost and transferable common credit are **separate ledgers**, not automatically deducted from these payoffs. Without independently justified conversion rules, the engine does not pretend to optimize a universal combined score.
- The game is **static**. It proves best responses and conditional joint admission under stipulated preferences; it does not simulate a real negotiation history, repeated-game learning, observed emotions or the implementation of consent.

## 5. The 22 named cases: other failure mechanisms live outside the incentive-only sweep

The diagnostic additionally publishes a grounded reason array for **every** named case, generated from the source physical status, individual reservation tests, common-credit balances and PASS/FAIL/UNKNOWN governance.

| Independent gate | Example and actual reason |
|---|---|
| Technical target feasibility | H01_TECHNICAL_TARGET_INFEASIBLE: resource budget excludes target |
| Physical setup/resource capacity | H01_INSUFFICIENT_TRANSITION_BUDGET: destination itself feasible but joint setup exceeds 3-unit resource budget |
| Individual willingness | H01_TOO_EXPENSIVE_COORDINATION: burden 3 consumes base positive joint gain 2, so each actor loses 1 |
| Explicit consent | H01_NO_CONSENT: actor B's FAIL prevents a joint move, despite positive payoff |
| Unknown mandate | H01_UNKNOWN_AUTHORITY: source status UNKNOWN must not be converted into automatic approval |
| Joint execution mechanism | H01_NO_JOINT_PROTOCOL: no authorized atomic collective transition |
| Credit source ownership | H01_CREDIT_INSUFFICIENT_SOURCE_BALANCE: payer's declared source balance would become negative |
| Recipient's valuation | H01_CREDIT_NO_VALUE_TO_RECEIVER: conserved credit may have zero private benefit to the receiver |
| Transfer right | H01_CREDIT_TRANSFER_NO_AUTHORITY: positive private payoff is not proof that credit transfer is permitted |
| Reservation beyond immediate payoff | H01_RESERVATION_FLOOR_NOT_MET: at least one actor's separately declared acceptable floor is not met |
| Conventional alternative | H01_CONVENTIONAL_COORDINATOR_CHEAPER: same candidate and authority, conventional instrument simply costs less |

These cases are *not counted as failures in the 180-cell incentive grid*, which deliberately fixes resources/consent/authority in order to isolate economic choice. Mixing their causes would destroy identifiability.

## 6. Reviewer action: challenge the mechanism, not the averages

The [implementation and adversarial tests](test_h01_failure_diagnostics.py) validate every predicted D/J/N margin against the independently run original source engine; reject fabricated status labels, altered payoff vectors, mismatched governance contract and changed physical constraints; and run exact matched burden comparisons.

An independent reviewer should:
1. Recompute the **4 × 2 mechanism/admission table** from individual source rows, *not* from the report text.
2. Verify all **66** rejection reasons and split out the **15 genuine strict traps whose remedy fails**. Never confuse "joint admissible" with "trap solved".
3. Challenge the **strict-gain rule** and the cost assumptions. Run weak no-loss as a separate policy and record cases that would pass *without yielding any joint improvement*.
4. Hold (r,c,s) fixed while altering burden, and independently verify the **18** changed admissions and **10** lost strict-trap remedies.
5. Check s=0 yields no strict rational trap despite sometimes allowing a profitable individual move.
6. Repeat the separate 22 governance/credit/technical scenarios. Never assert the experimental 66 rejections are attributable to legal rights or resource scarcity.
7. Review the model's **symmetric static assumptions** and test heterogeneous, dynamic and evidence-limited successors before extrapolating to real enterprise integration or society.

**Research conclusion:** We can now state precisely *why* each accepted or rejected transition occurs under the declared model. That is stronger than presenting an average and stronger than a single positive example. The result **establishes exact mechanism boundaries within an auditable finite game**, not their prevalence or validity in actual economic actors. Formal H-01 adjudication remains independent; there is no self-promotion, canon change or merge authorization.
