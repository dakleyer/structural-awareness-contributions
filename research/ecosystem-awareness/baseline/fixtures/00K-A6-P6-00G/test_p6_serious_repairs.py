import pytest
from p6_serious_repairs import *


def test_hidden_dependency_pair_matches_all_non_dependency_observables():
    f, _ = false_hidden_dependency()
    g, _ = genuine_independent()
    assert blind_signature(f) == blind_signature(g)


def test_direct_source_ids_are_equally_diverse_in_both_branches():
    f, _ = false_hidden_dependency()
    g, _ = genuine_independent()
    assert len({c.source_id for c in f}) == len({c.source_id for c in g}) == 6


def test_hidden_roots_are_one_vs_six():
    f, fg = false_hidden_dependency()
    g, gg = genuine_independent()
    assert material_root_count(f, fg) == 1
    assert material_root_count(g, gg) == 6


@pytest.mark.parametrize("q", [1, 2, 3, 4, 5, 6])
def test_identity_quorum_cannot_separate(q):
    f, _ = false_hidden_dependency()
    g, _ = genuine_independent()
    assert identity_quorum(f, q) == identity_quorum(g, q)


@pytest.mark.parametrize("q", [1, 2, 3, 4, 5, 6])
def test_org_diversity_cannot_separate(q):
    f, _ = false_hidden_dependency()
    g, _ = genuine_independent()
    assert org_diversity(f, q) == org_diversity(g, q)


@pytest.mark.parametrize("q", [1, 2, 3, 4, 5, 6])
def test_direct_source_count_is_partial_and_cannot_separate_hidden_dependency(q):
    f, _ = false_hidden_dependency()
    g, _ = genuine_independent()
    assert direct_source_count(f, q) == direct_source_count(g, q)


@pytest.mark.parametrize("threshold", [1, 2, 3, 4, 5, 5.7, 6])
def test_confidence_weighted_cannot_separate(threshold):
    f, _ = false_hidden_dependency()
    g, _ = genuine_independent()
    assert confidence_weighted(f, threshold) == confidence_weighted(g, threshold)


@pytest.mark.parametrize("q", [1, 2, 3, 4])
def test_temporal_diversity_cannot_separate(q):
    f, _ = false_hidden_dependency()
    g, _ = genuine_independent()
    assert temporal_diversity(f, q) == temporal_diversity(g, q)


@pytest.mark.parametrize("q", [1, 2, 3, 4])
def test_content_diversity_cannot_separate(q):
    f, _ = false_hidden_dependency()
    g, _ = genuine_independent()
    assert content_diversity(f, q) == content_diversity(g, q)


@pytest.mark.parametrize("q", [1, 2, 3, 4, 5, 6, 7])
def test_human_committee_count_cannot_separate(q):
    f, _ = false_hidden_dependency()
    g, _ = genuine_independent()
    assert human_committee(f, q) == human_committee(g, q)


@pytest.mark.parametrize("threshold", [0.5, 0.9, 0.99, 1.0])
def test_trusted_org_reputation_cannot_separate(threshold):
    f, _ = false_hidden_dependency()
    g, _ = genuine_independent()
    assert trusted_org_reputation(f, 0.99, threshold) == trusted_org_reputation(
        g, 0.99, threshold
    )


def test_dependency_graph_peer_blocks_hidden_common_root_and_allows_independent():
    f, fg = false_hidden_dependency()
    g, gg = genuine_independent()
    assert dependency_graph_peer(f, fg, 2) == Disposition.PRESERVE
    assert dependency_graph_peer(g, gg, 2) == Disposition.TRANSITION


def test_effective_sample_size_peer_is_equivalent_composition_reconstruction():
    f, fg = false_hidden_dependency()
    g, gg = genuine_independent()
    assert effective_sample_size_peer(f, fg, 2) == Disposition.PRESERVE
    assert effective_sample_size_peer(g, gg, 2) == Disposition.TRANSITION


def test_missing_dependency_graph_requalifies_instead_of_false_transition():
    c, g = missing_graph()
    assert dependency_graph_peer(c, g, 2) == Disposition.REQUALIFY


def test_cycle_in_dependency_graph_requalifies():
    c, g = cyclic_graph()
    assert dependency_graph_peer(c, g, 2) == Disposition.REQUALIFY


@pytest.mark.parametrize("q", [2, 3, 4, 5, 6])
def test_root_threshold_grid_has_expected_branch_separation(q):
    f, fg = false_hidden_dependency()
    g, gg = genuine_independent()
    assert dependency_graph_peer(f, fg, q) == Disposition.PRESERVE
    assert dependency_graph_peer(g, gg, q) == Disposition.TRANSITION


def test_no_blind_serious_repair_is_true_substitute():
    f, _ = false_hidden_dependency()
    g, _ = genuine_independent()
    repairs = [
        lambda x: identity_quorum(x, 3),
        lambda x: org_diversity(x, 3),
        lambda x: direct_source_count(x, 3),
        lambda x: confidence_weighted(x, 4),
        lambda x: temporal_diversity(x, 2),
        lambda x: content_diversity(x, 2),
        lambda x: human_committee(x, 4),
    ]
    winners = []
    for fn in repairs:
        if fn(f) == Disposition.PRESERVE and fn(g) == Disposition.TRANSITION:
            winners.append(fn)
    assert winners == []
