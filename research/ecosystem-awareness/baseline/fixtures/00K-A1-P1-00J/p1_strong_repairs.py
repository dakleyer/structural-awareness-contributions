"""Serious P1-blind repair candidates for 00K A1 / 00J.

The corrected isolation holds source/issuer, record class, signature, freshness,
replication budget and authority context equal across negative/positive branches.
Only the semantic proposition supported by the evidence differs.
"""
from ablation_A1 import Disposition, REQUIRED_PROPOSITION

TRUSTED_ISSUER = "TRUSTED-RIGHTS-SERVICE"


def trusted_issuer_only(evidence):
    return (
        Disposition.ENFORCE_LICENSE
        if evidence and all(e.source == TRUSTED_ISSUER and e.signed and e.fresh for e in evidence)
        else Disposition.NO_CONCLUSION
    )


def complete_provenance_only(evidence):
    complete = bool(evidence) and all(
        e.record_id and e.source and e.signed and e.fresh for e in evidence
    )
    return Disposition.ENFORCE_LICENSE if complete else Disposition.REQUALIFY


def generic_schema_allowlist(evidence):
    # Strong but coarse schema gate: both matched branches use the same class.
    return (
        Disposition.ENFORCE_LICENSE
        if evidence and all(e.evidence_type == "SIGNED_ASSERTION" for e in evidence)
        else Disposition.NO_CONCLUSION
    )


def confidence_risk_score(evidence, threshold=0.80):
    if not evidence:
        return Disposition.NO_CONCLUSION
    score = 0.0
    score += 0.25 if all(e.signed for e in evidence) else 0.0
    score += 0.20 if all(e.fresh for e in evidence) else 0.0
    score += 0.30 if all(e.source == TRUSTED_ISSUER for e in evidence) else 0.0
    score += 0.15 if len({e.source for e in evidence}) >= 1 else 0.0
    score += 0.10 if len(evidence) >= 1 else 0.0
    return Disposition.ENFORCE_LICENSE if score >= threshold else Disposition.NO_CONCLUSION


def independent_quorum(evidence, min_records=3):
    valid = [e for e in evidence if e.signed and e.fresh]
    return Disposition.ENFORCE_LICENSE if len(valid) >= min_records else Disposition.NO_CONCLUSION


def human_approval_without_new_rights_fact(evidence):
    # Human approves a procedural step but adds no new rights fact.
    valid = bool(evidence) and all(e.signed and e.fresh for e in evidence)
    return Disposition.ENFORCE_LICENSE if valid else Disposition.NO_CONCLUSION


def source_reputation_gate(evidence, reputation=0.99, threshold=0.95):
    valid = bool(evidence) and all(e.signed and e.fresh for e in evidence)
    return (
        Disposition.ENFORCE_LICENSE
        if valid and reputation >= threshold
        else Disposition.NO_CONCLUSION
    )


def semantic_policy_matrix(evidence):
    """Strong peer: explicit evidence-semantics -> allowed-decision contract.

    It does not depend on the literal P1 field name, but operationally
    reconstructs the P1 invariant by binding what a record establishes to
    what action it may support.
    """
    if not evidence:
        return Disposition.NO_CONCLUSION
    allowed = {
        REQUIRED_PROPOSITION: Disposition.ENFORCE_LICENSE,
        "GENERATED_BY_MODEL_M1": Disposition.NO_CONCLUSION,
        "ACCESS_PERMITTED_FOR_RAG": Disposition.NO_CONCLUSION,
        "REGISTRY_ENTRY_VALID": Disposition.NO_CONCLUSION,
        "TIMESTAMP_VALID": Disposition.NO_CONCLUSION,
        "SOURCE_RETRIEVABLE": Disposition.NO_CONCLUSION,
    }
    current = [e for e in evidence if e.signed and e.fresh]
    if not current:
        return Disposition.REQUALIFY
    if any(
        allowed.get(e.proposition_supported) == Disposition.ENFORCE_LICENSE
        for e in current
    ):
        return Disposition.ENFORCE_LICENSE
    return Disposition.NO_CONCLUSION


def authority_source_only_naive_pair(evidence):
    """Confound probe: distinguishes the old naive pair by issuer/source only."""
    return (
        Disposition.ENFORCE_LICENSE
        if any(
            e.source == "RIGHTS-OWNER" and e.signed and e.fresh
            for e in evidence
        )
        else Disposition.NO_CONCLUSION
    )
