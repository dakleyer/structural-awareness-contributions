# R01 Viability as a Trilemma — Proof Sketches and Review Plan

Oct 4, 2026 · @Ivan

## 1. Purpose and status

This document fixes, as proof sketches, the two results that define "viability" in R01: a trilemma between cost, risk and efficacy, and a classification of which technologies remove it and which only shrink it. Both are sketches written in one pass by a single reviewer (an AI assistant) on top of the M02 fixture at commit 419b8e9. None is a reviewed proof and none has been machine-checked.

- **Result 1 (Trilemma, section 4).** On a family of configurations, any two of {low cost, low risk, high efficacy} are jointly attainable, and the three together are not.
- **Result 2 (Technology classification, section 5).** The infeasible region never becomes empty for technologies whose information cost stays positive. It disappears only if verification becomes free and riskless inside execution itself.
- **Link (section 6).** Result 2 is Result 1 with the technology as the parameter. Both rest on one counting lemma (Lemma 1).
- **Review (sections 7 and 8).** Section 7 lists the assumptions that break the results if false; section 8 says what to review and how.

This is not a result about any real agent framework, not a claim about EA, and not an infeasibility proof for all policies on the original R01 campaign. Those remain M03, M04 and the technology block.

## 2. What we want to prove

We want a universal statement, not a collection of worked cases: for every technology of a stated kind, there are configurations where cost, risk and efficacy cannot all be good at once, however clever the policy.

1. **The three are coupled, not independent.** Information about the hidden binding costs something. Acting without it risks a violation. Refusing to act sacrifices efficacy.
2. **Each pair is attainable, so the trilemma is not vacuous.** Cheap and safe but useless: abstain or take the safe route. Cheap and effective but unsafe: commit blindly. Safe and effective but expensive: buy the information first.
3. **The triple is not attainable on a family of configurations.** More layers, more independent hidden bindings, a longer distance between the safe route M and the attractive route P: under a budget with fixed relative slack, no policy gets all three.
4. **Better technology moves the threshold but does not remove the region**, except through one specific kind of improvement (section 5).

Quantifier order is the main trap. The defensible claim is: for every technology with positive information cost there is a family and a budget where the triple is infeasible. The claim "one budget makes the triple infeasible for every technology" is false, because a good enough technology makes any fixed slack sufficient.

## 3. Formal setting

The setting generalizes M02 from one hidden bit to L independent hidden bits, so that information need can grow with problem size.

**Family F\_L.** There are L layers. Layer l has three nodes: m\_l (always active, benefit 1), x\_l (active iff chi\_l = 0, benefit 2) and y\_l (active iff chi\_l = 1, benefit 2). The hidden binding omega = (chi\_1, ..., chi\_L) is uniform on {0,1}^L. Executing an inactive node is a violation (V = 1), permanent and irreversible. The technical optimum is J\* = 2L; the safe route M (all m nodes) gives J = L. M02 is the degenerate instance with 3 layers but a single shared bit.

**Costs.** Setup costs c\_e. Each layer needs a gate of review, decision and execution, cost g = 3 per layer. Information about omega costs c per bit (Axiom A below). With s the spend above the execution minimum:

```latex
R_{exec}(L)=c_e+gL,\qquad s=R-R_{exec}(L),\qquad t(R)=\left\lfloor s/c\right\rfloor,\qquad d=L-\lfloor\varepsilon\rfloor
```

Here t(R) is the number of bits affordable and d is the minimum number of non-m nodes a legitimate delivery of quality at least J\* - epsilon must contain.

**Policy and outcomes.** A policy pi is history-dependent and randomized, with a hard cap R on total cost. Three outcome events:

- **T**: a complete route is delivered with technical quality at least J\* - epsilon, ignoring legitimacy.
- **V**: some inactive node was executed.
- **Legitimate success**: T and not V, with probability sigma.

**The three goals.** Efficacy eta = P(T). Risk rho = P(V). Cost is the cap R. Each probability is read either worst-case over omega (WC) or on average (AVG); the two are never merged. Legitimacy is derived, not a fourth axis:

```latex
\sigma \;\ge\; \eta-\rho \qquad(\text{Fr\'echet})
```

Efficacy is deliberately technical. If efficacy already required legitimacy, the pair (low cost, high efficacy) would be infeasible by itself and there would be no trilemma, only a cost-efficacy trade-off.

**Axioms for the class T\_lin(c).**

| Axiom | Statement |
| --- | --- |
| A (information cost) | An operation with N possible outputs costs at least c log2 N, with c > 0. |
| B (independent bits) | omega is uniform on {0,1}^L, with L unbounded. |
| R-loc (receipt locality) | Executing a node reveals only that node's binding status, and only after the effect. |
| NB (no barrier) | No operation tests a node's activity without executing it; V is permanent. |

## 4. Result 1: the trilemma

On F\_L every pair of goals has a witness policy, and the triple is infeasible below a budget whose slack grows linearly in L.

**Theorem 1.** Fix a technology in T\_lin(c), thresholds 0 <= r < e <= 1 and a tolerance epsilon < L. Then:

- **(a) Cost and risk.** At R = R\_exec, the safe policy (route M, abstain on x and y) has rho = 0 and eta = 0.
- **(b) Cost and efficacy.** At R = R\_exec, the blind policy (x on every layer) has eta = 1, with rho\_WC = 1 and rho\_AVG = 1 - 2^(-L).
- **(c) Risk and efficacy.** At R = R\_exec + c d, the policy "buy d bits, match on those d layers, take m elsewhere" has eta = 1 and rho = 0. Its quality is L + d = 2L - floor(epsilon), so it meets the target.
- **(d) The triple.** Every policy with cost at most R satisfies eta - rho <= sigma <= 2^(t(R) - d). Hence no policy attains cost at most R, risk at most r and efficacy at least e whenever:

```latex
e-r \;>\; 2^{-(d-t(R))}
```

- **(e) Tightness.** With t = d - j bits bought and j layers guessed blind, sigma = 2^(-j) is attained. So (d) is tight up to the additive constant log2(1/(e-r)) in the number of bits.

**Lemma 1 (counting).** Let B(s) be the maximum information capacity, in bits, that spend s can buy. Let b\* be the minimum number of independent bits that any legitimate delivery meeting the quality target must pin down (b\* = d in F\_L, b\* = 1 in M02). Then every policy with cost at most R satisfies:

```latex
\sigma \;\le\; 2^{\,B(R-R_{exec})-b^{*}}
```

**Proof sketch.**

1. A randomized policy is a mixture of deterministic ones and sigma is an average, so it is enough to bound deterministic policies.
2. Along any adaptive run the total capacity bought is at most B(s). By Axiom A the number of distinct paid-answer transcripts is therefore at most 2^B(s).
3. On the event not-V, a legitimate run is determined by its paid transcript. By R-loc each receipt only confirms what the policy had already assumed, so it adds no information. A wrong blind guess reveals chi only after the violation has happened.
4. Hence each transcript fixes one delivered route, and that route is legitimate on at most 2^(L - b\*) worlds, because it must agree with omega on at least b\* independent bits.
5. The legitimate-success worlds number at most 2^B(s) times 2^(L - b\*). Under uniform omega this gives the bound. Worst-case sigma is at most average sigma, so WC is covered. Frechet then gives eta - rho <= sigma.

**M02 as the base case.** M02 has one shared bit, so b\* = 1, with c = 1, c\_e = 2 and g = 3. At R = 11 there is no spare spend and sigma <= 1/2 < 3/4. At R = 12 one bit is affordable and the bound equals 1. This matches M02's controls. The 76 checks verify the arithmetic of this instance, not Lemma 1.

**Width of the infeasible band** (c\_e = 2, g = 3, c = 1, epsilon = 0, e - r = 3/4):

| Instance | R\_exec | Triple infeasible for R in | Width | Width / R\_exec |
| --- | --- | --- | --- | --- |
| M02 (3 layers, 1 shared bit) | 11 | \[11, 12) | 1 | 9% |
| F\_1 | 5 | \[5, 6) | 1 | 20% |
| F\_3 | 11 | \[11, 14) | 3 | 27% |
| F\_10 | 32 | \[32, 42) | 10 | 31% |
| F\_100 | 302 | \[302, 402) | 100 | 33% |

M02's band has width c because it needs only one bit. In F\_L the width grows linearly in L, and its share of R\_exec tends to c(1 - alpha)/g, where alpha = epsilon/L.

## 5. Result 2: which technologies remove the trilemma

A technology removes the trilemma only if the information needed for legitimate success becomes available at no marginal cost and no risk inside execution. Every other improvement shrinks the region or rescales it, and leaves it non-empty.

Summarize a technology by f(b), the cost of pinning b independent bits (the inverse of B in Lemma 1). By Lemma 1 the triple is infeasible exactly when B(s) < b\* - log2(1/(e-r)). So the infeasible band starts at R\_exec and has width about f(b\*), with b\* = (1 - alpha) L in F\_L.

**Theorem 2.**

- **(i) Persistence under linear cost.** Let f(b) = c b and give the budget a fixed relative slack: R = (1 + lambda) R\_exec(L). As L grows with alpha = epsilon/L fixed, the triple is infeasible when lambda < c(1 - alpha)/g and feasible when lambda > c(1 - alpha)/g. The threshold slack is:

```latex
\lambda^{*}=\frac{c\,(1-\alpha)}{g}
```

- **(ii) Scale-only improvements.** Cheaper probes, higher-capacity or lower-noise probes (effective cost c divided by capacity per unit) and cheaper detection change lambda\* by a constant factor. They never bring it to zero while c > 0. For any fixed c > 0 and any slack below lambda\*, the region persists for large L.
- **(iii) Elimination.** The band is empty for every L at every R >= R\_exec only if the needed information costs nothing and carries no risk (Tier 0). Tiers 1 and 2 leave a non-empty band whose share of R\_exec tends to zero.

| Tier | Information cost f(b) | Example | Band width | Share of R\_exec as L grows | Trilemma |
| --- | --- | --- | --- | --- | --- |
| 0 | zero | The gate's own review certifies the binding; free pre-effect barrier | none | none | Eliminated |
| 1 | constant c0 | One global certificate (the M02 certificate) | about c0 | tends to 0 | Non-empty, vanishing share |
| 2 | c log b | Hierarchical or aggregated certificates | about c log L | tends to 0 | Non-empty, vanishing share |
| 3 | c b | Per-bit probes, per-node verification | about c(1 - alpha)L | tends to c(1 - alpha)/g | Persistent |
| 3' | a b, with risk-free barrier | Pre-effect barrier where each attempt costs a | about a(1 - alpha)L | tends to a(1 - alpha)/g | Becomes a cost-efficacy dilemma, rho = 0 |

**Proof sketch.**

1. **Tier 3 and (i).** Take B(s) = floor(s/c) in Lemma 1 (Theorem 1). With R = (1 + lambda)(c\_e + gL), the affordable bits are t = floor(lambda(c\_e + gL)/c), about lambda g L / c. The triple is infeasible iff t < d - O(1), which is lambda g / c < 1 - alpha. The matching policy of Theorem 1(c) gives feasibility on the other side.
2. **(ii).** Replacing c by c/kappa multiplies lambda\* by 1/kappa, a constant factor. The condition lambda < lambda\* has no solution only when c = 0.
3. **Tier 1.** A certificate of cost c0 covering all bits gives B(s) = 0 for s < c0 and B(s) = L for s >= c0. At s = 0 Lemma 1 gives sigma <= 2^(-b\*), which is below e - r whenever b\* >= 1 and e - r > 1/2. So the band is \[R\_exec, R\_exec + c0), non-empty for every c0 > 0.
4. **Tier 2.** With f(b) = c log b, B(s) = 2^(s/c) and the band width is about c log2(b\*).
5. **Tier 0.** With B unbounded at s = 0, the policy of Theorem 1(c) runs at R\_exec and no band exists.
6. **Tier 3'.** A barrier removes V, so rho = 0 and sigma = eta. Each refused attempt reveals at most one bit at cost a, so Lemma 1 applies to eta with B(s) = floor(s/a). The band persists in the cost-efficacy plane.

**Reading.** "Never eliminated" is exact only in the absolute sense: any f with f(1) > 0 leaves a band at zero slack. In relative terms Tiers 1 and 2 shrink it to nothing. Improving risk, efficacy or verification cost by constants stays inside Tier 3. Only a change of scaling class, so that verification stops growing with the distance between M and P, changes the picture.

## 6. How the two results link

Both results are one inequality read two ways: Lemma 1 bounds legitimate success by what the budget can buy, and the technology decides how much a budget buys.

1. **Lemma 1** bounds sigma by 2^(B(s) - b\*). It uses only Axiom A, independent bits and receipt locality.
2. **Theorem 1** fixes B(s) = floor(s/c), supplies a witness policy for each pair, and reads the bound as a band of linear width.
3. **Theorem 2** varies B, which is the technology, and reads the same bound as the band width f(b\*). The tiers are the possible growth rates of f.
4. **M02** is Theorem 1 with b\* = 1. Its 76 checks cover the witnesses and controls of that instance, not the lemma.

The sketches map onto the R01 tasks as follows.

| Piece | R01 task | What closes it |
| --- | --- | --- |
| Contract: definitions, axioms A, B, R-loc, NB, technical efficacy | M10, P03 | Reconciled and accepted explicitly |
| Lemma 1 for adaptive, randomized, receipt-informed policies | M03 | Independent proof plus exhaustive finite check |
| Band width, thresholds, tightness, boundary cases | M04, M11 | Region stated as proved, measured or unresolved |
| Prior art and cheaper certificates | M06, P01, P02 | Counterexamples preserved, differential restated |

## 7. Assumptions and attacks

Eight assumptions carry the results, and each one, if false, moves the technology to a lower tier or removes the band. The first attacks to run are A1 and A2, because a cheaper legitimate certificate is the most likely way to change the outcome.

| ID | Assumption | If false | Attack or question | Task |
| --- | --- | --- | --- | --- |
| A1 | Information costs at least c per bit, with c > 0 | A cheaper certificate or protocol lowers the tier | Search for legitimate certificates, caching and reuse that beat linear cost; classify each by tier | M06, M10 |
| A2 | The M permission certificate is free in the initial evidence, while the binding state costs 1 | If the state ships in the manifest or the mandate query, the band vanishes (Tier 0) | Justify the asymmetry or price both | M10, P03 |
| A3 | A receipt reveals only the executed node's status | A safe execution that reveals the whole binding register is a free probe | Check exactly what each receipt contains | M10 |
| A4 | No pre-effect barrier; V is permanent | A barrier, dry run or reversible effect decouples risk from information | Treat as a changed contract; classify as Tier 3' or Tier 0 | M10, M11 |
| A5 | Bits are independent and uniform | Correlated or structured bindings lower b\* | State the prior; test correlated families | M11 |
| A6 | The budget R is a hard cap per run | With an expected-cost budget, randomizing between query and no query changes the thresholds | Prove both readings; keep AVG and WC apart | M03 |
| A7 | The gate costs g = 3 per layer and is mandatory | A batched review lowers R\_exec and moves the band | Treat g as a parameter, not a constant | M10 |
| A8 | Efficacy is technical; legitimacy is derived | A legitimacy-based efficacy removes the trilemma and leaves a dilemma | Fixed in section 3; confirm in the contract | M10, P03 |

A counterexample under any row does not refute the theorem. It changes the technology class, and the result is then restated for that class. A genuine counterexample would be a policy that violates Lemma 1 inside the stated axioms.

## 8. Review plan: what to review and how

The review must try to break the sketches, and it must be done by someone other than the author. Run the steps in order; each has a pass criterion that can fail.

| Step | Object | Question | Method | Pass criterion | Task |
| --- | --- | --- | --- | --- | --- |
| 1 | Definitions in section 3 | Is the trilemma real: each pair has a witness and the triple has none? | Enumerate the three witness policies exactly for L = 1 to 4 | Each witness reproduces its stated cost, risk and efficacy | M10, P03 |
| 2 | Lemma 1 | Does the counting argument hold for adaptive, randomized, receipt-informed policies? | Re-derive independently; enumerate the full policy tree under a hard cap for L <= 3 and compute maximum sigma | Maximum sigma never exceeds 2^(t - b\*) | M03 |
| 3 | Tightness | Is the bound attained at t = d - j for every j? | Construct the policy with j blind guesses and compute sigma | Equality 2^(-j) for j = 0 to d | M03, M04 |
| 4 | Boundaries | Do strict versus inclusive thresholds and degenerate cases break anything? | Tabulate epsilon = 0, epsilon >= L, e = r, c\_e = 0, g = 0 | Every case either holds or is excluded in the statement | M04 |
| 5 | Assumptions A1 to A8 | Is there a legitimate protocol, certificate or receipt that changes the tier? | Adversarial search; keep each counterexample and classify its tier | Every counterexample is preserved and placed in the tier table | M06, M11 |
| 6 | Prior art | Is Lemma 1 already known, and what does this add? | Literature intake with locators: value of information, metareasoning, budgeted and constrained POMDPs, safe exploration with irreversible constraints, query and communication lower bounds | A matrix of claim against source, with the differential restated | M06, P01, P02 |
| 7 | Independent check | Do two implementations agree? | A second implementation of the enumeration, written without the first one's code | Outputs agree byte for byte | C05 |

My belief, to be checked in step 6, is that Lemma 1 is a standard counting bound of Fano type. If so, any novelty lies in the normative-binding and irreversible-violation framing and in the tier classification, not in the bound.

**Possible verdicts.**

- **Proved.** Steps 2 to 4 pass and no counterexample survives step 5.
- **Proved with narrowed scope.** A counterexample changes the class; the result is restated for the narrower class.
- **Rejected.** A policy beats the bound inside the stated axioms, or the definitions make the trilemma vacuous.

This sketch alone closes none of M03, M04 or C05.

## 9. Non-claims, corrections and open items

These are sketches in an idealized ledger, and three statements made earlier in the discussion are superseded here.

**Non-claims.**

- Nothing here is a reviewed or machine-checked proof.
- Nothing applies to a real agent framework, to EA, or to any named technology's tier. That needs measurement in the technology block.
- Nothing covers the original R01 campaign generator (a random single invalid witness); F\_L is a different family.
- The band widths and shares in the tables hold only for the stated parameters and the idealized ledger, with zero sampler cost.

**Corrections to earlier statements.**

1. Efficacy was first proposed as legitimate delivery. That definition gives no trilemma, since the pair (low cost, high efficacy) would already be infeasible. Efficacy is now technical, and legitimacy is derived through Frechet.
2. Execution cost was said to stay fixed while information cost grows. Execution also grows, at g per layer. What grows is the gap, linearly, and its share of R\_exec tends to c(1 - alpha)/g.
3. The relation rho >= eta at M02 with R = 11 referred to legitimate delivery. In the corrected definitions the M02 statement is sigma <= 1/2.

**Open items.**

- Lemma 1 under expected-cost budgets, where randomizing between query and no query may shift the thresholds.
- Correlated or structured bindings, where b\* is below d.
- Multi-agent versions and whether collaboration changes the tier.
- Whether the distance between M and P corresponds to L or to b\*; the sketch assumes they grow together.
- Whether partial or noisy certificates give a better bound than the capacity argument.
- The parity block, which is a separate construction.

**Sources opened.** [M02 worlds and controls](https://github.com/dakleyer/structural-awareness-contributions/blob/419b8e93b4b13a3a96ca1534b0d134be4a764c78/research/ecosystem-awareness/baseline/reductions/00G-R01/M02_WORLDS_AND_CONTROLS.md) and [strategic workplan](https://github.com/dakleyer/structural-awareness-contributions/blob/419b8e93b4b13a3a96ca1534b0d134be4a764c78/research/ecosystem-awareness/baseline/reductions/00G-R01/STRATEGIC_WORKPLAN_AND_EXECUTION_PROMPT.md), both at commit 419b8e9. I did not run the M02 checker or open the fixture JSON.
