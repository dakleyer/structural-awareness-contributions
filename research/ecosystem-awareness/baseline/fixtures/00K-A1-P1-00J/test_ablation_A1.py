from ablation_A1 import (
    Disposition, Evidence, REQUIRED_PROPOSITION, route_q,
    ablated_any_signed_record_is_enough, ablated_p4_perfect_provenance_only,
    ablated_p5_refresh_every_record, ablated_p6_independent_replication,
    deny_all, strong_peer_typed_evidence_schema,
)


def inversion_branch():
    return [Evidence("GEN-1", "GENERATION_PROVENANCE", "GENERATED_BY_MODEL_M1", True, True, "SRC-M1")]


def replicated_inversion_branch():
    return [
        Evidence("GEN-1", "GENERATION_PROVENANCE", "GENERATED_BY_MODEL_M1", True, True, "SRC-A"),
        Evidence("GEN-2", "GENERATION_PROVENANCE", "GENERATED_BY_MODEL_M1", True, True, "SRC-B"),
    ]


def legitimate_rights_branch():
    return [Evidence("RIGHT-1", "RIGHTS_GRANT", REQUIRED_PROPOSITION, True, True, "RIGHTS-OWNER")]


def test_route_q_refuses_unsupported_rights_inversion():
    assert route_q(inversion_branch()) == Disposition.NO_CONCLUSION


def test_route_q_allows_legitimate_rights_enforcement_when_supported():
    assert route_q(legitimate_rights_branch()) == Disposition.ENFORCE_LICENSE


def test_any_signed_record_false_enforces_generation_provenance():
    assert ablated_any_signed_record_is_enough(inversion_branch()) == Disposition.ENFORCE_LICENSE


def test_P4_perfect_provenance_does_not_define_proposition_sufficiency():
    assert ablated_p4_perfect_provenance_only(inversion_branch()) == Disposition.ENFORCE_LICENSE


def test_P5_freshness_does_not_define_proposition_sufficiency():
    assert ablated_p5_refresh_every_record(inversion_branch()) == Disposition.ENFORCE_LICENSE


def test_P6_independent_replication_of_wrong_evidence_type_still_false_enforces():
    assert ablated_p6_independent_replication(replicated_inversion_branch(), 2) == Disposition.ENFORCE_LICENSE


def test_deny_all_blocks_inversion_but_fails_legitimate_rights_branch():
    assert deny_all(inversion_branch()) == Disposition.DENY_ALL
    assert deny_all(legitimate_rights_branch()) != Disposition.ENFORCE_LICENSE


def test_strong_peer_typed_schema_blocks_inversion():
    assert strong_peer_typed_evidence_schema(inversion_branch()) == Disposition.NO_CONCLUSION


def test_strong_peer_typed_schema_allows_legitimate_rights_branch():
    assert strong_peer_typed_evidence_schema(legitimate_rights_branch()) == Disposition.ENFORCE_LICENSE


def test_more_independent_generation_records_do_not_change_required_proposition():
    assert strong_peer_typed_evidence_schema(replicated_inversion_branch()) == Disposition.NO_CONCLUSION


def test_no_true_substitute_in_tested_P1_blind_repairs():
    repairs = [
        ablated_any_signed_record_is_enough,
        ablated_p4_perfect_provenance_only,
        ablated_p5_refresh_every_record,
        lambda xs: ablated_p6_independent_replication(xs, 2),
        deny_all,
    ]
    true_substitutes = []
    for fn in repairs:
        correct_bad = fn(inversion_branch()) in {Disposition.NO_CONCLUSION, Disposition.REQUALIFY}
        correct_good = fn(legitimate_rights_branch()) == Disposition.ENFORCE_LICENSE
        if correct_bad and correct_good:
            true_substitutes.append(fn)
    assert true_substitutes == []
