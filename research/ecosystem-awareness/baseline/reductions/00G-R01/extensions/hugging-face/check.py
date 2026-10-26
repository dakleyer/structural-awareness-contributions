"""R01 -> HF-inspired SYNTHETIC task-board encoding, v0.1.
Standard-library Python. No API, model, exploit, network or historical replay.
Finite transport checks and counterexamples; not full R01/A25 admission.
Run python3 check.py; results.json is regenerated beside this file.
"""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import product, combinations
from pathlib import Path
import hashlib
import json
import math


def powerset(items):
    for k in range(len(items) + 1):
        yield from combinations(items, k)


def make_world(length, spread, distance_spread, alignment, mixed, rule, bad):
    """Four chains, with optional cross-chain connectors; normative task fixed.
    bad=-1: all conditions on chain 2 hold. Otherwise one fails.
    Chain 3 has a visible-at-query prohibition. All labels are evaluator-only.
    Parity is explicitly an artificial composition control, not permission logic.
    """
    vertices, links = {}, {}
    for stage, branch in product(range(length), range(4)):
        z = F(2 * stage - length + 1, length - 1)
        vertices[(stage, branch)] = {
            'benefit': F(branch + 1) + spread * z,
            'position': F(0) if branch == 0 else F(branch + 1) + alignment * distance_spread * z,
            'bit': int((branch == 2 and stage == bad) or
                       (branch == 3 and stage == 0)),
        }
    for stage in range(length - 1):
        for left, right in product(range(4), repeat=2):
            if mixed or left == right:
                links[((stage, left), (stage + 1, right))] = {
                    'allowed': not (left == 3 and right == 2),
                    'cost': int(left != right),
                }
    return {'length': length, 'vertices': vertices, 'links': links, 'rule': rule}


def base_paths(world):
    for branches in product(range(4), repeat=world['length']):
        path = tuple(enumerate(branches))
        if all((a, b) in world['links'] for a, b in zip(path, path[1:])):
            yield path


def base_outcome(world, path):
    values = [world['vertices'][node] for node in path]
    checks = [v['bit'] == 0 for v in values]
    permission = all(checks) if world['rule'] == 'conjunction' else sum(v['bit'] for v in values) % 2 == 0
    permission &= all(world['links'][a, b]['allowed'] for a, b in zip(path, path[1:]))
    return bool(permission), sum(v['benefit'] for v in values)


def encode(world, salt):
    """HF-inspired vocabulary only: work items, a shared board and owner facts.
    Board claims do not issue authority. IDs contain no branch verdict labels.
    The bijection is held by this auditor, not furnished as agent evidence.
    """
    names = {node: hashlib.sha256(f'{salt}:{node}'.encode()).hexdigest()[:16]
             for node in world['vertices']}
    tasks, facts, transitions = {}, {}, {}
    for node, v in world['vertices'].items():
        key = names[node]
        tasks[key] = {'stage': node[0], 'technical_value': str(v['benefit']),
                      'search_coordinate': str(v['position']), 'next': []}
        facts[key] = {'owner': 'task-owner', 'mission': 'fixed-research-task',
                      'recipient': 'receiver-0', 'version': 1, 'bit': v['bit']}
    for (left, right), edge in world['links'].items():
        tasks[names[left]]['next'].append(names[right])
        transitions[names[left], names[right]] = dict(edge)
    for task in tasks.values():
        task['next'].sort()
    return {'tasks': tasks, 'owner_facts': facts, 'transitions': transitions,
            'composition': world['rule'], 'length': world['length']}, names


def target_paths(target):
    def visit(path):
        if len(path) == target['length']:
            yield tuple(path)
        else:
            for nxt in target['tasks'][path[-1]]['next']:
                yield from visit(path + [nxt])
    for key, task in target['tasks'].items():
        if task['stage'] == 0:
            yield from visit([key])


def target_outcome(target, path):
    bits = [target['owner_facts'][key]['bit'] for key in path]
    if target['composition'] == 'conjunction':
        acceptable = not any(bits)
    else:
        parity = 0
        for bit in bits:
            parity ^= bit
        acceptable = parity == 0
    for a, b in zip(path, path[1:]):
        acceptable = acceptable and target['transitions'][a, b]['allowed']
    return bool(acceptable), sum(F(target['tasks'][key]['technical_value']) for key in path)


def optimal_quality(world):
    return max(value for path in base_paths(world)
               for ok, value in [base_outcome(world, path)] if ok)


def query_value(size, budget, strict, certificate, encoded=False):
    """Exact finite decision problem; not the full graph/search/social campaign.
    Worlds: all U conditions valid (mass 1/2), or one invalid (mass 1/(2U)).
    Deliver high route in valid world, fallback in other worlds. A strict gate
    requires complete positive coverage for the high route. Queries cost one.
    encoded=True accesses a separately constructed target owner-record store.
    """
    names = tuple(hashlib.sha256(f'condition:{j}'.encode()).hexdigest()[:12]
                  for j in range(size))
    records = {w: {name: not (w == j + 1) for j, name in enumerate(names)}
               for w in range(size + 1)}
    prior = (F(1, 2),) + (F(1, 2 * size),) * size

    @lru_cache(None)
    def solve(possible, queried, left):
        high = prior[0] if 0 in possible else F(0)
        mass = sum(prior[w] for w in possible)
        options = [mass - high]
        if not strict or len(queried) == size or 0 not in possible:
            options.append(high)
        if left:
            if certificate:
                options.append(mass)
            for j in range(size):
                if j in queried:
                    continue
                total = F(0)
                for answer in (False, True):
                    subset = tuple(w for w in possible if
                                   (records[w][names[j]] if encoded else w != j + 1) == answer)
                    if subset:
                        total += solve(subset, tuple(sorted(queried + (j,))), left - 1)
                options.append(total)
        return max(options)
    return solve(tuple(range(size + 1)), (), budget)


def receipt_valid(receipt, question):
    return all(receipt.get(k) == value for k, value in question.items()) and receipt.get('bit') == 0


def run():
    counts = Counter()
    # Joint sweeps retain benefit/location pairing, connections and private facts.
    for length, spread, tau, alignment, mixed, rule in product(
            (2, 3, 4), (F(0), F(1, 4)), (F(0), F(1, 2)), (-1, 1),
            (False, True), ('conjunction', 'parity')):
        for bad in (-1, 0, length - 1):
            world = make_world(length, spread, tau, alignment, mixed, rule, bad)
            reference = list(base_paths(world))
            for salt in ('first-permutation', 'second-permutation'):
                target, names = encode(world, salt)
                reverse = {v: k for k, v in names.items()}
                paths = list(target_paths(target))
                assert {tuple(reverse[k] for k in p) for p in paths} == set(reference)
                counts['path_set_bijections'] += 1
                for path in reference:
                    target_path = tuple(names[n] for n in path)
                    assert base_outcome(world, path) == target_outcome(target, target_path)
                    for radius in (F(1), F(5, 2), F(5)):
                        a = all(abs(world['vertices'][n]['position']) <= radius for n in path)
                        b = all(abs(F(target['tasks'][k]['search_coordinate'])) <= radius for k in target_path)
                        assert a == b
                        counts['joint_radius_path_checks'] += 1
                    assert sum(world['links'][a, b]['cost'] for a, b in zip(path, path[1:])) == sum(
                        target['transitions'][a, b]['cost'] for a, b in zip(target_path, target_path[1:]))
                    counts['path_outcome_and_connector_checks'] += 1
                best = max(value for p in paths for ok, value in [target_outcome(target, p)] if ok)
                assert best == optimal_quality(world)
                counts['exact_optima'] += 1
                for branch in range(4):
                    seq = [world['vertices'][j, branch] for j in range(length)]
                    assert sum(v['benefit'] for v in seq) / length == branch + 1
                    assert max(v['benefit'] for v in seq) - min(v['benefit'] for v in seq) == 2 * spread
                    assert sum(v['position'] for v in seq) / length == (0 if branch == 0 else branch + 1)
                    assert max(v['position'] for v in seq) - min(v['position'] for v in seq) == (0 if branch == 0 else 2 * tau)
                    counts['realized_chain_profiles'] += 1
            counts['joint_configurations'] += 1

    # Same entire declared public view, distinct unqueried applicable owner fact.
    for length in (2, 3, 4):
        good = make_world(length, F(1, 4), F(1, 2), 1, False, 'conjunction', -1)
        app0, names = encode(good, 'view')
        for subset in powerset(tuple(range(length))):
            if len(subset) == length:
                continue
            missing = next(j for j in range(length) if j not in subset)
            bad = make_world(length, F(1, 4), F(1, 2), 1, False, 'conjunction', missing)
            app1, _ = encode(bad, 'view')
            def view(app):
                visible_facts = {key: fact for key, fact in app['owner_facts'].items()
                                 if key not in {names[j, 2] for j in range(length) if j not in subset}}
                return app['tasks'], app['transitions'], app['composition'], visible_facts
            assert view(app0) == view(app1)
            path = tuple(names[j, 2] for j in range(length))
            assert target_outcome(app0, path)[0] and not target_outcome(app1, path)[0]
            counts['complete_view_pairs'] += 1

    curves = []
    for size in (2, 3, 4):
        for budget in range(size + 1):
            row = {'U': size, 'budget': budget}
            for key, strict, certificate in [('optimistic', False, False),
                                             ('strict', True, False), ('certificate', True, True)]:
                a = query_value(size, budget, strict, certificate)
                b = query_value(size, budget, strict, certificate, encoded=True)
                expected = (F(1, 2) + F(budget, 2 * size) if key == 'optimistic'
                            else (F(1) if (budget >= 1 if certificate else budget == size) else F(1, 2)))
                assert a == b == expected
                row[key] = str(a)
                counts['exact_query_policy_values'] += 1
            curves.append(row)

    # Transfer the explicit cost identities of R01, not universal lower bounds.
    cost_identities = []
    for length, agents, cv in product((2, 3, 4, 8), (1, 2, 4), (F(1, 2), F(1))):
        ids = [hashlib.sha256(f'work:{j}'.encode()).hexdigest()[:16] for j in range(length)]
        once = [key for _ in range(agents) for key in ids]
        prefixes = [key for _ in range(agents) for end in range(1, length + 1) for key in ids[:end]]
        full_per_step = [key for _ in range(agents) for _ in ids for key in ids]
        assert cv * len(once) == cv * agents * length
        assert cv * len(prefixes) == cv * agents * length * (length + 1) / 2
        assert cv * len(full_per_step) == cv * agents * length * length
        rejection_counts = [next(k + 1 for k, key in enumerate(ids) if key == bad) for bad in ids]
        assert F(sum(rejection_counts), length) == F(length + 1, 2)
        for invalid_fraction in (F(0), F(1, 2), F(1)):
            actual = cv * (invalid_fraction * F(sum(rejection_counts), length) + (1 - invalid_fraction) * length)
            expected = cv * (invalid_fraction * F(length + 1, 2) + (1 - invalid_fraction) * length)
            assert actual == expected
            counts['early_exit_cost_identities'] += 1
        counts['full_and_repeated_cost_identities'] += 3
        for candidate, behind, ahead in product(range(length), (0, 1, length), (0, 1, length)):
            units = set(range(max(0, candidate - behind), min(length, candidate + ahead + 1)))
            mapped = {ids[j] for j in units}
            assert len(mapped) == len(units)
            assert len(mapped | mapped) == len(units)
            counts['window_unique_coverage_checks'] += 1
        cost_identities.append({'L': length, 'N': agents, 'cv': str(cv),
                                'once': str(cv * len(once)),
                                'prefixes': str(cv * len(prefixes)),
                                'full_per_step': str(cv * len(full_per_step))})

    # Coverage and resource coupling; N is not multiplied into necessary facts U.
    resources = []
    for length, uncovered, agents in product((2, 4, 8), (1, 2, 4), (1, 2, 4)):
        if uncovered > length:
            continue
        assignments = [list(range(a, uncovered, agents)) for a in range(agents)]
        assert sorted(j for group in assignments for j in group) == list(range(uncovered))
        ce, cv, cm = F(2), F(1), F(1, 4)  # 0 < cv < ce, synthetic units
        messages = sum(bool(group) for group in assignments)
        coordination = messages * cm
        shared_cost = uncovered * cv + coordination
        duplicate_cost = agents * uncovered * cv + agents * cm
        query_latency = max(map(len, assignments))
        assert query_latency == math.ceil(uncovered / agents)
        assert shared_cost <= duplicate_cost
        assert cv / ce == F(1, 2)
        fixed_total, fixed_per_agent = F(4), agents * F(4)
        resources.append({'L': length, 'U': uncovered, 'N': agents,
                          'shared_cost': str(shared_cost), 'duplicate_cost': str(duplicate_cost),
                          'query_rounds': query_latency, 'coordination_included_once': str(coordination),
                          'fits_fixed_total_4': shared_cost <= fixed_total,
                          'fits_4_per_agent': shared_cost <= fixed_per_agent})
        counts['population_resource_configurations'] += 1
        roots = {'root-0' for _ in range(agents)}
        assert len(roots) == 1
        counts['relay_deduplication_checks'] += 1

    question = {'owner': 'task-owner', 'mission': 'fixed-research-task',
                'recipient': 'receiver-0', 'version': 1}
    valid = dict(question, bit=0)
    assert receipt_valid(valid, question)
    for field, other in [('owner', 'peer-coordinator'), ('mission', 'collective-project'),
                         ('recipient', 'receiver-1'), ('version', 2), ('bit', 1)]:
        changed = dict(valid, **{field: other})
        assert not receipt_valid(changed, question)
        counts['scope_and_authority_rejections'] += 1

    # Counterexamples to claiming transfer from separate marginals or analogies.
    # The same benefit and distance multisets give different best reachable value.
    aligned, reversed_pairs = [(1, 1), (3, 3)], [(1, 3), (3, 1)]
    assert sorted(b for b, d in aligned) == sorted(b for b, d in reversed_pairs)
    assert sorted(d for b, d in aligned) == sorted(d for b, d in reversed_pairs)
    best1 = max(b for b, d in aligned if d <= 1)
    best2 = max(b for b, d in reversed_pairs if d <= 1)
    assert (best1, best2) == (1, 3)
    # AND and parity agree on one view yet differ on a hidden two-bit completion.
    assert all([False, False]) != (sum([1, 1]) % 2 == 0)
    # A known-negative rejecting receiver cannot reproduce known-negative execution.
    basic_transitions = {'denial_detected': {'reject'}, 'insufficient': {'review', 'hold'}}
    constructed_nonconforming_transition = ('denial_detected', 'execute')
    state, action = constructed_nonconforming_transition
    assert action not in basic_transitions[state]
    # No legal completion -> no M and no I as required by the admitted base class.
    legal_completions = [p for p, allowed in [('x', False), ('y', False)] if allowed]
    assert not legal_completions
    counterexamples = {
        'same_marginals_different_coupling': {'best_within_radius_1': [best1, best2]},
        'composition_rule_changed': 'AND and parity are not interchangeable',
        'known_prohibition_still_executed': 'outside the basic rejecting receiver',
        'no_legal_completion': 'cannot preserve required M/I without changing the task',
        'sufficient_aggregate': 'certificate curve removes the modeled information obstruction',
    }
    result = {
        'status': 'ALL_FINITE_ASSERTIONS_PASSED',
        'scope': 'Synthetic encoding and explicit counterexamples only; no historical replay, LLM, network or product execution',
        'full_R01_extensionality': 'NOT_ESTABLISHED', 'historical_HF_admission': 'NOT_ESTABLISHED',
        'EA_differential': 'NOT_TESTED', 'counts': dict(sorted(counts.items())),
        'query_curves': curves, 'resource_examples': resources, 'cost_identities': cost_identities,
        'counterexamples': counterexamples,
    }
    path = Path(__file__).with_name('results.json')
    path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps({k: result[k] for k in ('status', 'scope', 'counts', 'full_R01_extensionality')}, indent=2))


if __name__ == '__main__':
    run()
