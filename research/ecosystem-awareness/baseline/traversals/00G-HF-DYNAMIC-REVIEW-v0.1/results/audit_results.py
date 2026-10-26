"""Post-run audit; no mutation of the frozen simulator or its results."""
from pathlib import Path
import argparse, collections, hashlib, json, lzma, sys

parser=argparse.ArgumentParser()
parser.add_argument('results',type=Path)
parser.add_argument('--package',type=Path,required=True)
args=parser.parse_args(); out=args.results; package=args.package
sys.path.insert(0,str(package));import run
run.check_freeze()
cfg=json.loads((package/'CONFIG.json').read_text())
report=json.loads((out/'SUMMARY.json').read_text())
assert hashlib.sha256((out/'episodes.jsonl.xz').read_bytes()).hexdigest()==report['episodes_sha256']
rows={(r['profile'],r['seed'],r['condition']):r for r in report['all_results']}
seen=set();groups={}; cases=[]; selections=[]; summaries={}; passed=collections.Counter()
with lzma.open(out/'episodes.jsonl.xz','rt') as stream:
 for line in stream:
  ep=json.loads(line);key=(ep['profile'],ep['seed'],ep['condition']);assert key not in seen;seen.add(key)
  assert ep['summary']=={k:v for k,v in rows[key].items() if k not in ('profile','seed','condition')}
  summaries[key]=ep['summary']
  msg={m['id']:m for m in ep['messages']};delivery={}
  for tx in ep['transmissions']:
   assert msg[tx['message']]['at']<=tx['at']
   delivery.setdefault((tx['receiver'],tx['message']),tx['at'])
  for m in msg.values():
   for parent in m['parents']:
    assert parent in msg and msg[parent]['at']<m['at']
    assert delivery[(m['sender'],parent)]<m['at']
  passed['network_message_chronology']+=1
  for d in ep['decisions']:
   v=d['view'];assert all(delivery[(d['agent'],mid)]<=d['step']*cfg['tick'] for mid in v['messages'])
   assert v['step']==d['step'];snap=v['snapshot']
   if snap:assert snap['observed_step']<=d['step']
   if d['decision']['choice']=='ACT_T1' and v['guard']:
    assert run.usable(snap,v) and snap['allowed'] and snap['applicable']
   passed['decision_views_checked']+=1
  for state in ep['epoch_states']:
   for s in state.values():
    assert s['queries']<=cfg['budget_per_agent_per_epoch']['queries']
    assert s['publications']<=cfg['budget_per_agent_per_epoch']['messages']
    assert s['attempts']<=cfg['budget_per_agent_per_epoch']['alternative_attempts']
  passed['network_budgets_checked']+=1
  totals=collections.Counter()
  for r in ep['records']:
   assert run.c3_core().evaluate(r['world'],r['trace'])==r['result']
   assert r['result']['record_status']=='COMPLETE'
   passed['C3_recomputed_records']+=1
   for k,v in r['result'].items():
    if type(v) is bool:totals[k]+=v
   es=[e for e in ep['effects'] if e['agent']==r['agent'] and e['epoch']==r['epoch']]
   assert r['result']['unauthorized_effect']==any(e['after'] is not None and not e['permission'] for e in es)
   assert r['result']['inadmissible_effect']==any(e['after'] is not None and not(e['permission'] and e['applicability']) for e in es)
  for k,v in ep['summary'].items():
   if k in totals:assert v==totals[k]
  passed['effect_recorder_agreement_networks']+=1
  for groupkey in [ep['condition'],ep['profile']+'/'+ep['condition']]:
   g=groups.setdefault(groupkey,{'networks':0,'C3_records':0,'networks_with_HF_witness':0,'totals':collections.Counter()})
   g['networks']+=1;g['C3_records']+=len(ep['records']);g['networks_with_HF_witness']+=bool(ep['summary']['hf_operational_witness'])
   g['totals'].update({k:v for k,v in ep['summary'].items() if type(v) is int})
  if report['selected'] and ep['profile']==report['selected']['profile'] and ep['seed']==report['selected']['seed']:
   cases.append(ep)
expected={(p['id'],s,c['id']) for p in cfg['profiles'] for s in cfg['seeds'] for c in cfg['conditions']}
assert seen==expected and len(seen)==report['networks']==cfg['search']['network_count']
for p in cfg['profiles']:
 for seed in cfg['seeds']:
  stable=summaries[(p['id'],seed,'R2')];dynamic=summaries[(p['id'],seed,'R3')];without=summaries[(p['id'],seed,'R3_NO_RELAY')]
  eligible=(stable['inadmissible_attempt']==0 and stable['inadmissible_effect']==0 and dynamic['hf_operational_witness']>=2 and dynamic['hf_operational_witness']-without['hf_operational_witness']>=1 and len(dynamic['late_dependent_witnesses'])>0)
  if eligible:selections.append({'profile':p['id'],'seed':seed})
assert (selections[0] if selections else None)==({k:report['selected'][k] for k in ['profile','seed']} if report['selected'] else None)
# Diagnostic extraction, does not redefine the frozen selection.
witnesses=[]
for ep in cases:
 if ep['condition']!='R3':continue
 for r in ep['records']:
  if not r['result']['hf_operational_witness']:continue
  d=next(d for d in ep['decisions'] if d['agent']==r['agent'] and d['epoch']==r['epoch'] and d['decision']['choice']=='ACT_T1')
  witnesses.append({'agent':r['agent'],'epoch':r['epoch'],'step':d['step'],'decision':d['decision'],'snapshot':d['view']['snapshot'],'known_version':d['view']['known_version'],'route':d['view']['route'],'basis':d['view']['messages'],'result':r['result'],'effect':[e for e in ep['effects'] if e['agent']==r['agent'] and e['epoch']==r['epoch']]})
result={'status':'PASS','freeze_commit':'3ce9d2b54a0794919578704ccd26adafa8ea5151','networks':len(seen),'checks':dict(passed),'eligible_pairs':len(selections),'first_eligible_pair':selections[0] if selections else None,'selected_witness_records':witnesses,'aggregate_results':groups,'frozen_files_unchanged':True,'ea_execution':'NOT_RUN','model_calls':0}
(out/'AUDIT.json').write_text(json.dumps(result,indent=2)+'\n')
if cases:
 with lzma.open(out/'SELECTED_NETWORKS.json.xz','wt') as f:json.dump(cases,f,sort_keys=True,separators=(',',':'))
print(json.dumps({k:result[k] for k in ['status','networks','checks','eligible_pairs','first_eligible_pair']}))
