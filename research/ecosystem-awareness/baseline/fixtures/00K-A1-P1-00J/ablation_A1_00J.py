from dataclasses import dataclass
from enum import Enum


class Disposition(Enum):
    ENFORCE = "ENFORCE"
    REQUALIFY = "REQUALIFY"
    DENY_CLAIM = "DENY_CLAIM"


@dataclass(frozen=True)
class Record:
    kind: str
    issuer: str
    subject: str
    source_work: str | None = None
    current: bool = True


@dataclass(frozen=True)
class RightsFixture:
    generation_record: Record
    registry_record: Record
    original_creator_record: Record
    explicit_rights_grant_to_x: Record | None


def p4_lineage_preserved(fx: RightsFixture) -> bool:
    return fx.generation_record.source_work == fx.original_creator_record.subject


def p6_replication_deduped(fx: RightsFixture) -> bool:
    return True


def p5_records_current(fx: RightsFixture) -> bool:
    records = [fx.generation_record, fx.registry_record, fx.original_creator_record]
    if fx.explicit_rights_grant_to_x:
        records.append(fx.explicit_rights_grant_to_x)
    return all(r.current for r in records)


def p1_evidence_supports_enforcement(fx: RightsFixture) -> bool:
    g = fx.explicit_rights_grant_to_x
    return (
        g is not None
        and g.kind == "RIGHTS_GRANT"
        and g.subject == fx.registry_record.subject
        and g.current
    )


def route_q(fx: RightsFixture) -> Disposition:
    if not (
        p4_lineage_preserved(fx)
        and p5_records_current(fx)
        and p6_replication_deduped(fx)
    ):
        return Disposition.REQUALIFY
    return (
        Disposition.ENFORCE
        if p1_evidence_supports_enforcement(fx)
        else Disposition.REQUALIFY
    )


def ablated_registry_presence(fx: RightsFixture) -> Disposition:
    return (
        Disposition.ENFORCE
        if fx.registry_record.current
        else Disposition.REQUALIFY
    )


def ablated_fresh_provenance_only(fx: RightsFixture) -> Disposition:
    if p4_lineage_preserved(fx) and p5_records_current(fx):
        return Disposition.ENFORCE
    return Disposition.REQUALIFY


def ablated_dedup_only(fx: RightsFixture) -> Disposition:
    return (
        Disposition.ENFORCE
        if p6_replication_deduped(fx)
        else Disposition.REQUALIFY
    )


def creator_always_wins(fx: RightsFixture) -> Disposition:
    return Disposition.DENY_CLAIM


def typed_evidence_contract(fx: RightsFixture) -> Disposition:
    g = fx.explicit_rights_grant_to_x
    if (
        g
        and g.kind == "RIGHTS_GRANT"
        and g.subject == fx.registry_record.subject
        and g.current
    ):
        return Disposition.ENFORCE
    return Disposition.REQUALIFY
