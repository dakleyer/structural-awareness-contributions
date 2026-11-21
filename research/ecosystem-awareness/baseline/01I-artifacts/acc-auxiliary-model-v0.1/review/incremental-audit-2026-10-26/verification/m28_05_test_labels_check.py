"""Round 52: M28-05 / IP-39-40, test labels in PR #101 (child of #85).

Usage: python3 -B m28_05_test_labels_check.py <checkout of #85> <checkout of #101>

1. For the two changed test modules, parses both versions, maps the new
   test and local-variable names back to the old ones and compares the ASTs
   (comments are not in the AST). Expected: identical, i.e. the same calls,
   inputs and assertions.
2. Confirms each renamed test really calls the same function twice with
   identical arguments (the reason the old "peer" names over-claimed).
3. Runs the whole Theme 18 test suite (test_theme18_*.py) in both trees and
   compares the number of tests and the outcome.

Exit code 1 on a mismatch. Writes nothing.
"""
import ast
import os
import re
import subprocess
import sys

STUDY = ("research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/"
         "studies/mathematical-lineage-social-agentic-v0.1")
FILES = {
    "test_theme18_candidate_admission.py": {
        "test_supplied_candidate_procedure_reproduces_fixture": "test_strong_peer_with_same_evidence_ties"},
    "test_theme18_online_context.py": {
        "test_reusing_supplied_guard_reproduces_cost_ledger": "test_competent_same_guard_conventional_peer_ties",
        "first": "our", "repeated": "peer"},
}


class Rename(ast.NodeTransformer):
    def __init__(self, mapping):
        self.m = mapping

    def visit_FunctionDef(self, node):
        node.name = self.m.get(node.name, node.name)
        self.generic_visit(node)
        return node

    def visit_Name(self, node):
        node.id = self.m.get(node.id, node.id)
        return node


def parse(root, name):
    return ast.parse(open(os.path.join(root, STUDY, name), encoding="utf-8").read())


ok = True
for name, mapping in FILES.items():
    old, new = parse(sys.argv[1], name), parse(sys.argv[2], name)
    same = ast.dump(old) == ast.dump(Rename(mapping).visit(new))
    ok &= same
    print(f"{name}: AST identical after mapping names back: {same}")
    new = parse(sys.argv[2], name)
    for fn in (n for n in ast.walk(new) if isinstance(n, ast.FunctionDef) and n.name in mapping):
        calls = [ast.dump(c) for c in ast.walk(fn) if isinstance(c, ast.Call)
                 and isinstance(c.func, ast.Name) and c.func.id in ("assess_candidate", "ledger")]
        twice = len(calls) == 2 and calls[0] == calls[1]
        ok &= twice
        print(f"   {fn.name}: same function, same arguments, called twice: {twice}")


def suite(root):
    here = os.path.join(root, STUDY)
    r = subprocess.run([sys.executable, "-B", "-m", "unittest", "discover", "-p", "test_theme18_*.py"],
                       cwd=here, capture_output=True, text=True)
    m = re.search(r"Ran (\d+) tests", r.stderr)
    return (int(m.group(1)) if m else None, r.returncode)


p, c = suite(sys.argv[1]), suite(sys.argv[2])
print(f"Theme 18 suite: #85 {p[0]} tests (exit {p[1]}), #101 {c[0]} tests (exit {c[1]})")
ok &= p == c and c[1] == 0
print("RESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
