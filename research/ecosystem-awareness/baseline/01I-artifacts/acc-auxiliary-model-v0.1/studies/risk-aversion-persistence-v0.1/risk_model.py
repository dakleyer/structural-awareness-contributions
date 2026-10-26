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


def declared_examples() -> dict:
    """Exactly one numeric family of cases; no calibrated population statements."""
    gamma = 0.5
    early = RiskChoice(RiskOutcome(10.0, 4.0), RiskOutcome(16.0, 36.0), gamma)
    late = RiskChoice(RiskOutcome(14.0, 4.0), RiskOutcome(25.0, 64.0), gamma)
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
