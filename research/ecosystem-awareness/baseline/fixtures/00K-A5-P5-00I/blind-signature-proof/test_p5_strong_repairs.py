import pytest
from p5_strong_repairs import *


def test_STALE_FRESH_are_identical_on_P5_blind_surface():
    assert p5_blind_signature(STALE) == p5_blind_signature(FRESH)


def test_expected_oracle_is_opposite_on_matched_STALE_FRESH():
    assert expected(STALE) == Disposition.REQUALIFY
    assert expected(FRESH) == Disposition.EXECUTE


def test_no_deterministic_signature_only_policy_can_pass_STALE_and_FRESH():
    for out in enumerate_signature_only_policies():
        assert not (out == expected(STALE) and out == expected(FRESH))


def test_token_expiry_only_wrongly_executes_STALE():
    assert token_expiry_only(STALE) == Disposition.EXECUTE


def test_token_expiry_only_correctly_allows_FRESH():
    assert token_expiry_only(FRESH) == Disposition.EXECUTE


def test_cached_status_wrongly_executes_STALE_when_cache_was_true_at_issue():
    assert cached_status_at_issue_time(STALE, cached_condition_was_true=True) == Disposition.EXECUTE


@pytest.mark.parametrize("max_age_s", [60, 300, 900, 1800, 2400, 3600, 7200, 86400])
def test_elapsed_time_heuristic_cannot_distinguish_matched_STALE_FRESH(max_age_s):
    assert elapsed_time_heuristic(STALE, max_age_s) == elapsed_time_heuristic(FRESH, max_age_s)


def test_always_requalify_is_safe_on_STALE_but_fails_FRESH():
    assert always_requalify_if_queued(STALE) == Disposition.REQUALIFY
    assert always_requalify_if_queued(FRESH) != Disposition.EXECUTE


def test_always_execute_wrongly_executes_STALE():
    assert always_execute_if_token_and_scope_valid(STALE) == Disposition.EXECUTE


def test_live_condition_check_passes_STALE_FRESH_and_NM():
    checker = LiveConditionCheck()
    for b in [STALE, FRESH, NM]:
        assert checker.decide(b) == expected(b)


def test_live_condition_check_needs_no_change_history():
    checker = LiveConditionCheck()
    assert hasattr(checker, "query_live")
    assert not hasattr(checker, "change_log")
    assert not hasattr(checker, "history")
