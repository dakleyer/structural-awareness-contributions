"""G-06 source→review claim→case traceability; no historical inspection invented.

Source records register references. A historical text-review claim is not a
signed source-level access receipt. Case use is derived solely from exact
primary_source_id or explicit source_refs, not source titles or conceptual
mentions. S1-Pnnnn are internal ACC notes paragraphs, not a 24th Google Doc.
"""
from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import json
import re
from typing import Mapping, Any

HERE = Path(__file__).resolve().parent
NOTE_PATH = HERE.parent.parent / "model" / "01_NOTAS_COMPLETAS.md"

SCHEMA = "ACC-REGISTERED-SCREENING-CLAIMS-v0.1"
STATES = frozenset({
    "TEXT_REVIEW_REPORTED_AT_COHORT_LEVEL",
    "METADATA_ONLY_REPORTED_AT_BASELINE",
    "NOT_IN_GOOGLE_DOCS_SCREENING_POPULATION",
})
LATER = "CONCEPTUAL_TEXT_SCREENING_REPORTED"
ANCHOR_PATTERN = re.compile(r"^S1-P\d{4}$")
HASH_PATTERN = re.compile(r"^[a-f0-9]{64}$")


def read_json(name: str) -> dict[str, Any]:
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def _unique(rows: list[dict], key: str, context: str) -> dict[str, dict]:
    values = {}
    for row in rows:
        value = row.get(key)
        if not isinstance(value, str) or not value:
            raise ValueError("missing " + context + " identity")
        if value in values:
            raise ValueError("duplicate " + context + " identity " + value)
        values[value] = row
    return values


def _validate_review_source(item: dict, source: dict) -> None:
    if item.get("reference_kind") not in ("GOOGLE_DOC", "GITHUB_CORPUS_REFERENCE"):
        raise ValueError("invalid reference kind")
    doc = source["url"].startswith("https://docs.google.com/document/d/")
    if doc != (item["reference_kind"] == "GOOGLE_DOC"):
        raise ValueError("reference kind does not match source URL")
    status = item["baseline_status"]
    if status not in STATES:
        raise ValueError("unknown text review status")
    if (status == "NOT_IN_GOOGLE_DOCS_SCREENING_POPULATION") != (not doc):
        raise ValueError("corpus reference misclassified as a Google Doc")
    evidence = item["baseline_evidence"]
    if evidence["dated_cutoff"] != "2026-10-26":
        raise ValueError("baseline report date changed")
    if not evidence.get("reference", "").startswith("README.md#"):
        raise ValueError("missing trace to initial review claim")
    expected_method = {
        "TEXT_REVIEW_REPORTED_AT_COHORT_LEVEL":
            "INFERRED_BY_EXCLUSION_FROM_17_OF_19_AGGREGATE",
        "METADATA_ONLY_REPORTED_AT_BASELINE":
            "NAMED_EXCEPTION_IN_HISTORICAL_README",
        "NOT_IN_GOOGLE_DOCS_SCREENING_POPULATION":"NOT_APPLICABLE",
    }[status]
    if evidence.get("claim_scope") != expected_method:
        raise ValueError("unsupported individualized reading claim")
    later = item.get("later_review_claim")
    if later is not None:
        if status != "METADATA_ONLY_REPORTED_AT_BASELINE":
            raise ValueError("later screening claim outside historical exceptions")
        if later.get("status") != LATER or later.get("reported_at") != "2026-10-29":
            raise ValueError("unqualified subsequent review claim")
        if not later.get("reference", "").startswith("SOURCE_COVERAGE_AND_BACKLOG.md#"):
            raise ValueError("missing trace to later screening claim")
        if "NO_ARCHIVED_DOCUMENT_VERSION" not in later.get("proof_limit", ""):
            raise ValueError("later claim must retain its evidential limitation")
    # Future per-file attestation must carry a real immutable source snapshot,
    # a reviewer and an inspection date. It cannot be inferred from a cohort.
    if evidence.get("independent_source_level_review_attested") is True:
        snap = evidence.get("content_snapshot_sha256")
        if not isinstance(snap, str) or not HASH_PATTERN.fullmatch(snap):
            raise ValueError("attested historical review lacks snapshot hash")
        if not evidence.get("reviewer") or not evidence.get("reviewed_at"):
            raise ValueError("attested historical review lacks reviewer/time")
    elif evidence.get("content_snapshot_sha256") is not None:
        raise ValueError("unattested source unexpectedly claims a snapshot hash")
    if later is not None and later.get("independent_source_level_review_attested"):
        snap = later.get("content_snapshot_sha256")
        if not isinstance(snap,str) or not HASH_PATTERN.fullmatch(snap):
            raise ValueError("later independent review lacks snapshot hash")
        if not later.get("reviewer") or not later.get("reviewed_at"):
            raise ValueError("later independently attested review lacks reviewer/time")


def source_trace(
    source_register: Mapping[str, Any],
    review_ledger: Mapping[str, Any],
    case_register: Mapping[str, Any],
    narrative_registry: Mapping[str, Any],
    *,
    notes_text: str,
) -> dict[str, Any]:
    """Return exact source use and conservative screening evidence.

    Design is generic for changed sources and cases. No fixed 23 or 60 count
    is baked into the algorithm; those are assertions in versioned tests.
    """
    if review_ledger.get("schema") != SCHEMA:
        raise ValueError("unsupported source review ledger schema")
    if review_ledger.get("source_registry") != "SOURCE_REGISTER.json":
        raise ValueError("source claim register mismatch")
    sources = _unique(source_register["sources"],"source_id","registered source")
    ledger = _unique(review_ledger["sources"],"source_id","review ledger")
    if set(sources) != set(ledger):
        raise ValueError("review ledger must cover exactly the registered source identities")
    urls = [row["url"] for row in sources.values()]
    if len(set(urls)) != len(urls):
        raise ValueError("same URL registered with duplicate identities")
    for key in sources:
        _validate_review_source(ledger[key],sources[key])

    primary = _unique(case_register["cases"],"case_id","frozen case")
    if len(primary) != case_register["frozen_case_count"]:
        raise ValueError("frozen case identity count changed")
    narrative = _unique(narrative_registry["cases"],"case_id","narrative case")
    direct_primary=defaultdict(list)
    direct_narrative=defaultdict(list)
    internal_anchors=defaultdict(list)
    for case_id,case in primary.items():
        source_id = case.get("primary_source_id")
        if source_id not in sources:
            raise ValueError("frozen case has unregistered primary source: " + str(source_id))
        direct_primary[source_id].append(case_id)
    for case_id,case in narrative.items():
        refs = case.get("source_refs")
        if not isinstance(refs,list) or not refs:
            raise ValueError("narrative case missing source references")
        if len(set(refs)) != len(refs):
            raise ValueError("narrative case repeats a source reference")
        for ref in refs:
            if ref in sources:
                direct_narrative[ref].append(case_id)
            elif isinstance(ref,str) and ANCHOR_PATTERN.fullmatch(ref):
                if "<!-- " + ref + " -->" not in notes_text:
                    raise ValueError("unresolved internal source paragraph: " + ref)
                if '<a id="' + ref.lower() + '"></a>' not in notes_text:
                    raise ValueError("source paragraph missing anchor pair: " + ref)
                internal_anchors[ref].append(case_id)
            else:
                raise ValueError("unknown narrative source reference: " + str(ref))

    doc_ids=[x for x in sources if ledger[x]["reference_kind"]=="GOOGLE_DOC"]
    baselines={state:sum(ledger[x]["baseline_status"]==state for x in sources)
               for state in sorted(STATES)}
    later_ids=sorted(x for x in doc_ids if ledger[x].get("later_review_claim") is not None)
    reviewed_attested=sorted(x for x in doc_ids if
                           ledger[x]["baseline_evidence"]["independent_source_level_review_attested"] is True)
    direct_ids=sorted(set(direct_primary)|set(direct_narrative))
    used_frozen=sorted(direct_primary)
    summary={
        "registered_total":len(sources),
        "registered_google_docs":len(doc_ids),
        "registered_github_references":len(sources)-len(doc_ids),
        "baseline_text_review_reported_cohort_only":baselines["TEXT_REVIEW_REPORTED_AT_COHORT_LEVEL"],
        "baseline_metadata_only_reported":baselines["METADATA_ONLY_REPORTED_AT_BASELINE"],
        "later_conceptual_review_reported_without_snapshot":len(later_ids),
        "independent_source_level_historical_text_reviews_attested":len(reviewed_attested),
        "frozen_primary_cases":len(primary),
        "registered_sources_used_as_primary_in_frozen_cases":len(used_frozen),
        "narrative_cases_with_source_refs":len(narrative),
        "registered_sources_explicitly_used_in_either_case_registry":len(direct_ids),
        "internal_notes_paragraphs_referenced":len(internal_anchors),
        "legacy_source_documents_screened_23_meant":"REGISTERED_TOTAL_NOT_SCREENED_TEXT",
    }
    details=[]
    for source_id in sorted(sources):
        item=ledger[source_id]
        primary_ids=sorted(direct_primary[source_id])
        extra_ids=sorted(direct_narrative[source_id])
        details.append({
            "source_id":source_id,
            "reference_kind":item["reference_kind"],
            "baseline_review_claim":item["baseline_status"],
            "later_review_claim_status":(
                item["later_review_claim"]["status"] if item.get("later_review_claim") else None),
            "baseline_evidence_ref":item["baseline_evidence"]["reference"],
            "later_evidence_ref":(
                item["later_review_claim"]["reference"] if item.get("later_review_claim") else None),
            "source_level_review_attested":
                item["baseline_evidence"]["independent_source_level_review_attested"],
            "primary_frozen_case_ids":primary_ids,
            "explicit_narrative_case_ids":extra_ids,
            "used_as_case_source":bool(primary_ids or extra_ids),
            "not_used_does_not_mean_not_read":True,
        })
    return {
        "schema":"ACC-SOURCE-REVIEW-CASE-LINEAGE-v0.1",
        "original_source_cutoff":source_register["source_cutoff"],
        "review_ledger_as_of":review_ledger["as_of_review"],
        "counts":summary,
        "source_level_lineage":details,
        "internal_paragraph_lineage":{
            key:{"source_document":"model/01_NOTAS_COMPLETAS.md",
                 "case_ids":sorted(value)}
            for key,value in sorted(internal_anchors.items())},
        "later_conceptual_claim_ids":later_ids,
        "used_source_ids":direct_ids,
        "scope_notice":"Sources registered != texts inspected != evidence used as a case. Later screening self-report does not retroactively alter baseline or substitute an archived snapshot.",
        "fixture_limit":"Synthetic author examples; no empirical source validation or UC21 product run.",
    }


def build_provenance() -> dict[str, Any]:
    return source_trace(
        read_json("SOURCE_REGISTER.json"),
        read_json("SOURCE_REVIEW_CLAIMS.json"),
        read_json("CASE_REGISTRY.json"),
        read_json("ORIGINAL_EXPERIMENTS.json"),
        notes_text=NOTE_PATH.read_text(encoding="utf-8"),
    )


def main() -> int:
    result=build_provenance()
    print(json.dumps(result,sort_keys=True,ensure_ascii=False,indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
