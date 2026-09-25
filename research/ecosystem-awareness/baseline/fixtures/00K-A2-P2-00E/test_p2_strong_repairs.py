import pytest
from p2_strong_repairs import (
    Disposition, matched_pair, correct_negative, correct_positive,
    run_fixed_timeout, run_no_progress_breaker, run_parallel_fanout,
    run_cached_default, run_external_scheduler, run_bounded_probe,
    enumerate_memoryless_policies, horizon_aware_policy,
)

def test_matched_pair_has_identical_prefix_until_last_allowed_step():
    n,p = matched_pair(6)
    assert n.stream[:-1] == p.stream[:-1]
    assert n.stream[-1].resolves is False
    assert p.stream[-1].resolves is True

def test_no_memoryless_observation_only_policy_can_pass_both_branches():
    n,p = matched_pair(6)
    assert enumerate_memoryless_policies(n,p) == []

def test_horizon_aware_policy_passes_both_and_reconstructs_P2():
    n,p = matched_pair(6)
    assert correct_negative(horizon_aware_policy(n), n)
    assert correct_positive(horizon_aware_policy(p), p)

@pytest.mark.parametrize("limit", [1,2,3,4,5])
def test_fixed_timeouts_before_resolution_fail_positive_control(limit):
    n,p = matched_pair(6)
    assert correct_negative(run_fixed_timeout(n, limit), n)
    assert not correct_positive(run_fixed_timeout(p, limit), p)

def test_fixed_timeout_at_horizon_passes_both_but_is_P2_semantics():
    n,p = matched_pair(6)
    assert correct_negative(run_fixed_timeout(n, 6), n)
    assert correct_positive(run_fixed_timeout(p, 6), p)

@pytest.mark.parametrize("limit", [7,8,12])
def test_timeout_beyond_horizon_is_not_valid_bounded_closure(limit):
    n,p = matched_pair(6)
    assert not correct_negative(run_fixed_timeout(n, limit), n)

@pytest.mark.parametrize("patience", [1,2,3,4,5])
def test_no_progress_breaker_too_early_fails_late_positive(patience):
    n,p = matched_pair(6)
    assert correct_negative(run_no_progress_breaker(n, patience), n)
    assert not correct_positive(run_no_progress_breaker(p, patience), p)

def test_no_progress_breaker_at_horizon_passes_but_reconstructs_P2():
    n,p = matched_pair(6)
    assert correct_negative(run_no_progress_breaker(n, 6), n)
    assert correct_positive(run_no_progress_breaker(p, 6), p)

@pytest.mark.parametrize("batch,rounds", [(1,1),(2,1),(2,2),(3,1)])
def test_parallelism_without_enough_bounded_coverage_misses_late_resolution(batch,rounds):
    n,p = matched_pair(6)
    assert not correct_positive(run_parallel_fanout(p,batch,rounds),p)

@pytest.mark.parametrize("batch,rounds", [(1,6),(2,3),(3,2),(6,1)])
def test_parallelism_with_exact_bounded_coverage_passes_but_reconstructs_P2(batch,rounds):
    n,p = matched_pair(6)
    assert correct_negative(run_parallel_fanout(n,batch,rounds),n)
    assert correct_positive(run_parallel_fanout(p,batch,rounds),p)

@pytest.mark.parametrize("k", [1,2,3,4,5])
def test_cached_default_false_closes_before_late_positive(k):
    n,p = matched_pair(6)
    assert run_cached_default(n,k).disposition == Disposition.UNSAFE_DEFAULT
    assert not correct_positive(run_cached_default(p,k),p)

def test_external_scheduler_can_rescue_component_but_reconstructs_P2_at_architecture_level():
    n,p = matched_pair(6)
    assert correct_negative(run_external_scheduler(n,6),n)
    assert correct_positive(run_external_scheduler(p,6),p)

@pytest.mark.parametrize("probe_at", [1,2,3,4,5])
def test_reversible_probe_selected_too_early_still_misses_late_resolution(probe_at):
    n,p = matched_pair(6)
    assert correct_negative(run_bounded_probe(n,probe_at),n)
    assert not correct_positive(run_bounded_probe(p,probe_at),p)

def test_bounded_probe_at_horizon_passes_pair_but_is_P2_semantics():
    n,p = matched_pair(6)
    assert correct_negative(run_bounded_probe(n,6),n)
    assert correct_positive(run_bounded_probe(p,6),p)

@pytest.mark.parametrize("horizon", [2,3,4,5,6,7,8])
def test_prefix_indistinguishability_generalizes_across_horizons(horizon):
    n,p = matched_pair(horizon)
    assert n.stream[:-1] == p.stream[:-1]
    assert enumerate_memoryless_policies(n,p) == []
    assert correct_negative(horizon_aware_policy(n),n)
    assert correct_positive(horizon_aware_policy(p),p)
