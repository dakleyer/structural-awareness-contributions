"""Serious P2 repair search for 00K A2 / 00E.

P2 invariant:
Unresolved determination effort must be finite, decision-relevant and bounded
by available capacity/response horizon, with an explicit bounded fallback.

This module intentionally tests strong conventional alternatives. A repair that
passes only by introducing a finite search budget, deadline, patience window,
bounded probe, or externally enforced stop is classified as semantic
reconstruction of P2, not as a unique EA mechanism.
"""
from dataclasses import dataclass
from enum import Enum
from itertools import product


class Action(Enum):
    CONTINUE = "CONTINUE"
    EXECUTE = "EXECUTE"
    NO_CONCLUSION = "NO_CONCLUSION"


class Disposition(Enum):
    EXECUTE = "EXECUTE"
    NO_CONCLUSION = "NO_CONCLUSION"
    RESOURCE_EXHAUSTED = "RESOURCE_EXHAUSTED"
    UNSAFE_DEFAULT = "UNSAFE_DEFAULT"


@dataclass(frozen=True)
class Observation:
    resolves: bool = False
    decision_relevant: bool = False


@dataclass(frozen=True)
class Fixture:
    stream: tuple[Observation, ...]
    hard_capacity: int
    useful_horizon: int


@dataclass(frozen=True)
class Result:
    disposition: Disposition
    steps: int
    mechanism: str


def matched_pair(horizon=6):
    prefix = tuple(Observation(False, False) for _ in range(horizon - 1))
    negative = Fixture(prefix + (Observation(False, False),), horizon, horizon)
    positive = Fixture(prefix + (Observation(True, True),), horizon, horizon)
    return negative, positive


def correct_negative(r: Result, f: Fixture) -> bool:
    return r.disposition == Disposition.NO_CONCLUSION and r.steps <= f.useful_horizon


def correct_positive(r: Result, f: Fixture) -> bool:
    return r.disposition == Disposition.EXECUTE and r.steps <= f.useful_horizon


def run_fixed_timeout(f: Fixture, limit: int) -> Result:
    steps = 0
    for obs in f.stream:
        if steps >= min(limit, f.hard_capacity):
            return Result(Disposition.NO_CONCLUSION, steps, "fixed_timeout")
        steps += 1
        if obs.resolves:
            return Result(Disposition.EXECUTE, steps, "fixed_timeout")
    if limit > f.useful_horizon:
        return Result(Disposition.RESOURCE_EXHAUSTED, f.hard_capacity, "fixed_timeout")
    return Result(Disposition.NO_CONCLUSION, steps, "fixed_timeout")


def run_no_progress_breaker(f: Fixture, patience: int) -> Result:
    streak = 0
    steps = 0
    for obs in f.stream:
        steps += 1
        if obs.resolves:
            return Result(Disposition.EXECUTE, steps, "no_progress_breaker")
        if obs.decision_relevant:
            streak = 0
        else:
            streak += 1
        if streak >= patience:
            return Result(Disposition.NO_CONCLUSION, steps, "no_progress_breaker")
    return Result(Disposition.RESOURCE_EXHAUSTED, steps, "no_progress_breaker")


def run_parallel_fanout(f: Fixture, batch_size: int, max_rounds: int) -> Result:
    idx = 0
    steps = 0
    for _round in range(max_rounds):
        batch = f.stream[idx: idx + batch_size]
        if not batch:
            break
        for obs in batch:
            steps += 1
            if obs.resolves:
                return Result(Disposition.EXECUTE, steps, "parallel_fanout")
            if steps >= f.hard_capacity:
                break
        idx += len(batch)
        if steps >= f.hard_capacity:
            break
    if steps <= f.useful_horizon and idx >= len(f.stream):
        return Result(Disposition.NO_CONCLUSION, steps, "parallel_fanout")
    if steps <= f.useful_horizon and max_rounds * batch_size < len(f.stream):
        return Result(Disposition.NO_CONCLUSION, steps, "parallel_fanout")
    return Result(Disposition.RESOURCE_EXHAUSTED, steps, "parallel_fanout")


def run_cached_default(f: Fixture, default_after: int) -> Result:
    steps = 0
    for obs in f.stream:
        steps += 1
        if obs.resolves:
            return Result(Disposition.EXECUTE, steps, "cached_default")
        if steps >= default_after:
            return Result(Disposition.UNSAFE_DEFAULT, steps, "cached_default")
    return Result(Disposition.UNSAFE_DEFAULT, steps, "cached_default")


def run_external_scheduler(f: Fixture, deadline: int) -> Result:
    return run_fixed_timeout(f, deadline)


def run_bounded_probe(f: Fixture, probe_at: int) -> Result:
    steps = 0
    for obs in f.stream:
        steps += 1
        if obs.resolves:
            return Result(Disposition.EXECUTE, steps, "bounded_probe")
        if steps >= probe_at:
            return Result(Disposition.NO_CONCLUSION, steps, "bounded_probe")
    return Result(Disposition.NO_CONCLUSION, steps, "bounded_probe")


def memoryless_policy_passes(policy, negative: Fixture, positive: Fixture) -> bool:
    def run(f):
        for i, obs in enumerate(f.stream, start=1):
            key = "X" if obs.resolves else "I"
            a = policy[key]
            if a == Action.EXECUTE:
                return Result(Disposition.EXECUTE, i, "memoryless")
            if a == Action.NO_CONCLUSION:
                return Result(Disposition.NO_CONCLUSION, i, "memoryless")
        return Result(Disposition.RESOURCE_EXHAUSTED, f.hard_capacity, "memoryless")
    return correct_negative(run(negative), negative) and correct_positive(run(positive), positive)


def enumerate_memoryless_policies(negative: Fixture, positive: Fixture):
    winners = []
    for ai, ax in product(Action, repeat=2):
        policy = {"I": ai, "X": ax}
        if memoryless_policy_passes(policy, negative, positive):
            winners.append(policy)
    return winners


def horizon_aware_policy(f: Fixture) -> Result:
    for i, obs in enumerate(f.stream, start=1):
        if obs.resolves:
            return Result(Disposition.EXECUTE, i, "horizon_aware")
        if i >= f.useful_horizon:
            return Result(Disposition.NO_CONCLUSION, i, "horizon_aware")
    return Result(Disposition.NO_CONCLUSION, len(f.stream), "horizon_aware")
