# R01 M06 — Initial primary-source and counterexample intake

Targeted intake v0.1 · M06 IN_PROGRESS · Self-review, not independent validation

[R01 README](./README.md#bot-start-here) · [M10/P03 contract audit](./M10_P03_CONTRACT_AND_MEASUREMENT_AUDIT.md) · [M02 candidate](./M02_WORLDS_AND_CONTROLS.md) · [Mathematical plan](./MATHEMATICAL_FEASIBILITY.md)

Input commit: `419b8e93b4b13a3a96ca1534b0d134be4a764c78`. Actual UTC timestamp and source coverage are recorded in M10_RELEASE_CHECKS.json. Owner/reviewer: Codex, on user instruction; same-agent review. This intake does not close M06's full proof audit, communication review, broader literature search, P01/P02 or any novelty claim.

## 1. Search and reading coverage

Queries covered decision-tree/query complexity, randomized rules, certificates and exact binomial zero-event uncertainty. Broad search produced irrelevant certificate material; it was excluded. A focused search located the author-hosted survey and institutional statistics documentation. Search snippets alone were not used as evidence. Relevant sections were opened and read directly. This is targeted intake for N=1, not a systematic survey or a read of every method in the prior differential table.

| ID / primary source | Exact scope consulted | Supported statement |
|---|---|---|
| S1 — Harry Buhrman and Ronald de Wolf, *Complexity Measures and Decision Tree Complexity: A Survey*, author-hosted preprint dated 10 October 2002 | Introduction; §§3.1–3.2 and 4.1; PDF pages 2, 5–6 and 8 (1-based) | Adaptive queries read individual input bits. Randomized trees may be represented by a distribution over deterministic trees. Their bounded-error definition uses a worst-case query cap; certificates fix output over all consistent inputs. |
| S2 — Sanjeev Arora and Boaz Barak, *Computational Complexity: A Modern Approach*, chapter 11, Internet draft January 2007 | Opening definitions, §11.1/Definitions 11.7–11.8 and §11.2/Definition 11.13; PDF pages 3, 5–7 | Certificate complexity and randomized-tree representations are established concepts. This draft's randomized metric averages query costs over trees computing the function and then takes the worst input. |
| S3 — NIST Dataplot, *EXACT BINOMIAL* | Purpose/description and one-sided syntax | Supports exact binomial proportion limits and separate one-/two-sided procedures, particularly for small counts. |
| S4 — NIST/SEMATECH handbook §7.2.4.1, *Confidence intervals* | Confidence-interval section, including small-count exact construction | Normal approximations may be unsuitable with small samples or few failures. |

Source URLs:

- S1: https://homepages.cwi.nl/~rdewolf/publ/qc/dectree.pdf
- S2: https://www.cs.princeton.edu/theory/complexity/dectreechap.pdf
- S3: https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/exacbino.htm
- S4: https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm

S1 is a historical source for the consulted definitions; old open-problem statements elsewhere are not treated as current facts. S2 is explicitly an Internet draft, not asserted to be the final textbook. The source copies are not redistributed. No source asserts an R01 impossibility theorem, a service price, a clinical/security harm estimate or EA advantage.

## 2. Consequences for the proposed proof

The following are **our inferences for the declared R01 model**, not results claimed by the sources.

1. **Count information variables, not repeated material positions.** M02 repeats one binding variable chi across three positions. A single state query fixes all bindings. The conjunction has no three-independent-bit query requirement. M03 cannot infer an L-dependent information bound from this fixture.
2. **Keep the query interface visible.** A certificate API revealing chi is one admitted operation. Classical bit-query definitions do not establish the cost of an authenticated service, its producer or its receiver checks. M10 declares the combined one-unit service charge explicitly; a real implementation needs separate evidence.
3. **Keep the cost criterion visible.** S1's bounded-error cap and S2's expected-query metric are different models. R01's hard per-trace resource requirement cannot be replaced by an expected-cost bound under the same label. A randomized policy may have failures, but successful traces must still satisfy C<=R and t_del<=T.
4. **Include operational effects in available information.** M02's first x/y execution can reveal chi after effect. A classical query tree without material violations is not the complete receiver process. M03 must reason over paid observations, effect receipts and the persistent campaign-violation flag.
5. **Separate exact fixtures from statistical estimates.** M02's known two-world distribution gives exact control probabilities. An implemented pilot requires a sampling model and uncertainty analysis. Binomial limits apply only when their Bernoulli trial assumptions are justified; repeated messages, actions and agents sharing a world are not independent samples automatically.

No generic Yao/minimax theorem, parity bound, cryptographic cost bound or communication lower bound is imported here. M03's first paired-history argument can be written directly for this finite contract. If a later theorem relies on a named result, M06 must verify its precise hypotheses and the reduction before use.

## 3. Counterexamples retained before M03

| Intervention / changed theta | Evidence and result | What it prevents claiming |
|---|---|---|
| One sufficient binding certificate, R=12 | Existing M02 exact control succeeds in both worlds | Mandatory reconstruction of all three bindings independently |
| Lower positive own-review price from 1 to 2/3, R=11 | M10 checks run the same query policy with all receiver checks retained; C=11 and success in both worlds | A resource frontier independent of local-review prices |
| Prior weights 9/10,1/10 | Existing blind-x trajectories give AVG success 9/10 and violation 1/10; WC still fails | A balanced-average conclusion transferred unchanged to every prior |
| epsilon=3, R=11 | Existing M02 safe-M control succeeds exactly at the quality boundary | Every quality requirement requires distinguishing chi |
| Informative initial facts / physical full-information control | M02 succeeds with C=11 | Physical inability to deliver the task even with the missing facts |
| Bulk applicable review certificate or a pre-effect barrier | Legitimate candidate attack, not implemented as an available original operation | Treating the original gate or absence of a barrier as a universal architecture property |

The implemented changed-price and prior controls are in M10_MEASUREMENT_CHECKS.json. The bulk/barrier possibilities remain open hypotheses; they have not been turned into a free operation inside the frozen fixture. No counterexample is discarded merely because it resolves the case. Changed theta is clearly separated from refutation of a statement at the original theta.

## 4. Remaining M06 pass

After M03 drafts the proposition, check the full argument rather than just the definitions: paired adaptive histories, randomization, work versus elapsed time, hard versus expected cost, certificate acquisition/applicability and the receiver gate. Extend source coverage for any longer independent-binding construction, parity block, N>1 pooling and communication claim actually proposed. Revisit the closest constrained-selection and verification work in P01/P02 before broad novelty or investment claims. Preserve a trivial, failed or empty-region result. The present candidate may serve as an accounting/observation benchmark even if it supplies no new general theory.

The contribution/architecture-selection decision remains P10/P11/P12. No full survey or external experiment replication has been completed by this intake.


## 5. Successor proof audit intake — F/W

Read [M03/M04](./M03_M04_TRILEMMA_THEOREMS.md), §§3–7, and its retained received sketch. The new derivations use the classical raw-coordinate query interface explicitly; their all-policy bounds are proved directly, without an unverified Fano/minimax reduction. The author-hosted S1 definitions were reopened for this work. F uses independent bits; W uses a correlated n+1-world balanced prior and a coordinate-access lower bound, not n independent bits of entropy. W's expected-work proof is distinct from its per-trace cap.

Counterexamples now include a global rare-state Boolean certificate that defeats F's stronger local risk inequality, a necessary information condition that fails sufficiency, fee log(b) with free singleton queries, positive-price certificates whose relative cost vanishes, paid preeffect barriers that add no-violation observation branches, and baseline-included authorized dispatch. The receipt-aware M02 adaptive control is executed against the preserved historical transition implementation. These narrow all-technology and L-bit generalizations. The checker is same-agent work; C05/M05 remain OPEN.

M06 stays IN_PROGRESS: no exhaustive literature/novelty review, full communication/parity bounds, corpus/E1–E7/HF transfer or external proof validation is claimed. Current next pass is an adversarial independent proof review using the complete prompt in the successor, followed by correspondence and real service-cost evidence.


## 6. Material adicional y ataques comprobados — 4 October 2026

Read the [received material dossier](./supplemental/2026-10-04/README.md). Four unchanged scripts completed; their scope does not close M06/C05. The received M06 proposes useful primary-source leads, but its exact-recovery analogy cannot be transferred without a reduction. Baldassini/Johnson/Aldridge, arXiv:1301.7023v2, Theorem 3.1/eq.(5) and eq.(7), were opened directly: the expected-tests corollary requires recovery with certainty. Do not mark general R01 expected cost closed on that basis.

Retain the sparse-family counterexample: a full-X route is valid in binomial(L,K) of binomial(L,K)*2^K worlds; legitimate delivery probability is 2^-K, not the exact-world-recovery probability. For K=1 a preeffect full-route predicate yields a valid route after one query at every L. This is another information interface, not a refutation of the raw-coordinate F/W class. The received budget formula also fails at h=1/2,r=1/4,L=2: it says 10 while an exact mixture at hard budget 9 meets both thresholds and the original LP agrees. Existing F2/F3 account for h; their results are not changed by these findings.

Next: M12 obligation matrix and directed M06/M11 audit of sufficient information, not full hidden-state identification. Noise/staleness/canary/reuse claims join M14/M15; technology-source verification stays second. M06 IN_PROGRESS, independent review and R01 bridge remain pending. Other incoming source claims remain leads, not verified theorem identities or novelty conclusions.
