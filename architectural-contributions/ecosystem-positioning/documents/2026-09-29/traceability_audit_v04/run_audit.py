"""Run with Python 3.10+. Standard library only. No network or product APIs."""
import ast
import hashlib
import json
from itertools import combinations, product
from pathlib import Path
import candidates as c
import evaluators as e

HERE = Path(__file__).resolve().parent

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def bucket():
    return dict(checked=0, discrepancies=0, first_counterexample=None)

def observe(result, mismatch, example):
    result['checked'] += 1
    if mismatch:
        result['discrepancies'] += 1
        if result['first_counterexample'] is None:
            result['first_counterexample'] = example

def run():
    assert (HERE/'PROTOCOL.sha256').read_text().split()[0] == sha(HERE/'PROTOCOL.md')
    out = {'scope': 'same-author bounded semantic audit; no all-six HC or HS proof',
           'protocol_sha256': sha(HERE/'PROTOCOL.md')}
    p1 = {m: bucket() for m in ('qualified', 'promote_positive')}
    for evidence in product((-1, 0, 1), repeat=3):
        for mask in range(1, 8):
            required = [i for i in range(3) if mask & (1 << i)]
            expected = e.entailed(evidence, required)
            for name in p1:
                actual = c.support(evidence, required, name != 'qualified')
                observe(p1[name], actual != expected, dict(evidence=evidence, required=required, expected=expected, actual=actual))
    out['P1'] = p1
    p2 = {m: bucket() for m in ('reserved_response', 'ignore_response_cost')}
    for length in range(1, 6):
        for durations in product(range(1, 5), repeat=length):
            for budget in range(1, 9):
                for response in range(1, min(3, budget)+1):
                    for name in p2:
                        events = c.schedule(durations, budget, response, name != 'reserved_response')
                        observe(p2[name], not e.timely(events, budget), dict(durations=durations, budget=budget, response=response, events=events))
    out['P2'] = p2
    fixtures = [
        ('U1', {'stop'}, {'route'}, {'route'}, True, False),
        ('U2', {'stop'}, {'route'}, {'stop'}, True, True),
        ('U3', {'stop'}, {'route'}, {'stop'}, False, False),
        ('U4', {'route'}, {'weather'}, {'route'}, True, True),
        ('U5', set(), {'route'}, {'route'}, True, False),
        ('U6', {'route', 'stop'}, set(), {'route', 'stop'}, True, True),
        ('U7', {'stop'}, set(), {'route'}, True, False),
        ('U8', {'route'}, {'route'}, {'route'}, True, False)]
    p3 = {m: bucket() for m in ('none','unknown_is_permission','all_unknown_blocks','ignore_unknown')}
    for ident, established, unknown, required, authorized, expected in fixtures:
        for name in p3:
            actual = c.disposition(established, unknown, required, authorized, name)
            observe(p3[name], actual != expected, dict(fixture=ident, expected=expected, actual=actual))
    out['P3'] = p3
    p4 = {m: bucket() for m in ('none','union','revocation','cap')}
    # All chains, all revocation patterns, all nonempty requested batches.
    # Uniform cap 1/2/3; heterogeneous-cap examples are extra controls below.
    for scopes in product(range(8), repeat=3):
        for revoked in product((False, True), repeat=3):
            for cap in range(1, 4):
                caps = (cap, cap, cap)
                for actions in range(1, 8):
                    expected = e.permitted_by_issuers(scopes, revoked, caps, actions)
                    for name in p4:
                        actual = c.delegation(scopes, revoked, caps, actions, name)
                        observe(p4[name], actual != expected, dict(scopes=scopes, revoked=revoked, caps=caps, actions=actions, expected=expected, actual=actual))
    out['P4'] = p4
    p5 = {m: dict(checked=0, bad_traces=0, active_traces=0, first_counterexample=None) for m in ('atomic_visible','record_qualifies','cached','open','hold','atomic_hidden')}
    for length in range(1, 8):
        for events in product('QCRKAX', repeat=length):
            hidden = 'X' in events
            for name, stats in p5.items():
                if hidden and name != 'atomic_hidden':
                    continue
                policy = 'atomic' if name.startswith('atomic') else name
                actual = c.execution(events, policy)
                bad = e.bad_execution(events, actual)
                stats['checked'] += 1
                stats['bad_traces'] += bad
                stats['active_traces'] += any(actual)
                if bad and stats['first_counterexample'] is None:
                    stats['first_counterexample'] = dict(events=''.join(events), executions=actual)
    controls = {'qualified': 'QA', 'renewed': 'QCQA', 'record_only': 'QCRA', 'race': 'QKCA', 'hidden': 'QXA'}
    out['P5'] = p5
    out['P5_controls'] = {policy: {name: c.execution(events, policy)[-1] for name, events in controls.items()} for policy in ('atomic','record_qualifies','cached','open','hold')}
    p6 = {m: bucket() for m in ('none','names','parents')}
    possible_edges = list(combinations(range(5), 2))
    for bits in product((False, True), repeat=len(possible_edges)):
        edges = [edge for edge, bit in zip(possible_edges, bits) if bit]
        for a,b in combinations(range(5), 2):
            expected = e.unrelated_roots(edges, a, b)
            for name in p6:
                actual = c.independent(edges, a, b, name)
                observe(p6[name], actual != expected, dict(edges=edges, pair=[a,b], expected=expected, actual=actual))
    out['P6'] = p6
    contexts = list(product((0,1), repeat=2))
    cells = {str(x): [dict(context=w, required_action=w[1]) for w in contexts if w[0]==x] for x in (0,1)}
    decoders=[]
    for decoder in product((0,1), repeat=2):
        errors=[w for w in contexts if decoder[w[0]]!=w[1]]
        decoders.append(dict(outputs=decoder, incompatible_contexts=errors))
    full_cells = {str(w): {w[1]} for w in contexts}
    out['H4_observation_limit'] = dict(cells=cells, deterministic_decoders=decoders,
        impossible_decoders=len([d for d in decoders if d['incompatible_contexts']]), total_decoders=len(decoders),
        full_observation_ambiguous_cells=sum(len(actions)>1 for actions in full_cells.values()),
        limit='Separating observation cells is a representation property, not measured carrier feasibility or H4 confirmation.')
    # Structural isolation: evaluators do not import candidates or model predicates.
    tree=ast.parse((HERE/'evaluators.py').read_text())
    imports=[n.module for n in ast.walk(tree) if isinstance(n,ast.ImportFrom)]
    imports += [a.name for n in ast.walk(tree) if isinstance(n,ast.Import) for a in n.names]
    assert imports == ['itertools'], imports
    out['isolation'] = dict(evaluator_imports=imports, independent_authorship=False,
        semantic_validation='manual source-led translation; shared conceptual assumptions remain')
    # Check safety, non-vacuity and mutation sensitivity, not raw count inflation.
    for name,good in [('P1','qualified'),('P2','reserved_response'),('P3','none'),('P4','none'),('P6','none')]:
        assert out[name][good]['discrepancies']==0
        assert all(v['discrepancies']>0 for k,v in out[name].items() if k!=good)
    assert p5['atomic_visible']['bad_traces']==0 and p5['atomic_visible']['active_traces']>0
    assert all(p5[m]['bad_traces']>0 for m in ('record_qualifies','cached','open','atomic_hidden'))
    assert not out['P5_controls']['hold']['qualified']
    out['acceptance'] = 'All declared bounded checks and adverse-result controls behaved as specified; HC, empirical H1-H6, and HS remain unestablished.'
    out['file_sha256']={p.name:sha(p) for p in sorted(HERE.glob('*.py'))}
    (HERE/'results.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k in ('P5','acceptance')},indent=2))

if __name__ == '__main__':
    run()
