"""Replay the correction checks, original campaign and affected integrity gates.

The output identifies actual source hashes. It never attributes local execution
to GitHub Actions, and keeps the historical 379 separate from new regressions.
"""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import sys
import xml.etree.ElementTree as ET

HERE = Path(__file__).resolve().parent
FIX = HERE.parent
BASE = FIX.parent
ROOT = next(p for p in HERE.parents if (p / '.github').exists() and (p / 'research').exists())
PAIRS = BASE / '00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1'

def main(output):
    output = output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    jobs = [
        ('correction-regressions', ROOT, ['-m', 'pytest', '-q', str(HERE), '--junitxml=' + str(output / 'regressions.xml')]),
        ('original-379', FIX / '00K-SUITE', ['run_all.py']),
        ('manifest', FIX / '00K-SUITE', ['validate_manifest.py']),
        ('traceability', FIX / '00K-TRACE', ['validate_traceability.py']),
        ('closure', FIX / '00K-CLOSURE', ['validate_closure.py']),
        ('p5-blind', FIX / '00K-FORMAL/p5-blind-signature', ['-m', 'pytest', '-q']),
        ('ctv1', FIX / 'RS-00E-Q1a', ['-m', 'unittest', '-v', 'test_canonical_trace_v1.py']),
        ('stage0', FIX / 'RS-00E-Q1a', ['stage0_runner.py', '--output', str(output / 'stage0')]),
        ('pairs', PAIRS, ['verify_paired_symbolic.py', '--trace-jsonl', str(output / 'pairs.jsonl')]),
        ('documentation', ROOT, ['scripts/check_document_integrity.py']),
    ]
    results = []
    for label, cwd, args in jobs:
        proc = subprocess.run([sys.executable, *args], cwd=cwd, text=True, capture_output=True)
        log = proc.stdout + proc.stderr
        (output / (label + '.txt')).write_text(log)
        entry = dict(label=label, cwd=str(cwd.relative_to(ROOT)),
                     command=['python', *[a.replace(str(ROOT), '$REPO').replace(str(output), '$OUTPUT') for a in args]],
                     exit_code=proc.returncode, log_sha256=hashlib.sha256(log.encode()).hexdigest(),
                     output_tail=log[-500:])
        results.append(entry)
        print(label, proc.returncode, flush=True)
    xml = ET.parse(output / 'regressions.xml')
    cases = [dict(name=t.attrib['name'], passed=t.find('failure') is None and t.find('error') is None)
             for t in xml.iter('testcase')]
    reference = FIX / 'RS-00E-Q1a/runs/stage0_audit_corrections_v1'
    stage_same = {p.name: (output / 'stage0' / p.name).exists() and p.read_bytes() == (output / 'stage0' / p.name).read_bytes()
                  for p in sorted(reference.glob('*.json'))}
    pairs_same = (output / 'pairs.jsonl').read_bytes() == (PAIRS / '00L_A14_TRAZAS_CORREGIDAS.jsonl').read_bytes()
    source_files = sorted(BASE.rglob('*.py')) + sorted((ROOT / '.github/workflows').glob('*.yml'))
    report = dict(correction_base_commit='28b7666d8db26634a0f92458146b86f6b25c304f',
                  execution='local; source identity given by hashes, not remote CI', python=sys.version,
                  results=results, correction_tests=cases, correction_pass_count=sum(c['passed'] for c in cases),
                  stage0_reference_byte_matches=stage_same, paired_reference_byte_match=pairs_same,
                  source_sha256={str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in source_files})
    (output / 'results.json').write_text(json.dumps(report, indent=2) + '\n')
    if any(r['exit_code'] for r in results) or not all(stage_same.values()) or not pairs_same:
        raise SystemExit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    main(parser.parse_args().output)
