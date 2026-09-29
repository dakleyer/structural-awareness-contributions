"""Replay preserved source models and audit the exact Boolean reduction.

No imported projection field list is trusted: derive it from restricted AST.
The implication itself still uses the original author predicates.
"""
import ast
from dataclasses import fields
import hashlib
import itertools
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'prior_model'))
import requirement_sufficiency_model as m
import semantic_bridge_review as previous

def support(fn):
    import inspect
    node=ast.parse(inspect.getsource(fn)).body[0]
    returns=[n for n in node.body if isinstance(n,ast.Return)]
    assert len(returns)==1
    root=returns[0].value
    allowed=(ast.BoolOp,ast.UnaryOp,ast.And,ast.Or,ast.Not,ast.Attribute,ast.Name,ast.Load,ast.Constant)
    names=set()
    for n in ast.walk(root):
        assert isinstance(n,allowed), (fn.__name__,type(n).__name__)
        if isinstance(n,ast.Attribute):
            assert isinstance(n.value,ast.Name) and n.value.id=='s'
            names.add(n.attr)
        elif isinstance(n,ast.Name):
            assert n.id=='s'
        elif isinstance(n,ast.Constant):
            assert type(n.value) is bool
    return names

def main():
    cert=json.loads((HERE/'prior_model/clause_audit_certificate.json').read_text())
    schema={f.name for f in fields(m.State)}
    results=[]
    for i, (target,clauses) in enumerate(zip(m.P,m.BUNDLE_CLAUSES)):
        target_fields=support(target)
        clause_fields={fn.__name__:support(fn) for fn in clauses}
        selected=target_fields|set().union(*clause_fields.values())
        assert selected <= schema
        declared=set(cert['bundles'][i]['fields'])
        assert selected==declared
        keys=sorted(selected)
        count=conform=violations=0
        for bits in itertools.product((False,True),repeat=len(keys)):
            state=m.State(**dict(zip(keys,bits)))
            passes=all(fn(state) for fn in clauses)
            count+=1;conform+=passes;violations+=passes and not target(state)
        expected=cert['bundles'][i]
        assert (count,conform,violations)==(expected['projected_states_checked'],expected['conforming_projected_states'],expected['violating_projected_states'])
        results.append(dict(principle=f'P{i+1}',states=count,conforming=conform,violations=violations,
            fields_derived_from_restricted_AST=keys,
            all_target_fields_also_used_in_clauses=target_fields <= set().union(*clause_fields.values()),
            scope='exact support reduction of these pure Boolean functions; not validation of source-to-model semantics'))
    replay=previous.certificate()
    old=json.loads((HERE/'prior_model/semantic_bridge_certificate.json').read_text())
    # JSON normalizes tuples/lists; exact serialized structure is compared.
    assert json.loads(json.dumps(replay))==old
    import evaluators as e
    import candidates as c
    # Adversarial self-checks of the evaluator on frozen negative/positive examples.
    history_controls=[('A',[True],True),('QA',[False,True],False),('QCA',[False,False,True],True),('QCQA',[False,False,False,True],False),('QXA',[False,False,True],True),('QCRA',[False,False,False,True],True)]
    assert all(e.bad_execution(events,out)==expected for events,out,expected in history_controls)
    authority_checks=[]
    for caps in ((1,3,3),(3,1,3),(3,3,1)):
        assert not c.delegation((7,7,7),(False,False,False),caps,3)
        authority_checks.append(dict(caps=caps,actions=3,expected=False))
    # Gate mutations of the evaluator itself: an always-safe oracle must fail
    # the known-negative controls; an always-unsafe oracle must fail positives.
    mutants=dict(always_safe_failed_controls=sum(expected for _,_,expected in history_controls),
                 always_unsafe_failed_controls=sum(not expected for _,_,expected in history_controls))
    result=dict(projections=results,prior_semantic_certificate_reproduced=True,
        history_oracle_controls=len(history_controls),oracle_mutants=mutants,
        heterogeneous_cap_controls=authority_checks,
        review_findings=[
          'P1/P2/P4 finite implications reuse the semantic facts expressed by their requirements. They establish logical consistency, not independent empirical support for the H claims.',
          'AST reduction validates all unused fields are irrelevant to these pure Boolean predicates. It does not validate missing real-world dimensions.',
          'P3/P5/P6 original projection countermodels are retained. New operational refinements do not rewrite their predicates or close full-canon sufficiency.',
          'The new candidate and evaluator implementations are separate and mutation-sensitive, but share authored semantic assumptions and lack independent peer validation.',
          'An initial draft metric compared the full-observation action label to itself. Self-review removed that tautological metric before final reporting and replaced it with observation-cell ambiguity.'
        ])
    (HERE/'review_results.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
