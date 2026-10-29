"""Exact, question-scoped comparative accounting over source-owned policy outcomes.

The kernel does not simulate society or agents, qualify B/C/D, choose actions,
observe private worlds, or create a new benchmark. Adapters supply outcomes
from their own decision and post-hoc scoring functions. No import-time I/O.
"""
from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from fractions import Fraction
from math import isfinite
from typing import Any, Callable, Iterable, Mapping, Sequence


def quantity(value: Any) -> Fraction:
    """Finite exact decimal-facing amount, never a Boolean or missing value."""
    if type(value) is bool:
        raise ValueError("boolean is not a measured amount")
    if isinstance(value, Fraction):
        return value
    if isinstance(value, Decimal):
        if not value.is_finite():
            raise ValueError("non-finite decimal")
        return Fraction(value)
    if type(value) is int:
        return Fraction(value)
    if type(value) is float:
        if not isfinite(value):
            raise ValueError("non-finite float")
        return Fraction(str(value))
    if isinstance(value, str) and value.strip():
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError, OverflowError) as exc:
            raise ValueError("invalid rational amount") from exc
    raise ValueError("expected a finite integer, decimal or rational amount")


def _identity(value: Any, name: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(name + " must be a nonempty identifier")


@dataclass(frozen=True)
class ComparisonFrame:
    """One receiving question and one conserved public/physical reference.

    Contract ID identifies the source-visible envelope, not private capacities.
    Baseline A is an actual operating output. It is never a predicted optimum.
    """
    case_id: str
    model: str
    scope: str
    question: str
    metric: str
    output_unit: str
    cost_unit: str
    horizon: str
    public_contract_id: str
    baseline_a: Fraction

    def __post_init__(self) -> None:
        for name in ("case_id", "model", "scope", "question", "metric",
                     "output_unit", "cost_unit", "horizon", "public_contract_id"):
            _identity(getattr(self, name), name)
        object.__setattr__(self, "baseline_a", quantity(self.baseline_a))


@dataclass(frozen=True)
class CostLedger:
    """Charged source-native components of an arm; never an implicit cost model."""
    entries: tuple[tuple[str, Fraction], ...] = ()

    def __post_init__(self) -> None:
        seen = set()
        cleaned = []
        for key, raw in self.entries:
            _identity(key, "cost component")
            if key in seen:
                raise ValueError("duplicate cost component: " + key)
            seen.add(key)
            amount = quantity(raw)
            if amount < 0:
                raise ValueError("negative cost component: " + key)
            cleaned.append((key, amount))
        object.__setattr__(self, "entries", tuple(cleaned))

    @classmethod
    def of(cls, entries: Mapping[str, Any] | None = None) -> "CostLedger":
        if entries is None:
            return cls()
        if not isinstance(entries, Mapping):
            raise TypeError("cost components must be a mapping")
        return cls(tuple(sorted(entries.items())))

    @property
    def total(self) -> Fraction:
        return sum((v for _, v in self.entries), Fraction(0))

    def as_dict(self) -> dict[str, str]:
        return {key: str(val) for key, val in self.entries}


@dataclass(frozen=True)
class ArmObservation:
    """An ORIGINAL source policy's result, with its accounting reconciled.

    gross_value is output value/penalty already computed by that source.
    Unknown gross remains None and cannot win. Source decision and post-hoc
    referee remain separated by construction in the source-specific adapter.
    """
    frame: ComparisonFrame
    arm: str
    gross_value: Fraction | None
    costs: CostLedger
    source_status: str
    source_ref: str
    evidence_kind: str
    source_net: Fraction | None = None
    source_cost: Fraction | None = None
    rounding_tolerance: Fraction = Fraction(0)

    def __post_init__(self) -> None:
        if not isinstance(self.frame, ComparisonFrame):
            raise TypeError("frame must be ComparisonFrame")
        if not isinstance(self.costs, CostLedger):
            raise TypeError("costs must be CostLedger")
        for name in ("arm", "source_status", "source_ref", "evidence_kind"):
            _identity(getattr(self, name), name)
        for name in ("gross_value", "source_net", "source_cost", "rounding_tolerance"):
            raw = getattr(self, name)
            if raw is not None:
                object.__setattr__(self, name, quantity(raw))
        if self.rounding_tolerance < 0:
            raise ValueError("negative tolerance")
        if self.source_cost is not None and abs(self.costs.total - self.source_cost) > self.rounding_tolerance:
            raise ValueError("cost ledger disagrees with source: " + self.arm)
        if self.source_net is not None:
            if self.net is None:
                raise ValueError("cannot reconcile an unknown gross with known source net")
            if abs(self.net - self.source_net) > self.rounding_tolerance:
                raise ValueError("net calculation disagrees with source: " + self.arm)

    @property
    def net(self) -> Fraction | None:
        return None if self.gross_value is None else self.gross_value - self.costs.total


@dataclass(frozen=True)
class CaseComparison:
    frame: ComparisonFrame
    arms: tuple[ArmObservation, ...]
    baseline_arm: str
    leaders: tuple[str, ...]
    status: str

    def as_dict(self) -> dict[str, Any]:
        baseline = next(a for a in self.arms if a.arm == self.baseline_arm)
        return {
            "frame": {
                "case_id": self.frame.case_id,
                "model": self.frame.model,
                "scope": self.frame.scope,
                "question": self.frame.question,
                "metric": self.frame.metric,
                "output_unit": self.frame.output_unit,
                "cost_unit": self.frame.cost_unit,
                "horizon": self.frame.horizon,
                "public_contract_id": self.frame.public_contract_id,
                "baseline_a": str(self.frame.baseline_a),
            },
            "status": self.status,
            "evidence_kind": self.arms[0].evidence_kind,
            "baseline_arm": self.baseline_arm,
            "leaders": list(self.leaders),
            "arms": [{
                "arm": a.arm,
                "gross": None if a.gross_value is None else str(a.gross_value),
                "cost": str(a.costs.total),
                "components": a.costs.as_dict(),
                "net": None if a.net is None else str(a.net),
                "net_delta_vs_baseline": None if a.net is None else str(a.net - baseline.net),
                "status": a.source_status,
                "source": a.source_ref,
            } for a in self.arms],
        }


def compare_case(arms: Sequence[ArmObservation], *, baseline_arm: str = "A_ONLY") -> CaseComparison:
    """Rank only source-reported outcomes for EXACTLY one question/frame.

    Unknown arms prevent a complete ranking. Ties are retained and never
    broken in favor of a branded policy. No source policy is called here.
    """
    entries = tuple(arms)
    if len(entries) < 2:
        raise ValueError("at least two source arms required")
    if not all(isinstance(a, ArmObservation) for a in entries):
        raise TypeError("expected ArmObservation elements")
    first = entries[0]
    if any(a.frame != first.frame for a in entries):
        raise ValueError("incommensurable question, public A, units, horizon or envelope")
    if any(a.evidence_kind != first.evidence_kind for a in entries):
        raise ValueError("cannot compare evidence of different kinds as one ranking")
    names = [a.arm for a in entries]
    if len(names) != len(set(names)):
        raise ValueError("duplicate arm ID")
    if baseline_arm not in names:
        raise ValueError("missing baseline arm")
    baseline = next(a for a in entries if a.arm == baseline_arm)
    if baseline.net is None:
        raise ValueError("unscored baseline")
    eligible = tuple(a for a in entries if a.net is not None)
    best = max(a.net for a in eligible)
    leaders = tuple(a.arm for a in eligible if a.net == best)
    status = "COMPLETE_RANKING" if len(eligible) == len(entries) else "PARTIAL_RANKING"
    return CaseComparison(first.frame, entries, baseline_arm, leaders, status)


@dataclass(frozen=True)
class AffineCostCrossing:
    """Comparison of two declared path-length cost schedules, not a scaling law."""
    b_fixed: Fraction
    b_per_path: Fraction
    peer_fixed: Fraction
    peer_per_path: Fraction
    classification: str
    crossing_path_length: Fraction | None

    def at_path_length(self, path_length: Any) -> str:
        length = quantity(path_length)
        if length < 0:
            raise ValueError("negative path length")
        b = self.b_fixed + length * self.b_per_path
        peer = self.peer_fixed + length * self.peer_per_path
        return "B" if b < peer else "DIRECTED" if peer < b else "TIE"


def affine_cost_crossing(*, b_fixed: Any, b_per_path: Any,
                         peer_fixed: Any, peer_per_path: Any) -> AffineCostCrossing:
    fixed_b, slope_b, fixed_p, slope_p = map(quantity,
        (b_fixed, b_per_path, peer_fixed, peer_per_path))
    if min(fixed_b, slope_b, fixed_p, slope_p) < 0:
        raise ValueError("negative cost schedule")
    slope = slope_b - slope_p
    intercept = fixed_b - fixed_p
    if slope == 0:
        kind = "EVERYWHERE_TIE" if intercept == 0 else "NO_CROSSING"
        root = None
    else:
        root = -intercept / slope
        kind = "CROSSING_IN_NONNEGATIVE_DOMAIN" if root >= 0 else "CROSSING_OUTSIDE_DOMAIN"
    return AffineCostCrossing(fixed_b, slope_b, fixed_p, slope_p, kind, root)


def run_cases(scenarios: Iterable[Any],
              adapter: Callable[[Any], Sequence[ArmObservation]],
              *, baseline_arm: str = "A_ONLY") -> tuple[CaseComparison, ...]:
    """A third party supplies a scenario iterator and its own source adapter."""
    checked = []
    identifiers = set()
    for scenario in scenarios:
        result = compare_case(adapter(scenario), baseline_arm=baseline_arm)
        identity = (result.frame.model, result.frame.case_id)
        if identity in identifiers:
            raise ValueError("duplicate model/case identity")
        identifiers.add(identity)
        checked.append(result)
    return tuple(checked)


def summary(results: Sequence[CaseComparison]) -> dict[str, Any]:
    """Counts per model; NEVER sums money or utility across unrelated objectives."""
    seen = set()
    groups: dict[str, dict[str, Any]] = {}
    for result in results:
        identity = (result.frame.model, result.frame.case_id)
        if identity in seen:
            raise ValueError("duplicate model/case identity")
        seen.add(identity)
        g = groups.setdefault(result.frame.model, {
            "cases": 0, "complete": 0, "partial": 0,
            "leaders_including_ties": {}, "strict_wins": {},
        })
        g["cases"] += 1
        g["complete" if result.status == "COMPLETE_RANKING" else "partial"] += 1
        for name in result.leaders:
            g["leaders_including_ties"][name] = g["leaders_including_ties"].get(name, 0) + 1
        if len(result.leaders) == 1:
            name = result.leaders[0]
            g["strict_wins"][name] = g["strict_wins"].get(name, 0) + 1
    return {"groups": groups, "cases_total": len(results),
            "aggregation_rule": "COUNTS_ONLY_NO_CROSS_OBJECTIVE_UTILITY_SUM"}
