"""Round 45: PR #95 renames H-01 sensitivity grids so they are not read as economic K dimensions.

Usage: python3 -B sensitivity_grid_labels_check.py <checkout of #92> <checkout of #95>

1. Structural identity: parses strategic_choice.py in both trees, maps the
   renamed local `grid_keys` back to `dimensions`, removes docstrings and
   lists every remaining difference in the AST. Expected: only the text of
   one ValueError message.
2. Full report identity: runs `run_manifest` over H01_STRATEGIC_STUDY.json in
   each tree (separate subprocesses) and compares the JSON byte by byte.
3. Error path: a plan missing one grid is rejected in both trees.

Exit code 1 on a mismatch. Writes nothing.
"""
import ast
import json
import os
import subprocess
import sys

STUDY = ("research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/"
         "studies/bounded-traps-v0.1")


class Norm(ast.NodeTransformer):
    def visit_Name(self, node):
        if node.id == "grid_keys":
            node.id = "dimensions"
        return node

    def _strip_doc(self, node):
        self.generic_visit(node)
        body = node.body
        if body and isinstance(body[0], ast.Expr) and isinstance(getattr(body[0], "value", None), ast.Constant) \
                and isinstance(body[0].value.value, str):
            node.body = body[1:] or [ast.Pass()]
        return node

    visit_FunctionDef = visit_Module = visit_ClassDef = _strip_doc


def constants(tree):
    return [n.value for n in ast.walk(tree) if isinstance(n, ast.Constant)]


def norm(root):
    src = open(os.path.join(root, STUDY, "strategic_choice.py"), encoding="utf-8").read()
    return Norm().visit(ast.parse(src))


a, b = norm(sys.argv[1]), norm(sys.argv[2])
ca, cb = constants(a), constants(b)
diff = [(x, y) for x, y in zip(ca, cb) if x != y]
# Replace the differing constants and check the rest of the tree is equal.
for n in ast.walk(b):
    if isinstance(n, ast.Constant):
        for x, y in diff:
            if n.value == y:
                n.value = x
same_structure = ast.dump(a) == ast.dump(b) and len(ca) == len(cb)
print("AST differences after renaming and without docstrings:", diff)
ok = same_structure and len(diff) == 1

PROBE = r'''
import json, strategic_choice as sc
m = json.load(open("H01_STRATEGIC_STUDY.json"))
report = json.dumps(sc.run_manifest(m), sort_keys=True, default=str)
plan = dict(m["sensitivity"]); plan.pop("pairwise_synergies")
try:
    sc.sensitivity_grid(m["base_game"], plan); err = "ACCEPTED"
except ValueError as e:
    err = "REJECTED: " + str(e)
print(json.dumps({"report": report, "err": err}))
'''


def probe(root):
    here = os.path.join(root, STUDY)
    r = subprocess.run([sys.executable, "-B", "-c", PROBE], cwd=here, capture_output=True, text=True, check=True)
    return json.loads(r.stdout)


p, c = probe(sys.argv[1]), probe(sys.argv[2])
same_report = p["report"] == c["report"]
print(f"full H-01 report identical ({len(c['report'])} bytes):", same_report)
print("missing grid, #92:", p["err"])
print("missing grid, #95:", c["err"])
ok &= same_report and p["err"].startswith("REJECTED") and c["err"].startswith("REJECTED")
print("RESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
