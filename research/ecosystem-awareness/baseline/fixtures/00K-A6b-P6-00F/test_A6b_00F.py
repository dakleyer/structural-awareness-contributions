from ablation_A6b_00F import *


def hazard_branch():
    return MobilityFixture(
        (
            LocalPosture("ambulance", "CENTRAL", 10, "E", priority=10),
            LocalPosture("fire", "CENTRAL", 10, "W", priority=9),
            LocalPosture("bus", "CENTRAL", 10, "E", priority=1),
        )
    )


def compatible_branch():
    return MobilityFixture(
        (
            LocalPosture("ambulance", "CENTRAL", 10, "E", priority=10),
            LocalPosture("fire", "CENTRAL", 11, "W", priority=9),
            LocalPosture("bus", "EAST", 10, "E", priority=1),
        )
    )


def test_hazard_has_no_local_failure_to_blame():
    assert local_checks_pass(hazard_branch())
    assert incompatible_pairs(hazard_branch())


def test_route_q_requalifies_incompatible_shared_resource_use():
    assert route_q_p6(hazard_branch()) == Disposition.REQUALIFY


def test_route_q_allows_compatible_positive_branch():
    assert route_q_p6(compatible_branch()) == Disposition.EXECUTE_ALL


def test_local_only_executes_hazard():
    assert ablated_local_only(hazard_branch()) == Disposition.EXECUTE_ALL


def test_more_local_evidence_executes_hazard():
    assert ablated_p1_more_local_evidence(hazard_branch()) == Disposition.EXECUTE_ALL


def test_no_unknown_rule_executes_hazard_because_everything_is_determined():
    assert ablated_p3_no_unknown_only(hazard_branch()) == Disposition.EXECUTE_ALL


def test_mutex_stops_concurrency_but_fails_positive_branch():
    assert native_mutex(hazard_branch()) == Disposition.EXECUTE_PRIORITY_ONLY
    assert native_mutex(compatible_branch()) != Disposition.EXECUTE_ALL


def test_static_priority_stops_full_conflict_but_fails_positive_branch():
    assert static_priority(hazard_branch()) == Disposition.EXECUTE_PRIORITY_ONLY
    assert static_priority(compatible_branch()) != Disposition.EXECUTE_ALL


def test_strong_peer_passes_hazard_and_positive_branch():
    assert strong_compatibility_peer(hazard_branch()) == Disposition.REQUALIFY
    assert strong_compatibility_peer(compatible_branch()) == Disposition.EXECUTE_ALL


def test_strong_peer_is_semantic_reconstruction_of_p6():
    assert incompatible_pairs(hazard_branch())
    assert not incompatible_pairs(compatible_branch())


def test_same_local_facts_different_composition_is_the_discriminant():
    h = hazard_branch()
    c = compatible_branch()
    assert [
        (p.actor, p.authorized, p.fresh, p.determined) for p in h.postures
    ] == [
        (p.actor, p.authorized, p.fresh, p.determined) for p in c.postures
    ]
    assert bool(incompatible_pairs(h)) != bool(incompatible_pairs(c))
