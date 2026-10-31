#!/usr/bin/env python3
"""Round 21 checks behind premium delivery 02 (MODEL.md).

Usage:  python3 -B check_model_md_round21.py <checkout-of-main>

Checks, all read-only on the given checkout:
  1. RAV-01 certainty equivalents with the study's own risk_model.py (P-M06).
  2. q^v with q = 0.9 and v = 20 (P-M07).
  3. Inbound links to MODEL.md sections, and that adding commas to six
     headings leaves every GitHub anchor unchanged (P-M02).
  4. Test counts in the parametric toy folder (P-M11), by running them.
Exit code 1 if any expectation fails.
"""
import os
import re
import subprocess
import sys
import unicodedata

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
ACC = os.path.join(ROOT, "research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1")
MODEL = os.path.join(ACC, "MODEL.md")
fails = []


def expect(label, got, want):
    ok = got == want
    print(f"{'OK  ' if ok else 'FAIL'} {label}: {got!r}" + ("" if ok else f" (expected {want!r})"))
    if not ok:
        fails.append(label)


def slug(heading):
    """GitHub-style anchor: lower-case, drop punctuation except - and _, spaces to hyphens."""
    h = re.sub(r"`", "", heading).strip().lower()
    out = "".join(c for c in h if c in "-_ " or unicodedata.category(c)[0] in "LMN" or unicodedata.category(c) == "Pc")
    return out.replace(" ", "-")


# 1. RAV-01
sys.path.insert(0, os.path.join(ACC, "studies/risk-aversion-persistence-v0.1"))
import risk_model as rm  # noqa: E402

late = rm.RiskChoice(rm.RiskOutcome(14.0, 4.0), rm.RiskOutcome(25.0, 64.0), 0.5)
defense = rm.DefencePolicy(rm.RiskOutcome(14.0, 1.0), effort_cost=0.5)
ce = rm.policy_certainty_equivalents(late, defense)
expect("RAV-01 CE (stay, redesign, defend)", (ce["STAY"], ce["REDESIGN"], ce["DEFEND_STAY"]), (13.0, 9.0, 13.25))
expect("RAV-01 preferred with defense", rm.preferred_with_defense(late, defense), "DEFEND_STAY")

# 2. q^v
expect("0.9**20 rounded to 4 decimals", round(0.9 ** 20, 4), 0.1216)

# 3. Anchors and inbound links
headings = [m.group(2) for m in re.finditer(r"^(#{1,6})\s+(.*?)\s*$", open(MODEL, encoding="utf-8").read(), re.M)]
anchors = {slug(h) for h in headings}
with_commas = {
    "ACC — Modelo auxiliar de oportunidades transición y capacidades": "ACC — Modelo auxiliar de oportunidades, transición y capacidades",
    "Propuestas aceptación y reajuste": "Propuestas, aceptación y reajuste",
    "Utilidad bienestar y frustración": "Utilidad, bienestar y frustración",
    "Error irreversibilidad y tiempo": "Error, irreversibilidad y tiempo",
    "Dinero garantías opcionalidad y reconocimiento": "Dinero, garantías, opcionalidad y reconocimiento",
    "Preservación métodos y contextos": "Preservación, métodos y contextos",
}
for old in with_commas:
    if old not in headings:
        fails.append(f"heading not found: {old}")
expect("anchors unchanged after adding commas", all(slug(o) == slug(n) for o, n in with_commas.items()), True)

link = re.compile(r"MODEL\.md#([^)\s\"'>]+)")
total = 0
per = {}
for dirpath, _, files in os.walk(ROOT):
    if "/.git" in dirpath:
        continue
    for f in files:
        if f.endswith(".md"):
            for frag in link.findall(open(os.path.join(dirpath, f), encoding="utf-8", errors="replace").read()):
                if frag in anchors:
                    total += 1
                    per[frag] = per.get(frag, 0) + 1
renamed = {slug(o) for o in with_commas}
print("     inbound links per section:", dict(sorted(per.items(), key=lambda kv: -kv[1])))
expect("inbound links to MODEL.md sections", total, 81)
expect("inbound links to the retitled sections", sum(v for k, v in per.items() if k in renamed), 35)

# 4. Toy test counts
toy = os.path.join(ACC, "studies/parametric-economic-toy-v0.1")


def ran(args, cwd):
    r = subprocess.run([sys.executable, "-B", "-m", "unittest", *args], cwd=cwd, capture_output=True, text=True)
    m = re.search(r"Ran (\d+) tests?", r.stderr)
    return (int(m.group(1)) if m else None, r.returncode == 0)


expect("toy: unittest discover (count, all pass)", ran(["discover"], toy), (52, True))
expect("toy: tests/test_uc21_dds_bridge.py (count, all pass)", ran(["discover", "-s", "tests", "-p", "test_uc21_dds_bridge.py"], toy), (70, True))
txt = open(MODEL, encoding="utf-8").read()
expect("MODEL.md still says '34 comprobaciones'", "Las 34 comprobaciones" in txt, True)

print("RESULT:", "PASS" if not fails else f"FAIL {fails}")
sys.exit(1 if fails else 0)
