"""RAV-01: bounded ex-ante decision under risk in the ACC social model.

Only characterized lotteries within a declared finite scenario. No probability
is assigned to open B/C/D exteriors, no human suffering or HID is measured,
and no rights, governance or transition feasibility can be inferred from CE.
"""
from __future__ import annotations

from dataclasses import dataclass
import json
import math


def _finite_number(value: float, label: str, *, minimum: float | None = None) -> None:
    if isinstance(value, bool) or not isinstance(value, (float, int)) or not math.isfinite(value):
        raise ValueError(f"{label} must be a finite number")
    if minimum is not None and value < minimum:
        raise ValueError(f"{label} must be >= {minimum}")


@dataclass(frozen=True)
class RiskOutcome:
    """One declared normal net-outcome lottery, same actor/unit/horizon as its peer."""

    mean: float
    variance: float

    def __post_init__(self) -> None:
        _finite_number(self.mean, "mean")
        _finite_number(self.variance, "variance", minimum=0.0)


@dataclass(frozen=True)
class RiskChoice:
    """S=stay and R=redesign; C is outside both outcome means."""

    stay: RiskOutcome
    redesign: RiskOutcome
    gamma: float
    transition_cost: float = 0.0
    choice_sensitivity: float = 1.0

    def __post_init__(self) -> None:
        if not isinstance(self.stay, RiskOutcome) or not isinstance(self.redesign, RiskOutcome):
            raise ValueError("two explicit RiskOutcome lotteries are required")
        _finite_number(self.gamma, "gamma", minimum=0.0)
        _finite_number(self.transition_cost, "transition_cost", minimum=0.0)
        _finite_number(self.choice_sensitivity, "choice_sensitivity")
        if self.choice_sensitivity <= 0:
            raise ValueError("choice_sensitivity must be > 0")


@dataclass(frozen=True)
class DefencePolicy:
    """D=active defense of S, with its own auditable outcome and real private cost.

    defended_stay and RiskChoice.stay must use the same actor, numeraire and
    horizon. A separate defense cost must not already be in defended_stay.mean.
    This represents risk-reducing action, not proof that ideological defense
    benefits society or respects third-party rights.
    """

    defended_stay: RiskOutcome
    effort_cost: float

    def __post_init__(self) -> None:
        if not isinstance(self.defended_stay, RiskOutcome):
            raise ValueError("defended_stay must be a RiskOutcome")
        _finite_number(self.effort_cost, "effort_cost", minimum=0.0)


def foregone_utility_gap(
    actual: float, feasible_reference: float | None, *, justified_reference: bool
) -> float | None:
    """Economic counterfactual shortfall for ONE actor on a common utility scale.

    Caller must have independently verified a comparable, jointly feasible,
    rights-respecting reference. Unknown reference -> None (NOT zero).
    This is not an observation of distress F or the structural suffering S_struct
    defined by the other ACC study, and is not a social aggregate.
    """
    _finite_number(actual, "actual utility")
    if not isinstance(justified_reference, bool):
        raise ValueError("justified_reference must be boolean")
    if not justified_reference:
        return None
    if feasible_reference is None:
        raise ValueError("identified feasible reference required when justified")
    _finite_number(feasible_reference, "feasible reference utility")
    return max(0.0, feasible_reference - actual)


@dataclass(frozen=True)
class WelfareSnapshot:
    """Synthetic independent F input, NOT inferred from a structural gap G."""

    gross_benefit_excluding_discomfort: float
    stipulated_discomfort: float

    def __post_init__(self) -> None:
        _finite_number(self.gross_benefit_excluding_discomfort, "gross_benefit_excluding_discomfort")
        _finite_number(self.stipulated_discomfort, "stipulated_discomfort", minimum=0.0)

    @property
    def net_welfare(self) -> float:
        return self.gross_benefit_excluding_discomfort - self.stipulated_discomfort


def certainty_equivalent(outcome: RiskOutcome, gamma: float) -> float:
    """Exact for exponential CARA utility and a normal outcome only."""
    _finite_number(gamma, "gamma", minimum=0.0)
    ce = outcome.mean - 0.5 * gamma * outcome.variance
    if not math.isfinite(ce):
        raise ValueError("equivalent certainty overflow")
    return ce


def mean_advantage(choice: RiskChoice) -> float:
    """Difference in expected outcome before separately declared transition cost."""
    return choice.redesign.mean - choice.stay.mean


def relative_risk_premium(choice: RiskChoice) -> float:
    """Can be negative if redesign is less variable than remaining."""
    return 0.5 * choice.gamma * (choice.redesign.variance - choice.stay.variance)


def change_advantage_ce(choice: RiskChoice) -> float:
    """CE(R) - CE(S) - C; do not count C again inside means."""
    value = (
        certainty_equivalent(choice.redesign, choice.gamma)
        - certainty_equivalent(choice.stay, choice.gamma)
        - choice.transition_cost
    )
    if not math.isfinite(value):
        raise ValueError("CE difference overflow")
    return value


def preferred_course(choice: RiskChoice, *, tolerance: float = 1e-10) -> str:
    _finite_number(tolerance, "tolerance", minimum=0.0)
    delta = change_advantage_ce(choice)
    if delta > tolerance:
        return "REDESIGN"
    if delta < -tolerance:
        return "STAY"
    return "TIE"


def exit_probability(choice: RiskChoice) -> float:
    """Optional conditional logit with independent EV1 choice noise; not success rate."""
    z = choice.choice_sensitivity * change_advantage_ce(choice)
    if math.isnan(z):
        raise ValueError("invalid logit argument")
    if z >= 0:
        return 1.0 / (1.0 + math.exp(-z))
    ez = math.exp(z)
    return ez / (1.0 + ez)


def defense_advantage_over_stay(choice: RiskChoice, defense: DefencePolicy) -> float:
    """CE(D)-CE(S); only with a *real* improvement to the actor's distribution."""
    return (
        certainty_equivalent(defense.defended_stay, choice.gamma)
        - defense.effort_cost
        - certainty_equivalent(choice.stay, choice.gamma)
    )


def policy_certainty_equivalents(
    choice: RiskChoice, defense: DefencePolicy
) -> dict[str, float]:
    """Comparable CE values for the three mutually exclusive actions."""
    values = {
        "STAY": certainty_equivalent(choice.stay, choice.gamma),
        "REDESIGN": certainty_equivalent(choice.redesign, choice.gamma) - choice.transition_cost,
        "DEFEND_STAY": certainty_equivalent(defense.defended_stay, choice.gamma) - defense.effort_cost,
    }
    if not all(math.isfinite(value) for value in values.values()):
        raise ValueError("non-finite adjusted certainty equivalent")
    return values


def preferred_with_defense(
    choice: RiskChoice, defense: DefencePolicy, *, tolerance: float = 1e-10
) -> str:
    """Choose one of S, R, D or TIE; no empirical behavioral identification."""
    _finite_number(tolerance, "tolerance", minimum=0.0)
    values = policy_certainty_equivalents(choice, defense)
    best = max(values.values())
    winners = [name for name, value in values.items() if best - value <= tolerance]
    return winners[0] if len(winners) == 1 else "TIE"


def three_way_choice_probabilities(
    choice: RiskChoice, defense: DefencePolicy
) -> dict[str, float]:
    """Optional EV1 softmax for choice among S, R and D, NOT success odds."""
    values = policy_certainty_equivalents(choice, defense)
    scaled = {name: choice.choice_sensitivity * value for name, value in values.items()}
    if not all(math.isfinite(value) for value in scaled.values()):
        raise ValueError("non-finite logit score")
    largest = max(scaled.values())
    weights = {name: math.exp(value - largest) for name, value in scaled.items()}
    total = sum(weights.values())
    return {name: weight / total for name, weight in weights.items()}


def declared_examples() -> dict:
    """Exactly one numeric family of cases; no calibrated population statements."""
    gamma = 0.5
    early = RiskChoice(RiskOutcome(10.0, 4.0), RiskOutcome(16.0, 36.0), gamma)
    late = RiskChoice(RiskOutcome(14.0, 4.0), RiskOutcome(25.0, 64.0), gamma)
    defense = DefencePolicy(RiskOutcome(14.0, 1.0), effort_cost=0.5)
    welfare = [
        WelfareSnapshot(12.0, 2.0),
        WelfareSnapshot(20.0, 6.0),
        WelfareSnapshot(30.0, 13.0),
    ]

    def read(choice: RiskChoice) -> dict:
        return {
            "stay_ce": certainty_equivalent(choice.stay, choice.gamma),
            "redesign_ce_after_cost": certainty_equivalent(choice.redesign, choice.gamma) - choice.transition_cost,
            "mean_gain_redesign": mean_advantage(choice),
            "excess_variance_redesign": choice.redesign.variance - choice.stay.variance,
            "excess_risk_premium": relative_risk_premium(choice),
            "ce_gain_redesign": change_advantage_ce(choice),
            "preferred": preferred_course(choice),
            "exit_probability_postulated_logit": round(exit_probability(choice), 6),
        }

    return {
        "status": "SYNTHETIC_CONDITIONAL_NOT_EMPIRICAL",
        "scope": "NORMAL_CARA_FINITE_LOTTERIES_ONLY_NO_ABCD_EXTERIOR_PROBABILITIES",
        "fixed_gamma": gamma,
        "early": read(early),
        "late": read(late),
        "late_with_active_defense": {
            "stay_ce": certainty_equivalent(late.stay, gamma),
            "redesign_ce": certainty_equivalent(late.redesign, gamma) - late.transition_cost,
            "defend_stay_ce_after_effort": certainty_equivalent(defense.defended_stay, gamma) - defense.effort_cost,
            "defense_net_ce_advantage_over_passive_stay": defense_advantage_over_stay(late, defense),
            "preferred": preferred_with_defense(late, defense),
            "three_way_choice_probabilities_postulated_logit": {
                k: round(v, 6) for k, v in three_way_choice_probabilities(late, defense).items()
            },
        },
        "matched_feasible_reference_example": {
            "actual_utility": 17.0,
            "verified_feasible_reference_utility": 21.0,
            "economic_foregone_utility": foregone_utility_gap(17.0, 21.0, justified_reference=True),
            "empirical_feasibility": "STIPULATED_FOR_TOY_ONLY",
            "subjective_distress": "NOT_IDENTIFIED",
            "structural_suffering": "NOT_IDENTIFIED",
        },
        "stipulated_welfare_trajectory": [
            {"gross_benefit_excluding_discomfort": w.gross_benefit_excluding_discomfort,
             "stipulated_discomfort": w.stipulated_discomfort, "net_welfare": w.net_welfare}
            for w in welfare
        ],
        "late_current_net_welfare": welfare[-1].net_welfare,
        "late_stay_future_expected_outcome": late.stay.mean,
        "late_stay_future_forecast_below_current": late.stay.mean < welfare[-1].net_welfare,
        "outside_probabilities": "NOT_IDENTIFIED",
        "observed_human_suffering": "NOT_MEASURED",
    }


if __name__ == "__main__":
    print(json.dumps(declared_examples(), indent=2, sort_keys=True, ensure_ascii=False))
