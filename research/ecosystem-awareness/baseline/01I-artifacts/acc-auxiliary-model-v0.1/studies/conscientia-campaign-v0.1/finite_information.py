"""Reproducible Shannon quantities for a *declared finite distribution*.

Not an entropy measure of open epistemic C/D, unknown human motives, or the
number of possible unknown worlds. The weights are explicit and strictly
nonnegative. Real observations would need independent provenance/registration.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from math import isfinite, log2
from typing import Mapping, Sequence


def _weight(raw: object) -> Fraction:
    if type(raw) is bool or raw is None:
        raise ValueError("weight must be a finite nonnegative rational, not boolean/unknown")
    try:
        if isinstance(raw, float):
            if not isfinite(raw):
                raise ValueError("nonfinite weight")
            result = Fraction(str(raw))
        elif isinstance(raw, (str, int, Fraction)):
            result = Fraction(raw)
        else:
            raise ValueError("unsupported weight")
    except (ZeroDivisionError, OverflowError, TypeError, ValueError) as exc:
        raise ValueError("invalid probability weight") from exc
    if result < 0:
        raise ValueError("negative weight")
    return result


def joint_distribution(
    rows: Sequence[Mapping[str, object]],
    variables: Sequence[str],
    weights: Sequence[object],
) -> dict[tuple[object, ...], Fraction]:
    """Empirical mass of declared finite rows; weights MUST be supplied."""
    names = tuple(variables)
    if not names or len(set(names)) != len(names):
        raise ValueError("variables must be nonempty and distinct")
    if len(rows) == 0 or len(rows) != len(weights):
        raise ValueError("finite rows/weights mismatch")
    mass = defaultdict(Fraction)
    for row, raw in zip(rows, weights):
        if not isinstance(row, Mapping) or any(key not in row for key in names):
            raise ValueError("row is missing a declared variable")
        key = tuple(row[name] for name in names)
        try:
            hash(key)
        except TypeError as exc:
            raise ValueError("variables require discrete hashable values") from exc
        mass[key] += _weight(raw)
    total = sum(mass.values(), Fraction(0))
    if total <= 0:
        raise ValueError("total probability weight must be positive")
    return {k: w / total for k, w in mass.items() if w > 0}


def entropy(distribution: Mapping[object, Fraction]) -> float:
    """Bits of a normalized, explicitly finite probability distribution."""
    total = sum(distribution.values(), Fraction(0))
    if total != 1:
        raise ValueError("distribution must sum to one")
    if any(p < 0 for p in distribution.values()):
        raise ValueError("negative probability")
    return -sum(float(p) * log2(float(p)) for p in distribution.values() if p)


def entropy_of(rows, variables, weights) -> float:
    return entropy(joint_distribution(rows, variables, weights))


def conditional_entropy(rows, target: str, given: Sequence[str], weights) -> float:
    """H(target | given), computed from the same joint distribution."""
    conditioning = tuple(given)
    if target in conditioning:
        return 0.0
    if not conditioning:
        return entropy_of(rows, (target,), weights)
    return max(0.0, entropy_of(rows, (*conditioning, target), weights)
               - entropy_of(rows, conditioning, weights))


def mutual_information(rows, target: str, knowledge: Sequence[str], weights) -> float:
    """I(target; knowledge) from observed finite rows; never a hand-entered bit."""
    known = tuple(knowledge)
    if target in known:
        return entropy_of(rows, (target,), weights)
    return max(0.0, entropy_of(rows, (target,), weights)
               - conditional_entropy(rows, target, known, weights))


def kl_bits(
    p: Mapping[object, Fraction], q: Mapping[object, Fraction],
) -> float:
    """D_KL(P||Q); mathematical infinity on genuine support mismatch."""
    for distribution in (p, q):
        if sum(distribution.values(), Fraction(0)) != 1:
            raise ValueError("KL distributions must be normalized")
        if any(v < 0 for v in distribution.values()):
            raise ValueError("negative probability")
    if any(v and q.get(key, Fraction(0)) == 0 for key, v in p.items()):
        return float("inf")
    return sum(float(v) * log2(float(v / q[key]))
               for key, v in p.items() if v)


def original_uniform_coverage() -> dict[str, object]:
    """The source's m=4, n=2 illustration, generated from finite supports."""
    p = {i: Fraction(1, 4) for i in range(4)}
    q = {i: Fraction(1, 2) for i in range(2)}
    forward, backward = kl_bits(p, q), kl_bits(q, p)
    return {
        "m": len(p), "n": len(q),
        "log_coverage_bits": log2(len(p) / len(q)),
        "kl_p_to_q": "INFINITE_SUPPORT_MISMATCH" if forward == float("inf") else forward,
        "kl_q_to_p": backward,
    }
