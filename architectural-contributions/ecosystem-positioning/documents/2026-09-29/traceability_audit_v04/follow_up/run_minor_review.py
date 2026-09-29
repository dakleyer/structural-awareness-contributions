"""Targeted type/shape regression checks and preservation of prior results."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import checked_evaluators as c

if not __debug__:
    raise SystemExit('Run without -O or PYTHONOPTIMIZE so acceptance assertions remain active.')

HERE=Path(__file__).resolve().parent

def main():
    tests=[
      ('boolean_report',c.root_separation,([],False,1)),
      ('float_report',c.root_separation,([],0.0,1)),
      ('none_event',c.history_violation,([None],[False])),
      ('empty_charge_row',c.charged_response,([()],1,[1],1)),
      ('unhashable_claim',c.qualified_support,((1,1,1),[[]])),
      ('none_evidence',c.qualified_support,(None,[0])),
      ('none_output',c.history_violation,('QA',None)),
      ('none_ledger',c.charged_response,([('respond',1)],1,None,1)),
      ('none_edges',c.root_separation,(None,0,1)),
      ('short_edge',c.root_separation,([(0,)],0,1)),
      ('duplicate_list_edges',c.root_separation,([[0,1],[0,1]],0,1)),
      ('boolean_graph_node',c.root_separation,([(False,1)],0,1))]
    rejected={}
    for name,fn,args in tests:
        try:fn(*args)
        except ValueError:rejected[name]=True
        else:raise AssertionError('Malformed input admitted: '+name)
    # Both Python tuple records and JSON-style list records denote the same DAG.
    list_edges=c.root_separation([[0,2],[1,3]],2,3)
    assert list_edges == c.root_separation([(0,2),(1,3)],2,3) == True
    target=HERE/'follow_up_results.json'
    previous=target.read_bytes()
    # -E ignores a inherited PYTHONOPTIMIZE environment setting for the child.
    subprocess.run([sys.executable,'-E',str(HERE/'run_follow_up.py')],check=True,stdout=subprocess.DEVNULL)
    assert target.read_bytes()==previous,'Previous admitted-domain results changed'
    result={'malformed_type_and_shape_controls':rejected,'new_controls':len(tests),
      'list_and_tuple_graph_records_agree':True,'prior_follow_up_result_bytes_unchanged':True,
      'prior_result_sha256':hashlib.sha256(previous).hexdigest(),
      'checked_evaluator_sha256':hashlib.sha256((HERE/'checked_evaluators.py').read_bytes()).hexdigest(),
      'scope':'Minor input-admission correction; no new hypothesis validation or change to documented results.'}
    (HERE/'minor_review_results.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
