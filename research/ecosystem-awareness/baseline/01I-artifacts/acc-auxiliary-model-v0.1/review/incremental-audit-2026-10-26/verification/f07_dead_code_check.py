"""Round 50: F-07 (unused `loc` in the `nonmonotone` branch of #54's campaign.py), PR #99.

Usage: python3 -B f07_dead_code_check.py <checkout of #54> <checkout of #99>

1. AST: in #54, `loc` is assigned once and never read; in #99 the name is gone.
   The rest of `result` is identical after removing that one statement.
2. Behaviour: runs `result` on every nonmonotone table with values from
   {0, 1, 2}, lengths 1-7 and every valid start (21,324 cases), plus 5,000
   random tables of floats with NaN/inf mixed in, in both trees (separate
   subprocesses), and compares the result dictionaries (or exception types).
3. Full campaign: the CLI/report of both trees, compared byte for byte.

Exit code 1 on a mismatch. Writes nothing.
"""
import ast
import json
import os
import subprocess
import sys

STUDY = ("research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/"
         "studies/conscientia-additional-cases-v0.1")


def result_fn(root):
    tree = ast.parse(open(os.path.join(root, STUDY, "campaign.py"), encoding="utf-8").read())
    return next(n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == "result")


def names(fn, ctx):
    return [n for n in ast.walk(fn) if isinstance(n, ast.Name) and n.id == "loc" and isinstance(n.ctx, ctx)]


class DropLoc(ast.NodeTransformer):
    def visit_Assign(self, node):
        if any(isinstance(t, ast.Name) and t.id == "loc" for t in node.targets):
            return None
        return node


p_fn, c_fn = result_fn(sys.argv[1]), result_fn(sys.argv[2])
ok = True
p_store, p_load, c_any = len(names(p_fn, ast.Store)), len(names(p_fn, ast.Load)), len(names(c_fn, ast.AST))
same_rest = ast.dump(DropLoc().visit(p_fn)) == ast.dump(c_fn)
print(f"#54: loc assigned {p_store}x, read {p_load}x | #99: loc nodes {c_any} | rest of result() identical: {same_rest}")
ok &= p_store == 1 and p_load == 0 and c_any == 0 and same_rest

PROBE = r'''
import json, random, itertools, math
import campaign as c
out = []
def run(vals, start):
    try:
        r = c.result({"id": "probe", "type": "nonmonotone", "table": vals, "start": start})
        return json.dumps(r, sort_keys=True, default=str)
    except Exception as e:
        return type(e).__name__
for L in range(1, 8):
    for vals in itertools.product((0, 1, 2), repeat=L):
        for s in range(L):
            out.append(run(list(vals), s))
rng = random.Random(20261121)
pool = [0.0, 0.5, 1.0, 2.5, -1.0, float("nan"), float("inf")]
for _ in range(5000):
    L = rng.randint(1, 9)
    vals = [rng.choice(pool) for _ in range(L)]
    out.append(run(vals, rng.randrange(L)))
print(json.dumps(out))
'''


def probe(root):
    here = os.path.join(root, STUDY)
    r = subprocess.run([sys.executable, "-B", "-c", PROBE], cwd=here, capture_output=True, text=True,
                       check=True, env=dict(os.environ, PYTHONPATH=here))
    return json.loads(r.stdout)


def report(root):
    here = os.path.join(root, STUDY)
    r = subprocess.run([sys.executable, "-B", "campaign.py"], cwd=here, capture_output=True, text=True)
    return r.returncode, r.stdout


pa, ca = probe(sys.argv[1]), probe(sys.argv[2])
diff = sum(x != y for x, y in zip(pa, ca))
print(f"nonmonotone cases compared: {len(pa)} (21,324 exhaustive + 5,000 random with NaN/inf); differences: {diff}")
ok &= len(pa) == len(ca) == 26324 and diff == 0
rp, rc = report(sys.argv[1]), report(sys.argv[2])
print(f"full campaign CLI: exit {rp[0]}/{rc[0]}, {len(rc[1])} bytes, identical: {rp == rc}")
ok &= rp == rc and rp[0] == 0
print("RESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
