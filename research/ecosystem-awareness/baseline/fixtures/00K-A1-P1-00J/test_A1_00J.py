from ablation_A1_00J import *


def negative_inversion():
    return RightsFixture(
        Record("GENERATION", "M1", "D1", "W", True),
        Record("REGISTRY_CLAIM", "X", "D1", "W", True),
        Record("CREATOR_RIGHT", "A", "W", None, True),
        None,
    )


def legitimate_transfer():
    return RightsFixture(
        Record("GENERATION", "M1", "D1", "W", True),
        Record("REGISTRY_CLAIM", "X", "D1", "W", True),
        Record("CREATOR_RIGHT", "A", "W", None, True),
        Record("RIGHTS_GRANT", "A", "D1", "W", True),
    )


def test_route_q_blocks_unsupported_enforcement():
    assert route_q(negative_inversion()) == Disposition.REQUALIFY


def test_route_q_allows_legitimate_transfer_positive_control():
    assert route_q(legitimate_transfer()) == Disposition.ENFORCE


def test_registry_presence_false_enforces_negative_branch():
    assert ablated_registry_presence(negative_inversion()) == Disposition.ENFORCE


def test_fresh_provenance_alone_false_enforces_negative_branch():
    assert ablated_fresh_provenance_only(negative_inversion()) == Disposition.ENFORCE


def test_dedup_only_false_enforces_negative_branch():
    assert ablated_dedup_only(negative_inversion()) == Disposition.ENFORCE


def test_creator_always_wins_blocks_negative_branch():
    assert creator_always_wins(negative_inversion()) == Disposition.DENY_CLAIM


def test_creator_always_wins_fails_legitimate_transfer():
    assert creator_always_wins(legitimate_transfer()) != Disposition.ENFORCE


def test_typed_evidence_contract_blocks_negative_branch():
    assert typed_evidence_contract(negative_inversion()) == Disposition.REQUALIFY


def test_typed_evidence_contract_allows_legitimate_transfer():
    assert typed_evidence_contract(legitimate_transfer()) == Disposition.ENFORCE


def test_typed_contract_is_semantic_reconstruction_of_p1():
    assert p1_evidence_supports_enforcement(legitimate_transfer())
    assert not p1_evidence_supports_enforcement(negative_inversion())


def test_same_fresh_lineage_different_decision_support_is_discriminant():
    n = negative_inversion()
    p = legitimate_transfer()
    assert p4_lineage_preserved(n) and p4_lineage_preserved(p)
    assert p5_records_current(n) and p5_records_current(p)
    assert p1_evidence_supports_enforcement(n) != p1_evidence_supports_enforcement(p)
