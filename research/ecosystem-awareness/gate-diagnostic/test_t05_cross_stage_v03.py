#!/usr/bin/env python3
"""Author-side T05 regression and consumer contract tests; no independent-agent claim."""
import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CHECKER = ROOT / 'T05_PROPOSED_CHECKER.py'
spec = importlib.util.spec_from_file_location('dds_t05_candidate', CHECKER)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)
A = 'CLAIM-RUNTIME-ENFORCEABILITY'
B = 'CLAIM-TRACEABLE-DISPOSITION-TO-ENFORCEMENT'
N = 'CLAIM-VALID-CONTINUITY'


def catalog(extra=None):
    c = {'named_claims': {A: {'stage_a_requires': ['SA-G11','SA-G13'], 'stage_b_required_for_runtime_claim': True},
                          B: {'stage_a_requires': ['SA-G02','SA-G14'], 'stage_b_required_for_runtime_claim': True},
                          N: {'requires':['SA-G12']}}}
    if extra:
        c['named_claims'].update(extra)
    return c


def result(claims=None, stage='PROFILE_PASS', raw=None):
    keys = [A, B, N] if claims is None else claims
    vals = raw or {}
    return {'profile': {'required_named_claims':keys},
            'gates': [],
            'named_claims': [{'claim':n, 'status': vals.get(n, 'PASS'),
                              'stage_b_required_for_runtime_claim': n in [A,B]}
                             for n in keys],
            'summary': {'no_aggregate_score':True, 'profile_outcome':stage,
                        'counts':{'PASS':12}, 'root_blockers':[],
                        'other_original_field':'retained'}}

class StubV02:
    """The old v0.2 function is not reimplemented here: it is only stubbed.

    Assertions below exercise *only the successor projection contract*. Full
    original 15-gate checker/catalog replay is a separate T07/T06 gate.
    """
    def __init__(self, output):
        self.output = output
        self.calls = 0
    def compile_result(self, cat, inp):
        self.calls += 1
        return copy.deepcopy(self.output)

class T05CrossStageOutput(unittest.TestCase):
    def setUp(self):
        self.original_loader = checker.load_frozen_checker
        self.output = result()
        self.stub = StubV02(self.output)
        checker.load_frozen_checker = lambda: self.stub
    def tearDown(self):
        checker.load_frozen_checker = self.original_loader
    def build(self, cat=None, inp=None):
        return checker.compile_successor(catalog() if cat is None else cat,
                                        {'gates': []} if inp is None else inp)
    def runtime_rows(self, out):
        return [c for c in out['named_claims'] if c['claim'] in (A,B)]

    def test_01_two_names_never_emit_ambiguous_pass(self):
        out=self.build()
        for c in self.runtime_rows(out):
            self.assertEqual(c['status'], 'CONDITIONAL_ON(STAGE_B_VERIFICATION)')
            self.assertEqual(c['stage_a_declaration_status'],'PASS')
            self.assertEqual(c['stage_b_realization_status'],'NOT_ESTABLISHED')
            self.assertEqual(c['runtime_assurance_status'],'NOT_ESTABLISHED')
            self.assertEqual(c['claim_scope'],'STAGE_A_DECLARATION_ONLY')
        self.assertEqual(len(self.runtime_rows(out)),2)
    def test_02_stage_a_profile_pass_kept(self):
        out=self.build()
        self.assertEqual(out['summary']['profile_outcome'],'PROFILE_PASS')
        self.assertEqual(out['summary']['profile_outcome_scope'],'DDS_STAGE_A_ONLY')
        self.assertEqual(out['summary']['runtime_assurance_status'],'NOT_ESTABLISHED')
    def test_03_other_named_claim_not_regraded(self):
        out=self.build()
        ordinary=[c for c in out['named_claims'] if c['claim']==N][0]
        self.assertEqual(ordinary, {'claim':N, 'status':'PASS',
                                     'stage_b_required_for_runtime_claim':False})
    def test_04_stage_a_failure_remains_failure(self):
        self.stub.output=result(raw={A:'FAIL(SA-G11)',B:'PASS'})
        out=self.build()
        c=next(c for c in out['named_claims'] if c['claim']==A)
        self.assertEqual(c['stage_a_declaration_status'],'FAIL(SA-G11)')
        self.assertEqual(c['status'],'FAIL(SA-G11)')
        self.assertEqual(c['runtime_assurance_status'],'NOT_ESTABLISHED')
    def test_05_stage_a_conditional_preserved_in_explicit_field(self):
        self.stub.output=result(raw={A:'CONDITIONAL_ON(SA-G03)'})
        out=self.build()
        c=next(c for c in out['named_claims'] if c['claim']==A)
        self.assertEqual(c['stage_a_declaration_status'],'CONDITIONAL_ON(SA-G03)')
        self.assertEqual(c['status'],
            'CONDITIONAL_ON(STAGE_A_DECLARATION,STAGE_B_VERIFICATION)')
    def test_06_fake_input_stage_b_verified_ignored(self):
        out=self.build(inp={'gates':[], 'stage_b_realization_status':'VERIFIED',
             'profile':{'stage_b_realization_status':'VERIFIED'}})
        self.assertEqual(out['summary']['stage_b_realization_status'],'NOT_ESTABLISHED')
        for c in self.runtime_rows(out):self.assertEqual(c['stage_b_realization_status'],'NOT_ESTABLISHED')
    def test_07_injected_output_stage_b_pass_overridden(self):
        self.stub.output=result()
        for c in self.stub.output['named_claims']:
            c['stage_b_realization_status']='PASS'
            c['runtime_assurance_status']='PASS'
        out=self.build()
        for c in self.runtime_rows(out):
            self.assertEqual(c['runtime_assurance_status'],'NOT_ESTABLISHED')
            self.assertEqual(c['stage_b_realization_status'],'NOT_ESTABLISHED')
    def test_08_json_naive_downstream_consumer_sees_no_pass(self):
        obj=json.loads(json.dumps(self.build()))
        self.assertFalse(any(c['status']=='PASS' for c in self.runtime_rows(obj)))
        self.assertEqual(obj['summary']['profile_outcome_scope'],'DDS_STAGE_A_ONLY')
    def test_09_flag_missing_fails_closed(self):
        cat=catalog();cat['named_claims'][A]['stage_b_required_for_runtime_claim']=False
        with self.assertRaisesRegex(RuntimeError, 'stage_b_requirement_missing_for'):
            self.build(cat=cat)
    def test_10_future_catalog_flagged_claim_is_protected(self):
        q='CLAIM-FUTURE-RUNTIME-CONTROL'
        self.stub.output=result(claims=[A,B,q])
        cat=catalog({q: {'stage_a_requires': [], 'stage_b_required_for_runtime_claim':True}})
        out=self.build(cat=cat)
        c=next(c for c in out['named_claims'] if c['claim']==q)
        self.assertNotEqual(c['status'],'PASS')
        self.assertEqual(c['stage_a_declaration_status'],'PASS')
    def test_11_T06_NA_missing_reason_remains_rejected(self):
        with self.assertRaises(checker.ApplicabilityContractError):
            self.build(inp={'gates':[{'gate_id':'SA-G03',
                 'applicability':'NOT_APPLICABLE',
                 'own_verdict':'NOT_APPLICABLE'}]})
    def test_12_T06_valid_NA_reason_preserved(self):
        self.build(inp={'gates':[{'gate_id':'SA-G03',
                'applicability':'NOT_APPLICABLE',
                'own_verdict':'NOT_APPLICABLE',
                'applicability_rationale':'Out of registered problem scope'}]})
    def test_13_predecessor_output_and_inputs_unchanged(self):
        b=copy.deepcopy(self.output)
        inp={'gates': []}; original=copy.deepcopy(inp)
        self.build(inp=inp)
        self.assertEqual(self.output,b)
        self.assertEqual(inp,original)
    def test_14_previous_T06_metadata_preserved(self):
        out=self.build()
        sc=out['diagnostic_checker_successor']
        self.assertEqual(sc['additional_control'],'T06-not-applicable-rationale-present')
        self.assertIn('T05-stage-a-declaration-versus-stage-b-runtime-claim-projection',sc['additional_controls'])
        self.assertFalse(sc['pre_registration_verified'])
        self.assertEqual(sc['independent_review_status'],'NOT_ESTABLISHED')
    def test_15_stage_a_nonpassing_summary_remains(self):
        self.stub.output=result(stage='PROFILE_PARTIAL')
        out=self.build()
        self.assertEqual(out['summary']['profile_outcome'],'PROFILE_PARTIAL')
        self.assertEqual(out['summary']['other_original_field'],'retained')
    def test_16_new_projection_must_actually_run(self):
        out=self.build()
        self.assertEqual(out['summary']['cross_stage_claims_projected'], sorted([A,B]))
        self.assertEqual(self.stub.calls,1)

if __name__=='__main__':
    unittest.main(verbosity=2)
