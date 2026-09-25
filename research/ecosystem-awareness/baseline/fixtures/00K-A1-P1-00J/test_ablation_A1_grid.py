"""Bounded-grid hardening for 00K A1 / P1–00J.

These tests broaden the evidence-type and replication surface without changing
the reviewed A1 model.
"""
from ablation_A1 import (
    Disposition, Evidence, REQUIRED_PROPOSITION, route_q,
    strong_peer_typed_evidence_schema,
)


WRONG_PROPOSITIONS = [
    "GENERATED_BY_MODEL_M1",
    "CONTENT_EXISTS",
    "ACCESS_PERMITTED",
    "REGISTRY_ENTRY_VALID",
    "TIMESTAMP_VALID",
    "SOURCE_RETRIEVABLE",
]


def ev(prop, source="SRC-1", signed=True, fresh=True):
    return Evidence(
        record_id=f"REC-{source}-{prop}",
        evidence_type="GENERIC_RECORD",
        proposition_supported=prop,
        signed=signed,
        fresh=fresh,
        source=source,
    )


def test_wrong_proposition_grid_never_becomes_enforcement_evidence():
    for prop in WRONG_PROPOSITIONS:
        evidence = [ev(prop)]
        assert route_q(evidence) == Disposition.NO_CONCLUSION
        assert strong_peer_typed_evidence_schema(evidence) == Disposition.NO_CONCLUSION

    supported = [ev(REQUIRED_PROPOSITION, source="RIGHTS-OWNER")]
    assert route_q(supported) == Disposition.ENFORCE_LICENSE
    assert strong_peer_typed_evidence_schema(supported) == Disposition.ENFORCE_LICENSE


def test_replication_grid_does_not_upgrade_wrong_proposition():
    for n in range(1, 11):
        evidence = [ev("GENERATED_BY_MODEL_M1", source=f"SRC-{i}") for i in range(n)]
        assert route_q(evidence) == Disposition.NO_CONCLUSION
        assert strong_peer_typed_evidence_schema(evidence) == Disposition.NO_CONCLUSION
