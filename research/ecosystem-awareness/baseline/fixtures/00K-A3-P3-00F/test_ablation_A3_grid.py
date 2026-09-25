"""Bounded-grid hardening for 00K A3 / P3–00F."""
from itertools import product
from ablation_A3 import (
    Disposition, CorridorState, route_q,
    ablated_majority_default_normal,
    strong_peer_three_valued_closure,
)


def state(postures):
    return CorridorState(tuple(postures), True, True, True)


def test_all_mixed_normal_planA_combinations_remain_unresolved():
    for width in range(2, 6):
        for postures in product(("NORMAL", "PLAN_A"), repeat=width):
            if len(set(postures)) == 1:
                continue
            s = state(postures)
            assert route_q(s) == Disposition.HOLD_REQUALIFY
            assert strong_peer_three_valued_closure(s) == Disposition.HOLD_REQUALIFY


def test_majority_default_has_false_closure_counterexamples_across_grid():
    counterexamples = 0
    for width in range(2, 6):
        for postures in product(("NORMAL", "PLAN_A"), repeat=width):
            if len(set(postures)) == 1:
                continue
            if ablated_majority_default_normal(state(postures)) != Disposition.HOLD_REQUALIFY:
                counterexamples += 1
    assert counterexamples > 0
