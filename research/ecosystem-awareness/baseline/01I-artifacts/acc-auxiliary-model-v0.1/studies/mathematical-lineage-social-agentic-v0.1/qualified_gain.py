"""Exact source-typed interval-sign helper from canonical 00M section 6.2.

This downstream arithmetic is not the F1/D1 structural sufficiency mechanism,
the source-owned agentic gradient or the five-module architectural search.
The evaluator knows nothing about human suffering, agency, geometry, costs,
consent or authentication. Domain adapters establish those meanings before
presenting comparable value intervals; the result preserves both evidence kinds.
"""
from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from fractions import Fraction
from math import isfinite
from typing import Any


def exact_number(value: Any) -> Fraction:
    """Use decimal-visible float values; reject bool, invalid and infinite data."""
    if type(value) is bool:
        raise ValueError("boolean is not a measured numeric bound")
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, Decimal):
        if not value.is_finite():
            raise ValueError("non-finite decimal bound")
        return Fraction(value)
    if isinstance(value, float):
        if not isfinite(value):
            raise ValueError("non-finite float bound")
        return Fraction(str(value))
    raise ValueError("bound must be int, float, Decimal or Fraction")


@dataclass(frozen=True)
class ValueInterval:
    """A partial or exact interval for one metric in one decision scope.

    None is an unknown side, not zero.  Kind distinguishes OBSERVED,
    FEASIBLE, PROPOSED_BOUND, etc.; evidence identifies the source.
    """
    metric: str
    unit: str
    scope: str
    kind: str
    evidence: str
    lower: Fraction | None = None
    upper: Fraction | None = None
    verification: str = "UNVERIFIED"

    def __post_init__(self) -> None:
        for field in ("metric", "unit", "scope", "kind", "evidence"):
            value = getattr(self, field)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(field + " must be a nonempty string")
        if self.verification not in ("SUPPORTED", "UNVERIFIED", "REFUTED"):
            raise ValueError("verification must be SUPPORTED, UNVERIFIED or REFUTED")
        if self.lower is None and self.upper is None:
            raise ValueError("an interval requires at least one bound")
        lower = None if self.lower is None else exact_number(self.lower)
        upper = None if self.upper is None else exact_number(self.upper)
        if lower is not None and upper is not None and lower > upper:
            raise ValueError("empty interval: lower exceeds upper")
        object.__setattr__(self, "lower", lower)
        object.__setattr__(self, "upper", upper)


@dataclass(frozen=True)
class GainCertificate:
    status: str
    gain_lower: Fraction | None
    gain_upper: Fraction | None
    baseline: ValueInterval
    candidate: ValueInterval

    def as_dict(self) -> dict[str, str | None]:
        """Serialize exact rationals without converting them back to float."""
        return {
            "status": self.status,
            "metric": self.baseline.metric,
            "unit": self.baseline.unit,
            "scope": self.baseline.scope,
            "gain_lower": None if self.gain_lower is None else str(self.gain_lower),
            "gain_upper": None if self.gain_upper is None else str(self.gain_upper),
            "baseline_kind": self.baseline.kind,
            "candidate_kind": self.candidate.kind,
            "baseline_evidence": self.baseline.evidence,
            "candidate_evidence": self.candidate.evidence,
            "baseline_verification": self.baseline.verification,
            "candidate_verification": self.candidate.verification,
        }


def compare_gain(baseline: ValueInterval, candidate: ValueInterval) -> GainCertificate:
    """Certified strict sign from bounds: (candidate - baseline).

    Lower gain = candidate.lower - baseline.upper.
    Upper gain = candidate.upper - baseline.lower.
    Unknown endpoints remain unknown; no fabricated numeric closure.
    """
    if not isinstance(baseline, ValueInterval) or not isinstance(candidate, ValueInterval):
        raise TypeError("expected two ValueInterval values")
    if (baseline.metric, baseline.unit, baseline.scope) != (
            candidate.metric, candidate.unit, candidate.scope):
        raise ValueError("incommensurable metric, unit or decision scope")
    lower = (None if candidate.lower is None or baseline.upper is None
             else candidate.lower - baseline.upper)
    upper = (None if candidate.upper is None or baseline.lower is None
             else candidate.upper - baseline.lower)
    if "REFUTED" in (baseline.verification, candidate.verification):
        status = "REFUTED_EVIDENCE"
    elif "UNVERIFIED" in (baseline.verification, candidate.verification):
        status = "UNVERIFIED_EVIDENCE"
    elif lower is not None and lower > 0:
        status = "CERTIFIED_STRICT_GAIN"
    elif upper is not None and upper <= 0:
        status = "CERTIFIED_NO_STRICT_GAIN"
    else:
        status = "GAIN_NOT_ESTABLISHED"
    return GainCertificate(status, lower, upper, baseline, candidate)
