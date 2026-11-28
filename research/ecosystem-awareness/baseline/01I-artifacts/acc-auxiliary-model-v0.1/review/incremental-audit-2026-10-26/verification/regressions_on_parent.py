"""Round 40: run each technical fix's new regression module on the fix and on its parent.

Usage: python3 -B regressions_on_parent.py <repository root with origin/pr86h ... fetched>

For each (parent, child, test module) pair, checks out both into temporary
worktrees, runs the child's test module in the child (must pass), copies it
into the parent and runs it there (must fail: it reproduces the defect).
Also probes pareto() and two_arm_order() of l08_robustness on #72 and #91
with NaN, "UNKNOWN" and the text pair "10"/"2". Cleans its worktrees up.
"""
import os
import shutil
import subprocess
import sys
import tempfile

root = os.path.abspath(sys.argv[1])
C = "research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/conscientia-campaign-v0.1"
PAIRS = [("0d2d77d7", "origin/pr86h", "test_l08_pareto_numeric", "#86"),
         ("origin/pr86h", "origin/pr87h", "test_l08_pareto_numeric", "#87"),
         ("0d2d77d7", "origin/pr88h", "test_l08_resource_conservation", "#88"),
         ("0d2d77d7", "origin/pr90h", "test_l08_executive_summary", "#90"),
         ("origin/pr87h", "origin/pr91h", "test_l08_pareto_numeric", "#91")]


def git(*args):
    subprocess.run(["git", "-C", root, *args], check=True, capture_output=True)


def unittest(path, module):
    r = subprocess.run([sys.executable, "-B", "-m", "unittest", module], cwd=path, capture_output=True, text=True)
    return r.returncode == 0, r.stderr.strip().splitlines()[-1]


tmp = tempfile.mkdtemp()
ok = True
try:
    for parent, child, module, label in PAIRS:
        wp, wc = os.path.join(tmp, "p"), os.path.join(tmp, "c")
        git("worktree", "add", "-q", "--detach", wp, parent)
        git("worktree", "add", "-q", "--detach", wc, child)
        try:
            c_ok, c_msg = unittest(os.path.join(wc, C), module)
            shutil.copy(os.path.join(wc, C, module + ".py"), os.path.join(wp, C))
            p_ok, p_msg = unittest(os.path.join(wp, C), module)
            print(f"{label} {module}: fix {c_msg} | parent {p_msg}")
            ok &= c_ok and not p_ok
        finally:
            git("worktree", "remove", "--force", wp)
            git("worktree", "remove", "--force", wc)
    probe = r"""
import l08_robustness as l
def t(f):
    try: return f()
    except Exception as e: return 'REJECTED ' + type(e).__name__
row = lambda e, m: {'invalid_proposals': e, 'missed_valid_opportunities': m}
print('   pareto NaN:', t(lambda: l.pareto({'a': (float('nan'), 1), 'b': (0, 0)}, axes=('x', 'y'))),
      '| pareto "10" vs "2":', t(lambda: l.pareto({'a': ('10', 0), 'b': ('2', 0)}, axes=('x', 'y'))))
print('   two_arm NaN:', t(lambda: l.two_arm_order(row(float('nan'), 1), row(0, 0))),
      '| UNKNOWN:', t(lambda: l.two_arm_order(row('UNKNOWN', 0), row(0, 0))),
      '| "10" vs "2":', t(lambda: l.two_arm_order(row('10', 0), row('2', 0))))
"""
    for ref, label in (("0d2d77d7", "#72"), ("origin/pr91h", "#91")):
        w = os.path.join(tmp, "x")
        git("worktree", "add", "-q", "--detach", w, ref)
        try:
            print(label)
            print(subprocess.run([sys.executable, "-B", "-c", probe], cwd=os.path.join(w, C),
                                 capture_output=True, text=True).stdout.rstrip())
        finally:
            git("worktree", "remove", "--force", w)
finally:
    shutil.rmtree(tmp, ignore_errors=True)
print("RESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
