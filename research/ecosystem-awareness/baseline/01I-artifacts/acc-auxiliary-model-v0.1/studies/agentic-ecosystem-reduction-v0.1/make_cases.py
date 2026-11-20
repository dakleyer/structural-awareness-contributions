"""Generate deterministic, traceable, entirely SYNTHETIC agentic-reduction cases.

This generator never reads Google Docs or private humans at run time. The
SOURCE_MAP registers precisely what inspired each toy mechanism.
"""
from __future__ import annotations
import json
from copy import deepcopy
from pathlib import Path

ROOT=Path(__file__).resolve().parent
PUBLIC={
 "scope":"vendor-ecosystem-v1", "total_resources":10, "donor_current":6,
 "recipient_current":4, "donor_marginal_rate":1, "donor_minimum":2,
 "transfer_maximum":4, "overhead_resources":0.25,
 "metamorph_declared_in_A":True, "release_declared_in_A":True,
 "release_consent":True, "meta_owner_authority":True,
 "joint_protocol_available":True, "mission_target":12,
 "known_upper_rate_bound":2.5, "material_D_for_joint_decision":False
}
Q={"kind":"B", "scope":PUBLIC["scope"], "source_named":True, "valid_until":20,
   "lower_rate":1.6, "transfer_ceiling":2, "cost":0.3,
   "material_D_for_question":False, "origin":"recipient's characterized B capacity margin"}
PEER={"available":True,"cost":1.2,"measured_rate":2.0,"equivalent_Q_cost":0.3}
FULL={"available":True,"cost":8.0,"fully_measured_rate":2.0}


def case(id, *, public=None, q=None, directed=None, full=None, true_rate=2.0, source_ids=None, note=""):
    s={"id":id, "public":deepcopy(PUBLIC), "Q":deepcopy(Q),
       "directed":deepcopy(PEER),"full_A":deepcopy(FULL),
       "truth_private":{"recipient_incremental_rate":true_rate},
       "source_ids":source_ids or ["CE-ANTS","CE-WORKBENCH","ACC-00M"],
       "notes":note,"source_evidence_level":"CONCEPTUAL_SOURCE_THEN_SYNTHETIC_FIXTURE"}
    for key,x in [("public",public),("Q",q),("directed",directed),("full_A",full)]:
        if x is None: continue
        if x is False: s[key]=None
        else: s[key].update(x)
    if source_ids is None:
        tags = ["CE-WORKBENCH", "ACC-00M"]
        if "ROLE" in id or "METAMORPH" in id or "NO-A" in id: tags += ["CE-ANTS"]
        if "CONSENT" in id or "RELEASE" in id or "VOLUNTARY" in id: tags += ["CE-SOLIDARITY"]
        if "D-" in id or "UNCHARACTERIZED" in id or "FALSE" in id or "BOGUS" in id: tags += ["CE-SCHEME", "ACC-00N"]
        if "REWRITE" in id or "COST" in id or "PEER" in id: tags += ["CE-CORRESPONDENCE"]
        s["source_ids"] = sorted(set(tags))
    return s


def scenarios():
    return [
       case("AG01-QUALIFIED-NEAR-OPTIMUM",note="B certifies a nearby partial improvement, not the global optimum"),
       case("AG02-LOW-CAPABILITY-SAME-A",true_rate=0.5,q={"lower_rate":0.4},directed={"measured_rate":0.5},full={"fully_measured_rate":0.5},note="Identical current A; no advantageous reallocation"),
       case("AG03-A-ONLY-Q-ABSENT",q=False,note="No Q; traditional directed information may still exist"),
       case("AG04-Q-REVIEW-NO-EXECUTION",public={"joint_protocol_available":False},note="Second-order visible but no physically executable joint path"),
       case("AG05-NO-A-ROLE-CHANGE",public={"metamorph_declared_in_A":False},note="Metamorphosis absent from A: the protocol cannot manufacture capabilities"),
       case("AG06-NO-DONOR-RELEASE-CAPABILITY",public={"release_declared_in_A":False},note="Declining local output without a predeclared release is not authorized"),
       case("AG07-DONOR-REFUSES",public={"release_consent":False},note="No forced functional solidarity or sacrifice"),
       case("AG08-META-OWNER-LACKS-AUTHORITY",public={"meta_owner_authority":False},note="Meta process observes but cannot assign rights"),
       case("AG09-MATERIAL-D-UNRESOLVED",public={"material_D_for_joint_decision":True},q={"material_D_for_question":True},note="Material D remains beyond an effective assessment route"),
       case("AG10-D-OTHER-SCOPE-UNPERTINENT",q={"material_D_for_question":False},note="An unrelated D does not cause blanket HOLD"),
       case("AG11-BOGUS-B-CERTIFICATE",true_rate=0.5,directed={"measured_rate":0.5},full={"fully_measured_rate":0.5},note="A syntactically correct Q may lie; real output can fall"),
       case("AG12-EXPIRED-B",q={"valid_until":8},note="No automatic permission from obsolete signal"),
       case("AG13-WRONG-SCOPE",q={"scope":"different-vendor-contract"},note="Partial B cannot be transferred across incompatible scope"),
       case("AG14-UNCHARACTERIZED-C",q={"kind":"C","lower_rate":None},note="C is a grounded exploration avenue without a usable ROI guarantee"),
       case("AG15-D-NOT-A-MARGINAL",q={"kind":"D","lower_rate":None},note="D is not a variable with a known rate"),
       case("AG16-EXCESSIVE-Q-MAINTENANCE",q={"cost":1.5},note="Acquiring Q may be net worse than skipping it"),
       case("AG17-RECONFIGURATION-CONSUMES-MOST",public={"overhead_resources":1.8},note="True physical potential does not imply cheap/continuous path"),
       case("AG18-EFFICIENT-DIRECTED-PEER",directed={"cost":0.1},note="Conventional peer with genuine effective inspection can win"),
       case("AG19-FULL-A-CHEAP",full={"cost":0.1},note="When whole-A information is actually inexpensive it may dominate"),
       case("AG20-FULL-A-UNAVAILABLE",full={"available":False},note="No omniscient comparator within the profile"),
       case("AG21-DIRECTED-PEER-UNAVAILABLE",directed={"available":False},note="Strong targeted competitor must have an actual instrument"),
       case("AG22-CONVENTIONAL-EQUIVALENT-CHEAP",directed={"equivalent_Q_cost":0.05},note="A conventional implementation of Q deserves full credit"),
       case("AG23-AGENTIC-LOW-REWRITE-COST",public={"overhead_resources":0.1},note="A parameter scenario, not a measured cost superiority"),
       case("AG24-LEGACY-HIGH-REWRITE-COST",public={"overhead_resources":1.8},note="Legacy/human reconfiguration overhead parameter; no population claim"),
       case("AG25-MISSION-HAS-ALREADY-BEEN-MET",public={"mission_target":9},note="Meeting service mission does not imply optimizing all functions"),
       case("AG26-NO-UNRESTRICTED-DONOR",public={"donor_minimum":5.5,"transfer_maximum":4},note="Donor indispensable floor restricts options; no invented reserve"),
       case("AG27-THIRD-PARTY-REVIEW-LIMIT",public={"meta_owner_authority":False,"release_consent":True},note="Social governance cannot be overwritten by meta decision"),
       case("AG28-BARRED-PRIVATE-EVIDENCE",q={"source_named":False},note="Unattributed Q gives no justified claim"),
       case("AG29-CHEAP-Q-BUT-WRONG-WORLD",q={"cost":0.01},true_rate=0.5,directed={"measured_rate":0.5},full={"fully_measured_rate":0.5},note="Low cost of false B does not make it true"),
       case("AG30-SHARED-PROTOCOL-BUT-UNCHARACTERIZED-Q",q={"kind":"C","lower_rate":None},directed={"available":False},full={"available":False},note="Residual cannot be turned into A by desire"),
    ]


def main():
    cases=scenarios()
    ids=[s["id"] for s in cases]
    if len(ids)!=len(set(ids)):
        raise ValueError("duplicate case")
    d={"schema":"ACC-AGENTIC-REDUCTION-v0.1","evidence":"SYNTHETIC_AUTHOR_INSPIRED_CASES_NOT_REAL_AGENT_RUNS",
       "cases":cases}
    (ROOT/"CASES.json").write_text(json.dumps(d,ensure_ascii=False,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print(len(cases))
if __name__=="__main__":main()
