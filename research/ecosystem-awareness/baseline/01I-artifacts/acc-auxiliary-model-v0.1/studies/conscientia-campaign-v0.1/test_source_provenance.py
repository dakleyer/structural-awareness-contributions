"""G-06 tests: registration, reported reading, and case use are not synonyms."""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import unittest

import campaign
from source_provenance import build_provenance, read_json, source_trace, NOTE_PATH


REG = read_json("SOURCE_REGISTER.json")
CLAIMS = read_json("SOURCE_REVIEW_CLAIMS.json")
CASES = read_json("CASE_REGISTRY.json")
NARRATIVE = read_json("ORIGINAL_EXPERIMENTS.json")
NOTES = NOTE_PATH.read_text(encoding="utf-8")


def result(r=None, l=None, c=None, n=None, notes=None):
    return source_trace(
        deepcopy(REG if r is None else r),
        deepcopy(CLAIMS if l is None else l),
        deepcopy(CASES if c is None else c),
        deepcopy(NARRATIVE if n is None else n),
        notes_text=NOTES if notes is None else notes,
    )


class RegistrationVsReviewTests(unittest.TestCase):
    def test_23_registered_but_only_19_are_google_docs(self):
        counts=build_provenance()["counts"]
        self.assertEqual((counts["registered_total"],counts["registered_google_docs"],
                          counts["registered_github_references"]),(23,19,4))
        self.assertEqual(counts["legacy_source_documents_screened_23_meant"],
                         "REGISTERED_TOTAL_NOT_SCREENED_TEXT")

    def test_baseline_cohort_report_is_17_and_two_metadata_only(self):
        t=build_provenance()
        c=t["counts"]
        self.assertEqual(c["baseline_text_review_reported_cohort_only"],17)
        self.assertEqual(c["baseline_metadata_only_reported"],2)
        self.assertEqual(c["independent_source_level_historical_text_reviews_attested"],0)
        names={x["source_id"]:x for x in t["source_level_lineage"]}
        for sid in ("CE-MH-ONEPAGER","CE-PRESCIENCE"):
            self.assertEqual(names[sid]["baseline_review_claim"],
                             "METADATA_ONLY_REPORTED_AT_BASELINE")
            self.assertEqual(names[sid]["later_review_claim_status"],
                             "CONCEPTUAL_TEXT_SCREENING_REPORTED")
            self.assertFalse(names[sid]["source_level_review_attested"])

    def test_later_conceptual_note_does_not_retroactively_certify_original_reading(self):
        ledger=deepcopy(CLAIMS)
        late={s["source_id"]:s for s in ledger["sources"]}
        for sid in ("CE-MH-ONEPAGER","CE-PRESCIENCE"):
            late[sid]["later_review_claim"]=None
        a=result(l=ledger)["counts"]
        b=result()["counts"]
        self.assertEqual(a["baseline_text_review_reported_cohort_only"],
                         b["baseline_text_review_reported_cohort_only"])
        self.assertEqual(a["baseline_metadata_only_reported"],
                         b["baseline_metadata_only_reported"])
        self.assertEqual(a["later_conceptual_review_reported_without_snapshot"],0)
        self.assertEqual(b["later_conceptual_review_reported_without_snapshot"],2)

    def test_reviewer_proof_cannot_be_invented_without_snapshot_and_date(self):
        ledger=deepcopy(CLAIMS)
        ledger["sources"][0]["baseline_evidence"]["independent_source_level_review_attested"]=True
        with self.assertRaisesRegex(ValueError,"snapshot"):
            result(l=ledger)
        ledger["sources"][0]["baseline_evidence"]["content_snapshot_sha256"]="a"*64
        with self.assertRaisesRegex(ValueError,"reviewer/time"):
            result(l=ledger)

    def test_later_conceptual_claim_cannot_silently_become_verification(self):
        ledger=deepcopy(CLAIMS)
        x=next(s for s in ledger["sources"] if s["source_id"]=="CE-PRESCIENCE")
        x["later_review_claim"]["independent_source_level_review_attested"]=True
        with self.assertRaisesRegex(ValueError,"snapshot"):
            result(l=ledger)

    def test_all_23_ledger_records_match_unique_registered_urls(self):
        self.assertEqual(len(REG["sources"]),len(CLAIMS["sources"]))
        self.assertEqual(len(build_provenance()["source_input_sha256"]),5)
        self.assertTrue(all(len(value)==64
                            for value in build_provenance()["source_input_sha256"].values()))
        bad=deepcopy(CLAIMS)
        bad["sources"].pop()
        with self.assertRaisesRegex(ValueError,"exactly the registered"):
            result(l=bad)
        bad=deepcopy(REG)
        bad["sources"][1]["url"]=bad["sources"][0]["url"]
        with self.assertRaisesRegex(ValueError,"duplicate identities"):
            result(r=bad)

    def test_wrong_document_population_and_baseline_claim_fail(self):
        l=deepcopy(CLAIMS)
        l["sources"][0]["reference_kind"]="GITHUB_CORPUS_REFERENCE"
        with self.assertRaisesRegex(ValueError,"kind does not match"):
            result(l=l)
        l=deepcopy(CLAIMS)
        l["sources"][0]["baseline_status"]="SOURCE_LEVEL_FULL_READ_PROVEN"
        with self.assertRaisesRegex(ValueError,"unknown text review status"):
            result(l=l)


class CaseLineageTests(unittest.TestCase):
    def test_frozen_cases_use_ten_explicit_primary_sources_not_23(self):
        t=build_provenance()
        c=t["counts"]
        self.assertEqual(c["frozen_primary_cases"],60)
        self.assertEqual(c["registered_sources_used_as_primary_in_frozen_cases"],10)
        self.assertEqual(c["narrative_cases_with_source_refs"],40)
        self.assertEqual(c["registered_sources_explicitly_used_in_either_case_registry"],13)
        self.assertEqual(len(t["used_source_ids"]),13)
        self.assertTrue(set(t["used_source_ids"])<=
                        {x["source_id"] for x in REG["sources"]})

    def test_source_references_are_auditable_at_case_id_granularity(self):
        d={x["source_id"]:x for x in build_provenance()["source_level_lineage"]}
        self.assertEqual(len(d["CE-SCHEME"]["primary_frozen_case_ids"]),10)
        self.assertEqual(len(d["CE-NOTES"]["primary_frozen_case_ids"]),10)
        self.assertFalse(d["CE-PRESCIENCE"]["used_as_case_source"])
        self.assertTrue(d["ACC-EXAMPLES"]["used_as_case_source"])
        self.assertTrue(d["CE-ANTS"]["explicit_narrative_case_ids"])
        self.assertTrue(all(x["not_used_does_not_mean_not_read"] for x in d.values()))

    def test_usage_changes_with_fixtures_without_faking_review_status(self):
        altered=deepcopy(CASES)
        altered["cases"][0]["primary_source_id"]="CE-SOLIDARITY-V3"
        after=result(c=altered)
        self.assertEqual(after["counts"]["registered_sources_used_as_primary_in_frozen_cases"],11)
        details={x["source_id"]:x for x in after["source_level_lineage"]}
        self.assertIn(altered["cases"][0]["case_id"],
                      details["CE-SOLIDARITY-V3"]["primary_frozen_case_ids"])
        self.assertFalse(details["CE-SOLIDARITY-V3"]["source_level_review_attested"])

    def test_unknown_primary_or_narrative_source_must_fail(self):
        c=deepcopy(CASES)
        c["cases"][0]["primary_source_id"]="MADE_UP_SOURCE"
        with self.assertRaisesRegex(ValueError,"unregistered primary source"):
            result(c=c)
        n=deepcopy(NARRATIVE)
        n["cases"][0]["source_refs"]=["MADE_UP_SOURCE"]
        with self.assertRaisesRegex(ValueError,"unknown narrative source"):
            result(n=n)

    def test_internal_S1_paragraph_refs_are_not_24th_registered_doc(self):
        t=build_provenance()
        s=t["internal_paragraph_lineage"]
        self.assertTrue(s)
        self.assertEqual(t["counts"]["internal_notes_paragraphs_referenced"],len(s))
        self.assertIn("S1-P0639",s)
        self.assertEqual(s["S1-P0639"]["source_document"],
                         "model/01_NOTAS_COMPLETAS.md")
        self.assertEqual(t["counts"]["registered_total"],23)
        self.assertFalse(any(x.startswith("S1-P") for x in t["used_source_ids"]))

    def test_orphaned_S1_paragraph_does_not_get_a_source(self):
        n=deepcopy(NARRATIVE)
        n["cases"][0]["source_refs"]=["S1-P9999"]
        with self.assertRaisesRegex(ValueError,"unresolved internal source paragraph"):
            result(n=n)

    def test_missing_internal_anchor_pair_fails_even_when_comment_exists(self):
        corrupted=NOTES.replace('<a id="s1-p0639"></a>','')
        with self.assertRaisesRegex(ValueError,"source paragraph missing anchor pair"):
            result(notes=corrupted)

    def test_primary_references_not_inferred_from_contextual_roles(self):
        d={x["source_id"]:x for x in build_provenance()["source_level_lineage"]}
        self.assertEqual(d["UC21-SOURCE"]["primary_frozen_case_ids"],[])
        self.assertEqual(d["00M-CANON"]["primary_frozen_case_ids"],[])
        self.assertEqual(d["01K-HID"]["primary_frozen_case_ids"],[])
        self.assertTrue(all(not d[sid]["used_as_case_source"]
                            for sid in ("00M-CANON","01K-HID","UC21-SOURCE")))
        # Still required as semantic owners; this is not a denial they are
        # mentioned in project prose or used as a conceptual framework.

    def test_no_double_counting_repeated_case_reference(self):
        n=deepcopy(NARRATIVE)
        n["cases"][0]["source_refs"].append(n["cases"][0]["source_refs"][0])
        with self.assertRaisesRegex(ValueError,"repeats a source reference"):
            result(n=n)

    def test_public_campaign_retired_misleading_active_screened_field(self):
        old=read_json("REFERENCE_SYNTHETIC_RESULTS.json")
        self.assertEqual(old["source_documents_screened"],23)  # immutable history
        fresh=campaign.build_campaign(require_existing=False)
        self.assertNotIn("source_documents_screened",fresh)
        self.assertEqual(fresh["source_provenance"]["counts"]["registered_total"],23)
        text=campaign.report_summary(fresh)
        self.assertIn("fuentes registradas",text)
        self.assertIn("17 de 19",text)
        self.assertIn("23",text)
        self.assertIn("histórico",text)
        self.assertEqual(fresh["decision_experiments"],old["decision_experiments"])
        self.assertEqual(fresh["factorial_joint_mechanism"],old["factorial_joint_mechanism"])
        self.assertEqual(fresh["FH_C_competing_ablations"],old["FH_C_competing_ablations"])


if __name__ == "__main__":
    unittest.main()
