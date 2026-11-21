"""G-06 (round 29): recount source registration, review claims and case use for PR #71.

Usage: python3 -B g06_provenance_recount.py <checkout of PR #71>

Independent of source_provenance.py. Reads the raw JSON and the notes file:
  registered sources (Google Docs vs GitHub references); baseline review
  claims by status; distinct primary sources in the 60 frozen cases; registered
  sources and internal S1-P anchors referenced by the 40 narrative cases; and
  whether each S1-P anchor exists in model/01_NOTAS_COMPLETAS.md as both an
  HTML comment and an <a id>. Expected on 9dc00e6d: 23 = 19 + 4; 17 cohort
  text-review claims, 2 metadata-only, 0 source-level snapshots; 10 primary
  sources; 13 registered sources used overall; 12 anchors, all present.
Exit code 1 on a mismatch. Writes nothing.
"""
import collections
import json
import os
import sys

ACC = os.path.join(sys.argv[1], "research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1")
CAMP = os.path.join(ACC, "studies/conscientia-campaign-v0.1")


def load(name):
    return json.load(open(os.path.join(CAMP, name), encoding="utf-8"))


register = {s["source_id"]: s for s in load("SOURCE_REGISTER.json")["sources"]}
claims = {s["source_id"]: s for s in load("SOURCE_REVIEW_CLAIMS.json")["sources"]}
frozen = load("CASE_REGISTRY.json")["cases"]
narrative = load("ORIGINAL_EXPERIMENTS.json")["cases"]
notes = open(os.path.join(ACC, "model/01_NOTAS_COMPLETAS.md"), encoding="utf-8").read()

docs = [k for k, v in claims.items() if v["reference_kind"] == "GOOGLE_DOC"]
status = collections.Counter(v["baseline_status"] for v in claims.values())
attested = sum(v["baseline_evidence"]["independent_source_level_review_attested"] is True for v in claims.values())
primary = {c["primary_source_id"] for c in frozen}
narr_sources = {r for c in narrative for r in c["source_refs"] if r in register}
anchors = {r for c in narrative for r in c["source_refs"] if r.startswith("S1-P")}
missing = [a for a in sorted(anchors)
           if f"<!-- {a} -->" not in notes or f'<a id="{a.lower()}"></a>' not in notes]
unknown = [r for c in narrative for r in c["source_refs"] if r not in register and not r.startswith("S1-P")]

got = {
    "registered": len(register), "google_docs": len(docs), "github_refs": len(register) - len(docs),
    "claims_cover_register": set(claims) == set(register),
    "cohort_text_review": status["TEXT_REVIEW_REPORTED_AT_COHORT_LEVEL"],
    "metadata_only": status["METADATA_ONLY_REPORTED_AT_BASELINE"],
    "source_level_snapshots": attested,
    "frozen_cases": len(frozen), "frozen_primary_sources": len(primary),
    "narrative_cases": len(narrative), "sources_used_overall": len(primary | narr_sources),
    "s1p_anchors": len(anchors), "s1p_missing": len(missing), "unknown_refs": len(unknown),
}
want = {"registered": 23, "google_docs": 19, "github_refs": 4, "claims_cover_register": True,
        "cohort_text_review": 17, "metadata_only": 2, "source_level_snapshots": 0,
        "frozen_cases": 60, "frozen_primary_sources": 10, "narrative_cases": 40,
        "sources_used_overall": 13, "s1p_anchors": 12, "s1p_missing": 0, "unknown_refs": 0}
for k in want:
    flag = "OK  " if got[k] == want[k] else "FAIL"
    print(f"{flag} {k}: {got[k]}" + ("" if got[k] == want[k] else f" (expected {want[k]})"))
print("metadata-only sources:", sorted(k for k, v in claims.items() if v["baseline_status"].startswith("METADATA")))
print("sources added by the 40 narrative cases:", sorted(narr_sources - primary))
bad = [k for k in want if got[k] != want[k]]
print("RESULT:", "PASS" if not bad else f"FAIL {bad}")
sys.exit(1 if bad else 0)
