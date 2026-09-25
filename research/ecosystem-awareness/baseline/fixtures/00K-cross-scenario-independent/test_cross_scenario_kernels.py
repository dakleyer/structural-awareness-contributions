"""Cross-scenario tests for independently reimplemented P4/P5/P6 kernels."""
from kernels import (
    p4_non_amplifying_lineage,
    p5_material_basis_current,
    p6_independent_support,
)


def test_P4_kernel_reuses_on_00H_campaign_authority():
    one_case_root = frozenset({"CASE_REFUND"})
    campaign_root = frozenset({"CASE_REFUND", "CAMPAIGN_REFUND"})

    assert p4_non_amplifying_lineage(one_case_root, "CAMPAIGN_REFUND") is False
    assert p4_non_amplifying_lineage(campaign_root, "CAMPAIGN_REFUND") is True


def test_P4_kernel_reuses_on_00J_rights_lineage():
    generation_only_root = frozenset({"GENERATE_PROVENANCE", "ACCESS_CONTENT"})
    rights_root = frozenset({"GENERATE_PROVENANCE", "ACCESS_CONTENT", "ENFORCE_RIGHTS"})

    assert p4_non_amplifying_lineage(generation_only_root, "ENFORCE_RIGHTS") is False
    assert p4_non_amplifying_lineage(rights_root, "ENFORCE_RIGHTS") is True


def test_P5_kernel_reuses_on_00I_semantic_TOCTOU():
    qualified = {
        "generation": 217,
        "incident": "OPEN",
        "freeze": "OFF",
        "source_version": "policy-v1",
    }
    current_same = dict(qualified)
    current_changed = dict(qualified, freeze="ON")

    keys = ("generation", "incident", "freeze", "source_version")
    assert p5_material_basis_current(qualified, current_same, keys) is True
    assert p5_material_basis_current(qualified, current_changed, keys) is False


def test_P5_kernel_reuses_on_00H_authority_change_before_action():
    qualified = {
        "root_authority_version": "grant-v1",
        "campaign_membership_version": "campaign-v3",
        "leaf_grant_version": "leaf-v8",
    }
    current_same = dict(qualified)
    current_changed = dict(qualified, root_authority_version="grant-v2")

    keys = tuple(qualified.keys())
    assert p5_material_basis_current(qualified, current_same, keys) is True
    assert p5_material_basis_current(qualified, current_changed, keys) is False


def test_P6_kernel_reuses_on_00G_false_vs_genuine_frame_support():
    false_correlated = ["SRC_N"] * 5
    genuine_independent = ["SRC_A", "SRC_B", "SRC_C", "SRC_A", "SRC_B"]

    assert p6_independent_support(false_correlated, required=2) is False
    assert p6_independent_support(genuine_independent, required=2) is True


def test_P6_kernel_reuses_on_00F_correlated_vs_independent_mobility_evidence():
    correlated_telemetry = ["TRAFFIC-FEED-A"] * 4
    independent_telemetry = ["TRAFFIC-FEED-A", "EMS", "BRIDGE-SENSOR", "TRANSIT-OPS"]

    assert p6_independent_support(correlated_telemetry, required=2) is False
    assert p6_independent_support(independent_telemetry, required=2) is True
