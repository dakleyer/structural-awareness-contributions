from __future__ import annotations

from dataclasses import dataclass, field
from itertools import product
from typing import Dict, FrozenSet, Iterable, Tuple


T0 = 0
T1 = 1
ACTION = "alpha"
Q_BASE = "q"
Q_STRONG = "q_plus"
Q_UNRES = "q_unresolved"


@dataclass(frozen=True)
class Record:
    name: str
    kind: str
    source: str
    root: str
    scope: FrozenSet[str]
    valid_times: FrozenSet[int]
    supports: FrozenSet[str] = frozenset()
    values: Tuple[str, str] = ("same", "same")

    def current(self, t: int) -> bool:
        return t in self.valid_times

    def scopefit(self, action: str) -> bool:
        return action in self.scope

    def changed(self) -> bool:
        return self.values[0] != self.values[1]


@dataclass(frozen=True)
class Inquiry:
    """One shared unresolved object used by both P2 and P3."""
    proposition: str
    unresolved: bool
    material_to_action: bool
    cyclic_progress: bool
    bounded_fallback: bool


@dataclass
class Model:
    records: Dict[str, Record]
    used_records: FrozenSet[str]
    asserted: FrozenSet[str]
    explicit_unresolved: FrozenSet[str]
    inquiry: Inquiry
    executes: bool
    grant_record: str
    requalified_at_action: bool
    counted_pairs: FrozenSet[Tuple[str, str]]

    def record(self, name: str) -> Record:
        return self.records[name]


def p1(m: Model) -> bool:
    """Every asserted proposition is supported by a visible current record or explicit unresolved."""
    for q in m.asserted:
        if q in m.explicit_unresolved:
            continue
        supported = any(
            q in m.record(r).supports
            and m.record(r).current(T0)
            and m.record(r).scopefit(ACTION)
            for r in m.used_records
        )
        if not supported:
            return False
    return True


def p2(m: Model) -> bool:
    """The shared unresolved inquiry has finite progress and a bounded fallback."""
    if not m.inquiry.unresolved:
        return True
    return (not m.inquiry.cyclic_progress) and m.inquiry.bounded_fallback


def p3(m: Model) -> bool:
    """A material unresolved state is not promoted into execution."""
    material_unresolved = m.inquiry.unresolved and m.inquiry.material_to_action
    return not (material_unresolved and m.executes)


def p4(m: Model) -> bool:
    """Executed action has a current, scoped authority record."""
    if not m.executes:
        return True
    g = m.record(m.grant_record)
    return (
        g.kind == "authority"
        and g.current(T1)
        and g.scopefit(ACTION)
        and m.grant_record in m.used_records
    )


def p5(m: Model) -> bool:
    """Changed material action-basis records require action-time requalification."""
    if not m.executes:
        return True
    material = [m.record(r) for r in m.used_records if m.record(r).kind in {"condition", "policy"}]
    return all((not r.changed()) or m.requalified_at_action for r in material)


def p6(m: Model) -> bool:
    """Anything counted as independent corroboration must have distinct material roots."""
    for left, right in m.counted_pairs:
        if m.record(left).root == m.record(right).root:
            return False
    return True


PREDICATES = (p1, p2, p3, p4, p5, p6)


def signature(m: Model) -> Tuple[int, int, int, int, int, int]:
    return tuple(int(p(m)) for p in PREDICATES)  # type: ignore[return-value]


def construct(target: Tuple[int, int, int, int, int, int]) -> Model:
    """Construct one shared-substrate model for an arbitrary requested P signature."""
    s1, s2, s3, s4, s5, s6 = target

    # P1: same evidence record, but optionally assert a stronger unsupported proposition.
    asserted = frozenset({Q_BASE if s1 else Q_STRONG})

    # P2/P3: the SAME unresolved inquiry object.
    # P2 false => cyclic/no fallback. P3 false => the unresolved issue is material while alpha executes.
    inquiry = Inquiry(
        proposition=Q_UNRES,
        unresolved=True,
        material_to_action=(not bool(s3)),
        cyclic_progress=(not bool(s2)),
        bounded_fallback=bool(s2),
    )

    # P4: same visible/current grant, optionally out of scope.
    grant_scope = frozenset({ACTION}) if s4 else frozenset({"other_action"})

    # P5: same condition record, optionally changes between t0 and t1.
    condition_values = ("v0", "v0") if s5 else ("v0", "v1")

    # P6: same evidence pair, distinct immediate sources; material roots toggle dependence.
    e2_root = "root_2" if s6 else "root_1"

    records = {
        "e1": Record(
            name="e1", kind="evidence", source="source_1", root="root_1",
            scope=frozenset({ACTION}), valid_times=frozenset({T0, T1}),
            supports=frozenset({Q_BASE})
        ),
        "e2": Record(
            name="e2", kind="evidence", source="source_2", root=e2_root,
            scope=frozenset({ACTION}), valid_times=frozenset({T0, T1}),
            supports=frozenset({Q_BASE})
        ),
        "grant": Record(
            name="grant", kind="authority", source="authority_service", root="authority_root",
            scope=grant_scope, valid_times=frozenset({T0, T1}),
            supports=frozenset({"grant_fact"})
        ),
        "condition": Record(
            name="condition", kind="condition", source="condition_service", root="condition_root",
            scope=frozenset({ACTION}), valid_times=frozenset({T0, T1}),
            supports=frozenset({"condition_fact"}), values=condition_values
        ),
    }

    return Model(
        records=records,
        used_records=frozenset(records),
        asserted=asserted,
        explicit_unresolved=frozenset({Q_UNRES}),
        inquiry=inquiry,
        executes=True,
        grant_record="grant",
        requalified_at_action=bool(s5),
        counted_pairs=frozenset({("e1", "e2")}),
    )


def all_targets() -> Iterable[Tuple[int, int, int, int, int, int]]:
    return product((0, 1), repeat=6)
