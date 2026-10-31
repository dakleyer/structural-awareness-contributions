"""M28-01: the two float-boundary adversaries of the numeric guard (round 13).

Usage: python3 -B m28_01_float_boundary.py <studies/scoped-closure-metacognition-v0.1>
Expected on main 51fc686: case 1 EVIDENCE_OR_ASSUMPTIONS_INCONSISTENT, case 2
UNDETERMINED_FROM_AVAILABLE_EVIDENCE; both exact checks False. Writes nothing.
"""
import sys
from fractions import Fraction as F
sys.path.insert(0, sys.argv[1])
from metacognition import Point, Frame, DecisionQuestion, qualify
eps = 2.0**-54
def P(cid, x, y): return Point(claim_id=cid, origin_id=cid, scope="x", revision="v1", observed_at=4, x_min=x, x_max=x, y_min=y, y_max=y, source_attested=True)
def Fr(L): return Frame(scope="x", revision="v1", now=5, max_age=5, domain_min=0, domain_max=2, lipschitz=L, regularity_qualified=True)
r1 = qualify(Fr(1.0), DecisionQuestion(x=0, threshold=1), (P("a",0.0,1.0), P("b",1.0,-eps)))
print("case1 status:", r1["local_answer_status"], "| exact consistent?", abs(F(1)-F(-eps)) <= F(1)*1)
r2 = qualify(Fr(eps), DecisionQuestion(x=1, threshold=1), (P("a",0.0,1.0),))
print("case2 status:", r2["local_answer_status"], "| exact lower bound >= 1?", F(1) - F(eps)*1 >= 1)
