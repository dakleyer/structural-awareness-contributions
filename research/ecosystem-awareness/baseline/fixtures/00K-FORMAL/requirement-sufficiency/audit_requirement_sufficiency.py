"""Exact Boolean support projections; no reachability or source-fidelity proof.

Every omitted field is absent from a validated Boolean expression, so each
projected row represents all assignments to those omitted fields.
"""
from __future__ import annotations
import ast
import inspect
import json
import textwrap
from dataclasses import asdict, fields
from functools import lru_cache
from pathlib import Path
from requirement_sufficiency_model import BUNDLE_CLAUSES, P, State, states
FIELDS = tuple(f.name for f in fields(State))

@lru_cache(maxsize=None)
def support(fn):
    node = ast.parse(textwrap.dedent(inspect.getsource(fn))).body[0]
    if not isinstance(node, ast.FunctionDef) or len(node.args.args) != 1:
        raise ValueError('predicate must be a one-argument function')
    if len(node.body) != 1 or not isinstance(node.body[0], ast.Return):
        raise ValueError('predicate must contain one Boolean return expression')
    arg, names = node.args.args[0].arg, set()
    def check(expr):
        if isinstance(expr, ast.Attribute) and isinstance(expr.value, ast.Name):
            if expr.value.id != arg or expr.attr not in FIELDS:
                raise ValueError('only declared State fields are allowed')
            names.add(expr.attr)
        elif isinstance(expr, ast.BoolOp) and isinstance(expr.op, (ast.And, ast.Or)):
            for value in expr.values: check(value)
        elif isinstance(expr, ast.UnaryOp) and isinstance(expr.op, ast.Not):
            check(expr.operand)
        elif isinstance(expr, ast.Constant) and type(expr.value) is bool:
            pass
        else:
            raise ValueError('calls, hidden globals and non-Boolean expressions are forbidden')
    check(node.body[0].value)
    return frozenset(names)

def projected_fields(functions):
    used = set().union(*(support(fn) for fn in functions))
    return tuple(name for name in FIELDS if name in used)

def clause_relation(clause, target):
    names = projected_fields((clause, target))
    different = without_target = None
    satisfiable = falsifiable = False
    for s in states(names):
        c, p = clause(s), target(s)
        satisfiable |= c
        falsifiable |= not c
        if c != p and different is None:
            different = {name: getattr(s, name) for name in names}
        if c and not p and without_target is None:
            without_target = {name: getattr(s, name) for name in names}
    return dict(fields=names, states_checked=2**len(names),
                equivalent_to_target=different is None,
                alone_implies_target=without_target is None,
                satisfiable=satisfiable, falsifiable=falsifiable,
                non_equivalence_witness=different,
                clause_without_target_witness=without_target)

def assert_no_target_shortcut(clause, target):
    result = clause_relation(clause, target)
    assert not result['equivalent_to_target'], f'{clause.__name__} alone is equivalent to {target.__name__}'
    # Stronger guard: target AND an unrelated field also conceals the target.
    assert not result['alone_implies_target'], f'{clause.__name__} alone implies {target.__name__}'
    assert result['satisfiable'] and result['falsifiable'], 'vacuous clause'
    return result

def bundle_result(index):
    target, clauses = P[index], BUNDLE_CLAUSES[index]
    names = projected_fields((target, *clauses))
    counterexample, conforming, violations = None, 0, 0
    for s in states(names):
        if all(clause(s) for clause in clauses):
            conforming += 1
            if not target(s):
                violations += 1
                if counterexample is None: counterexample = asdict(s)
    return dict(principle=f'P{index+1}',
                status='finite-projection implication' if not violations else 'countermodel; semantic review pending',
                fields=names, projected_states_checked=2**len(names),
                full_cube_assignments_per_row=2**(len(FIELDS)-len(names)),
                conforming_projected_states=conforming,
                violating_projected_states=violations, implies_target=violations==0,
                counterexample=counterexample,
                clauses={c.__name__: assert_no_target_shortcut(c, target) for c in clauses})

def certificate():
    return dict(schema='A23-clause-audit-v1',
                source='00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md sections 2-3',
                state_fields=FIELDS, full_state_count=2**len(FIELDS),
                method='exhaustive support projections; syntactically validated Boolean field expressions',
                scope='partial clause projections, not full canonical conformance or reachability',
                bundles=[bundle_result(i) for i in range(6)])

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    encoded = json.dumps(certificate(), indent=2, sort_keys=True) + '\n'
    if args.output: args.output.write_text(encoded, encoding='utf-8')
    else: print(encoded, end='')
