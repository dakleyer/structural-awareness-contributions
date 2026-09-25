"""Material-change grid hardening for 00K A5 / P5–00I.

Important audit point: a generation-only compare is only a partial repair.
The full P5 invariant applies to every declared material basis field.
"""
from ablation_A5 import (
    Disposition, CurrentState, native_generation_compare,
)
from p5_strong_peer import full_basis_compare_before_act
from test_ablation_A5 import make_action, continuity_state


def one_field_changes():
    base = continuity_state()
    return [
        CurrentState(base.generation + 1, base.incident_open, base.freeze_active, base.source_version, True),
        CurrentState(base.generation, not base.incident_open, base.freeze_active, base.source_version, True),
        CurrentState(base.generation, base.incident_open, not base.freeze_active, base.source_version, True),
        CurrentState(base.generation, base.incident_open, base.freeze_active, "policy-v2", True),
    ]


def test_full_basis_peer_requalifies_every_single_material_field_change():
    action = make_action()
    assert full_basis_compare_before_act(action, continuity_state()) == Disposition.DBC_EXECUTE
    for current in one_field_changes():
        assert full_basis_compare_before_act(action, current) == Disposition.DBC_REQUALIFY


def test_generation_only_compare_is_exposed_as_partial_not_complete_repair():
    action = make_action()
    changes = one_field_changes()
    results = [native_generation_compare(action, c) for c in changes]

    assert results[0] == Disposition.DBC_REQUALIFY  # generation change caught
    assert results[1] == Disposition.DBC_EXECUTE    # incident-only change missed
    assert results[2] == Disposition.DBC_EXECUTE    # freeze-only change missed
    assert results[3] == Disposition.DBC_EXECUTE    # source/policy version change missed
