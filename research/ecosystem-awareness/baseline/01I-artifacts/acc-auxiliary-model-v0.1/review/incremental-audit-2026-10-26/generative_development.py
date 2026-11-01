"""Reusable reference kernels: memory refinement, ODE forecast, joint resources, risk coordination.

Python standard library; exact rational arithmetic; importing performs no I/O.
Run this module for four worked examples as JSON. No deployment state is modified.
"""
from __future__ import annotations

from dataclasses import dataclass
from collections import deque
from fractions import Fraction
from itertools import combinations
from threading import Lock
from types import MappingProxyType
from typing import Callable, Hashable, Mapping, Sequence
import json


def rational(value) -> Fraction:
    """Exact input value; decimal strings retain decimal intent, finite floats their encoded value."""
    if isinstance(value, bool):
        raise ValueError('a boolean is not a quantity')
    try:
        return Fraction(value)
    except (ValueError, TypeError, OverflowError, ZeroDivisionError) as exc:
        raise ValueError('a finite rational quantity is required') from exc


@dataclass(frozen=True)
class MemoryRefinement:
    blocks: tuple[tuple[Hashable, ...], ...]
    witnesses: tuple[dict, ...]

    def class_of(self, state: Hashable) -> int:
        for i, block in enumerate(self.blocks):
            if state in block:
                return i
        raise KeyError(state)


def distinguishing_word(left, right, actions, output, step):
    """Shortest finite action word that gives different outputs, or None."""
    todo=deque([(left,right,())]);seen=set()
    while todo:
        x,y,word=todo.popleft()
        if (x,y) in seen:continue
        seen.add((x,y))
        if output(x)!=output(y):return word
        todo.extend((step(x,a),step(y,a),word+(a,)) for a in actions)
    return None


def refine_memory(states: Sequence[Hashable], actions: Sequence[Hashable],
                  output: Callable[[Hashable], Hashable],
                  step: Callable[[Hashable, Hashable], Hashable]) -> MemoryRefinement:
    """Coarsest output-respecting stable partition of a finite deterministic transition model.

    The supplied transition model is total and closed on states. Each witness
    identifies an action whose next output-class requires a finer memory.
    """
    states, actions = tuple(states), tuple(actions)
    if not states or len(set(states)) != len(states) or len(set(actions)) != len(actions):
        raise ValueError('states are nonempty and state/action identities are unique')
    outputs = {s: output(s) for s in states}
    next_state = {(s, a): step(s, a) for s in states for a in actions}
    if any(t not in outputs for t in next_state.values()):
        raise ValueError('transition leaves the supplied finite model')
    grouped = {}
    for s in states:
        grouped.setdefault(outputs[s], []).append(s)
    blocks = tuple(tuple(g) for g in grouped.values())
    witnesses = []
    iteration = 0
    while True:
        index = {s: i for i, block in enumerate(blocks) for s in block}
        refined = []
        for block in blocks:
            groups = {}
            for s in block:
                signature = tuple(index[next_state[s, a]] for a in actions)
                groups.setdefault(signature, []).append(s)
            values = list(groups.values())
            for other in values[1:]:
                left, right = values[0][0], other[0]
                action = next(a for a in actions
                              if index[next_state[left, a]] != index[next_state[right, a]])
                witnesses.append({'left': left, 'right': right, 'action': action,
                                  'witness_word':distinguishing_word(left,right,actions,outputs.__getitem__,
                                                                   lambda s,a:next_state[s,a]),
                                  'reason': 'next memory classes differ', 'iteration': iteration})
            refined.extend(tuple(g) for g in values)
        refined = tuple(refined)
        if refined == blocks:
            return MemoryRefinement(blocks, tuple(witnesses))
        blocks = refined
        iteration += 1


@dataclass(frozen=True)
class Forecast:
    center: Fraction
    noise_radius: Fraction
    curvature_radius: Fraction

    @property
    def radius(self):
        return self.noise_radius + self.curvature_radius

    @property
    def lower(self):
        return self.center - self.radius

    @property
    def upper(self):
        return self.center + self.radius

    def capacity_decision(self, capacity) -> str:
        capacity = rational(capacity)
        if self.upper <= capacity:
            return 'within_capacity'
        if self.lower > capacity:
            return 'exceeds_capacity'
        return 'measure_again'


def forecast(y0, y1, delta, horizon, measurement_error=0, acceleration_bound=0) -> Forecast:
    """Forecast x(T) from observations at 0 and delta, T>=delta>0.

    Inputs specify |measurement error|<=eps and |x''(t)|<=a on [0,T].
    Returned radii follow exact secant-noise and interpolation-remainder bounds.
    """
    y0, y1, delta, horizon, eps, accel = map(rational,
        (y0, y1, delta, horizon, measurement_error, acceleration_bound))
    if not delta > 0 or horizon < delta or min(eps, accel) < 0:
        raise ValueError('require T>=delta>0 and nonnegative error bounds')
    ratio = horizon / delta
    return Forecast(y0 + ratio * (y1-y0), eps*(2*ratio-1),
                    accel*horizon*(horizon-delta)/2)


def measurement_window(delta, error_budget, measurement_error, acceleration_bound,
                       max_horizon, steps=40):
    """Bracket the first forecast-error-budget crossing using exact rational bisection.

    Return (safe_until, breach_by). None in the first position means refresh
    immediately; None in the second means no crossing before max_horizon.
    Time is measured from the older of the two observations.
    """
    delta,budget,eps,accel,maximum=map(rational,
        (delta,error_budget,measurement_error,acceleration_bound,max_horizon))
    if type(steps) is not int or steps<1 or budget<0 or maximum<delta:
        raise ValueError('positive steps, nonnegative budget and max_horizon>=delta required')
    radius=lambda t:forecast(0,0,delta,t,eps,accel).radius
    if radius(delta)>budget:return None,delta
    if radius(maximum)<=budget:return maximum,None
    low,high=delta,maximum
    for _ in range(steps):
        middle=(low+high)/2
        if radius(middle)<=budget:low=middle
        else:high=middle
    return low,high


@dataclass(frozen=True)
class Action:
    name: str
    loads: Mapping[str, Fraction]
    gain: Fraction

    def __post_init__(self):
        if not isinstance(self.name,str) or not self.name:
            raise ValueError('a nonempty action identity is required')
        if any(not isinstance(r,str) or not r for r in self.loads):
            raise ValueError('nonempty resource identities are required')
        loads = {r:rational(v) for r,v in self.loads.items()}
        if any(v < 0 for v in loads.values()):
            raise ValueError('loads are nonnegative')
        object.__setattr__(self,'loads',MappingProxyType(loads))
        object.__setattr__(self,'gain',rational(self.gain))

    @classmethod
    def make(cls, name, loads, gain):
        loads = {r: rational(v) for r, v in loads.items()}
        if any(v < 0 for v in loads.values()):
            raise ValueError('loads are nonnegative resource consumption')
        return cls(name, loads, rational(gain))


def used_resources(actions: Sequence[Action]) -> dict[str, Fraction]:
    used = {}
    if len({a.name for a in actions}) != len(actions):
        raise ValueError('each action identity occurs once')
    for a in actions:
        for resource, amount in a.loads.items():
            if amount < 0:
                raise ValueError('negative load')
            used[resource] = used.get(resource, Fraction(0)) + amount
    return used


def resource_conflicts(actions: Sequence[Action], capacities: Mapping) -> dict:
    capacities = {r: rational(v) for r, v in capacities.items()}
    if any(v < 0 for v in capacities.values()):
        raise ValueError('negative capacity')
    used = used_resources(actions)
    missing = set(used) - set(capacities)
    if missing:
        raise ValueError('resource capacity missing: '+','.join(sorted(missing)))
    return {r: {'requested': value, 'remaining': capacities[r]}
            for r, value in used.items() if value > capacities[r]}


def best_joint_plan(actions: Sequence[Action], capacities: Mapping) -> tuple[Action, ...]:
    """Exact finite reference optimizer; callers provide gains in one declared task unit.

    All subsets are explored; an ILP backend may replace this small-model solver
    behind the same resource certificate interface.
    """
    actions = tuple(actions)
    capacities = {r:rational(v) for r,v in capacities.items()}
    resource_conflicts(actions, capacities)  # validate identities, units and resources
    best = ()
    best_score = (Fraction(0), 0)
    for n in range(1, len(actions)+1):
        for chosen in combinations(actions, n):
            if not resource_conflicts(chosen, capacities):
                score = (sum((a.gain for a in chosen), Fraction(0)), -n)
                if score > best_score:
                    best, best_score = chosen, score
    return tuple(best)


class ResourceConflict(ValueError):
    pass


class ReservationBook:
    """Atomic reservations in one process, indexed by a monotone capacity version."""
    def __init__(self, capacities: Mapping):
        resource_conflicts((), capacities)
        self._remaining = {r: rational(v) for r, v in capacities.items()}
        self._version = 0
        self._reserved = set()
        self._lock = Lock()

    def snapshot(self):
        with self._lock:
            return self._version, dict(self._remaining)

    def reserve(self, expected_version: int, actions: Sequence[Action]):
        actions=tuple(actions)
        with self._lock:
            if expected_version != self._version:
                raise ResourceConflict('capacity version advanced; read current resources')
            if any(a.name in self._reserved for a in actions):
                raise ResourceConflict('action identity already reserved')
            conflicts = resource_conflicts(actions, self._remaining)
            if conflicts:
                raise ResourceConflict(str(conflicts))
            for resource, amount in used_resources(actions).items():
                self._remaining[resource] -= amount
            self._reserved.update(a.name for a in actions)
            self._version += 1
            return self._version, dict(self._remaining)


def normal_posterior(prior_mean, prior_variance, observations, noise_variance):
    """Normal location model, independent normal measurement errors of common variance."""
    mu, prior, noise = map(rational, (prior_mean, prior_variance, noise_variance))
    observations = tuple(map(rational, observations))
    if min(prior, noise) <= 0:
        raise ValueError('prior and observation variances are positive')
    variance = 1/(1/prior + len(observations)/noise)
    mean = variance*(mu/prior + sum(observations, Fraction(0))/noise)
    return mean, variance


def certainty_equivalent(mean, variance, risk_aversion=1, cost=0):
    mean, variance, gamma, cost = map(rational, (mean, variance, risk_aversion, cost))
    if min(variance, gamma, cost) < 0:
        raise ValueError('variance, risk aversion and cost are nonnegative')
    return mean-gamma*variance/2-cost


def coordination_regimes(stay, prior_solo_mean, posterior_solo_mean, prior_joint_mean, posterior_joint_mean,
                         prior_variance, posterior_variance, risk_aversion=1, information_cost=0):
    """Unilateral best-response from (stay,stay), or all-or-none joint offer.

    In the unilateral regimes, solo means refer to the result when the other stays.
    Stay has the given certain payoff. The offer executes only on joint assent.
    """
    stay = rational(stay)
    values = {
        'neither': certainty_equivalent(prior_solo_mean, prior_variance, risk_aversion),
        'information_only': certainty_equivalent(posterior_solo_mean, posterior_variance, risk_aversion),
        'coordination_only': certainty_equivalent(prior_joint_mean, prior_variance, risk_aversion),
        'information_and_coordination': certainty_equivalent(posterior_joint_mean, posterior_variance, risk_aversion),
    }
    result={}
    for name,ce in values.items():
        paid=rational(information_cost) if name in ('information_only','information_and_coordination') else Fraction(0)
        if paid<0:raise ValueError('information cost is nonnegative')
        result[name]={'redesign_ce':ce-paid,'stay_ce':stay-paid,'information_cost_paid':paid,
                     'choice':'redesign' if ce>stay else 'stay','value':max(ce,stay)-paid}
    return result


def examples():
    states = ('00','01','10','11')
    def step(s,a):
        x,z = map(int,s)
        return str(x ^ (a*z))+str(z)
    memory = refine_memory(states,(0,1),lambda s:s[0],step)
    before = forecast(0,1,1,3,'0.05','0.2')
    after = forecast(1,2,1,2,'0.05','0.2')
    a = Action.make('left',{'root':1},1)
    b = Action.make('right',{'root':1},1)
    first = best_joint_plan((a,b),{'root':1}); upgraded=best_joint_plan((a,b),{'root':2})
    mu,variance = normal_posterior(5,4,(5,5,5),4)
    regimes = coordination_regimes(4,3,mu-2,5,mu,4,variance,1,'0.1')
    return {
        'memory': {'initial_blocks':2,'stable_blocks':memory.blocks,'witnesses':memory.witnesses},
        'forecast': {'before':before,'after':after,'capacity':'3.5',
                     'half_unit_error_budget_window':measurement_window(1,'0.5','0.05','0.2',4),
                     'old_decision':before.capacity_decision('3.5'),
                     'new_decision':after.capacity_decision('3.5')},
        'composition': {'individual_gains':[a.gain,b.gain],
                        'joint_conflict':resource_conflicts((a,b),{'root':1}),
                        'plan':[x.name for x in first],'upgrade_plan':[x.name for x in upgraded],
                        'upgrade_net_gain':sum(x.gain for x in upgraded)-sum(x.gain for x in first)-rational('0.2')},
        'coordination': {'posterior_mean':mu,'posterior_variance':variance,'regimes':regimes,
                         'interaction':regimes['information_and_coordination']['value']-
                          regimes['information_only']['value']-regimes['coordination_only']['value']+
                          regimes['neither']['value']},
    }


def json_value(value):
    if isinstance(value,Fraction):
        return str(value)
    if isinstance(value,Forecast):
        return {k:json_value(getattr(value,k)) for k in
                ('center','noise_radius','curvature_radius','lower','upper')}
    raise TypeError(type(value).__name__)


if __name__ == '__main__':
    print(json.dumps(examples(),default=json_value,ensure_ascii=False,indent=2))
