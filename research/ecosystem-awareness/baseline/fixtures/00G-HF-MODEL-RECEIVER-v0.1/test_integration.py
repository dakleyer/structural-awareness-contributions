"""Offline harness tests with explicit mock responses; zero model/API execution."""
from copy import deepcopy
import json
from pathlib import Path
import sys
import unittest
from adapter import Client, AccessError
from runner import SCENARIO, Journal, episode, audit, valid_arguments

CASES=json.loads((SCENARIO/'CASES.json').read_text())


def arguments(action,frame=None,total=None,receipts=None,signal_id=None):
    return dict(action=action,frame=frame,total=total,receipts=receipts or [],signal_id=signal_id)


class MockClient:
    def __init__(self,steps):
        self.steps=iter(steps)
        self.calls=[]

    def respond(self,items,previous=None):
        self.calls.append(deepcopy((items,previous)))
        step=next(self.steps)
        if isinstance(step,Exception): raise step
        if isinstance(step,dict) and 'status' in step: return step
        index=len(self.calls)
        return dict(id='mock-'+str(index),model='OFFLINE_TEST_DOUBLE',status='completed',
                    usage=dict(total_tokens=10),output=[dict(type='function_call',name='step',
                    call_id='call-'+str(index),arguments=json.dumps(step))])


class Integration(unittest.TestCase):
    def exercise(self,case,arm,steps,limits=None):
        world=next(w for w in CASES if w['id']==case)
        client=MockClient(steps)
        journal=Journal()
        result=episode(world,arm,client,journal,limits)
        audit(world,journal.rows,result)
        return result,journal.rows,client

    def test_native_wrong_mission_is_an_effect_failure(self):
        result,_,_=self.exercise('F-direct','native',[arguments('read','FRAME_B'),arguments('deliver','FRAME_B',33)])
        self.assertTrue(result['outcome']['unauthorized_mission_change'])

    def test_model_can_resolve_without_EA(self):
        steps=[arguments('resolve',receipts=['receipt-N','receipt-R1','receipt-R2']),
               arguments('read','FRAME_A'),arguments('deliver','FRAME_A',11)]
        result,_,client=self.exercise('F-direct','native',steps)
        self.assertTrue(result['outcome']['operational_pass'])
        self.assertEqual(client.calls[1][1],'mock-1')
        self.assertEqual(client.calls[1][0][0]['call_id'],'call-1')

    def test_EA_does_not_force_repair(self):
        result,rows,_=self.exercise('F-direct','ea',[arguments('read','FRAME_B'),arguments('deliver','FRAME_B',33)])
        self.assertTrue(result['outcome']['unauthorized_mission_change'])
        self.assertTrue(any(r['kind']=='advisory_received' for r in rows))

    def test_EA_can_be_followed(self):
        result,_,_=self.exercise('F-direct','ea',[arguments('read','FRAME_A'),arguments('deliver','FRAME_A',11)])
        self.assertTrue(result['outcome']['operational_pass'])

    def test_genuine_transition(self):
        result,_,_=self.exercise('G-direct','ea',[arguments('read','FRAME_B'),arguments('deliver','FRAME_B',33)])
        self.assertTrue(result['outcome']['operational_pass'])

    def test_raw_and_EA_same_acquisition_and_logical_overhead(self):
        _,a,ca=self.exercise('F-direct','raw',[arguments('stop')])
        _,b,cb=self.exercise('F-direct','ea',[arguments('stop')])
        charges=lambda rows:[r['data'] for r in rows if r['kind']=='charge']
        self.assertEqual(charges(a),charges(b))
        left=json.loads(ca.calls[0][0][0]['content'])
        right=json.loads(cb.calls[0][0][0]['content'])
        self.assertEqual(left['advisory']['current_evidence'],right['advisory']['current_evidence'])
        self.assertNotIn('assessment',left['advisory'])
        self.assertIn('assessment',right['advisory'])

    def test_no_outcome_truth_leaks_to_native(self):
        _,_,a=self.exercise('F-direct','native',[arguments('stop')])
        _,_,b=self.exercise('G-direct','native',[arguments('stop')])
        self.assertEqual(a.calls,b.calls)

    def test_infrastructure_error_is_not_operational_episode(self):
        result,_,_=self.exercise('F-direct','native',[AccessError('http_status_503')])
        self.assertFalse(result['operational_result_eligible'])
        self.assertEqual(result['model_responses'],0)

    def test_incomplete_response_never_dispatches(self):
        result,rows,_=self.exercise('F-direct','native',[dict(status='incomplete',output=[])])
        self.assertTrue(result['infrastructure_interrupted'])
        self.assertFalse(any(r['kind']=='model_action' for r in rows))

    def test_invalid_arguments_and_forged_signal_acknowledgment(self):
        self.assertFalse(valid_arguments(arguments('deliver','FRAME_B',True),None))
        self.assertFalse(valid_arguments(arguments('stop',signal_id='unreceived'),None))
        self.assertTrue(valid_arguments(arguments('stop',signal_id='received'),'received'))
        result,_,_=self.exercise('F-direct','native',[arguments('stop',signal_id='unreceived'),arguments('stop')])
        self.assertEqual(result['reason'],'model_stop')

    def test_short_deadline_cannot_deliver_after_expiry(self):
        result,_,_=self.exercise('D-G','ea',[arguments('read','FRAME_B'),arguments('deliver','FRAME_B',33)])
        self.assertFalse(result['outcome']['operational_pass'])
        self.assertEqual(result['reason'],'logical_deadline')

    def test_token_overshoot_prevents_dispatch(self):
        from runner import LIMITS
        result,rows,_=self.exercise('F-direct','native',[arguments('deliver','FRAME_B',33)],{**LIMITS,'charged_token_stop':5})
        self.assertEqual(result['reason'],'token_threshold_exceeded_before_dispatch')
        self.assertFalse(any(r['kind']=='model_action' for r in rows))

    def test_adapter_carries_context_and_resends_instructions(self):
        client=Client('EXPLICIT_MODEL','test-placeholder','stable instructions')
        body=client.body([dict(type='function_call_output',call_id='c1',output='{}')],'prior-response')
        self.assertEqual(body['previous_response_id'],'prior-response')
        self.assertEqual(body['instructions'],'stable instructions')
        self.assertFalse(body['parallel_tool_calls'])
        self.assertNotIn('test-placeholder',json.dumps(body))

    def test_private_reasoning_is_not_published(self):
        response=dict(id='mock-1',model='OFFLINE_TEST_DOUBLE',status='completed',usage=dict(total_tokens=10),
                      output=[dict(type='reasoning',summary=['PRIVATE_TEST_MARKER']),
                              dict(type='function_call',name='step',call_id='c1',arguments=json.dumps(arguments('stop')))])
        _,rows,_=self.exercise('F-direct','native',[response])
        self.assertNotIn('PRIVATE_TEST_MARKER',json.dumps(rows))

    def test_effect_tampering_is_detected(self):
        from runner import digest
        result,rows,_=self.exercise('F-direct','native',[arguments('read','FRAME_B'),arguments('deliver','FRAME_B',33)])
        for row in rows:
            if row['kind']=='model_action' and row['data']['arguments']['action']=='deliver':
                row['data']['arguments']['frame']='FRAME_A'
        head='0'*64
        for row in rows:
            row['previous']=head
            row['hash']=digest({k:v for k,v in row.items() if k!='hash'})
            head=row['hash']
        result['journal_head']=head
        with self.assertRaises(AssertionError):
            audit(next(w for w in CASES if w['id']=='F-direct'),rows,result)

    def test_offline_results_cannot_open_model_repair_gate(self):
        from tempfile import TemporaryDirectory
        from run_model import native_witness
        from runner import write, digest
        with TemporaryDirectory() as directory:
            p=Path(directory)
            write(p/'REGISTRATION.json',dict(requested_model='X',phase='native',
                  decision_source='OFFLINE_TEST_DOUBLE',freeze_sha256=digest({})))
            write(p/'REPORT.json',dict(results=[]))
            with self.assertRaises(AssertionError):
                native_witness(p,'X',{},CASES)

    def test_journal_is_persisted_at_each_event(self):
        from tempfile import TemporaryDirectory
        from runner import DurableJournal
        with TemporaryDirectory() as directory:
            p=Path(directory)/'JOURNAL.jsonl'
            journal=DurableJournal(p)
            journal.add('event',0,dict(state='recorded'))
            self.assertEqual(json.loads(p.read_text()),journal.rows[0])
            with self.assertRaises(FileExistsError):
                DurableJournal(p)


if __name__=='__main__':
    unittest.main(verbosity=2)
