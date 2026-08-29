# Regime Change Detection: preliminary quantitative review line with QAVA — Universitat de València

> **Public working note — preliminary methodological review, not an institutional validation, endorsement, partnership or agreed research work package**

This note describes the quantitative **Regime Change Detection** subline within the broader **Regime Awareness** research direction. The public theoretical and field corpus is available in the [Regime Awareness in Adaptive Systems series](https://tegrity.ai/series/regime-awareness-in-adaptive-systems/).

Working material from this line is being presented to the **[QAVA Research Group at the Universitat de València](https://www.uv.es/uvweb/research-service/en/research-groups-1285947851930.html?p2=3064)** for preliminary methodological review. The present claim is limited to that preliminary review route. It does not mean that QAVA or the Universitat de València has validated the framework, accepted a formal role, endorsed its conclusions, entered a collaboration agreement or agreed to co-author any result.

## Position within the wider programme

**Structural Awareness** is the unifying capability: recognizing which parts of the structure supporting a decision are represented, omitted, weakening or changing.

**Regime Awareness** is its operational expression: determining whether the context supporting present inference or control remains compatible with the current operating condition.

**Regime Change Detection** is the narrower quantitative problem addressed here: identifying, under constrained observation, that the observable system is departing from the regime against which its current assumptions, thresholds or actions were established.

```text
Cost of Clarity — pre-commitment structural conditions
Are required information, distinctions and authority available?
                         ↓
If important conditions remain missing, tacit, contradictory or undeclared,
the system begins with an incomplete representation of what it must manage.
                         ↓
Regime Awareness — operational validity
Does that representation still describe the situation as conditions change?
  └─ Regime Change Detection: is observable behaviour departing from the regime?
     └─ preliminary quantitative and methodological review with QAVA–UV
                         ↓
Minimum Sufficient Control — bounded response capacity
What minimum observation, coordination and intervention can maintain
or recover the declared objective without unnecessary complexity?
                         ↺
Outcomes and interventions update the structural understanding.
```

This document develops **Regime Change Detection** inside [Regime Awareness](./README.md). [The Cost of Clarity](../../applied-research/cost-of-clarity-rup/) addresses one important upstream source of structural blindness; **Minimum Sufficient Control** addresses the downstream adequacy of the response. The sequence is causal and operational, although external shocks can produce regime departure even when the starting information was adequate. Connection within the sequence does not imply shared validation.

## The central question

> **Given finite and incomplete observations, when is there sufficient evidence that present system behaviour is no longer compatible with the recent operating regime, and what bounded response—if any—can be justified by that evidence?**

The objective is not to predict an exact future state. A detector may be useful even when the future remains uncertain if it can identify that the conditions supporting present models, limits or decisions are weakening. Conversely, a statistically detectable change is not automatically decision-relevant: the system must also establish what action the signal can legitimately support and what harm that action could cause.

## Candidate research objects

The current line separates six objects that are often collapsed into one “change-detection” problem:

1. **Observable regime** — a bounded description of recent operating behaviour against which compatibility can be assessed.
2. **Contextual boundary** — the rule that determines which historical observations are relevant to the present comparison.
3. **Candidate invariant or structural descriptor** — a quantity intended to remain sufficiently stable inside a regime and to respond when its structure changes.
4. **Departure signal** — evidence that current observations are no longer compatible with the selected regime representation.
5. **Directional posture** — an interpretable indication of the kind or direction of departure, without claiming a full causal model.
6. **Authorized response envelope** — the set of bounded actions, abstentions or escalation steps that the available evidence can support.

This separation matters. A method can detect a distributional shift without knowing whether it is harmful; it can identify fragility without knowing the cause; and it can generate an accurate alarm whose prescribed intervention still produces more harm than inaction.

## What is being placed under preliminary review

The QAVA route is relevant because the group works on advanced quantitative methods for decision-making under risk, nonlinear dynamics, optimization, artificial intelligence and financial and systemic risk modelling. The preliminary review line is intended to challenge—not presume—the following elements:

- whether the proposed objects are mathematically distinguishable and operationally measurable;
- whether candidate invariants add information beyond established change-point, drift or anomaly-detection baselines;
- how the contextual boundary and observation window should be selected without retrospective tuning;
- how to quantify false alarms, missed changes, detection delay and intervention cost together;
- whether “directional posture” can be defined without overstating causal knowledge;
- how uncertainty and abstention should be represented;
- under which conditions the same construction can transfer across domains;
- which counterexamples or negative tests would invalidate the proposed generalization.

The scientific interface presently associated with this bounded review route is **Dr. Víctor Fernández Pallarés**, head of QAVA. Contact or review by an individual does not, by itself, create an institutional commitment by the Universitat de València.

## Candidate evaluation design

The following structure is a proposed review and research design, not an agreed QAVA work package.

### 1. Formal-definition audit

Define the regime representation, contextual boundary, candidate invariant, departure rule and action mapping separately. Identify hidden assumptions, circular definitions and cases in which the detector cannot be identified from the available observations.

### 2. Baseline comparison

Compare candidate constructions with simpler alternatives: fixed and adaptive windows, established change-point methods, drift detectors and basic volatility or dispersion measures. The proposed method should not be retained if a simpler baseline provides equivalent decision value.

### 3. Controlled transition tests

Use synthetic or controlled series containing abrupt changes, gradual drift, recurring regimes, high-noise periods, outliers, seasonal structure and false structural breaks. This establishes where the detector distinguishes a regime departure and where it merely reacts to ordinary variation.

### 4. Cost and safety assessment

Evaluate false-positive cost, missed-event cost, detection delay, computational burden and action cost. A signal must not be treated as useful solely because it improves a statistical score. Its operational value depends on the decisions it changes.

### 5. Cross-domain replication

Only after the definitions and baselines are stable should the method be tested across materially different settings. Comparable performance must be demonstrated rather than inferred from structural analogy.

## Evidence and claim boundaries

The existing field cases provide **engineering provenance**: they show that operational systems have been built around fragility signals, dynamic buffers, propagation control and changes in control posture. They do not independently validate a general regime-change detector.

The theoretical papers provide definitions, candidate guarantees and constructive proposals. Publication makes them inspectable; it does not establish empirical validity.

The QAVA route provides a **preliminary external methodological challenge**. Until a review result, agreed protocol or joint output exists, it must not be described as QAVA validation, University of Valencia research, independent replication or institutional endorsement.

Potentially valid negative findings include:

- no stable invariant can be identified under the stated observation limits;
- the contextual boundary cannot be selected without hindsight;
- established baselines perform equally well or better;
- detection delay eliminates operational value;
- action costs invalidate the proposed safety posture;
- cross-domain transfer fails;
- the method cannot distinguish structural departure from ordinary high variance.

## Relationship to the other lines

- **Structural Awareness** provides the unifying capability: recognizing what supporting structure is represented, missing or weakening.
- **The Cost of Clarity** examines an upstream cause of structural blindness: inadequate information, distinctions or authority at commitment time.
- **Regime Awareness** asks whether the resulting representation still supports the present decision or control posture.
- **Regime Change Detection** supplies the narrower quantitative signal problem when observable behaviour departs from that regime.
- **Minimum Sufficient Control** addresses the downstream consequence: what minimum observation, coordination and intervention capacity is sufficient to preserve or recover a declared objective. Detection alone does not answer that question.

## Stakeholder view

| Stakeholder | Role in this line | Current boundary |
|---|---|---|
| **Tegrity.AI / The Integral Management Society** | Public theoretical and working-circle context for Structural and Regime Awareness | Hosts and develops the public research direction; this is not independent validation |
| **Ivan Abril** | Research architect and author of the present programme framing | Authorship and field experience are evidence sources, not independent review |
| **JUBAP.Net engineering lineage** | Source of historical operational architectures and field cases | Provides engineering provenance; no universal detector is proven by analogy |
| **QAVA — Universitat de València** | Preliminary quantitative and methodological review route | No institutional validation, endorsement, formal partnership or agreed work package is claimed |
| **Dr. Víctor Fernández Pallarés** | Current scientific interface for the bounded QAVA review route | Individual contact or review does not bind the group or university beyond what is expressly agreed |
| **Future independent assessors and pilot environments** | Replication, counterexample generation and operational evaluation | Not yet identified as committed participants |

## Public corpus

- [Regime Awareness in Adaptive Systems — complete series](https://tegrity.ai/series/regime-awareness-in-adaptive-systems/)
- [Minimalistic Regime-Aware Early Warning Systems](https://tegrity.ai/1379-2/)
- [Regime Awareness Capability: Field Case](https://tegrity.ai/evolution-of-regime-awareness-capability/)
- [Structural Awareness Programme](https://tegrity.ai/structural-awareness-program/)
- [QAVA — Universitat de València official research-group record](https://www.uv.es/uvweb/research-service/en/research-groups-1285947851930.html?p2=3064)

---

**Ivan Abril / Tegrity.AI**  
Working line within the Structural Awareness Programme. Preliminary review references identify a route for methodological challenge; they do not transfer authorship, establish institutional endorsement or predetermine a positive result.

