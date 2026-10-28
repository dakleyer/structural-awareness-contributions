# Qualified Gain v0.1 — a reusable social/agentic comparison interface

**Research implementation (28 October 2026).** Core code: [qualified_gain.py](./qualified_gain.py); adapters: [qualified_gain_adapters.py](./qualified_gain_adapters.py); cross-model tests: [test_theme18_qualified_gain.py](./test_theme18_qualified_gain.py).

## Core contract, independent of any ACC example

The shared primitive is **a comparison between partial value intervals with the same metric, unit and decision scope**, not a universal utility score or a proxy for consciousness.

For baseline B in [bL,bU] and candidate C in [cL,cU]:

- Lower guaranteed difference: dL = cL - bU, when both endpoints are known.
- Upper possible difference: dU = cU - bL, when both endpoints are known.
- If dL > 0: CERTIFIED_STRICT_GAIN.
- If dU <= 0: CERTIFIED_NO_STRICT_GAIN.
- Otherwise: GAIN_NOT_ESTABLISHED.

Unknown bounds remain unknown. Empty intervals, nonfinite values and booleans are rejected. Decimal and rational inputs are compared with Python Fraction arithmetic; no epsilon, no floating threshold used to reverse a certificate.

Each ValueInterval also preserves:

| Field | Why the core requires it |
|---|---|
| metric, unit, scope | Prevents comparing production units with geometry scores, net cost or human development; prevents silent scope switches |
| kind | Distinguishes OBSERVED, FEASIBLE, PROPOSED_BOUND and other caller-defined evidence roles; a feasible capacity does not become an executed output |
| evidence | Identifies the input observation, model or proposed source |
| verification | SUPPORTED, UNVERIFIED, REFUTED; an unverified or refuted bound cannot receive a positive arithmetic certificate |

The verification status is supplied by a source/evidence adapter, never invented by the arithmetic kernel. UNVERIFIED_EVIDENCE and REFUTED_EVIDENCE retain the numerical claimed delta for inspection, but do not treat it as established. A SUPPORTED result means supported **within the declared finite evidence**, not real-world authentication beyond that evidence.

## Adapters and actual corpus checks

| Adapter | Baseline | Candidate | Result | Evidence role |
|---|---:|---:|---:|---|
| Social nested ProducerWorld(True), using the existing current_handoff/full_state_joint_capacity functions | 8 | 10 | +2 | Feasible joint capacity, not yet executed |
| Social ProducerWorld(False) | 8 | 8 | 0 | Negative control |
| Agentic AG01, using PR57 run_case output | 10 | 11.5 | +1.5 | Physical referee output after authorized Q transfer (synthetic) |
| AG01 prior Q bound | 10 | at least 10.8 | at least +0.8 | Proposed marginal, separately evidenced by the finite referee |
| AG01 Q method versus conventional peer with equivalent Q | 11.5 | 11.5 | 0 | Same-information/capability peer ties; no exclusive architectural superiority |
| Agentic AG04 Q_REVIEW_ONLY | 10 | 10 actual; +0.8 claimed possible | 0 actual | Awareness of a possible gain does not execute it |
| Agentic AG11 and AG29 (bogus B) | 10 | 8.875 actual | -1.125 | Q still claims +0.8, but source is REFUTED; no positive certificate |
| Theme18 synthetic four-feature geometry | 0.75 | 0.98125 | 37/160 | Numeric feature vector, not a qualitative source-label inference |

We actually executed the **30 independent PR57 case definitions** through the unchanged PR57 agentic code (commit a98940490e8a84051ad314f2392c15338dbf1de9), then fed every returned run_case dictionary to the new adapter. The CI test in PR60 uses a pinned, source-labelled AG01/AG11 output **shape** because PR57 is a different open branch; it does not claim to import that branch. Social integration runs directly against the existing nested_model.py on the PR60 base.

The agentic adapter deliberately does not collapse physical output and acquisition cost into one score. Existing PR57 mission_net_value_after_information_cost remains an independent metric; to compare net outputs, create a separate set of ValueInterval objects with metric=mission_net_after_information_cost and the same cost-accounting definition on both sides.

## Theme18 geometry: derived rather than asserted

For four independently qualified numeric feature intervals vi in [li,ui], with 0 <= li <= ui <= 1, the adapter calculates:

    G(v1,v2,v3,v4) = 1 - ((1-v1)^2 + (1-v2)^2 + (1-v3)^2 + (1-v4)^2) / 4

On this entire box, each partial derivative (1-vi)/2 is nonnegative. Therefore the lower/upper extrema are obtained by evaluating all li / all ui. For the four values (0.90, 0.85, 0.80, 0.95), G = 157/160 = 0.98125; compared to 3/4, the increase is **37/160 = 0.23125**. Four qualified lower feature bounds 0.60 imply G >= 21/25 = 0.84, yielding a **guaranteed geometry difference >= 9/100** from 0.75. This arithmetic conclusion does not follow from the four categorical "outside local A" labels alone: a separate source-to-feature/value mapping must exist, and candidate admission retains its explicit source_to_value_link_qualified gate.

The previous Theme18 candidate-admission test used direct <= on the claimed source_value_lower_bound. It could mistakenly treat NaN, +infinity or True as a strict improvement. Now the same typed interval core checks the value, preserving the positive 0.84 path, the no-established-improvement 0.50 path and the distinct authorization/budget gates.

## Third-party integration

Both modules use only Python's standard library and accept values from external domains without importing ACC models. A third-party adapter decides the metric and validates the evidence, then constructs intervals:

~~~python
from decimal import Decimal
from qualified_gain import ValueInterval, compare_gain

measured = ValueInterval(
    metric="energy_produced", unit="MWh", scope="factory-c",
    kind="OBSERVED", evidence="meter-7",
    lower=Decimal("100.0"), upper=Decimal("100.0"),
    verification="SUPPORTED",
)
forecast = ValueInterval(
    metric="energy_produced", unit="MWh", scope="factory-c",
    kind="PROPOSED_BOUND", evidence="verified-model-4",
    lower=Decimal("103.5"), verification="SUPPORTED",
)
certificate = compare_gain(measured, forecast)
assert certificate.status == "CERTIFIED_STRICT_GAIN"
assert certificate.as_dict()["gain_lower"] == "7/2"
~~~

The same API can be used for capacity, energy, latency (with sign/orientation handled by the caller's declared metric), service access or resource outputs. It does not automatically authorize intervention. A "higher is better" comparison must be expressed as such a metric; for latency or harm where lower is better, an adapter can supply a monotone benefit transformation or reverse the comparison deliberately.

## Repeatable verification and merge boundary

From repository root:

~~~bash
python3 -B -m unittest discover -s research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/mathematical-lineage-social-agentic-v0.1 -p 'test_theme18_*.py' -v
~~~

This covers exact interval signs, partial endpoints, invalid input, metric/unit/scope mismatch, unverified/refuted evidence, direct social model, AG01/AG11 adapter shapes, and the Theme18 numeric geometry gate. The API is on research PR60, with no rewrite of 00M/00N, no cost-only superiority claim and no merge to main in this change.
