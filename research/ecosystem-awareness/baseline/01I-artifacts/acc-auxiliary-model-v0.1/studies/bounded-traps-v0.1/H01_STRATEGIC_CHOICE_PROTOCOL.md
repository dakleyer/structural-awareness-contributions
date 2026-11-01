# H-01 — Strategic coordination versus a physically forbidden transition

**ACC / bounded-traps research supplement · 1 November 2026 · Stage A synthetic study**

**Scientific owner and source:** Iván Abril Palma / The Integral Management Society. The existing PR #42 study and its historical output remain the source-owned feasibility example. This supplemental model/code and audit note are AI-assisted research implementation for independent scientific review, not an amendment to the original theory or the ACC/ITU-T corpus.

## 1. Auditor's precise question

[Scientific audit PR #58, H-01](https://github.com/dakleyer/structural-awareness-contributions/pull/58) correctly distinguishes two different phenomena:

- **Original source / EX-LINEAR-01:** the constraints x1≤x2 and x2≤x1 exclude both intermediate profiles (1,0) and (0,1). The source's only feasible states are (0,0) and (1,1), with utilities (4,4) and (5,5). Joint atomic switching could work, but **an agent cannot make the first unilateral move**. This is a feasibility/protocol result, not proof of a choice equilibrium.
- **H-01 requested extension:** all four binary profiles should be physically feasible, but agents at a Pareto-inferior profile should **choose not to move**, because a unilateral deviation lowers their own payoff. Test this with actor-specific payoff mechanics, computed best responses and Nash equilibria. Do not relabel the source example.

This is the established *stag hunt / assurance / coordination game* phenomenon, not an original Nash-equilibrium theorem. Classical reference: [Stanford Encyclopedia of Philosophy, Prisoner's Dilemma, §8 "The Stag Hunt and the PD"](https://plato.stanford.edu/entries/prisoner-dilemma/), and [Epistemic Foundations of Game Theory §5.1](https://plato.stanford.edu/entries/epistemic-game/). An ACC contribution, if any, concerns **faithful separation of incentives, physical capacities, transition protocols and legitimate authority**, not discovery of the game.

## 2. Explicit finite model — no answer stored as an equilibrium label

The executable [strategic_choice.py](strategic_choice.py) reads [H01_STRATEGIC_STUDY.json](H01_STRATEGIC_STUDY.json). There are n declared binary agents (2≤n≤6), a bounded finite physical state set, an optional family of rational linear capacity constraints, and each actor's separate payoff parameters.

For actor i, the finite utility *in that actor's own declared toy units* is computed from the full joint profile x:

    u_i(x) = b_i + x_i(r_i - c_i)
             + Σ_{j≠i} x_i x_j s_{i,j}
             - Σ_{j≠i} (1-x_i)x_j e_{i,j}

where b is the retained baseline, r is individual return, c is investment cost, s is a **declared pairwise complementarity**, and e is the cost/exposure while i remains inactive when j moves. Neither s nor any welfare number is inferred from fruit, a ministry count, suffering or hidden epistemic C/D. The observed source mechanism does **not** claim this parametric payoff law was implemented in any prior real operation.

All profiles and payoff vectors are calculated from these parameters using exact rational arithmetic (not prefilled outcome matrices). Material feasibility is checked separately by physical budget and explicit linear inequalities. Nash equilibrium is evaluated **only within the declared feasible unilateral deviation set**:

- A pure Nash profile has **no actor with a profitable feasible unilateral deviation**.
- A **strict strategic trap** additionally requires *every* actor to have an available unilateral deviation, each individually unprofitable, plus a physically feasible Pareto-superior joint alternative.
- If unilateral changes are forbidden, the label is **feasibility/protocol trap**, even if the current state would be a vacuous Nash equilibrium over the restricted feasible set.
- With profitable unilateral escape, weak ties, no global Pareto gain or no pure Nash equilibrium, report the corresponding negative result. A deterministic strict-better-response path may stop at Nash or cycle; it is never presumed to optimize globally.

**No aggregation of actor utilities into a global scalar.** Pareto dominance is evaluated componentwise within the actor vector. Original economic dimensions E/R/C/V are not renamed A/B/C/D or converted automatically into one common welfare unit.

### Core positive witness: four feasible states

For the source-linked but **new** strategic case, b_i=3, investment c_i=3, complement s_{ij}=5, inactive exposure e_{ij}=1, and standalone return r_i=0 (symmetric two actors):

| Joint actions (A,B) | Computed utility A | Computed utility B | Material status |
|---|---:|---:|---|
| (0,0) | 3 | 3 | Feasible |
| (0,1) | 2 | 0 | Feasible |
| (1,0) | 0 | 2 | Feasible |
| (1,1) | 5 | 5 | Feasible |

The **engine**, not the manifest, computes Nash equilibria (0,0) and (1,1). At (0,0), each actor's feasible unilateral move changes their own payoff by **−3**. Thus staying is a strict best response, even though (1,1) Pareto-dominates (0,0). The source (0,0)→(1,1) constrained model, by contrast, forbids the intermediate moves and returns a different classification.

The separate two-actor belief exercise introduces a **declared** subjective p that the other actor moves. Under this payoff law, moving has expected payoff 5p and staying 3−p. Therefore p<1/2 favors staying, p>1/2 favors moving, and at p=1/2 the actor is indifferent. These are conditional numerical assumptions, **not a probability of an unknown epistemic C or D** or measured beliefs of individuals.

## 3. Proposed joint coordination, its burden and authorization are different layers

[The source's E/R/C/V dimensions](README.md#1-cuatro-coordenadas-de-decisión-no-cuatro-agentes-soberanos) remain separate from strategy choices. A physically attractive candidate can fail because participation is not individually acceptable, resources for coordination are unavailable, rights are missing, or a protocol/consent is absent.

The executor checks, independently and in order, that:

1. The target profile is technically feasible **and** target resources plus physical joint setup do not exceed the declared budget.
2. Each participant's *net* result after explicitly costed coordination and any transfers meets its own reservation floor and the declared strict or weak gain requirement. The model does not assume a positive global aggregate can compensate an unconsenting participant.
3. Transfers of actor payoff units are **zero-sum** and require an explicit transfer-authority status; a transfer is not legitimate merely because it balances mathematically.
4. Explicit consents, coordination protocol and institutional authority are **PASS**, rather than FAIL or UNKNOWN. Consent is not derived from an attractive payoff.
5. Only then does the **synthetic candidate become admissible under stipulated assumptions**. It is **not** an executed real-world commitment or a source of rights.

The reference case permits a joint move with zero-sum costs, but negative controls show a physically superior solution becoming inadmissible under excessive cost, missing consent, unknown authority, missing joint protocol, inadequate physical budget or stronger per-actor reservation floors.

### Conventional comparator: same capabilities, not a weak straw man

Two equally capable proposed coordinators are represented: CONVENTIONAL_COORDINATOR and ACC_META_PROTOCOL. Both receive the **same data, physical candidate, authority and transition mechanism**, so **neither is given a technical advantage**. Instrumental information prices are varied *only* as separate hypothetical accounting: the conventional method can be cheaper, the ACC-labelled method can be cheaper, or they tie. A cost reversal **cannot alter payoffs, admission or physical resources**. No claimed superiority of EA or agentic systems follows from these synthetic price regimes.

## 4. Versioned acceptance and falsification corpus

The manifest contains **19 source-anchored experiments** (one positive strategic case, negative controls, source feasibility control, governance, voluntary acceptance, finite transfer, price comparisons) and the tests additionally construct a three-actor coordination game and a two-actor no-pure-Nash/cyclic strict-response counterexample.

| Family / example | What the experiment must establish |
|---|---|
| **H01_STRICT_COORDINATION_TRAP** | All four states feasible; (0,0) and (1,1) strict pure Nash; private deviation −3; (1,1) Pareto-superior |
| **H01_ORIGINAL_FEASIBILITY_REFERENCE / EX-LINEAR-01** | Only (0,0) and (1,1) feasible under original constraints; **not classified** as a strategic choice trap; source outputs unchanged |
| **H01_PROFITABLE_UNILATERAL_ESCAPE** | Changing declared incentives makes staying non-Nash; the method must admit this counterexample |
| **H01_WEAK_BEST_RESPONSE_TIE** | Zero payoff difference is not evidence of strict rational refusal |
| **H01_NO_PARETO_JOINT_GAIN** | An attractive-sounding coordination arrangement is rejected if participants are not jointly better off |
| **H01_TOO_EXPENSIVE_COORDINATION / BUDGET / RESERVATION** | Benefits, resources and participant acceptance are independently tested and can block |
| **H01_NO_CONSENT / UNKNOWN_CONSENT / UNKNOWN_AUTHORITY / NO_PROTOCOL** | A physical opportunity does not invent consent, authority or a collective action mechanism |
| **H01_CREDIT_WITHOUT_COMPENSATION / WITH_BALANCED_TRANSFER / NO_AUTHORITY** | Unequal actor gains, *authorized* net-zero transfer and still-unknown rights remain separate |
| **H01_CONVENTIONAL_CHEAPER / META_CHEAPER / EQUAL_COST** | An equally capable conventional solution gets full credit and prices cannot manufacture an informational advantage |
| **Three-actor and no-pure-Nash negative controls** | Generic bounded n-player engine, exact finite state scan, no fake universal equilibrium |

**Relationship to other author examples:** EX-BAN-01/02, EX-BAN-03 (donor/credit), EX-BAN-04 (two fruit), EX-ROBIN-01, EX-MIN-01 and EX-APPLE-01 retain their **original** source questions in [EXAMPLE_LEDGER.md](EXAMPLE_LEDGER.md) and PR #69. The H-01 willingness-to-coordinate parameters are **not evidence** about any of their real participants, benefits, credit or human experience. The transfer example tests just the *abstract* necessary condition of two individually accepted shares; no real charity, ministry or banana allocation is silently converted into this game.

## 5. Reproduction, invariants and reviewer request

From this directory (Python 3.12, standard library):

    python -B -m unittest discover -s . -p test_bounded_traps.py -v
    python -B -m unittest discover -s . -p test_strategic_choice.py -v
    python -B bounded_traps.py > /tmp/old_bounded_traps.json
    python -B strategic_choice.py --manifest H01_STRATEGIC_STUDY.json --output /tmp/h01_strategic_results.json

CI checks the **original main source blob hash**, original historical output reference blob, all original bounded_traps tests, the new H-01 tests and the source-owned example report; it publishes the new JSON under a separate synthetic artifact. No original source result is edited to force a green test.

Reviewers are asked to try mutations of the payoff coefficients, feasibility constraints, resource caps, authorizations, consent and common instrument prices; verify the classification switches correctly; verify Nash, full feasible deviations and beliefs independently; and ensure that equal capabilities never imply exclusive ACC superiority. Compare feasible unilateral reachability to best-response choice without confusing them.

### Claim status

- **Proven in a finite stipulated game:** the existence of a strict Pareto-inferior Nash equilibrium under four technically feasible states, with explicitly computed payoffs and adverse controls.
- **Not proven:** actual human irrationality or rationality, spontaneous action in an organization, a universally superior coordination architecture, the right to enforce a transfer, true preferences, measurable real-world opportunity gap, novelty over stag hunt, or a probability over residual C/D.
- **Review state requested:** H-01 **RESPONDIDO after independent verification**. It cannot be CERRADO or promoted by CI alone; source-owner and audit authorization remain necessary.

The operational lineage of [JubAp.NET Field Notes](https://jubap.net/field-notes/) documents proposal–authorization–commitment boundaries in other contexts, but it is **not evidence that this game-theoretic model was a deployed optimization capability**. The [Tegrity.AI programme](https://tegrity.ai/) frames ecosystem epistemic and coordination questions, but does not validate any empirical equilibrium claim here.

## 6. Predeclared incentive sensitivity, separate from the named examples

The [manifest](H01_STRATEGIC_STUDY.json) predeclares a **four-axis, 180-cell** grid: 3 standalone-return values × 5 investment-cost values × 4 pairwise-complementarity values × 3 joint payoff-burden values. Every cell is run through the same physical feasibility, actor-payoff, Nash and joint-admission algorithms; neither the label "Nash" nor the admission verdict appears in the input. Every output retains payoff vectors, profitable unilateral deviation count, all pure Nash profiles, joint status, and the four input values.

This is a counterexample test against generating only favourable stag-hunt examples. Some cells must show profitable unilateral escape, others a Pareto-superior but blocked joint candidate, weak equilibrium, or no jointly superior alternative. If altering complementarity or cost leaves the output fixed, the study fails. No metric is calculated by adding actor welfare or converting a coordination payoff burden into information price.

The grid is not independent empirical evidence of an economic prevalence or a survey of individuals. It deliberately perturbs a bounded model of incentives while preserving the same question and authorization statuses. It must be reported as a synthetic sensitivity surface, not repeated confirmation of its own premise.


## 7. Received H-01 experimental results — 1 November 2026

**Source of executable figures:** [GitHub Actions #41290524931](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/41290524931), **success**. The 19 named scenarios and the separately predeclared 180-cell sensitivity surface ran with **31/31 new H-01 tests passing**, alongside all original bounded-traps and broader document-integrity regressions. The source-owned frozen outputs and original bounded_traps.py blob hashes were explicitly checked and unchanged.

### Core computed witness and its falsifiers

| Experiment | Nash / physical distinction | Joint proposal result |
|---|---|---|
| Strict strategic coordination | All four profiles feasible; strict Nash at 00 and 11; individual deviation −3 at 00; 11 Pareto-superior | Admissible **under synthetic consent, authority and resource assumptions** |
| Original EX-LINEAR-01 feasibility witness | Only 00 and 11 technically feasible; unilateral intermediate moves do not exist | Joint change conditionally available, but **no strategic refusal is demonstrated** |
| Profitable unilateral control | The choice to stay is no longer Nash; strict better-response can escape | Joint coordination not necessary to claim unilateral blockage |
| Weak best-response tie | Nash at 00 is weak, **not a strict refusal** | No claim of strict rational trap |
| No jointly superior target | Nash may still exist, but joint candidate does not Pareto-dominate | Not an improvement by the source criterion |
| Missing consent / authority / joint protocol | Payoff temptation and Nash source state may be unchanged | Explicitly FAIL or UNKNOWN; never real commitment |
| No available setup budget | Both game states physically feasible, but required switch setup resources are not | Materially infeasible transition |
| Zero-sum compensation | One actor lacks strict gain before transfer; both gain after declared authorized transfer | Only conditionally admissible; transfer itself needs a separate right |
| Strong conventional peer | Conventional and ACC-labelled arms receive the same transition proposal and rights | Conventional can be cheaper, equal or more expensive **solely by the hypothetical instrument cost** |

The three-actor negative/positive extensions and a **no-pure-Nash, cycling best-response** counterexample pass. The engine therefore does not assume every finite game must converge to a pure equilibrium.

### Actual 180-cell sensitivity outcomes (not preregistered winners)

| Mechanism classification, computed from the payoff law | Cells |
|---|---:|
| Strict rational coordination trap | **39** |
| Profitable unilateral escape: not an inferior Nash trap | **72** |
| Weak rather than strict Nash equilibrium | **27** |
| No Pareto-superior joint target | **42** |
| **Total** | **180** |

Under the assumed PASS governance and adequate resource budget of this parameter sweep, **114** configurations have an individually admissible joint payoff and **66** fail the voluntary participation test. Those 114 are **not real-world authorizations**, and admission is a different question from Nash classification. The individually named scenarios additionally test governance FAIL/UNKNOWN, coordination resource budgets and explicit credit permissions.

One particularly informative control fixes private return = 0, investment = 3, complementarity = 4. With actor coordination burden 0, both receive 4 instead of the initial 3 and the joint candidate passes. With burden 1, the proposed net result becomes 3, so a strictly improving voluntary commitment is **not** justified. The **same strict Nash source state exists in both cases**: whether a trap exists and whether a remedy is admissible are demonstrably distinct.

**Interpretable result:** the research question H-01 now has a source-preserving, reproducible positive finite strategic-choice witness and a falsifiable family of negative counterparts. It is **not** evidence that all constrained organizations display Nash behaviour, that ACC invented coordination games, or that an ACC-labelled coordinator outperforms a competent conventional one.

### Exact independent audit handoff

1. Reproduce the four computed payoff profiles and original two-state constraint from source files, not from the report's status labels.
2. Verify that all unilateral moves are feasible and strictly unprofitable at strategic 00, while they are physically infeasible in the frozen original EX-LINEAR-01.
3. Repeat best-response and Pareto checks for the 19 scenarios and all 180 sweep cells. Inspect profitable deviation, weak equilibrium, no pure Nash and no gain counterexamples.
4. Recompute consent, transfer balance, reservation floors, physical setup units and unknown authority. Do not infer authorization from a positive payoff.
5. Ensure both comparison coordinators have **identical capabilities**, and that instrument price variations never change Nash states or physical admission.
6. Inspect original file hashes, CI artifacts and author-example crosswalk; check that no changes were made to controlled mathematics, human preference evidence or synthetic/empirical status.

**H-01 can be marked RESPONDIDO only after independent adjudication, and not CERRADO until applicable accepted integration.** A green CI run is a reproducible software result, not institutional or scientific adoption.
