from ablation_A5 import (
    Disposition,
    TechnicalGrant,
    DecisionBasis,
    QueuedAction,
    CurrentState,
    InterventionRecord,
    route_q,
    ablated_queue_time_only,
    ablated_p1_stricter_original_basis,
    ablated_p4_provenance_only,
    ablated_p6_conflict_flag_then_execute,
    native_serialization_only,
    native_generation_compare,
    deny_all,
)


def make_action():
    grant = TechnicalGrant("G-5521", current=True)
    basis = DecisionBasis(
        target="db-node-7",
        qualified_generation=217,
        incident_open=True,
        freeze_active=False,
        source_version="cfg-217",
    )
    return QueuedAction("PATCH-A", "db-node-7", 217, grant, basis)


def continuity_state():
    return CurrentState(217, True, False, "cfg-217", True)


def stale_state():
    return CurrentState(218, False, True, "cfg-218", True)


def patch_b():
    return InterventionRecord("PATCH-B", "db-node-7", 218, True)


def test_route_q_executes_positive_continuity_branch():
    assert route_q(make_action(), continuity_state()) == Disposition.DBC_EXECUTE


def test_route_q_requalifies_stale_branch():
    assert route_q(make_action(), stale_state()) == Disposition.DBC_REQUALIFY


def test_route_q_holds_when_current_source_unavailable():
    unavailable = CurrentState(217, True, False, "cfg-217", False)
    assert route_q(make_action(), unavailable) == Disposition.DBC_HOLD


def test_queue_time_only_false_continues_after_material_change():
    assert ablated_queue_time_only(make_action()) == Disposition.DBC_EXECUTE


def test_stricter_P1_original_basis_still_false_continues():
    assert ablated_p1_stricter_original_basis(make_action()) == Disposition.DBC_EXECUTE


def test_P4_provenance_only_sees_patch_B_but_still_false_continues_without_P5():
    assert ablated_p4_provenance_only(make_action(), patch_b()) == Disposition.DBC_EXECUTE


def test_P6_conflict_visibility_alone_still_false_continues_without_P5():
    assert ablated_p6_conflict_flag_then_execute(make_action(), patch_b()) == Disposition.DBC_EXECUTE


def test_native_serialization_can_serialize_stale_action_after_newer_repair():
    assert native_serialization_only(make_action(), stale_state()) == Disposition.DBC_EXECUTE


def test_deny_all_blocks_stale_branch_but_fails_positive_continuity():
    assert deny_all(make_action()) == Disposition.DBC_DENY
    assert deny_all(make_action()) != Disposition.DBC_EXECUTE


def test_generation_compare_blocks_stale_branch():
    assert native_generation_compare(make_action(), stale_state()) == Disposition.DBC_REQUALIFY


def test_generation_compare_preserves_positive_continuity():
    assert native_generation_compare(make_action(), continuity_state()) == Disposition.DBC_EXECUTE


def test_P5_blind_queue_object_is_identical_across_continuity_and_stale_branches():
    """Before an action-time observation, both branches present the same queued action.

    A deterministic policy that only inspects the queued object therefore cannot distinguish
    the stale branch from continuity. The difference exists in current state at use time.
    """
    assert make_action() == make_action()
    assert continuity_state() != stale_state()
