"""Deterministic positive and negative controls for local scoped closure.
All of these are finite mathematical illustrations, not observations of people.
"""
import json
import unittest

from metacognition import (
    ContractError, Point, FrontierWitness, Frame, DecisionQuestion,
    qualify, advisory, structural_exposure, cost_comparison, synthetic_report
)


def sample(**kwargs):
    d=dict(claim_id="p1",origin_id="s1",scope="x",revision="v1",observed_at=4,
           x_min=0,x_max=0,y_min=9,y_max=10,source_attested=True)
    d.update(kwargs)
    return Point(**d)


def frame(**kwargs):
    d=dict(scope="x",revision="v1",now=5,max_age=5,domain_min=0,
           domain_max=2,lipschitz=1,regularity_qualified=True)
    d.update(kwargs)
    return Frame(**d)


def q(**kwargs):
    d=dict(x=1,threshold=7); d.update(kwargs);return DecisionQuestion(**d)


def witness(kind="C",**kwargs):
    d=dict(witness_id="w1",origin_id="s2",scope="x",kind=kind,
           material_to_question=True,grounded=True,effective_evaluation_route=kind=="C")
    d.update(kwargs);return FrontierWitness(**d)


class LocalSufficiency(unittest.TestCase):
    def test_locally_true(self):
        r=qualify(frame(),q(),(sample(),))
        self.assertEqual(r["local_answer_status"],"LOCALLY_SUPPORTED_TRUE")
        self.assertEqual(r["conditional_answer_bounds"],[8,11])
    def test_locally_false(self):
        r=qualify(frame(),q(),(sample(y_min=2,y_max=3),))
        self.assertEqual(r["local_answer_status"],"LOCALLY_SUPPORTED_FALSE")
    def test_undetermined_threshold_crosses_interval(self):
        self.assertEqual(qualify(frame(),q(threshold=9),(sample(),))["local_answer_status"],"UNDETERMINED_FROM_AVAILABLE_EVIDENCE")
    def test_boundary_equal_threshold_is_true(self):
        self.assertEqual(qualify(frame(),q(threshold=8),(sample(),))["local_answer_status"],"LOCALLY_SUPPORTED_TRUE")
    def test_threshold_equal_high_is_not_false(self):
        self.assertEqual(qualify(frame(),q(threshold=11),(sample(),))["local_answer_status"],"UNDETERMINED_FROM_AVAILABLE_EVIDENCE")
    def test_scope_filter(self):
        r=qualify(frame(),q(),(sample(scope="other"),))
        self.assertEqual(r["local_answer_status"],"NO_RELEVANT_EVIDENCE")
        self.assertEqual(r["rejected_claim_ids"],["p1"])
    def test_bad_revision_filter(self):
        self.assertEqual(qualify(frame(),q(),(sample(revision="v0"),))["local_answer_status"],"NO_RELEVANT_EVIDENCE")
    def test_future_claim_rejected(self):
        self.assertEqual(qualify(frame(),q(),(sample(observed_at=6),))["local_answer_status"],"NO_RELEVANT_EVIDENCE")
    def test_stale_claim_rejected(self):
        self.assertEqual(qualify(frame(max_age=0),q(),(sample(),))["local_answer_status"],"NO_RELEVANT_EVIDENCE")
    def test_outside_scope_query_not_extrapolated(self):
        self.assertEqual(qualify(frame(),q(x=4),(sample(),))["local_answer_status"],"OUTSIDE_DECLARED_DOMAIN")
    def test_claim_beyond_declared_domain_rejected(self):
        self.assertEqual(qualify(frame(),q(),(sample(x_min=-1),))["local_answer_status"],"NO_RELEVANT_EVIDENCE")
    def test_empty_observations_not_zero(self):
        self.assertEqual(qualify(frame(),q(),())["local_answer_status"],"NO_RELEVANT_EVIDENCE")
    def test_no_regularality_assumption_does_not_interpolate(self):
        self.assertEqual(qualify(frame(regularity_qualified=False),q(),(sample(),))["local_answer_status"],"NO_JUSTIFIED_REGULARITY")
    def test_no_lipschitz_parameter_does_not_interpolate(self):
        self.assertEqual(qualify(frame(lipschitz=None),q(),(sample(),))["local_answer_status"],"NO_JUSTIFIED_REGULARITY")
    def test_untrusted_claim_rejected_not_silently_accepted(self):
        self.assertEqual(qualify(frame(),q(),(sample(source_attested=False),))["local_answer_status"],"NO_RELEVANT_EVIDENCE")
    def test_duplicate_exact_claim_does_not_count_twice(self):
        r=qualify(frame(),q(),(sample(),sample()))
        self.assertEqual(r["retained_claim_ids"],["p1"])
        self.assertEqual(r["distinct_declared_origins"],["s1"])
    def test_duplicate_id_with_different_values_is_conflict(self):
        r=qualify(frame(),q(),(sample(),sample(y_min=0,y_max=1)))
        self.assertEqual(r["local_answer_status"],"SOURCE_CONFLICT")
    def test_two_sources_known_conflict(self):
        r=qualify(frame(),q(),(sample(),sample(claim_id="p2",origin_id="s2",y_min=0,y_max=1)))
        self.assertEqual(r["local_answer_status"],"EVIDENCE_OR_ASSUMPTIONS_INCONSISTENT")
    def test_sources_with_same_origin_not_independent_corrob(self):
        r=qualify(frame(),q(),(sample(),sample(claim_id="p2",origin_id="s1")))
        self.assertEqual(r["distinct_declared_origins"],["s1"])
    def test_uncertain_coordinates_have_conservative_bounds(self):
        r=qualify(frame(),q(threshold=7),(sample(x_min=0,x_max=0.5),))
        self.assertEqual(r["conditional_answer_bounds"],[8,11])
    def test_new_compatible_evidence_can_refine(self):
        p2=sample(claim_id="p2",origin_id="s2",x_min=1,x_max=1,y_min=9,y_max=9)
        old=qualify(frame(),q(),(sample(),))["conditional_answer_bounds"]
        new=qualify(frame(),q(),(sample(),p2))["conditional_answer_bounds"]
        self.assertTrue(new[0]>=old[0] and new[1]<=old[1])
        self.assertEqual(new,[9,9])
    def test_tiny_empty_intersection_cannot_certify_truth(self):
        points=(sample(y_min=1e-13,y_max=1e-13),
                sample(claim_id="p2",origin_id="s2",y_min=0,y_max=0))
        result=qualify(frame(lipschitz=0),q(x=0,threshold=5e-14),points)
        self.assertEqual(result["local_answer_status"],"EVIDENCE_OR_ASSUMPTIONS_INCONSISTENT")

    def test_local_overlap_does_not_hide_global_source_conflict(self):
        points=(sample(y_min=0,y_max=0),
                sample(claim_id="p2",origin_id="s2",y_min=2,y_max=2))
        # Both projections at x=1 contain 1. No single f can obey both
        # values at x=0, even though their query-local intervals intersect.
        result=qualify(frame(),q(x=1,threshold=1),points)
        self.assertEqual(result["local_answer_status"],"EVIDENCE_OR_ASSUMPTIONS_INCONSISTENT")
        self.assertIsNone(result["conditional_answer_bounds"])

    def test_joint_exact_intervals_feasible(self):
        points=(sample(y_min=0,y_max=1),
                sample(claim_id="p2",origin_id="s2",x_min=1,x_max=1,y_min=1,y_max=2))
        result=qualify(frame(),q(x=0.5,threshold=0.5),points)
        self.assertEqual(result["local_answer_status"],"LOCALLY_SUPPORTED_TRUE")

    def test_uncertain_source_positions_do_not_fake_joint_certification(self):
        points=(sample(y_min=0,y_max=0),
                sample(claim_id="p2",origin_id="s2",x_min=0,x_max=2,y_min=1,y_max=1))
        result=qualify(frame(),q(x=1,threshold=0.5),points)
        self.assertEqual(result["local_answer_status"],"JOINT_CONSISTENCY_NOT_ESTABLISHED")
        review=advisory(result["local_answer_status"],owner_authorized=True,
            actor_consent="GRANTED",solidarity_elected=False,
            nonwaivable_rights_preserved=True)
        self.assertEqual(review["advisory_status"],"RETAIN_SCOPED_UNDETERMINED")

    def test_uncertain_source_positions_proven_inconsistent(self):
        points=(sample(x_min=0,x_max=0.1,y_min=0,y_max=0),
                sample(claim_id="p2",origin_id="s2",x_min=0.2,x_max=0.3,y_min=1,y_max=1))
        result=qualify(frame(),q(),points)
        self.assertEqual(result["local_answer_status"],"EVIDENCE_OR_ASSUMPTIONS_INCONSISTENT")

    def test_uncertain_source_positions_robustly_compatible(self):
        points=(sample(y_min=0,y_max=2),
                sample(claim_id="p2",origin_id="s2",x_min=0,x_max=2,y_min=1,y_max=1))
        result=qualify(frame(),q(x=1,threshold=0),points)
        self.assertNotEqual(result["local_answer_status"],"JOINT_CONSISTENCY_NOT_ESTABLISHED")

    def test_C_does_not_automatically_veto(self):
        r=qualify(frame(),q(),(sample(),),(witness("C"),))
        self.assertEqual(r["local_answer_status"],"LOCALLY_SUPPORTED_TRUE")
    def test_irrelevant_D_preserved_without_veto(self):
        r=qualify(frame(),q(),(sample(),),(witness("D",material_to_question=False),))
        self.assertEqual(r["local_answer_status"],"LOCALLY_SUPPORTED_TRUE")
    def test_material_D_blocks_global_certainty(self):
        r=qualify(frame(),q(),(sample(),),(witness("D"),))
        self.assertEqual(r["local_answer_status"],"MATERIAL_D_NOT_EVALUABLE")
        self.assertEqual(r["material_D_witnesses"],["w1"])
    def test_unknown_residual_remains_open_when_local_answer_found(self):
        self.assertEqual(qualify(frame(),q(),(sample(),))["residual_exterior"],"OPEN_NOT_ENUMERATED_OR_PROBABILIZED")
    def test_duplicate_frontier_id_rejected(self):
        with self.assertRaises(ContractError): qualify(frame(),q(),(sample(),),(witness("C"),witness("C")))
    def test_witness_wrong_scope_has_no_grant(self):
        r=qualify(frame(),q(),(sample(),),(witness("D",scope="y"),))
        self.assertEqual(r["local_answer_status"],"LOCALLY_SUPPORTED_TRUE")


class Contracts(unittest.TestCase):
    def test_point_invalid_interval(self):
        with self.assertRaises(ContractError): sample(y_min=12,y_max=11)
    def test_point_nonfinite(self):
        with self.assertRaises(ContractError): sample(x_min=float("nan"))
    def test_point_bad_time(self):
        with self.assertRaises(ContractError): sample(observed_at=-1)
    def test_frame_wrong_domain(self):
        with self.assertRaises(ContractError): frame(domain_min=4)
    def test_negative_regularality_not_accepted(self):
        with self.assertRaises(ContractError): frame(lipschitz=-1)
    def test_frame_nan_regularality_not_accepted(self):
        with self.assertRaises(ContractError): frame(lipschitz=float("nan"))
    def test_C_must_have_plausible_route(self):
        with self.assertRaises(ContractError): witness("C",effective_evaluation_route=False)
    def test_D_must_not_have_effective_route(self):
        with self.assertRaises(ContractError): witness("D",effective_evaluation_route=True)
    def test_witness_unclear_not_assigned_to_C_or_D(self):
        with self.assertRaises(ContractError): witness("UNKNOWN")
    def test_query_only_explicit_predefined_predicate(self):
        with self.assertRaises(ContractError): q(comparison="some_other")
    def test_immutable_evidence_inputs_required(self):
        with self.assertRaises(ContractError): qualify(frame(),q(),[sample()])


class MetaPolicy(unittest.TestCase):
    def decide(self,status="UNDETERMINED_FROM_AVAILABLE_EVIDENCE",**opts):
        x=dict(owner_authorized=True,actor_consent="GRANTED",solidarity_elected=False,nonwaivable_rights_preserved=True)
        x.update(opts)
        return advisory(status,**x)
    def test_positive_is_advisory_not_automatic_action(self):
        r=self.decide("LOCALLY_SUPPORTED_TRUE")
        self.assertEqual(r["advisory_status"],"QUALIFIED_POSITIVE_FOR_OWNER")
        self.assertFalse(r["automatic_action"])
        self.assertFalse(r["truth_of_unknown_effect_computed"])
    def test_unknown_remains_unknown_without_solidarity(self):
        self.assertEqual(self.decide()["advisory_status"],"RETAIN_SCOPED_UNDETERMINED")
    def test_voluntary_solidarity_under_unknown_only_review(self):
        self.assertEqual(self.decide(solidarity_elected=True)["advisory_status"],"VOLUNTARY_UNQUANTIFIED_RISK_REVIEW_ONLY")
    def test_solidarity_does_not_override_missing_consent(self):
        self.assertEqual(self.decide(solidarity_elected=True,actor_consent="UNESTABLISHED")["advisory_status"],"CONSENT_NOT_ESTABLISHED")
    def test_solidarity_does_not_override_denial(self):
        self.assertEqual(self.decide(solidarity_elected=True,actor_consent="DENIED")["advisory_status"],"NOT_ADMISSIBLE_DENIED")
    def test_solidarity_does_not_override_rights(self):
        self.assertEqual(self.decide(solidarity_elected=True,nonwaivable_rights_preserved=False)["advisory_status"],"NOT_ADMISSIBLE_RIGHTS")
    def test_solidarity_does_not_create_owner_authority(self):
        self.assertEqual(self.decide(solidarity_elected=True,owner_authorized=False)["advisory_status"],"REQUIRES_REAL_AUTHORIZATION")
    def test_solidarity_cannot_repair_conflicting_evidence(self):
        self.assertEqual(self.decide("SOURCE_CONFLICT",solidarity_elected=True)["advisory_status"],"REPAIR_INCONSISTENT_EVIDENCE")
    def test_advisory_unqualified_negative_cannot_force_general_stop(self):
        self.assertEqual(self.decide("LOCALLY_SUPPORTED_FALSE")["advisory_status"],"NEGATIVE_FOR_DECLARED_QUESTION")
    def test_bad_consent_is_rejected(self):
        with self.assertRaises(ContractError): self.decide(actor_consent="IMPLIED")
    def test_unknown_evidence_status_rejected(self):
        with self.assertRaises(ContractError): self.decide("ABSOLUTE_ORACLE")


class HumanAndEconomics(unittest.TestCase):
    def test_three_conditions_real_gap_proxy(self):
        r=structural_exposure(actual_development=4,feasible_development=6,contribution_endorsed=True,external_block=True,perspective_indeterminate=True)
        self.assertEqual(r["proxy"],2.0)
        self.assertEqual(r["subjective_suffering"],"NOT_MEASURED")
    def test_absent_external_block_no_proxy(self):
        r=structural_exposure(actual_development=4,feasible_development=6,contribution_endorsed=True,external_block=False,perspective_indeterminate=True)
        self.assertEqual(r["proxy"],0.0)
    def test_no_alternative_not_identified_not_zero(self):
        r=structural_exposure(actual_development=4,feasible_development=None,contribution_endorsed=True,external_block=True,perspective_indeterminate=True)
        self.assertEqual(r["status"],"NOT_IDENTIFIED")
    def test_new_awareness_without_resources_does_not_change_gap(self):
        kwargs=dict(actual_development=4,feasible_development=6,contribution_endorsed=True,external_block=True,perspective_indeterminate=True)
        a=structural_exposure(**kwargs,newly_recognized_gap=False)
        b=structural_exposure(**kwargs,newly_recognized_gap=True)
        self.assertEqual(a["proxy"],b["proxy"])
        self.assertNotEqual(a["new_gap_recognized"],b["new_gap_recognized"])
    def test_invalid_optimum_rejected(self):
        with self.assertRaises(ContractError): structural_exposure(actual_development=6,feasible_development=4,contribution_endorsed=True,external_block=True,perspective_indeterminate=True)
    def test_cost_profile_favorable_for_B_conditionally(self):
        d=cost_comparison(benefit_if_correct=10,cost_b=2.25,cost_target=3,cost_full=32)
        self.assertEqual(d["net_if_correct"],{"B":7.75,"targeted_conventional":7,"full_reconstruction":-22})
    def test_conventional_peer_can_win(self):
        d=cost_comparison(benefit_if_correct=10,cost_b=6,cost_target=1,cost_full=32)
        self.assertGreater(d["net_if_correct"]["targeted_conventional"],d["net_if_correct"]["B"])
    def test_B_can_be_loss_making(self):
        d=cost_comparison(benefit_if_correct=10,cost_b=13,cost_target=11,cost_full=32)
        self.assertLess(d["net_if_correct"]["B"],0)
    def test_inaccessible_full_expansion_not_computed(self):
        d=cost_comparison(benefit_if_correct=10,cost_b=2,cost_target=3,cost_full=32,full_information_accessible=False)
        self.assertIsNone(d["net_if_correct"]["full_reconstruction"])
    def test_reject_negative_costs(self):
        with self.assertRaises(ContractError): cost_comparison(benefit_if_correct=10,cost_b=-1,cost_target=3,cost_full=5)
    def test_synthetic_report_reproducible(self):
        d=synthetic_report()
        self.assertEqual(d["study"],"FINITE_LOCAL_SUFFICIENCY_NOT_OPEN_WORLD_CLOSURE")
        self.assertEqual(d["material_D"],"MATERIAL_D_NOT_EVALUABLE")
        json.dumps(d,sort_keys=True)

if __name__=="__main__":
    unittest.main()
