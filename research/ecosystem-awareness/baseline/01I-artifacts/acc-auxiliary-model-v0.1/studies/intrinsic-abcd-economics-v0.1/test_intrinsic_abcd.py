"""Independent deterministic controls; no empirical claims about humans or EA."""
import unittest
from dataclasses import replace
from intrinsic_abcd import (
    Leaf, Module, Costs, ExplorationC, MaterialD, balanced_tree,
    deliver, descendants, node_count, base_demand, selected_demand,
    path_to, upstream_B, receiver_B_valid, route_status, policy,
    receiver_decision, bounded_roi_gate, communication_lower_bounds,
    sample_report, public_outline, observe_view, plan_from_public,
    score_public_plan, source_current_log,
)


class RecursiveWorldControls(unittest.TestCase):
    def setUp(self):
        self.bits = (0, 0, 1, 0, 0, 1, 0, 0)
        self.world = balanced_tree(self.bits)
        self.target = "source-2"

    def test_identity_of_current_A_across_hidden_states(self):
        a = balanced_tree((0,) * 8)
        b = balanced_tree((1,) * 8)
        self.assertEqual(deliver(a, base_demand(a)), deliver(b, base_demand(b)))

    def test_future_differs_with_same_A(self):
        a = balanced_tree((0,) * 8)
        b = balanced_tree((1,) * 8)
        self.assertEqual(deliver(a, selected_demand(a, "source-2")), 64)
        self.assertEqual(deliver(b, selected_demand(b, "source-2")), 66)

    def test_recursive_composition_is_total(self):
        self.assertEqual(deliver(self.world, base_demand(self.world)), 64)
        self.assertEqual(len(descendants(self.world)), 8)

    def test_recursion_has_multiple_layers(self):
        self.assertGreaterEqual(len(path_to(self.world, self.target)), 5)

    def test_no_pseudo_oracle_from_current_A(self):
        y1 = deliver(self.world, base_demand(self.world))
        w2 = balanced_tree((0,) * 8)
        self.assertEqual(y1, deliver(w2, base_demand(w2)))
        self.assertNotEqual(deliver(self.world, selected_demand(self.world, self.target)),
                            deliver(w2, selected_demand(w2, self.target)))

    def test_hidden_root_bottleneck_blocks_future(self):
        bottleneck = balanced_tree(self.bits, cap_root=64)
        self.assertEqual(deliver(bottleneck, base_demand(bottleneck)), 64)
        self.assertEqual(deliver(bottleneck, selected_demand(bottleneck, self.target)), 64)

    def test_source_leaf_capacity_not_sufficient_for_parent(self):
        bottleneck = balanced_tree(self.bits, cap_root=64)
        b = upstream_B(bottleneck, self.target, now=0, ttl=1)
        self.assertEqual(b.delivered_if_requested, 0)

    def test_deliver_validates_all_inputs(self):
        with self.assertRaises(ValueError): deliver(self.world, {})
        with self.assertRaises(ValueError): deliver(self.world, {"source-2":-1})

    def test_invalid_binary_world_rejected(self):
        with self.assertRaises(ValueError): balanced_tree((0, 2))
        with self.assertRaises(ValueError): balanced_tree((0,))

    def test_selected_nonexistent_target_rejected(self):
        with self.assertRaises(ValueError): selected_demand(self.world, "not-a-source")


class QualificationControls(unittest.TestCase):
    def setUp(self):
        self.world = balanced_tree((0, 1, 0, 1))
        self.target = "source-1"
        self.cert = upstream_B(self.world, self.target, now=2, ttl=4)
        self.costs = Costs()

    def test_B_generated_by_source_from_actual_characterized_path(self):
        self.assertEqual(self.cert.delivered_if_requested, 2)
        self.assertEqual(self.cert.source_evidence, "DECLARED_SOURCE_NATIVE_NOT_INDEPENDENTLY_ATTESTED")

    def test_B_exploited_after_source_qualification(self):
        o = policy(self.world, self.target, "B_QUALIFIED", self.costs, now=3,b=self.cert)
        self.assertEqual(o["promised_increment"], 2)
        self.assertGreater(o["net_realized_value_SYNTHETIC"], 0)

    def test_expired_B_cannot_justify_increment(self):
        o = policy(self.world, self.target, "B_QUALIFIED", self.costs, now=7,b=self.cert)
        self.assertEqual(o["promised_increment"], 0)
        self.assertEqual(o["status"], "STALE")

    def test_wrong_target_B_not_fungible(self):
        o = policy(self.world, "source-3", "B_QUALIFIED", self.costs, now=3,b=self.cert)
        self.assertEqual(o["status"], "WRONG_QUESTION")
        self.assertEqual(o["promised_increment"], 0)

    def test_wrong_version_rejected(self):
        c = replace(self.cert, path_versions=("v2",)+self.cert.path_versions[1:])
        self.assertFalse(receiver_B_valid(public_outline(self.world),c,self.target,now=3)[0])

    def test_missing_path_member_rejected(self):
        c=replace(self.cert,path_ids=self.cert.path_ids[1:])
        self.assertFalse(receiver_B_valid(public_outline(self.world),c,self.target,now=3)[0])

    def test_unapproved_issuer_rejected(self):
        c=replace(self.cert, source="unknown-issuer")
        self.assertFalse(receiver_B_valid(public_outline(self.world),c,self.target,now=3)[0])

    def test_invalid_increment_rejected(self):
        c=replace(self.cert, delivered_if_requested=5)
        self.assertFalse(receiver_B_valid(public_outline(self.world),c,self.target,now=3)[0])

    def test_forged_correct_format_CANNOT_be_authenticated_by_this_checker(self):
        low=balanced_tree((0,0,0,0))
        bogus=replace(self.cert,delivered_if_requested=2)
        valid,status=receiver_B_valid(public_outline(low),bogus,self.target,now=3)
        self.assertTrue(valid)
        self.assertEqual(status,"DECLARED_B_VALID_SCOPE_NOT_AUTHENTICATED")
        effect=policy(low,self.target,"B_QUALIFIED",self.costs,now=3,b=bogus)
        self.assertTrue(effect["false_promise_PRIVATE_ORACLE"])
        self.assertLess(effect["net_realized_value_SYNTHETIC"],0)

    def test_native_source_log_matches_operational_output(self):
        logs=source_current_log(self.world,base_demand(self.world))
        self.assertEqual(logs["root"],deliver(self.world,base_demand(self.world)))
        self.assertEqual(logs["source-1"],8)

    def test_B_path_capacity_matches_private_effect_under_independent_fixed_demands(self):
        # Exhaustive on 4 leaves and a range of shared global bottlenecks.
        from itertools import product
        for bits in product((0,1),repeat=4):
            for cap in (None,32,33,34,35,36,40):
                world=balanced_tree(bits,cap_root=cap)
                current=deliver(world,base_demand(world))
                for k in range(4):
                    target=f"source-{k}"
                    b=upstream_B(world,target,now=0,ttl=1)
                    effect=deliver(world,selected_demand(world,target))-current
                    self.assertEqual(b.delivered_if_requested,effect)

    def test_inaccessible_source_blocks_synthetic_B_construction(self):
        w=balanced_tree((0,1,0,0),inaccessible_path_leaf=1)
        self.assertIsNone(upstream_B(w,"source-1",now=0,ttl=1))

    def test_C_is_grounded_not_quantified(self):
        c=ExplorationC("peer","potential specialist assessment of supplier interfaces",question_target=self.target)
        self.assertIn("UNCHARACTERIZED_ROI",route_status(c))

    def test_C_requires_uncharacterized_basis(self):
        with self.assertRaises(ValueError):
            ExplorationC("peer","already fully evaluated",question_target=self.target, targets_and_method_characterized=True)

    def test_D_is_witnessed_material_no_effective_route(self):
        d=MaterialD("peer","external operational shift with no access",question_target=self.target)
        self.assertIn("NOT_ASSESSABLE",route_status(d))

    def test_D_does_not_convert_silence_to_diagnosis(self):
        self.assertEqual(route_status(None), "ROLE_NOT_ESTABLISHED")

    def test_D_cannot_relabel_assessable_known_route(self):
        with self.assertRaises(ValueError):
            MaterialD("peer","can analyze under current method",question_target=self.target,has_effective_evaluation_route=True)


class EconomicExplorationControls(unittest.TestCase):
    def setUp(self):
        self.world=balanced_tree(tuple(1 if j==3 else 0 for j in range(16)))
        self.target="source-3"
        self.cert=upstream_B(self.world,self.target,now=5,ttl=10)
        self.c=Costs()

    def test_A_only_conservative_unchanged(self):
        r=policy(self.world,self.target,"A_ONLY",self.c)
        self.assertEqual(r["promised_increment"],0)
        self.assertEqual(r["information_cost_declared"],0)

    def test_B_cheaper_than_full_under_declared_cost(self):
        b=policy(self.world,self.target,"B_QUALIFIED",self.c,now=6,b=self.cert)
        f=policy(self.world,self.target,"FULL_EXPAND_A",self.c)
        self.assertGreater(b["net_realized_value_SYNTHETIC"],f["net_realized_value_SYNTHETIC"])
        self.assertEqual(f["gross_realized_value_SYNTHETIC"],10)

    def test_full_can_be_unprofitable_for_one_query(self):
        f=policy(self.world,self.target,"FULL_EXPAND_A",self.c)
        self.assertLess(f["net_realized_value_SYNTHETIC"],0)
        self.assertTrue(bounded_roi_gate(node_count(self.world),self.c.full_node,2,5)["full_expansion_cannot_beat_conservative_A"])

    def test_full_not_always_worse_if_acquisition_cheap(self):
        small=Costs(full_node=.01,b_issuance_per_path_node=10)
        f=policy(self.world,self.target,"FULL_EXPAND_A",small)
        b=policy(self.world,self.target,"B_QUALIFIED",small,now=6,b=self.cert)
        self.assertGreater(f["net_realized_value_SYNTHETIC"],b["net_realized_value_SYNTHETIC"])

    def test_targeted_conventional_can_match_or_beat_qualification(self):
        c=Costs(target_observation=.1)
        t=policy(self.world,self.target,"TARGETED_EXPLORATION_OF_A",c)
        b=policy(self.world,self.target,"B_QUALIFIED",c,b=self.cert,now=6)
        self.assertGreater(t["net_realized_value_SYNTHETIC"],b["net_realized_value_SYNTHETIC"])

    def test_targeted_not_guaranteed_positive_on_low_capacity(self):
        low=balanced_tree((0,)*16)
        t=policy(low,"source-3","TARGETED_EXPLORATION_OF_A",self.c)
        self.assertLess(t["net_realized_value_SYNTHETIC"],0)

    def test_full_scan_prohibited_when_source_not_accessible(self):
        w=balanced_tree((1,1,1,1),inaccessible_path_leaf=1)
        f=policy(w,"source-0","FULL_EXPAND_A",self.c)
        self.assertEqual(f["status"],"FULL_SCOPE_NOT_ACCESSIBLE")

    def test_A_cannot_commit_based_on_D(self):
        d=MaterialD("peer","outside influence with no effective path",question_target=self.target)
        r=receiver_decision(self.world,self.target,self.c,budget=100,now=6,b=self.cert,d=d)
        self.assertEqual(r["promised_increment"],0)
        self.assertIn("D_MATERIAL",r["decision_rule"])

    def test_C_signpost_not_baked_in_expected_gain(self):
        c=ExplorationC("peer","potential interface inspection route",question_target=self.target)
        r=receiver_decision(self.world,self.target,self.c,budget=10,now=0,c=c)
        self.assertEqual(r["promised_increment"],0)
        self.assertIn("UNASSESSED",r["decision_rule"])

    def test_agent_is_budget_bounded(self):
        r=receiver_decision(self.world,self.target,self.c,budget=1,now=6,b=self.cert)
        self.assertEqual(r["promised_increment"],0)

    def test_agent_uses_B_if_cost_and_benefit_sufficient(self):
        r=receiver_decision(self.world,self.target,self.c,budget=4,now=6,b=self.cert)
        self.assertEqual(r["promised_increment"],2)
        self.assertEqual(r["open_residual"],"NOT_CHARACTERIZED_OUTSIDE_QUESTION")

    def test_B_low_capacity_and_cost_disallows_redundant_acquisition(self):
        low=balanced_tree((0,)*16)
        b=upstream_B(low,self.target,now=5,ttl=10)
        r=receiver_decision(low,self.target,self.c,budget=4,now=6,b=b)
        self.assertEqual(r["promised_increment"],0)
        self.assertEqual(r["decision_rule"],"B_INFO_NOT_ECONOMIC_FOR_THIS_ONE_QUESTION")

    def test_C_cannot_be_misclassified_as_B(self):
        valid, status=receiver_B_valid(public_outline(self.world),ExplorationC("peer","route",question_target=self.target),self.target,now=0)
        self.assertFalse(valid)
        self.assertEqual(status,"SOURCE_NOT_ALLOWED")

    def test_information_cost_is_nonnegative(self):
        with self.assertRaises(ValueError):Costs(full_node=-1)

    def test_roi_gate_is_scope_specific(self):
        self.assertFalse(bounded_roi_gate(2,1,2,5)["full_expansion_cannot_beat_conservative_A"])

    def test_B_full_maintenance_cost_can_defeat_B_economic_case(self):
        high=Costs(b_maintenance=30)
        p=receiver_decision(self.world,self.target,high,budget=100,now=6,b=self.cert)
        self.assertEqual(p["promised_increment"],0)
        self.assertEqual(p["decision_rule"],"B_INFO_NOT_ECONOMIC_FOR_THIS_ONE_QUESTION")

    def test_roi_bound_requires_finite_cost(self):
        with self.assertRaises(ValueError):
            bounded_roi_gate(10,float("inf"),2,5)
        with self.assertRaises(ValueError):
            bounded_roi_gate(10,float("nan"),2,5)

    def test_source_metadata_is_not_independently_authenticated(self):
        self.assertTrue(self.cert.source_evidence.endswith("NOT_INDEPENDENTLY_ATTESTED"))


class PublicAbstractionSafetyControls(unittest.TestCase):
    def setUp(self):
        self.one=balanced_tree((0,0,0,0))
        self.two=balanced_tree((0,1,0,0))
        self.target="source-1"
        self.cost=Costs()

    def test_public_observation_identical_despite_hidden_future(self):
        self.assertEqual(observe_view(self.one),observe_view(self.two))
        self.assertNotEqual(deliver(self.one,selected_demand(self.one,self.target)),
                            deliver(self.two,selected_demand(self.two,self.target)))

    def test_public_outline_has_no_capacity_or_private_access(self):
        o=public_outline(self.two)
        self.assertFalse(hasattr(o,"throughput_ceiling"))
        self.assertFalse(hasattr(o,"source_can_assess"))
        self.assertFalse(hasattr(o,"capacity"))
        member=o.children[0].children[0]
        self.assertFalse(hasattr(member,"capacity"))
        self.assertFalse(hasattr(member,"source_can_assess"))

    def test_receiver_rejects_private_world_reference(self):
        cert=upstream_B(self.two,self.target,now=1,ttl=3)
        with self.assertRaises(TypeError):
            receiver_B_valid(self.two,cert,self.target,now=2)

    def test_public_planner_same_action_without_qualifications(self):
        p1=plan_from_public(observe_view(self.one),self.target,self.cost,budget=9,now=2)
        p2=plan_from_public(observe_view(self.two),self.target,self.cost,budget=9,now=2)
        self.assertEqual(p1,p2)
        self.assertEqual(p1["promised_increment"],0)

    def test_public_planner_uses_source_B_but_not_oracle(self):
        cert=upstream_B(self.two,self.target,now=1,ttl=3)
        p=plan_from_public(observe_view(self.two),self.target,self.cost,budget=9,now=2,b=cert)
        self.assertEqual(p["promised_increment"],2)
        self.assertNotIn("physical_increment_PRIVATE_ORACLE",p)
        score=score_public_plan(self.two,p,self.cost)
        self.assertEqual(score["physical_increment_PRIVATE_ORACLE"],2)

    def test_public_source_B_for_wrong_hidden_state_does_not_prove_truth(self):
        honest=upstream_B(self.two,self.target,now=1,ttl=3)
        bad_plan=plan_from_public(observe_view(self.one),self.target,self.cost,budget=9,now=2,b=honest)
        self.assertEqual(bad_plan["promised_increment"],2)
        self.assertTrue(score_public_plan(self.one,bad_plan,self.cost)["false_promise_PRIVATE_ORACLE"])

    def test_D_for_other_question_does_not_universally_block(self):
        cert=upstream_B(self.two,self.target,now=1,ttl=3)
        d=MaterialD("partner","separate inaccessible material cause",question_target="source-3")
        p=plan_from_public(observe_view(self.two),self.target,self.cost,budget=9,now=2,b=cert,d=d)
        self.assertEqual(p["promised_increment"],2)

    def test_C_for_other_question_cannot_create_benefit(self):
        c=ExplorationC("partner","different route",question_target="source-0")
        p=plan_from_public(observe_view(self.two),self.target,self.cost,budget=9,now=2,c=c)
        self.assertEqual(p["decision_rule"],"EXPLOIT_A_WITH_OPEN_RESIDUAL")

    def test_D_is_not_right_to_veto_every_agent(self):
        d=MaterialD("partner","unevaluable relevant effect",question_target=self.target)
        p=plan_from_public(observe_view(self.two),self.target,self.cost,budget=9,now=2,d=d)
        self.assertIn("NO_HIGH_PROMISE",p["decision_rule"])
        self.assertEqual(p["promised_increment"],0)


class InformationContractControls(unittest.TestCase):
    def test_all_query_signatures_need_n_bits_in_finite_lab(self):
        for n in (1,2,4,8,16,32):
            r=communication_lower_bounds(n)
            self.assertEqual(r["all_n_binary_queries_bits_min"],n)
            self.assertEqual(r["full_vector_profiles"],2**n)

    def test_aggregate_and_selected_families_smaller(self):
        r=communication_lower_bounds(16)
        self.assertEqual(r["aggregate_count_bits_min"],5)
        self.assertEqual(r["one_selected_binary_query_bits_min"],1)
        self.assertLess(r["aggregate_count_bits_min"],r["all_n_binary_queries_bits_min"])

    def test_ceil_number_of_output_profiles(self):
        for n in range(1,15):
            d=communication_lower_bounds(n)
            self.assertEqual(d["aggregate_count_bits_min"],ceil_log2(n+1))

    def test_expected_value_not_assigned_to_C_or_D(self):
        d=sample_report()
        self.assertNotIn("probability",d["C_status"].lower())
        self.assertNotIn("expected",d["D_status"].lower())

    def test_open_residual_cannot_be_nullified_by_certificate(self):
        d=sample_report()
        self.assertEqual(d["policies"][1]["indeterminacy_of_outside"],"NOT_INVENTORIED_NOT_MEASURED")

    def test_invalid_profile_size(self):
        with self.assertRaises(ValueError):communication_lower_bounds(0)
        with self.assertRaises(ValueError):communication_lower_bounds(257)

    def test_report_has_scored_favorable_and_adverse_policies(self):
        d=sample_report()
        self.assertEqual(d["n_leaves"],16)
        self.assertEqual(d["current_A"],128)
        self.assertEqual(d["same_current_A_with_root_bottleneck"],128)
        self.assertGreater(d["policies"][1]["net_realized_value_SYNTHETIC"],0)
        self.assertLess(d["policies"][3]["net_realized_value_SYNTHETIC"],0)


def ceil_log2(n):
    return (n-1).bit_length()


if __name__ == "__main__":
    unittest.main()
