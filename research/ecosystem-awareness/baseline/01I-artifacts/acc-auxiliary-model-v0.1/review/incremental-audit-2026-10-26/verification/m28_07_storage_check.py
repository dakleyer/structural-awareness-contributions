"""Round 42: M28-07, storage hygiene of the mathematical companion (PR #93).

Usage: python3 -B m28_07_storage_check.py <checkout of #58 parent> <checkout of #93>

Copies each tree's math_audit_companion_2026-10-27.py and its frozen
MATH_AUDIT_RESULTS_2026-10-27.json to a private temporary folder and runs
them there, so neither checkout is touched. Needs network access to
raw.githubusercontent.com (four pinned public blobs).

Parent, default run: expected to rewrite the frozen JSON (same parsed
content, different bytes) and leave a source cache with bytecode next to it.

#93:
  1. default run: full JSON on stdout equal to the frozen reference; the
     reference keeps its exact bytes; no new file next to the script; no
     leftover temporary folder.
  2. --output on an existing file: refused, file unchanged.
  3. --output on a new path: file created, equal to the reference.
  4. --source-archive (the parent's cache): same result, archive unchanged,
     no bytecode written into it.
  5. --source-archive on an empty folder: fails, creates nothing.
  6. informative: a returned report whose summary says 31/32 while all 32
     checks still pass exits 0 on #93 (1 on #97). This is NOT a real failing
     check: a failing `require` raises and exits non-zero on every version.
     Round 42 described it wrongly; see round 47 and m28_07_exit_status_check.py.

Exit code 1 on a mismatch in 1-5.
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REL = Path("research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/"
           "review/incremental-audit-2026-10-26")
SCRIPT, REF = "math_audit_companion_2026-10-27.py", "MATH_AUDIT_RESULTS_2026-10-27.json"


def stage(root, dest):
    dest.mkdir()
    for name in (SCRIPT, REF):
        shutil.copy2(Path(root) / REL / name, dest / name)
    return dest


def tree(path):
    return {str(p.relative_to(path)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(Path(path).rglob("*")) if p.is_file()}


def run(folder, *args, tmp):
    env = dict(os.environ, TMPDIR=str(tmp))
    return subprocess.run([sys.executable, SCRIPT, *args], cwd=folder, env=env,
                          capture_output=True, text=True)


ok = True


def check(label, cond):
    global ok
    ok &= bool(cond)
    print(f"{'OK ' if cond else 'BAD'} {label}")


with tempfile.TemporaryDirectory() as work:
    work = Path(work)
    tmp = work / "tmp"
    tmp.mkdir()

    # Parent: reproduce the defect.
    p = stage(sys.argv[1], work / "parent")
    ref_bytes = (p / REF).read_bytes()
    ref = json.loads(ref_bytes)
    r = run(p, tmp=tmp)
    after = (p / REF).read_bytes()
    cache = p / ".pinned-math-audit-sources"
    pyc = len(list(cache.rglob("*.pyc"))) if cache.exists() else 0
    print(f"parent default: exit {r.returncode}; frozen JSON bytes changed: {after != ref_bytes}; "
          f"parsed equal: {json.loads(after) == ref}; cache left: {cache.exists()} ({pyc} .pyc)")
    check("parent reproduces M28-07 (reference rewritten, cache left)", after != ref_bytes and cache.exists())
    archive = work / "archive"
    shutil.copytree(cache, archive, ignore=shutil.ignore_patterns("__pycache__"))

    # Child.
    c = stage(sys.argv[2], work / "child")
    before = tree(c)
    r = run(c, tmp=tmp)
    out = json.loads(r.stdout) if r.returncode == 0 else None
    check(f"#93 default: exit 0, stdout equals reference ({out and out['passed']}/{out and out['total']})",
          r.returncode == 0 and out == ref)
    check("#93 default: reference bytes and folder unchanged", tree(c) == before)
    check("#93 default: no temporary folder left", not any(tmp.iterdir()))

    existing = work / "existing.json"
    existing.write_text("keep me\n", encoding="utf-8")
    r = run(c, "--output", str(existing), tmp=tmp)
    check("#93 --output existing: refused, file unchanged",
          r.returncode != 0 and existing.read_text(encoding="utf-8") == "keep me\n")

    new = work / "new.json"
    r = run(c, "--output", str(new), tmp=tmp)
    check("#93 --output new: created and equal to reference",
          r.returncode == 0 and new.exists() and json.loads(new.read_text(encoding="utf-8")) == ref)

    arch_before = tree(archive)
    r = run(c, "--source-archive", str(archive), tmp=tmp)
    check("#93 --source-archive: same result, archive unchanged, no bytecode",
          r.returncode == 0 and json.loads(r.stdout) == ref and tree(archive) == arch_before)

    empty = work / "empty"
    empty.mkdir()
    r = run(c, "--source-archive", str(empty), tmp=tmp)
    check("#93 --source-archive empty: fails and creates nothing",
          r.returncode != 0 and not any(empty.iterdir()) and tree(c) == before)

    probe = ("import sys; import importlib.util as u; "
             "s=u.spec_from_file_location('m', %r); m=u.module_from_spec(s); "
             "s.loader.exec_module(m); real=m.run_checks; "
             "m.run_checks=lambda *a, **k: dict(real(*a, **k), passed=31); "
             "sys.exit(m.main([]))") % str(c / SCRIPT)
    r = subprocess.run([sys.executable, "-B", "-c", probe], cwd=c, capture_output=True, text=True,
                       env=dict(os.environ, TMPDIR=str(tmp)))
    print(f"INFO summary-only inconsistency (passed=31, all 32 checks pass): exit code {r.returncode} "
          "(a real failing check raises and exits non-zero; see round 47)")

print("RESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
