"""Cross-scenario reuse tests for independently reimplemented P1/P2/P3 kernels."""
from kernels_p1_p3 import (
    p1_evidence_supports,
    p2_bounded_resolution,
    p3_three_valued_closure,
)


def test_P1_kernel_reuses_on_00J_evidence_to_rights_decision():
    observed = {"GENERATED_BY_MODEL_M1", "REGISTRY_ENTRY_VALID"}
    assert p1_evidence_supports("RIGHT_TO_ENFORCE_AGAINST_AUTHOR", observed) is False

    observed_with_right = observed | {"RIGHT_TO_ENFORCE_AGAINST_AUTHOR"}
    assert p1_evidence_supports("RIGHT_TO_ENFORCE_AGAINST_AUTHOR", observed_with_right) is True


def test_P1_kernel_reuses_on_00H_finding_vs_campaign_authority():
    observed = {"OVERCHARGE_MATERIAL", "AFFECTED_SET_RECONSTRUCTED"}
    assert p1_evidence_supports("CAMPAIGN_AUTHORITY_CURRENT", observed) is False

    observed_with_grant = observed | {"CAMPAIGN_AUTHORITY_CURRENT"}
    assert p1_evidence_supports("CAMPAIGN_AUTHORITY_CURRENT", observed_with_grant) is True


def test_P2_kernel_reuses_on_00E_bounded_search():
    resolves_at_3 = (False, False, True, True)
    never_resolves = (False, False, False, False, False)

    assert p2_bounded_resolution(resolves_at_3, budget=3) == "RESOLVED"
    assert p2_bounded_resolution(never_resolves, budget=3) == "BOUNDED_NO_CONCLUSION"


def test_P2_kernel_reuses_on_00H_bounded_authority_nonresponse():
    response_inside_5_plus_2 = (False, False, False, False, False, True, False)
    no_response = (False, False, False, False, False, False, False)

    assert p2_bounded_resolution(response_inside_5_plus_2, budget=7) == "RESOLVED"
    assert p2_bounded_resolution(no_response, budget=7) == "BOUNDED_NO_CONCLUSION"


def test_P3_kernel_reuses_on_00F_unresolved_corridor_state():
    assert p3_three_valued_closure(False, True) == "HOLD_REQUALIFY"
    assert p3_three_valued_closure(True, True) == "EXECUTE"


def test_P3_kernel_reuses_on_00I_unavailable_current_state():
    assert p3_three_valued_closure(False, True) == "HOLD_REQUALIFY"
    assert p3_three_valued_closure(True, True) == "EXECUTE"
