# PR57 research extension — Shared cartography, candidate arrival and online meta-label

**EX-AG-CART-01 · Source-preserving synthetic study extension · 27 October 2026**

**Scientific provenance:** This is a new overlay, not a rewriting of PR57's 30 original synthetic scenarios, 6 policy arms or 160 sensitivity cases. The original agentic physical model has **two resource-holding providers**, not N independent physical providers. The new cartography adds **four abstract observers** of one event, distinct from the underlying two providers. Mathematical source: [SA-MATH-CART-01](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/structural-awareness/SA_MULTIAGENT_COMMON_RESIDUAL_AND_ARRIVAL_v0.1.md); prior experiments: [PR57](https://github.com/dakleyer/structural-awareness-contributions/pull/57), [PR45 source-qualified cloud](https://github.com/dakleyer/structural-awareness-contributions/pull/45).

## Hypothesis and exact De Morgan qualification

For four interpreted local admitted sets A_i in a common Omega, the **common exterior** is

\[
\mathcal R=\bigcap_{i=1}^{4}(\Omega\setminus A_i)
=\Omega\setminus\bigcup_{i=1}^{4}A_i.
\]

Source-qualified, same-event, distinct-observer negative predicates can establish that a concrete incoming event belongs to this region. A generic UNKNOWN, malformed event, no recorded event or duplicate source does **not** prove such a negative predicate. The mathematical complement **is not identical** to the whole open epistemic A′ and may be empty. The predicates do not imply any utility bound.

## New four-dimensional illustrative qualified region

Each of four observers sees only its own feature z_i. The local admitted class is A_i = {z:z_i <= 0.6}, with z in [0,1]^4. A properly received event for which **all four z_i > 0.6** lies in the common region (0.6,1]^4. We **separately postulate** the pedagogical objective

\[
u(z)=1-\frac14\sum_{i=1}^{4}(1-z_i)^2.
\]

The present toy choice (.5,.5,.5,.5) has u=.75 and toy optimum u*=1. Every member of the common region satisfies **u>.84**; a constructed candidate (.90,.85,.80,.95) has **u=.98125**, so it is near-optimal but not equal to the optimum. This is a rigorous, **new analytic construction** and not the physical ACC productivity equation. It establishes neither an actual physical population of candidates nor a natural frequency of encounter. Under an **additional artificial i.i.d. uniform-coordinate assumption**, a candidate has chance 0.0256 to lie in the region; without that premise no probability or guaranteed arrival horizon is justified.

## Three new stages reusing original PR57 AG01 physical code

We directly reuse the original case AG01-QUALIFIED-NEAR-OPTIMUM from [CASES.json](CASES.json) and the unchanged functions [declared_public / plan_public / score_after_plan](agentic_reduction.py). Resource budget stays 10: donor6/receiver4; source Q lower-rate 1.6 and transfer limit2; referee hidden receiving rate2; same physical coordination overhead .25. The existing physical reference scores Y(0)=10, Y(2)=11.5 and Y(4)=13.5.

| Stage | Source PR57 policy reused | New research condition | Mission output | Technical gap to13.5 |
| --- | --- | --- | ---: | ---: |
| I: original restricted operation | A_ONLY | no new observer evidence | **10** | **3.5** |
| II: qualified meta-opportunity | Q_REVIEW_ONLY | shared region and independently scoped source Q, **no matching candidate after exchange** | **10** | **3.5** |
| III: candidate actually received | Q_META_PROTOCOL | **NEW event-arrival gate after exchange plus NEW assumed qualified link from cartographic class to existing Q** | **11.5** | **2.0** |
| Original referee-only technical optimum | best physical transfer k=4 | reference only | **13.5** | **0** |

At stage II the **existing PR57 claimed second-order near gain is 0.8**, not a new realized output. It is not added to the technical gap; no subjective experience of frustration is attributed to AI.

**Important source correction:** the old PR57 Q_META_PROTOCOL has **no arrival gate** and would act when Q, consent, authority and original capabilities permit. This NEW overlay introduces a stage-III availability gate; it also assumes a valid class-to-AG01-Q relation not implied by De Morgan, by the four-dimensional geometry or by PR57 itself. In stage III the source model's existing ordinary transfer is invoked, not a new actuation capability. The outside candidate feature vector is scored only by a **separate pedagogical geometry referee**, never substituted for ACC physical Y(k).

## Actual meta-syntax emitted, not a fictional network broadcast

The added research code [residual_cartography_stage.py](residual_cartography_stage.py) exposes a **stage-II cartography record** and a **stage-III source-qualified rule proposal**. The latter has:

- source scope, event ID and rule version;
- COMMON_RESIDUAL_CANDIDATE label with four distinct local observer IDs;
- synthetic source-link qualification and the old authorized transfer action only if AG01's actual permission gates allow it;
- compulsory receiving checks of version/source truth, target, capacity, consent, authority and cost;
- explicit **broadcast_performed = false** and **full_external_population_identified = false** fields.

Thus **emitting a new qualified syntax is implemented** but **network diffusion, external adoption or independent source authentication is not**. Meta-information does not grant another agent extra authority. The stage-II report is prefix-grounded: an earlier qualified observation is *recorded as earlier*, not falsely declared absent. The stage-III gate does not retroactively act on earlier events; genuine replay would require an additional explicitly qualified rule.

## Tests, negative controls and reproducibility

[The new unittest module](test_residual_cartography_stage.py) adds **27 synthetic tests** (21 original additions plus 6 scope/rule-emission checks). It verifies all 16 local threshold combinations, exact same-source De Morgan conditions, source/event mismatches, malformed inputs, nonreceived candidates, absence of arrival, prefix honesty, stage1/2/3 values, actual output and held second-order .8, AG07 lack of consent, AG11 false-Q downside **Y=8.875 when misleading information is trusted**, and the strong conventional controller with **the same Q and event** also getting **Y=11.5**. It also verifies that a newly generated schema/rule is **not actually broadcast** and that a rejected action is not silently authorized.

Run from repository root using Python standard library:

~~~bash
python -B -m unittest discover -s research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/agentic-ecosystem-reduction-v0.1 -p 'test_*.py' -v
python -B research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/agentic-ecosystem-reduction-v0.1/residual_cartography_stage.py
~~~

**Source results preserved:** original AG01–AG30 cases, source Q fields, score functions, resource conservation, original 6 policies and reference sweep remain unchanged. This extension is on the **open PR57 research branch**, not automatically merged to main or canon. CI status must be evaluated on the **latest branch commit**; a prior successful run verified the first 21 extension tests, but it cannot substitute for verification of the six subsequent tests and later stage-II honesty fix.

**Failure conditions:** common blind region empty; no proof of objective value; invalid negative predicates; no event captured at ingress; no source-class-to-Q correspondence; permissions/consent blocked; infinite unknown waiting time without encounter fairness; unsafe/source-invalid Q; zero or negative gain; equally qualified conventional comparator ties. None is hidden or averaged away.
