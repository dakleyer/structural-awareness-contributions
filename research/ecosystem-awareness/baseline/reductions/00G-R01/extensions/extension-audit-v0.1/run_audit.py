"""Audit-successor replay, deliberately separate from frozen predecessor execution."""
import argparse,hashlib,json,sys,subprocess
from pathlib import Path
HERE=Path(__file__).resolve().parent
def validate_freeze():
 f=json.loads((HERE/'FREEZE.json').read_text(encoding='utf-8'))
 for rel,sha in f['files'].items():assert hashlib.sha256((HERE/rel).read_bytes()).hexdigest()==sha,rel
 return f
def run(output):
 validate_freeze();out=Path(output);out.mkdir(parents=True,exist_ok=False)
 # Each family has its own process; metering hooks cannot leak into another family.
 for name in ['cache-ttl','queues-ack-redelivery','structured-output','observability-response']:
  subprocess.run([sys.executable,'-B',str(HERE/'series2'/name/'current_study.py'),'--output',str(out/name)],check=True)
 subprocess.run([sys.executable,'-B',str(HERE/'run_metrics_audited.py'),'--output',str(out/'metrics')],check=True)
 subprocess.run([sys.executable,'-B',str(HERE/'verify_controls.py'),'--output',str(out/'controls')],check=True)
 result={'status':'PASS_SCOPED_EXTENSION_AUDIT_SUCCESSOR','predecessor_head':'f0edbbb840585b1991874c54aa8c8118c7210f5c','stage':'A','same_author_audit':True,'native_product_or_independent_validation':False,'first_cohort':{'operations':122,'separate_controls':18},'second_cohort':{'cases':40,'separate_controls':8},'audit_controls':json.loads((out/'controls/RESULTS.json').read_text(encoding='utf-8')),'source_card_sha256':hashlib.sha256((HERE/'RUN_CARD.json').read_bytes()).hexdigest(),'freeze_sha256':hashlib.sha256((HERE/'FREEZE.json').read_bytes()).hexdigest()}
 (out/'RESULTS.json').open('x',encoding='utf-8').write(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'status':result['status'],'cases':162,'separate_original_controls':26,'repair_control_vectors':result['audit_controls']['cases']}))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();run(a.output)
