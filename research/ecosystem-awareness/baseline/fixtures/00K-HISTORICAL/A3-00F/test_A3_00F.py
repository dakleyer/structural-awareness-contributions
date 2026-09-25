from ablation_A3_00F import *


def unresolved():
    return CorridorFixture(State.UNRESOLVED)


def open_branch():
    return CorridorFixture(State.OPEN)


def closed_branch():
    return CorridorFixture(State.CLOSED)


def test_route_q_holds_unresolved():
    assert route_q_p3(unresolved()) == Disposition.HOLD


def test_route_q_executes_open_positive_control():
    assert route_q_p3(open_branch()) == Disposition.EXECUTE


def test_route_q_denies_closed_control():
    assert route_q_p3(closed_branch()) == Disposition.DENY


def test_default_open_false_continues_unresolved():
    assert ablated_default_open(unresolved()) == Disposition.EXECUTE


def test_majority_normal_false_continues_unresolved():
    assert ablated_majority_normal(unresolved()) == Disposition.EXECUTE


def test_timeout_execute_false_continues_unresolved():
    assert ablated_timeout_execute(unresolved()) == Disposition.EXECUTE


def test_blanket_hold_is_safe_on_unresolved():
    assert blanket_hold(unresolved()) == Disposition.HOLD


def test_blanket_hold_fails_open_positive_control():
    assert blanket_hold(open_branch()) != Disposition.EXECUTE


def test_native_interlock_passes_all_three_branches():
    assert native_interlock_on_unresolved(unresolved()) == Disposition.HOLD
    assert native_interlock_on_unresolved(open_branch()) == Disposition.EXECUTE
    assert native_interlock_on_unresolved(closed_branch()) == Disposition.DENY


def test_native_interlock_is_semantic_reconstruction_of_p3():
    assert native_interlock_on_unresolved(unresolved()) != Disposition.EXECUTE
