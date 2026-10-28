"""Finite, decision-relative structural adequacy diagnostic (00M F1 / PR60 D1).

This is an independent offline/referee utility, not an EA/RA/MSCA runtime or
a generator of hidden world states. It takes declared, qualified observations
and checks whether the receiving question and eligible operation effects
factor through the currently available A projection.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from math import isfinite
from typing import Any, Mapping, Sequence


def _safe_payload(value: Any) -> None:
    """Reject nonfinite comparison values, including nested known payloads."""
    if isinstance(value, float) and not isfinite(value):
        raise ValueError("nonfinite observation or answer")
    if isinstance(value, Decimal) and not value.is_finite():
        raise ValueError("nonfinite decimal observation or answer")
    if isinstance(value, (list, tuple)):
        for item in value:
            _safe_payload(item)
    elif isinstance(value, Mapping):
        for key, item in value.items():
            _safe_payload(key)
            _safe_payload(item)


def _equal(a: Any, b: Any) -> bool:
    """Type-preserving equality: Python True == 1 must not merge A fibers."""
    if type(a) is not type(b):
        return False
    if isinstance(a, (tuple, list)):
        return len(a) == len(b) and all(_equal(x, y) for x, y in zip(a, b))
    if isinstance(a, Mapping):
        if len(a) != len(b):
            return False
        return all(
            any(_equal(ka, kb) and _equal(va, vb) for kb, vb in b.items())
            for ka, va in a.items()
        )
    equal = a == b
    if type(equal) is not bool:
        raise TypeError("use value-like comparison payloads, not vector truth objects")
    return equal


@dataclass(frozen=True)
class FiniteDecisionCase:
    case_id: str
    scope: str
    question: str
    observed_a: Any
    answer: Any
    evidence: str
    observed_a_qualified: bool = True
    answer_qualified: bool = True
    successor_a: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not isinstance(self.case_id, str) or not self.case_id.strip():
            raise ValueError("case_id must be nonempty")
        for field in ("scope", "question"):
            value = getattr(self, field)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(field + " must be nonempty")
        if not isinstance(self.evidence, str) or not self.evidence.strip():
            raise ValueError("evidence must be nonempty")
        if type(self.observed_a_qualified) is not bool or type(self.answer_qualified) is not bool:
            raise ValueError("qualification indicators must be boolean")
        if not isinstance(self.successor_a, Mapping):
            raise ValueError("successor_a must map operation to qualified post-A value")
        _safe_payload(self.observed_a)
        _safe_payload(self.answer)
        for key, val in self.successor_a.items():
            if not isinstance(key, str) or not key.strip():
                raise ValueError("operation identifiers must be nonempty strings")
            _safe_payload(val)


@dataclass(frozen=True)
class StructuralAdequacyResult:
    frame_id: str
    scope: str
    question: str
    decision_status: str
    decision_witnesses: tuple[tuple[str, str], ...]
    operation_statuses: dict[str, str]
    operation_witnesses: dict[str, tuple[tuple[str, str], ...]]
    unknown_case_ids: tuple[str, ...]
    assessed_cases: int

    @property
    def structural_status(self) -> str:
        if self.decision_status == "WITNESSED_RESIDUAL" or any(
                v == "WITNESSED_NONCONGRUENCE" for v in self.operation_statuses.values()):
            return "REQUALIFICATION_WITNESSED"
        if self.decision_status == "UNKNOWN" or any(
                v == "UNKNOWN" for v in self.operation_statuses.values()):
            return "UNKNOWN"
        return "ADEQUATE_IN_DECLARED_FINITE_FRAME"

    def as_dict(self) -> dict[str, Any]:
        return {
            "frame_id": self.frame_id,
            "scope": self.scope,
            "question": self.question,
            "structural_status": self.structural_status,
            "decision_status": self.decision_status,
            "decision_witnesses": list(self.decision_witnesses),
            "operation_statuses": dict(self.operation_statuses),
            "operation_witnesses": {
                key: list(value) for key, value in self.operation_witnesses.items()
            },
            "unknown_case_ids": list(self.unknown_case_ids),
            "assessed_cases": self.assessed_cases,
        }


def assess_finite_adequacy(
    cases: Sequence[FiniteDecisionCase], *,
    frame_id: str,
    scope: str,
    question: str,
    operations: Sequence[str] = (),
) -> StructuralAdequacyResult:
    """F1: A-equivalent cases must share the question's answer.

    D1: A-equivalent cases must have A-equivalent successors for each
    explicitly declared operation. Missing source evidence remains UNKNOWN.
    The question, case domain and operations must come from external adapters;
    a passed finite frame says nothing about undisclosed states or actions.
    """
    if not isinstance(frame_id, str) or not frame_id.strip():
        raise ValueError("frame_id required")
    if not isinstance(scope, str) or not scope.strip():
        raise ValueError("declared receiving scope required")
    if not isinstance(question, str) or not question.strip():
        raise ValueError("independently declared question required")
    operations = tuple(operations)
    if any(not isinstance(op, str) or not op.strip() for op in operations):
        raise ValueError("operations must have nonempty names")
    if len(set(operations)) != len(operations):
        raise ValueError("duplicate operation")
    cases = tuple(cases)
    if any(not isinstance(c, FiniteDecisionCase) for c in cases):
        raise TypeError("expected FiniteDecisionCase")
    ids = tuple(c.case_id for c in cases)
    if len(set(ids)) != len(ids):
        raise ValueError("duplicate case_id")
    if any(c.scope != scope or c.question != question for c in cases):
        raise ValueError("cases must share receiving scope and question")
    if not cases:
        return StructuralAdequacyResult(
            frame_id, scope, question, "UNKNOWN", (), {op: "UNKNOWN" for op in operations},
            {op: () for op in operations}, (), 0,
        )

    decision_pairs: list[tuple[str, str]] = []
    operation_pairs: dict[str, list[tuple[str, str]]] = {op: [] for op in operations}
    unknown: set[str] = set()
    missing_op: dict[str, bool] = {op: False for op in operations}

    for case in cases:
        if not case.observed_a_qualified or not case.answer_qualified:
            unknown.add(case.case_id)
        for op in operations:
            if case.observed_a_qualified and op not in case.successor_a:
                missing_op[op] = True
                unknown.add(case.case_id)

    for index, left in enumerate(cases):
        for right in cases[index + 1:]:
            if not (left.observed_a_qualified and right.observed_a_qualified):
                continue
            if not _equal(left.observed_a, right.observed_a):
                continue
            if left.answer_qualified and right.answer_qualified:
                if not _equal(left.answer, right.answer):
                    decision_pairs.append((left.case_id, right.case_id))
            for op in operations:
                if op in left.successor_a and op in right.successor_a:
                    if not _equal(left.successor_a[op], right.successor_a[op]):
                        operation_pairs[op].append((left.case_id, right.case_id))

    decision_status = (
        "WITNESSED_RESIDUAL" if decision_pairs else
        "UNKNOWN" if any(not c.observed_a_qualified or not c.answer_qualified
                         for c in cases) else "ADEQUATE_IN_DECLARED_FINITE_FRAME"
    )
    operation_statuses = {}
    for op in operations:
        operation_statuses[op] = (
            "WITNESSED_NONCONGRUENCE" if operation_pairs[op] else
            "UNKNOWN" if missing_op[op] or any(not c.observed_a_qualified for c in cases)
            else "CONGRUENT_IN_DECLARED_FINITE_FRAME"
        )

    return StructuralAdequacyResult(
        frame_id, scope, question, decision_status, tuple(decision_pairs),
        operation_statuses, {k: tuple(v) for k, v in operation_pairs.items()},
        tuple(sorted(unknown)), len(cases),
    )
