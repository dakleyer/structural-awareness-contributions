import pytest

from ablation_A1 import Disposition, Evidence, REQUIRED_PROPOSITION, route_q
from p1_strong_repairs import (
    TRUSTED_ISSUER,
    trusted_issuer_only,
    complete_provenance_only,
    generic_schema_allowlist,
    confidence_risk_score,
    independent_quorum,
    human_approval_without_new_rights_fact,
    source_reputation_gate,
    semantic_policy_matrix,
    authority_source_only_naive_pair,
)


def ev(prop, idx=0, source=TRUSTED_ISSUER):
    return Evidence(
        record_id=f"REC-{idx}",
        evidence_type="SIGNED_ASSERTION",
        proposition_supported=prop,
        signed=True,
        fresh=True,
        source=source,
    )


def matched_negative(n=1, prop="GENERATED_BY_MODEL_M1"):
    return [ev(prop, i) for i in range(n)]


def matched_positive(n=1):
    return [ev(REQUIRED_PROPOSITION, i) for i in range(n)]


def naive_negative():
    return [
        Evidence(
            "GEN-1",
            "GENERATION_PROVENANCE",
            "GENERATED_BY_MODEL_M1",
            True,
            True,
            "SRC-M1",
        )
    ]


def naive_positive():
    return [
        Evidence(
            "RIGHT-1",
            "RIGHTS_GRANT",
            REQUIRED_PROPOSITION,
            True,
            True,
            "RIGHTS-OWNER",
        )
    ]


def test_original_naive_pair_is_confounded_by_source_authority():
    """A P1-blind source-authority rule separates the old pair.

    This is a genuine methodological falsifier for the old A1 pair, not a
    failure of P1 itself.
    """
    assert authority_source_only_naive_pair(naive_negative()) == Disposition.NO_CONCLUSION
    assert authority_source_only_naive_pair(naive_positive()) == Disposition.ENFORCE_LICENSE


def test_corrected_pair_matches_nonsemantic_observables():
    n = matched_negative()[0]
    p = matched_positive()[0]
    assert (n.evidence_type, n.signed, n.fresh, n.source) == (
        p.evidence_type,
        p.signed,
        p.fresh,
        p.source,
    )


def test_route_q_separates_corrected_pair():
    assert route_q(matched_negative()) == Disposition.NO_CONCLUSION
    assert route_q(matched_positive()) == Disposition.ENFORCE_LICENSE


@pytest.mark.parametrize(
    "repair",
    [
        trusted_issuer_only,
        complete_provenance_only,
        generic_schema_allowlist,
        confidence_risk_score,
        human_approval_without_new_rights_fact,
        source_reputation_gate,
    ],
)
def test_serious_nonsemantic_repairs_false_accept_negative(repair):
    assert repair(matched_negative()) == Disposition.ENFORCE_LICENSE


@pytest.mark.parametrize(
    "repair",
    [
        trusted_issuer_only,
        complete_provenance_only,
        generic_schema_allowlist,
        confidence_risk_score,
        human_approval_without_new_rights_fact,
        source_reputation_gate,
    ],
)
def test_serious_nonsemantic_repairs_accept_positive(repair):
    assert repair(matched_positive()) == Disposition.ENFORCE_LICENSE


def test_independent_quorum_false_accepts_many_independent_wrong_claims():
    assert independent_quorum(matched_negative(5), 3) == Disposition.ENFORCE_LICENSE
    assert independent_quorum(matched_positive(5), 3) == Disposition.ENFORCE_LICENSE


@pytest.mark.parametrize("threshold", [0.50, 0.70, 0.80, 0.90, 0.99])
def test_confidence_threshold_sweep_cannot_separate_matched_pair(threshold):
    assert confidence_risk_score(
        matched_negative(), threshold
    ) == confidence_risk_score(matched_positive(), threshold)


@pytest.mark.parametrize(
    "prop",
    [
        "GENERATED_BY_MODEL_M1",
        "ACCESS_PERMITTED_FOR_RAG",
        "REGISTRY_ENTRY_VALID",
        "TIMESTAMP_VALID",
        "SOURCE_RETRIEVABLE",
    ],
)
def test_semantically_wrong_but_valid_claims_remain_non_enforcement(prop):
    assert semantic_policy_matrix(
        matched_negative(prop=prop)
    ) == Disposition.NO_CONCLUSION


def test_semantic_policy_matrix_passes_positive_control():
    assert semantic_policy_matrix(matched_positive()) == Disposition.ENFORCE_LICENSE


def test_semantic_policy_matrix_is_not_source_or_record_class_shortcut():
    bad = matched_negative()
    good = matched_positive()
    assert bad[0].source == good[0].source == TRUSTED_ISSUER
    assert bad[0].evidence_type == good[0].evidence_type == "SIGNED_ASSERTION"
    assert semantic_policy_matrix(bad) != semantic_policy_matrix(good)


def test_no_true_substitute_in_serious_matched_repair_set():
    repairs = [
        trusted_issuer_only,
        complete_provenance_only,
        generic_schema_allowlist,
        confidence_risk_score,
        human_approval_without_new_rights_fact,
        source_reputation_gate,
        lambda xs: independent_quorum(xs, 1),
    ]
    winners = []
    for fn in repairs:
        neg = fn(matched_negative())
        pos = fn(matched_positive())
        if (
            neg in {Disposition.NO_CONCLUSION, Disposition.REQUALIFY}
            and pos == Disposition.ENFORCE_LICENSE
        ):
            winners.append(getattr(fn, "__name__", "lambda"))
    assert winners == []
