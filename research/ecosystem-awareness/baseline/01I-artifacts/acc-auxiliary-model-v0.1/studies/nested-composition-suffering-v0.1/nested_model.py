"""ACC bounded research toy: nested composition, lost distinctions, and structural development gaps.

NO individual welfare measurement, no enumeration of open B/C/D, and no proof of
indeterminacy/undecidability in unbounded physical and social systems.
Only finite, declared test worlds. Standard library, deterministic.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import ceil, log2
from typing import Iterable, Sequence


@dataclass(frozen=True)
class ProducerWorld:
    """One upstream composite at current output 8; joint action may release 2."""
    joint_reallocation_possible: bool
    current_output: int = 8
    joint_output_if_possible: int = 10

    def __post_init__(self) -> None:
        if self.current_output != 8 or self.joint_output_if_possible != 10:
            raise ValueError('Fixed synthetic profile 8 to 10 only')


def current_handoff(w: ProducerWorld) -> tuple[int, int]:
    """Bounded receiver-visible A: supply request 8, actual delivered 8."""
    return (8, w.current_output)


def full_state_joint_capacity(w: ProducerWorld) -> int:
    """Full-state adjudication, never to be provided to an A-only receiver."""
    return w.joint_output_if_possible if w.joint_reallocation_possible else w.current_output


def receiver_only_decision_classes(worlds: Iterable[ProducerWorld]) -> dict[tuple[int, int], set[int]]:
    """Group legitimate responses to 'how much can be jointly delivered?' by observed A."""
    result: dict[tuple[int, int], set[int]] = {}
    for w in worlds:
        result.setdefault(current_handoff(w), set()).add(full_state_joint_capacity(w))
    return result


def agent_unilateral_reachability() -> dict[str, object]:
    """Two binary codependent actions x1=x2, unavailable unilateral changes."""
    states = [(0, 0), (1, 1)]
    initial = (0, 0)
    unilateral = [s for s in states if sum(int(a != b) for a, b in zip(initial, s)) == 1]
    return {
        'states': states,
        'initial': initial,
        'joint_pareto_superior': (1, 1),
        'strictly_better_for_both': (5, 5),
        'initial_utilities': (4, 4),
        'unilateral_successors': unilateral,
        'atomic_joint_edge_if_authorized': [initial, (1, 1)],
    }


@dataclass(frozen=True)
class HumanDevelopmentCandidate:
    """A stipulated STRUCTURAL definition, not self-reported suffering or dignity score."""
    actual_genuine_contribution: float
    demonstrated_jointly_feasible_contribution: float | None
    positive_contribution_to_others: bool | None
    blocked_without_unilateral_control: bool | None
    evidence_of_epistemic_insufficiency: bool | None
    rights_and_mission_preserved: bool | None


def structural_suffering_proxy(p: HumanDevelopmentCandidate) -> dict[str, object]:
    """Require all three author-specified conditions plus legitimate feasible comparator."""
    a, z = p.actual_genuine_contribution, p.demonstrated_jointly_feasible_contribution
    if not isinstance(a, (float, int)) or a < 0 or a != a:
        raise ValueError('Actual contribution must be observed and finite/nonnegative')
    if z is None or any(v is None for v in (p.positive_contribution_to_others,
                                             p.blocked_without_unilateral_control,
                                             p.evidence_of_epistemic_insufficiency,
                                             p.rights_and_mission_preserved)):
        return {'status': 'NOT_IDENTIFIED', 'structural_development_gap': None,
                'structural_suffering_proxy': None, 'subjective_suffering': 'NOT_MEASURED'}
    if not isinstance(z, (int, float)) or z < 0 or z != z or z == float('inf'):
        raise ValueError('Reference contribution must be finite and nonnegative')
    gap = max(0.0, float(z) - float(a))
    criteria = bool(gap > 0 and p.positive_contribution_to_others
                    and p.blocked_without_unilateral_control
                    and p.evidence_of_epistemic_insufficiency
                    and p.rights_and_mission_preserved)
    return {
        'status': 'STIPULATED_STRUCTURAL_CASE' if criteria else 'CRITERIA_NOT_ALL_MET',
        'structural_development_gap': gap,
        'structural_suffering_proxy': gap if criteria else 0.0,
        'subjective_suffering': 'NOT_MEASURED',
    }


def branch_profiles(n: int) -> list[tuple[int, ...]]:
    """Finite control family, NOT full external domain: capacities 8 or 10 per branch."""
    if type(n) is not int or n < 1 or n > 12:
        raise ValueError('Small bounded n required')
    return list(product((8, 10), repeat=n))


def current_nested_output(capacity_vector: Sequence[int]) -> int:
    """Aggregate of n measured outputs at request 8 on each branch."""
    if any(k not in (8, 10) for k in capacity_vector):
        raise ValueError('Only frozen synthetic capacities allowed')
    return sum(min(8, k) for k in capacity_vector)


def answer_future_branch(capacity_vector: Sequence[int], branch: int, request: int = 10) -> int:
    if not (0 <= branch < len(capacity_vector)) or request < 0:
        raise ValueError('Invalid branch or request')
    return min(request, capacity_vector[branch])


def distinct_future_answer_profiles(n: int) -> set[tuple[int, ...]]:
    """n independent branch-queries require distinguishing 2**n response vectors."""
    return {tuple(answer_future_branch(cap, i) for i in range(n)) for cap in branch_profiles(n)}


def minimum_interface_bits_for_all_branch_queries(n: int) -> int:
    """Pigeonhole lower bound for exact universal answers to the declared n queries."""
    m = len(distinct_future_answer_profiles(n))
    return (m - 1).bit_length()  # ceil(log2 m) for positive integers


def capacity_counterexample(n: int) -> dict[str, object]:
    """Current A alone cannot answer every future branch query for all n-bit capacities."""
    profiles = branch_profiles(n)
    values = {current_nested_output(x) for x in profiles}
    assert values == {8 * n}
    f = distinct_future_answer_profiles(n)
    return {'branch_count': n, 'distinct_hidden_states': len(profiles),
            'same_current_A': next(iter(values)),
            'distinct_future_query_response_vectors': len(f),
            'min_exact_message_bits_for_all_branch_queries': minimum_interface_bits_for_all_branch_queries(n),
            'not_uncomputability': True}


def cnf_satisfiable(nvars: int, clauses: Sequence[Sequence[int]]) -> tuple[bool, tuple[bool, ...] | None]:
    """Exhaustive finite SAT illustration: local clause tests compose into global search."""
    if nvars < 1 or nvars > 12 or any(not clause or any(abs(k) > nvars or k == 0 for k in clause) for clause in clauses):
        raise ValueError('Malformed finite CNF')
    for assignment in product((False, True), repeat=nvars):
        if all(any(assignment[abs(lit) - 1] if lit > 0 else not assignment[abs(lit) - 1]
                   for lit in clause) for clause in clauses):
            return True, assignment
    return False, None


def report() -> dict[str, object]:
    worlds = (ProducerWorld(False), ProducerWorld(True))
    structural = structural_suffering_proxy(HumanDevelopmentCandidate(
        actual_genuine_contribution=8,
        demonstrated_jointly_feasible_contribution=10,
        positive_contribution_to_others=True,
        blocked_without_unilateral_control=True,
        evidence_of_epistemic_insufficiency=True,
        rights_and_mission_preserved=True))
    return {
        'status': 'FINITE_SYNTHETIC_RESEARCH_ONLY',
        'current_handoff': current_handoff(worlds[0]),
        'joint_capacity_answers_under_same_A': sorted(receiver_only_decision_classes(worlds)[(8, 8)]),
        'rational_joint_trap': agent_unilateral_reachability(),
        'structural_human_analogue': structural,
        'nested_capacity_cases': [capacity_counterexample(n) for n in (1, 2, 3, 4, 6)],
        'cnf_local_checks_global_search': {
            'satisfiable': cnf_satisfiable(3, [(1, 2, 3), (-1, 2), (-2, 3)])[0],
            'unsatisfiable': cnf_satisfiable(1, [(1,), (-1,)])[0],
        },
        'undetermined_open_exterior': 'NOT_ENUMERATED_OR_QUANTIFIED',
        'empirical_welfare': 'NOT_MEASURED',
    }


if __name__ == '__main__':
    import json
    print(json.dumps(report(), indent=2, sort_keys=True, ensure_ascii=False))
