# Structural adequacy + qualified gain v0.1 — two reusable, independent components

**Research implementation (28 October 2026).** Finite structural diagnostic: [structural_adequacy.py](./structural_adequacy.py); value-sign helper: [qualified_gain.py](./qualified_gain.py); social/agentic/geometry adapters: [qualified_gain_adapters.py](./qualified_gain_adapters.py); [structural tests](./test_theme18_structural_adequacy.py) and [numeric tests](./test_theme18_qualified_gain.py).

## Explicit derivation from the existing corpus

This design implements **two separate, pre-existing mathematical tasks** instead of claiming a new unified intelligence engine.

1. **Structural adequacy of the receiving representation.** Canonical [00M §4.1](../../../../00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md) defines F1: two possible source states with the same qualified projection A cannot have different answers to the **independently specified** receiving question if A is exactly sufficient. [PR60 §02 D1](./02_FORMAL_CORE_AND_PROOFS.md) adds the familiar operation-congruence condition: a newly eligible operation can invalidate an earlier adequate quotient without making the original A wrong. The new structural_adequacy.py evaluates precisely those two predicates for a finite external/referee frame, returning **witness pairs and UNKNOWN**, not hidden-state predictions or an MSCA implementation.
2. **Direction of an already established comparable metric.** Canonical [00M §6.2](../../../../00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md) already specifies the interval difference [c-b, d-a]. qualified_gain.py merely implements that arithmetic with exact rational bounds, evidence status and type identity. **This is standard, downstream arithmetic, not the discovery mechanism or an original theorem.**

The architecture claim is the **typed relationship** between these independent functions and the larger corpus. [00N §§1–3](../../../../00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.7_RESEARCH_NOTE.md) places between them source-preserving A/B/C/D interpretation, relevant scope, complementary qualified B and bounded requalification. [PR60 §02 D3-A](./02_FORMAL_CORE_AND_PROOFS.md) requires extra queries Q to be selected **given already qualified A**. Neither module reconstructs open C/D, proves source eligibility, mints action authority or assumes a numeric gain whenever a structural witness exists.

The [new five-mechanism architecture-search decomposition in PR62 §15](https://github.com/dakleyer/structural-awareness-contributions/blob/research/sa-ea-ep-dds-foundational-bridge-20261027/research/structural-awareness/SA_POSITIONED_RESIDUAL_REUSE_AND_LOCAL_ADAPTATION_v0.1.md) makes this positioning even clearer:

| Source-owned mechanism | How the present code relates |
|---|---|
| 1. Metasyntactic pre-gradient / proprietary MSCA position | A distinct, upstream architectural selection capability; **not implemented by a scalar interval** |
| 2. Qualified residual status / observable UNKNOWN traces | A distinct source qualification. structural_adequacy returns only a *finite receiving-question witness*, not a density map or unseen exterior |
| 3. Non-fungible by-leaf composition across actors | Distinct lineage/dependence and scope service; not replaced by summing values |
| 4. Bounded verification, objective-conditioned agentic gradient and consent/ACC | qualified_gain is a **small scalar sign subroutine**, not the proprietary MSCA or the source-owned Agentic Gradient Law; actual model adapters retain authority and peer comparators |
| 5. Independent Regime Awareness | Context/history validity stays source-owned; no RA regime signal is inferred from a gain or witness |

This preserves **SA mathematical origin → EA source qualification → EP architectural realization**, with DDS/UC21 as a separate test route. The social model's feasible opportunity and human welfare remain distinct; an agentic mission-output gap is not human suffering or HID.

## A real dynamic witness in both existing models

| Model, same visible A | Old question | Independently frozen new question/operation | Diagnostic |
|---|---|---|---|
| Social nested_model: ProducerWorld(True/False) both expose handoff (8,8) | Current output = 8 in both: A sufficient | Joint feasible capacity = 10 versus 8; or operation joint_reallocation produces distinct post-A values | F1 residual and D1 operation noncongruence; **+2 is feasible**, not executed |
| Agentic PR57 AG01/AG02: identical full declared_public A and initial output 10 | Current output = 10 in both: A sufficient | Same fixed allowed transfer of two units gives 11.5 versus 8.875 under the independently modeled hidden recipient rates | D1 operation noncongruence; the Q source rates 1.6 and 0.4 can distinguish the cases **only after eligible source qualification** |

The agentic witness was independently replayed through PR57's actual declared_public and physical_response at commit a98940490e8a84051ad314f2392c15338dbf1de9. CI in PR60 pins the finite public-A and post-action observations because PR57 remains another branch; the social check imports nested_model directly.

A structural residual does **not** establish benefit: an agent may recognize an opportunity yet execute nothing. Conversely, two states can have different, perfectly visible A values and a positive quantitative gain without any hidden decision-relevant distinction. Both negative controls are executable tests.

**Reusable entry point:** callers supply a frame ID/version, receiving scope, independently specified question, qualified A observations, qualified reference answers and optional post-operation A values as FiniteDecisionCase objects:

~~~python
from structural_adequacy import FiniteDecisionCase, assess_finite_adequacy

rows = [
    FiniteDecisionCase("s1", "service-v1", "compatible_versions",
                       ("READY", "READY"), True, "independent-version-ref"),
    FiniteDecisionCase("s2", "service-v1", "compatible_versions",
                       ("READY", "READY"), False, "independent-version-ref"),
]
diagnosis = assess_finite_adequacy(
    rows, frame_id="versioned-contract-1", scope="service-v1",
    question="compatible_versions")
assert diagnosis.decision_status == "WITNESSED_RESIDUAL"
assert diagnosis.decision_witnesses == (("s1", "s2"),)
~~~

Adding version metadata to a legitimate A+Q projection can resolve that bounded question; the *source's rights, freshness, method and role at the receiver* must be qualified separately under 00M/00N before constructing that richer projection. The structural checker consumes no private population survey, executes no transition, and does not assign roles A/B/C/D to object sets. It reports a finite pair witness or a stated finite-frame adequacy result, never a universal closed-world proof.



## Numeric subroutine: qualified gain, independent of any ACC example

The separate numeric subroutine compares **partial value intervals with the same metric, unit and decision scope**. Its original mathematical source is 00M §6.2. It is not a universal utility score, a proxy for consciousness, or a substitute for the structural diagnosis above.

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

The adapter also refuses to reuse PR57's original-Q truth flag to validate a separately directed or full-A measurement: that instrument needs its own verification.

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

This covers F1/D1 old-versus-new sufficiency, social and agentic structural witnesses, a canonical four-state operation signature, UNKNOWN/invalid frames, exact interval signs, partial endpoints, metric/unit/scope mismatch, unverified/refuted evidence, direct social model, AG01/AG11 gain shapes and the Theme18 numeric geometry gate. These reusable *standard finite diagnostics* are on research PR60; no rewrite of 00M/00N or the five source-owned mechanisms, no cost-only superiority claim and no merge to main in this change.
