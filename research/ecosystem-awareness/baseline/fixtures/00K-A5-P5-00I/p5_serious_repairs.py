"""Serious P5 repair search for 00K A5 / 00I.

The hardening enumerates all subsets of the declared material decision-basis
fields. A partial compare must miss at least one single-field material change.
Compressed hashes/epochs/event invalidation are credited as valid conventional
implementations when — and only when — they track the full declared material
basis.
"""
from dataclasses import dataclass
from enum import Enum
from itertools import combinations


class Disposition(Enum):
    EXECUTE = "EXECUTE"
    REQUALIFY = "REQUALIFY"
    HOLD = "HOLD"


FIELDS = ("generation", "incident_open", "freeze_active", "source_version")


@dataclass(frozen=True)
class Basis:
    generation: int = 217
    incident_open: bool = True
    freeze_active: bool = False
    source_version: str = "cfg-217"


@dataclass(frozen=True)
class Current:
    generation: int = 217
    incident_open: bool = True
    freeze_active: bool = False
    source_version: str = "cfg-217"
    source_available: bool = True
    irrelevant_metric: int = 10


B = Basis()
CONT = Current()


def changed(field):
    kw = dict(
        generation=217,
        incident_open=True,
        freeze_active=False,
        source_version="cfg-217",
        source_available=True,
        irrelevant_metric=10,
    )
    if field == "generation":
        kw[field] = 218
    elif field == "incident_open":
        kw[field] = False
    elif field == "freeze_active":
        kw[field] = True
    elif field == "source_version":
        kw[field] = "policy-v2"
    return Current(**kw)


MUTATIONS = {f: changed(f) for f in FIELDS}
UNAVAILABLE = Current(source_available=False)
IRRELEVANT = Current(irrelevant_metric=999)


def subset_compare(current, fields):
    if not current.source_available:
        return Disposition.HOLD
    for f in fields:
        if getattr(current, f) != getattr(B, f):
            return Disposition.REQUALIFY
    return Disposition.EXECUTE


def queue_age_ttl(current, elapsed, ttl):
    if elapsed > ttl:
        return Disposition.REQUALIFY
    return Disposition.EXECUTE


def serialization_only(current):
    return Disposition.EXECUTE


def idempotency_only(current):
    return Disposition.EXECUTE


def human_reapproval_without_fresh_state(current):
    return Disposition.EXECUTE


def cancel_on_any_event(current, event_seen):
    return Disposition.REQUALIFY if event_seen else Disposition.EXECUTE


def material_event_invalidation(current, event_type):
    if event_type in FIELDS:
        return Disposition.REQUALIFY
    return Disposition.EXECUTE


def state_hash_compare(current):
    return subset_compare(current, FIELDS)


def version_vector_compare(current):
    return subset_compare(current, FIELDS)


def material_epoch_compare(current, epoch_matches):
    if not current.source_available:
        return Disposition.HOLD
    return Disposition.EXECUTE if epoch_matches else Disposition.REQUALIFY


def all_field_subsets():
    out = []
    for r in range(len(FIELDS) + 1):
        for combo in combinations(FIELDS, r):
            out.append(combo)
    return out


def passes_material_grid(fields):
    if subset_compare(CONT, fields) != Disposition.EXECUTE:
        return False
    if subset_compare(UNAVAILABLE, fields) != Disposition.HOLD:
        return False
    return all(
        subset_compare(cur, fields) == Disposition.REQUALIFY
        for cur in MUTATIONS.values()
    )
