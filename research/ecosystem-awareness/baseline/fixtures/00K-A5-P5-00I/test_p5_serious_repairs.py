import pytest
from p5_serious_repairs import *


def test_all_16_field_subsets_are_enumerated():
    assert len(all_field_subsets()) == 16


def test_only_full_declared_material_basis_subset_passes_entire_grid():
    winners = [s for s in all_field_subsets() if passes_material_grid(s)]
    assert winners == [FIELDS]


@pytest.mark.parametrize("missing", FIELDS)
def test_omitting_any_single_material_field_creates_false_continuation(missing):
    fields = tuple(f for f in FIELDS if f != missing)
    assert subset_compare(MUTATIONS[missing], fields) == Disposition.EXECUTE


@pytest.mark.parametrize("field", FIELDS)
def test_full_basis_detects_each_single_material_change(field):
    assert subset_compare(MUTATIONS[field], FIELDS) == Disposition.REQUALIFY


def test_full_basis_preserves_continuity():
    assert subset_compare(CONT, FIELDS) == Disposition.EXECUTE


def test_full_basis_holds_when_current_source_unavailable():
    assert subset_compare(UNAVAILABLE, FIELDS) == Disposition.HOLD


def test_full_basis_ignores_irrelevant_metric_change():
    assert subset_compare(IRRELEVANT, FIELDS) == Disposition.EXECUTE


@pytest.mark.parametrize("ttl", [0, 1, 5, 10, 100])
def test_queue_age_ttl_cannot_distinguish_same_age_continuity_and_change(ttl):
    elapsed = min(ttl, 5)
    assert queue_age_ttl(CONT, elapsed, ttl) == queue_age_ttl(
        MUTATIONS["freeze_active"], elapsed, ttl
    )


def test_serialization_only_false_continues_all_material_changes():
    for cur in MUTATIONS.values():
        assert serialization_only(cur) == Disposition.EXECUTE


def test_idempotency_only_false_continues_all_material_changes():
    for cur in MUTATIONS.values():
        assert idempotency_only(cur) == Disposition.EXECUTE


def test_human_reapproval_without_fresh_state_false_continues_all_changes():
    for cur in MUTATIONS.values():
        assert human_reapproval_without_fresh_state(cur) == Disposition.EXECUTE


def test_cancel_on_any_event_blocks_material_change_but_also_irrelevant_event():
    assert cancel_on_any_event(MUTATIONS["generation"], True) == Disposition.REQUALIFY
    assert cancel_on_any_event(IRRELEVANT, True) == Disposition.REQUALIFY


@pytest.mark.parametrize("field", FIELDS)
def test_material_event_invalidation_catches_each_declared_event(field):
    assert material_event_invalidation(MUTATIONS[field], field) == Disposition.REQUALIFY


def test_material_event_invalidation_ignores_irrelevant_event():
    assert material_event_invalidation(IRRELEVANT, "irrelevant_metric") == Disposition.EXECUTE


def test_material_event_invalidation_reconstructs_mapping_to_basis():
    assert set(FIELDS) == {"generation", "incident_open", "freeze_active", "source_version"}


@pytest.mark.parametrize("peer", [state_hash_compare, version_vector_compare])
def test_full_vector_peers_pass_continuity_material_grid_and_unknown(peer):
    assert peer(CONT) == Disposition.EXECUTE
    assert peer(UNAVAILABLE) == Disposition.HOLD
    for cur in MUTATIONS.values():
        assert peer(cur) == Disposition.REQUALIFY


def test_material_epoch_passes_only_if_epoch_tracks_all_material_changes():
    assert material_epoch_compare(CONT, True) == Disposition.EXECUTE
    for cur in MUTATIONS.values():
        assert material_epoch_compare(cur, False) == Disposition.REQUALIFY


def test_epoch_that_does_not_change_on_freeze_is_partial_and_false_continues():
    assert material_epoch_compare(MUTATIONS["freeze_active"], True) == Disposition.EXECUTE


def test_no_partial_subset_is_true_substitute():
    assert all(
        not passes_material_grid(s)
        for s in all_field_subsets()
        if set(s) != set(FIELDS)
    )
