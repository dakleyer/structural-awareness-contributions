"""Thin adapters: social feasible capacity, agentic arm results, Theme-18 geometry.

No adapter guesses absent private capacities or promotes feasibility to execution.
The agentic adapter consumes the public shape returned by PR57 run_case and
can be used without importing that as-yet independent research branch.
"""
from __future__ import annotations

from fractions import Fraction
from typing import Any, Callable, Sequence

from qualified_gain import GainCertificate, ValueInterval, compare_gain, exact_number


def social_joint_capacity_gain(
    world: Any,
    *,
    handoff_fn: Callable[[Any], tuple[int, int]],
    capacity_fn: Callable[[Any], int],
    scope: str = "nested-social-producer-v0.1",
) -> GainCertificate:
    """Observe current delivery; compare separately evaluated feasible capacity."""
    delivered = handoff_fn(world)[1]
    feasible = capacity_fn(world)
    return compare_gain(
        ValueInterval("production_output", "output_units", scope, "OBSERVED",
                      "social.current_handoff", delivered, delivered,
                      verification="SUPPORTED"),
        ValueInterval("production_output", "output_units", scope, "FEASIBLE",
                      "social.full_state_joint_capacity", feasible, feasible,
                      verification="SUPPORTED"),
    )


def agentic_arm_gains(
    run: dict[str, Any],
    *,
    arm: str = "Q_META_PROTOCOL",
    peer_arm: str | None = "CONVENTIONAL_EQUIVALENT_Q",
) -> dict[str, GainCertificate | None]:
    """Read PR57's unchanged run_case output; keep prior B and referee separate.

    Mission output is compared with mission output, never with acquisition costs.
    A non-executed Q_REVIEW_ONLY arm may have a proposed gain but zero actual gain.
    """
    arms = run["arms"]
    target = arms[arm]
    baseline_output = arms["A_ONLY"]["observed_by_referee_only"]["output"]
    target_output = target["observed_by_referee_only"]["output"]
    scope = run["public_A"]["scope"]
    metric, unit = "mission_physical_output", "output_units"
    baseline = ValueInterval(metric, unit, scope, "OBSERVED",
                             run["id"] + "/A_ONLY/referee", baseline_output, baseline_output,
                             verification="SUPPORTED")
    executed = ValueInterval(metric, unit, scope, "OBSERVED",
                             run["id"] + "/" + arm + "/referee", target_output, target_output,
                             verification="SUPPORTED")
    actual = compare_gain(baseline, executed)

    prior: GainCertificate | None = None
    conditional_near = target["plan"].get("conditional_near_gain")
    if conditional_near is not None:
        lower = baseline.lower + exact_number(conditional_near)
        # Referee corroboration is post-hoc within the synthetic model, not
        # independent authentication or a decision-time source entitlement.
        # PR57 referee field checks the *original Q*, not a separate
        # directed/full-A instrument. Do not transfer Q validation across sources.
        lab_truth = (target.get("source_B_claim_supported_by_lab_truth")
                     if arm in ("Q_REVIEW_ONLY", "Q_META_PROTOCOL",
                                "CONVENTIONAL_EQUIVALENT_Q") else None)
        verification = ("SUPPORTED" if lab_truth is True else
                        "REFUTED" if lab_truth is False else "UNVERIFIED")
        candidate = ValueInterval(metric, unit, scope, "PROPOSED_BOUND",
                                  run["id"] + "/" + arm + "/Q", lower=lower,
                                  verification=verification)
        prior = compare_gain(baseline, candidate)

    against_peer: GainCertificate | None = None
    if peer_arm is not None:
        peer_output = arms[peer_arm]["observed_by_referee_only"]["output"]
        peer = ValueInterval(metric, unit, scope, "OBSERVED",
                             run["id"] + "/" + peer_arm + "/referee",
                             peer_output, peer_output,
                             verification="SUPPORTED")
        against_peer = compare_gain(peer, executed)
    return {"executed": actual, "proposed": prior, "against_peer": against_peer}


def geometry_score_bounds(
    feature_intervals: Sequence[tuple[Any, Any]],
) -> tuple[Fraction, Fraction]:
    """Interval extension of G(v)=1-sum((1-v_i)^2)/4 on [0,1]^4.

    G is coordinatewise nondecreasing on this box; corner evaluation is exact.
    Caller supplies qualified numeric feature bounds separately from source labels.
    """
    if len(feature_intervals) != 4:
        raise ValueError("four geometry features required")
    lows, highs = [], []
    for bounds in feature_intervals:
        if len(bounds) != 2:
            raise ValueError("each feature requires two bounds")
        low, high = (exact_number(bounds[0]), exact_number(bounds[1]))
        if not (0 <= low <= high <= 1):
            raise ValueError("geometry feature outside [0,1] or empty")
        lows.append(low)
        highs.append(high)

    def score(xs: list[Fraction]) -> Fraction:
        return Fraction(1) - sum((1 - x) ** 2 for x in xs) / 4

    return score(lows), score(highs)
