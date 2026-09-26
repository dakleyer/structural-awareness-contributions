from pathlib import Path
import subprocess,json,sys,hashlib,time,concurrent.futures
HERE=Path(__file__).resolve().parent
root=next(p for p in HERE.parents if (p/'.github').exists() and (p/'research').exists())
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('--output',type=Path,required=True)
args=parser.parse_args()
out=args.output.resolve()
out.mkdir(parents=True,exist_ok=True)
base=root/'research/ecosystem-awareness/baseline'
fixtures=base/'fixtures'
jobs=[]
for folder in sorted(fixtures.iterdir()):
 if (folder.name.startswith('00K-A') or folder.name=='00K-cross-scenario-independent') and any(folder.glob('test*.py')):
  jobs.append((folder.name,folder,[sys.executable,'-m','pytest','-q']))
for folder in sorted((fixtures/'00K-HISTORICAL').iterdir()):
 if folder.is_dir(): jobs.append(('historical-'+folder.name,folder,[sys.executable,'-m','pytest','-q']))
for label,folder,script in [
 ('manifest','00K-SUITE','validate_manifest.py'),('formal','00K-FORMAL','formal_independence_certificate.py'),
 ('traceability','00K-TRACE','validate_traceability.py'),('closure','00K-CLOSURE','validate_closure.py'),
 ('extension','CASE-EXTENSION','validate_extensibility.py')]:
 jobs.append((label,fixtures/folder,[sys.executable,script]))
for label,folder,args in [
 ('full-cube','00K-FORMAL/full-cube',['-m','unittest','-v']),
 ('A23','00K-FORMAL/requirement-sufficiency',['-m','unittest','-v']),
 ('P5-blind','00K-FORMAL/p5-blind-signature',['-m','pytest','-q']),
 ('CTv1','RS-00E-Q1a',['-m','unittest','-v','test_canonical_trace_v1.py']),
 ('stage0','RS-00E-Q1a',['stage0_runner.py','--output',str(out/'stage0-replay')])]:
 jobs.append((label,fixtures/folder,[sys.executable,*args]))
lp=base/'00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1'
jobs.append(('00L',lp,[sys.executable,'verify_paired_symbolic.py','--trace-jsonl',str(out/'00L-replay.jsonl')]))
jobs.append(('doc-integrity',root,[sys.executable,'scripts/check_document_integrity.py']))
def run(job):
 label,cwd,cmd=job
 p=subprocess.run(cmd,cwd=cwd,capture_output=True,text=True,timeout=180)
 log=p.stdout+p.stderr
 (out/(label+'.txt')).write_text(log)
 return dict(label=label,working_directory=str(cwd.relative_to(root)),command=['python',*cmd[1:]],exit_code=p.returncode,output_sha256=hashlib.sha256(log.encode()).hexdigest(),output_tail=log[-450:])
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 results=list(pool.map(run,jobs))
stage_expected=fixtures/'RS-00E-Q1a/runs/stage0_v05_4193199'
stage_actual=out/'stage0-replay'
stage_same=all((stage_actual/f.name).exists() and f.read_bytes()==(stage_actual/f.name).read_bytes() for f in stage_expected.iterdir() if f.is_file())
inventory={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(base.rglob('*.py')) if 'AUDIT-20260926' not in p.parts}
report=dict(audited_commit='8f17843c568114f31cc0ad486b4a1303396021e6',python=sys.version,results=results,stage0_byte_replay_identical=stage_same,paired_byte_replay_identical=(out/'00L-replay.jsonl').read_bytes()==(lp/'00L_A11_TRAZAS_EJECUTADAS.jsonl').read_bytes(),python_source_inventory=inventory)
(out/'baseline_results.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='python_source_inventory'},indent=2))

# Historical ZIP reproduction is independent of the active corrected source.
from zipfile import ZipFile
import tempfile
zip_path=fixtures/'00K-A4-P4-00H-v0.2/00K_A4_executed_ablation_v0.2.zip'
with tempfile.TemporaryDirectory() as td:
    with ZipFile(zip_path) as archive:
        assert all(not Path(n).is_absolute() and '..' not in Path(n).parts for n in archive.namelist())
        archive.extractall(td)
    folder=next(Path(td).rglob('test_ablation_A4.py')).parent
    proc=subprocess.run([sys.executable,'-m','pytest','-q'],cwd=folder,capture_output=True,text=True)
    (out/'A4-archive.txt').write_text(proc.stdout+proc.stderr)
    report['archive_replay']={'archive_sha256':hashlib.sha256(zip_path.read_bytes()).hexdigest(),'exit_code':proc.returncode,'output':proc.stdout+proc.stderr}
(out/'baseline_results.json').write_text(json.dumps(report,indent=2)+'\n')
if any(r['exit_code'] for r in report['results']) or report['archive_replay']['exit_code']:
    raise SystemExit(1)

# A second support extraction/enumeration, independent of the auditor algorithm.
import itertools
sys.path.insert(0,str(fixtures/'00K-FORMAL/requirement-sufficiency'))
import requirement_sufficiency_model as model
rows=[]
for i,clauses in enumerate(model.BUNDLE_CLAUSES):
    functions=(model.P[i],*clauses)
    names=sorted(set().union(*(set(f.__code__.co_names)&set(model.State.__dataclass_fields__) for f in functions)))
    positive=bad=0
    for bits in itertools.product([False,True],repeat=len(names)):
        state=model.State(**dict(zip(names,bits)))
        if all(f(state) for f in clauses):
            positive+=1
            bad+=not model.P[i](state)
    rows.append({'principle':'P'+str(i+1),'support':names,'rows':2**len(names),'conforming':positive,'violations':bad})
report['independent_A23_support_enumeration']=rows
(out/'baseline_results.json').write_text(json.dumps(report,indent=2)+'\n')
