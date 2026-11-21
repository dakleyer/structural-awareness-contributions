"""Mechanism properties and adversarial cases for the reusable development kernels."""
import unittest
from fractions import Fraction as F
from itertools import product
from concurrent.futures import ThreadPoolExecutor
from threading import Barrier

from generative_development import (refine_memory, forecast, Action, best_joint_plan,
    resource_conflicts, ReservationBook, ResourceConflict, normal_posterior,
    certainty_equivalent, coordination_regimes, examples,measurement_window)


class DevelopmentTests(unittest.TestCase):
    def test_memory_synthesizes_missing_feature_witness(self):
        data=examples()['memory']
        self.assertEqual(len(data['stable_blocks']),4)
        self.assertTrue(all(w['action']==1 for w in data['witnesses']))

    def test_memory_quotient_preserves_traces_all_729_three_state_models(self):
        states=(0,1,2);actions=(0,1)
        for encoded in product(states,repeat=6):
            step=lambda s,a:encoded[2*s+a]
            result=refine_memory(states,actions,lambda s:s%2,step)
            for block in result.blocks:
                for left in block:
                    for right in block:
                        for word in product(actions,repeat=3):
                            x,y=left,right
                            for a in word:
                                self.assertEqual(x%2,y%2)
                                x,y=step(x,a),step(y,a)
                            self.assertEqual(x%2,y%2)

    def test_current_task_does_not_force_extra_memory(self):
        result=refine_memory((0,1,2,3),(),lambda s:s%2,lambda s,a:s)
        self.assertEqual(len(result.blocks),2)
        self.assertEqual(result.witnesses,())

    def test_model_must_supply_transitions_within_its_state_set(self):
        with self.assertRaises(ValueError):refine_memory((0,),(0,),lambda s:0,lambda s,a:1)

    def test_ode_error_bound_attained_at_measurement_and_curvature_extremes(self):
        for delta,T,eps,accel in product((F(1,2),F(1)),(F(2),F(3)),(F(0),F(1,20)),(F(0),F(1,5))):
            for curvature,e0,e1 in product((-accel,accel),(-eps,eps),(-eps,eps)):
                true=lambda t:F(2)+F(3)*t+curvature*t*t/2
                projection=forecast(true(0)+e0,true(delta)+e1,delta,T,eps,accel)
                self.assertLessEqual(projection.lower,true(T))
                self.assertGreaterEqual(projection.upper,true(T))

    def test_new_observation_turns_forecast_into_a_capacity_decision(self):
        d=examples()['forecast']
        self.assertEqual((d['before'].lower,d['before'].upper),(F(43,20),F(77,20)))
        self.assertEqual((d['after'].lower,d['after'].upper),(F(53,20),F(67,20)))
        self.assertEqual((d['old_decision'],d['new_decision']),('measure_again','within_capacity'))

    def test_ode_driven_measurement_window_brackets_the_error_crossing(self):
        low,high=measurement_window(1,F(1,2),F(1,20),F(1,5),4)
        self.assertLessEqual(forecast(0,0,1,low,F(1,20),F(1,5)).radius,F(1,2))
        self.assertGreater(forecast(0,0,1,high,F(1,20),F(1,5)).radius,F(1,2))
        self.assertLess(high-low,F(1,10**10))
        self.assertEqual(measurement_window(1,F(1,100),F(1,20),0,4),(None,F(1)))
        self.assertEqual(measurement_window(1,1,0,0,4),(F(4),None))

    def test_invalid_forecast_inputs_are_not_certificates(self):
        for args in [(0,1,0,2,0,0),(0,1,1,0,0,0),(0,1,1,2,float('nan'),0),(0,1,1,2,0,-1)]:
            with self.assertRaises(ValueError):forecast(*args)

    def test_joint_action_law_and_capacity_upgrade(self):
        actions=tuple(Action.make(str(i),{'root':1},1) for i in range(3))
        for capacity in range(5):
            plan=best_joint_plan(actions,{'root':capacity})
            self.assertEqual(sum(a.gain for a in plan),min(capacity,3))
            self.assertFalse(resource_conflicts(plan,{'root':capacity}))
        self.assertEqual(examples()['composition']['upgrade_net_gain'],F(4,5))

    def test_joint_planning_respects_all_resource_dimensions(self):
        a=Action.make('a',{'root':1,'specialist':1},4)
        b=Action.make('b',{'root':1,'specialist':1},3)
        c=Action.make('c',{'root':1},2)
        plan=best_joint_plan((a,b,c),{'root':2,'specialist':1})
        self.assertEqual({x.name for x in plan},{'a','c'})

    def test_atomic_reservation_does_not_double_spend_or_repeat_identity(self):
        book=ReservationBook({'root':1});barrier=Barrier(2)
        def reserve(name):
            v,_=book.snapshot();barrier.wait()
            try:book.reserve(v,(Action.make(name,{'root':1},1),));return True
            except ResourceConflict:return False
        with ThreadPoolExecutor(max_workers=2) as pool:
            result=list(pool.map(reserve,('left','right')))
        self.assertEqual(sum(result),1)
        self.assertEqual(book.snapshot(),(1,{'root':F(0)}))
        b=ReservationBook({'root':2});a=Action.make('one',{'root':1},1);b.reserve(0,(a,))
        with self.assertRaises(ResourceConflict):b.reserve(1,(a,))

    def test_action_payload_is_immutable_and_finite(self):
        source={'root':1};a=Action.make('a',source,1);source['root']=100
        self.assertEqual(a.loads['root'],1)
        with self.assertRaises(TypeError):a.loads['root']=100
        for value in (float('nan'),float('inf'),True):
            with self.assertRaises(ValueError):Action('bad',{'root':value},1)

    def test_gaussian_update_uses_observations_not_a_declared_conclusion(self):
        self.assertEqual(normal_posterior(5,4,(5,5,5),4),(F(5),F(1)))
        self.assertEqual(normal_posterior(5,4,(1,1,1),4),(F(2),F(1)))
        self.assertEqual(normal_posterior(5,4,(),4),(F(5),F(4)))

    def test_information_coordination_interaction_and_all_information_costs(self):
        d=examples()['coordination'];r=d['regimes']
        self.assertEqual([r[k]['choice'] for k in r],['stay','stay','stay','redesign'])
        self.assertEqual([r[k]['value'] for k in r],[F(4),F(39,10),F(4),F(22,5)])
        self.assertEqual(r['information_only']['information_cost_paid'],F(1,10))
        self.assertEqual(d['interaction'],F(1,2))

    def test_precision_risk_threshold_and_cost_sensitivity(self):
        for variance in (F(1,2),F(1),F(2),F(4)):
            net=certainty_equivalent(5,variance,1,F(1,10))
            self.assertEqual(net>4,variance<F(9,5))
        r=coordination_regimes(4,3,3,5,5,4,1,1,1)
        self.assertLess(r['information_and_coordination']['value'],r['neither']['value'])


if __name__=='__main__':unittest.main()
