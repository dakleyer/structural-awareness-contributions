"""Round 47: exit status of the mathematical companion (PR #97, child of #93), and erratum to round 42.

Usage: python3 -B m28_07_exit_status_check.py <checkout of #93> <checkout of #97>

Copies each tree's math_audit_companion_2026-10-27.py and its frozen JSON to
a private temporary folder and runs them there (needs network access to
raw.githubusercontent.com for the four pinned blobs). Three situations:

  A. Normal run: exit 0 and stdout equal to the frozen reference, in both.
  B. Real failing check: inside the companion only (the pinned sources keep
     the real math module), math.isclose returns False, so the M27-12
     `require` fails. `require` raises AssertionError, so the
     process exits non-zero in BOTH trees, with no report on stdout. This
     is the case round 42 described wrongly (see round 47).
  C. Returned report inconsistent with its checks (only `passed` set to 31,
     the 32 checks still pass), as in the round 42 probe: #93 exits 0,
     #97 exits 1 and still prints the full injected report. With --output,
     #97 creates the file and exits 1.

Exit code 1 on a mismatch. Writes nothing outside its temporary folder.
"""
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

RUN = r'''
import sys, math, types, importlib.util as u
mode, out = sys.argv[1], sys.argv[2:]
s = u.spec_from_file_location("companion", "%s"); m = u.module_from_spec(s); s.loader.exec_module(m)
if mode == "fail":
    m.math = types.SimpleNamespace(**{k: getattr(math, k) for k in dir(math) if not k.startswith("_")})
    m.math.isclose = lambda *a, **k: False
elif mode == "summary":
    real = m.run_checks
    m.run_checks = lambda *a, **k: dict(real(*a, **k), passed=31)
sys.exit(m.main(out))
''' % SCRIPT


def run(folder, mode, *args, tmp):
    return subprocess.run([sys.executable, "-B", "-c", RUN, mode, *args], cwd=folder,
                          capture_output=True, text=True, env=dict(os.environ, TMPDIR=str(tmp)))


ok = True


def check(label, cond):
    global ok
    ok &= bool(cond)
    print(f"{'OK ' if cond else 'BAD'} {label}")


with tempfile.TemporaryDirectory() as work:
    work = Path(work)
    tmp = work / "tmp"
    tmp.mkdir()
    res = {}
    for tag, root in (("#93", sys.argv[1]), ("#97", sys.argv[2])):
        d = work / tag.strip("#")
        d.mkdir()
        for name in (SCRIPT, REF):
            shutil.copy2(Path(root) / REL / name, d / name)
        ref = json.loads((d / REF).read_text(encoding="utf-8"))
        a, b, c = run(d, "normal", tmp=tmp), run(d, "fail", tmp=tmp), run(d, "summary", tmp=tmp)
        out = work / f"out{tag.strip('#')}.json"
        c2 = run(d, "summary", "--output", str(out), tmp=tmp)
        res[tag] = dict(
            normal=(a.returncode, a.returncode == 0 and json.loads(a.stdout) == ref),
            fail=(b.returncode, "AssertionError: M27-12" in b.stderr, b.stdout.strip() == ""),
            summary=(c.returncode, c.returncode in (0, 1) and json.loads(c.stdout)["passed"] == 31
                     and json.loads(c.stdout)["checks"] == ref["checks"]),
            summary_output=(c2.returncode, out.exists()))
        print(f"{tag}: normal exit {a.returncode} | real failing check exit {b.returncode} "
              f"(AssertionError, no report) | summary-only 31/32 exit {c.returncode} | "
              f"same with --output exit {c2.returncode}, file created {out.exists()}")

    p, c = res["#93"], res["#97"]
    check("A: normal run exits 0 with the exact reference on both", p["normal"] == c["normal"] == (0, True))
    check("B: a real failing require exits non-zero on both, without a report",
          p["fail"][0] != 0 and c["fail"][0] != 0 and all(p["fail"][1:]) and all(c["fail"][1:]))
    check("C: summary-only inconsistency exits 0 on #93 and 1 on #97, report kept",
          p["summary"] == (0, True) and c["summary"] == (1, True))
    check("C: with --output, #97 writes the injected report and exits 1", c["summary_output"] == (1, True))

print("RESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
