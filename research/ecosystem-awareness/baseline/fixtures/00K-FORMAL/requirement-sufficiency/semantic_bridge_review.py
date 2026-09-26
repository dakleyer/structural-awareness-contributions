"""Bounded semantic diagnostics, not a canonical sufficiency certificate.

The historical A23 projection and its counterexamples remain unchanged.
Typed observations below supply information absent from that projection.
"""
from dataclasses import dataclass
from itertools import product
import json
from pathlib import Path

from requirement_sufficiency_model import State, P, R


@dataclass(frozen=True)
class Action:
    name: str
    required_propositions: frozenset[str]
    authority_scope: frozenset[str]


def unresolved_basis(action, unresolved):
    # A20 P3: unresolved propositions must belong to this action's basis.
    return bool(action.required_propositions & unresolved)


def qualified_response(action, unresolved, established):
    # Partial S5/T3/S14 implementation policy. No call to an A23 P function.
    return (action.name in action.authority_scope
            and action.required_propositions <= established
            and not (action.required_propositions & unresolved))


def false_corroboration(roots, counted):
    # A20 P6 targets independent corroboration, not every composition.
    return any(roots[a] == roots[b] for a, b in counted)


def replay(events, enforce=True):
    """One decision, always-authorized action, observable material changes.

    candidate S10/T2/S14 interlock: qualified revision must match the basis
    at each actuation; recording a disposition cannot update that revision.
    This is a declared operational refinement, not deduced canonical closure.
    """
    revision, qualified, disposition = 0, None, None
    log = []
    for event in events:
        if event == 'qualify':
            qualified = revision
        elif event == 'change':
            revision += 1
        elif event == 'record':
            disposition = revision
        elif event != 'act':
            raise ValueError(event)
        executed = event == 'act' and (not enforce or qualified == revision)
        log.append(dict(event=event, revision=revision, qualified=qualified,
                        disposition=disposition, executed=executed))
    return log


def stale_executions(events, log):
    # Independent history oracle: latest qualifying event must follow the
    # latest change. It does not inspect the runner's revision variables.
    last_qualification, last_change = -1, -1
    bad = []
    for i, (event, row) in enumerate(zip(events, log)):
        if event == 'qualify':
            last_qualification = i
        elif event == 'change':
            last_change = i
        elif event == 'act' and row['executed']:
            if last_qualification < 0 or last_qualification < last_change:
                bad.append(i)
    return bad


def certificate():
    original = json.loads(Path(__file__).with_name('clause_audit_certificate.json').read_text())
    retained = {}
    for i in (2, 4, 5):
        s = State(**original['bundles'][i]['counterexample'])
        retained[f'P{i+1}'] = {'bundle': R[i](s), 'target': P[i](s)}
    unresolved = frozenset({'route_safe'})
    established = frozenset({'stop_available'})
    response = Action('stop', frozenset({'stop_available'}), frozenset({'stop'}))
    continuation = Action('continue', frozenset({'route_safe'}), frozenset({'continue'}))
    p3 = {
        'response': {'material_to_this_action': unresolved_basis(response, unresolved),
                     'permitted_by_partial_policy': qualified_response(response, unresolved, established)},
        'continuation': {'material_to_this_action': unresolved_basis(continuation, unresolved),
                         'permitted_by_partial_policy': qualified_response(continuation, unresolved, established)},
        'classification': 'action/proposition linkage absent from the flat projection',
    }
    roots = {'r1': 'origin', 'r2': 'origin'}
    p6 = {'qualified_correlated_composition': false_corroboration(roots, ()),
          'same_records_counted_independent': false_corroboration(roots, (('r1', 'r2'),)),
          'classification': 'composition_active is not independent-corroboration counting'}
    traces = {
        'valid_continuity': ('qualify', 'act'),
        'record_only': ('qualify', 'change', 'record', 'act'),
        'requalified': ('qualify', 'change', 'record', 'qualify', 'act'),
        'second_change': ('qualify', 'change', 'qualify', 'change', 'act'),
    }
    examples = {name: {'events': events, 'enforced': replay(events),
                      'interlock_removed': replay(events, False)} for name, events in traces.items()}
    checked = valid_execution_traces = detected_mutant_traces = violations = 0
    alphabet = ('qualify', 'change', 'record', 'act')
    for length in range(1, 7):
        for events in product(alphabet, repeat=length):
            checked += 1
            good = replay(events)
            violations += bool(stale_executions(events, good))
            valid_execution_traces += any(row['executed'] for row in good)
            detected_mutant_traces += bool(stale_executions(events, replay(events, False)))
    return {'scope': 'one decision; observable changes; fixed authority; all event words of length 1..6',
            'historical_counterexamples_retained': retained, 'P3_diagnostic': p3, 'P6_diagnostic': p6,
            'P5_traces': examples, 'P5_bounded_enumeration': {
                'traces_checked': checked, 'stale_execution_traces_with_interlock': violations,
                'traces_with_permitted_execution': valid_execution_traces,
                'stale_execution_traces_when_interlock_removed': detected_mutant_traces},
            'all_six_canonical_sufficiency': 'NOT ESTABLISHED',
            'review_status': 'source-led author review, not independent peer review'}


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    Path(args.output).write_text(json.dumps(certificate(), indent=2, sort_keys=True) + '\n')
