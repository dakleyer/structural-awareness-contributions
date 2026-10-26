"""Companion calculations for INCREMENTAL_SCIENTIFIC_AUDIT_2026-10-26.md.

Self-contained, standard library only. It does NOT import the audited studies:
it re-implements the minimal arithmetic needed to check the audit's claims
independently, so a reviewer can see each number derived in a few lines.

    python -B audit_companion.py              # print results as JSON
    python -B audit_companion.py --write      # also regenerate COMPANION_RESULTS.json and figures/

Every function names the finding it supports (F-xx, G-xx, H-xx).
"""
from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
ACC = HERE.parents[1]
CASE_REGISTRY = ACC / "studies" / "conscientia-campaign-v0.1" / "CASE_REGISTRY.json"

# ---------------------------------------------------------------------------
# F-01, F-03, F-04 — minimal re-implementation of the PR #57 decision rule
# (AGR/agentic_reduction.py at fb79df2: plan_public, source_proposed_near_gain,
#  physical_response). Base values from AGR/make_cases.py.
# ---------------------------------------------------------------------------
BASE = dict(donor=6, recipient=4, donor_rate=1.0, donor_min=2, t_max=4, upper=2.5)


def near_gain(overhead: float, lower_rate: float, ceiling: int) -> tuple[float, int]:
    """Conditional lower-bound gain and amount, as in source_proposed_near_gain."""
    cap = int(min(BASE["t_max"], BASE["donor"] - BASE["donor_min"], ceiling))
    candidates = []
    for k in range(1, cap + 1):
        net = k - overhead
        if net <= 0:
            continue
        candidates.append((round(net * lower_rate - k * BASE["donor_rate"], 6), k))
    if not candidates:
        return 0.0, 0
    gain, k = max(candidates)
    return max(0.0, gain), k


def arm_net_value(overhead: float, true_rate: float, lower_rate: float, ceiling: int, cost: float) -> float:
    """Net synthetic value of an informed arm: it pays `cost` whether or not it acts."""
    near, k = near_gain(overhead, lower_rate, ceiling)
    transfer = k if (near > 0 and near > cost) else 0
    if transfer:
        output = (BASE["donor"] - transfer) * BASE["donor_rate"] + BASE["recipient"] + (transfer - overhead) * true_rate
    else:
        output = BASE["donor"] * BASE["donor_rate"] + BASE["recipient"]
    return round(round(output, 4) - cost, 4)


def ag01() -> dict:
    """F-04: AG01 with default values (overhead 0.25, true rate 2.0)."""
    o, r = 0.25, 2.0
    return {
        "A_ONLY": 10.0,
        "Q_META_PROTOCOL": arm_net_value(o, r, lower_rate=1.6, ceiling=2, cost=0.3),
        "CONVENTIONAL_EQUIVALENT_Q": arm_net_value(o, r, lower_rate=1.6, ceiling=2, cost=0.3),
        "CONVENTIONAL_DIRECTED": arm_net_value(o, r, lower_rate=2.0, ceiling=4, cost=1.2),
        "technical_optimum_output": (BASE["donor"] - 4) + BASE["recipient"] + (4 - o) * r,
    }


def sweep(include_equivalent_at_same_price: bool = False) -> dict:
    """F-03: the 160-cell grid of AGR/sensitivity.py, winners per cell."""
    cells = []
    for true_rate in (0.6, 2.0):
        for overhead in (0.1, 0.25, 0.5, 0.75, 1.5):
            for q_cost in (0.05, 0.3, 0.8, 1.5):
                for peer_cost in (0.1, 1.0, 3.0, 5.0):
                    lower = 1.6 if true_rate == 2.0 else 0.5
                    gains = {
                        "A_ONLY": 0.0,
                        "Q_META_PROTOCOL": round(arm_net_value(overhead, true_rate, lower, 2, q_cost) - 10, 4),
                        "CONVENTIONAL_DIRECTED": round(arm_net_value(overhead, true_rate, true_rate, 4, peer_cost) - 10, 4),
                    }
                    if include_equivalent_at_same_price:
                        gains["CONVENTIONAL_EQUIVALENT_Q"] = round(arm_net_value(overhead, true_rate, lower, 2, q_cost) - 10, 4)
                    best = max(gains.values())
                    cells.append({"true_rate": true_rate, "overhead": overhead, "q_cost": q_cost,
                                  "peer_cost": peer_cost, "winners": sorted(k for k, v in gains.items() if v == best)})
    exclusive = Counter(c["winners"][0] for c in cells if len(c["winners"]) == 1)
    by_half = {str(r): Counter(c["winners"][0] if len(c["winners"]) == 1 else "TIE"
                               for c in cells if c["true_rate"] == r) for r in (0.6, 2.0)}
    q_wins = [c for c in cells if c["winners"] == ["Q_META_PROTOCOL"]]
    return {"cells": len(cells), "exclusive_winners": dict(exclusive),
            "by_true_rate": {k: dict(v) for k, v in by_half.items()},
            "q_meta_exclusive_wins_peer_costs": sorted({c["peer_cost"] for c in q_wins}),
            "q_meta_exclusive_wins": len(q_wins), "grid": cells}


# ---------------------------------------------------------------------------
# G-01, G-02 — structure of the 60-case registry (PR #48/#49)
# ---------------------------------------------------------------------------
def registry_structure() -> dict:
    cases = json.loads(CASE_REGISTRY.read_text(encoding="utf-8"))["cases"]
    adjudicable = [c for c in cases if c["truth_private_for_scoring"] != "NOT_ADJUDICABLE"]
    peer_oracle = sum(c["peer"]["has_direct_evidence"] and c["peer"]["verdict"] == c["truth_private_for_scoring"]
                      for c in adjudicable)
    full_avail = [c for c in adjudicable if c["expanded_A"]["available"]]
    full_oracle = sum(c["expanded_A"]["verdict"] == c["truth_private_for_scoring"] for c in full_avail)
    false_q = [c for c in cases if c["variant"] == "FALSE_Q"]
    return {"cases": len(cases), "adjudicable": len(adjudicable),
            "peer_verdict_equals_truth": peer_oracle,
            "expanded_A_available": len(full_avail), "expanded_A_verdict_equals_truth": full_oracle,
            "false_q_cases": len(false_q),
            "false_q_with_independent_audit_flag": sum(c["Q"]["independent_audit"] for c in false_q),
            "distinct_utility_tables": len({json.dumps(c["utility"], sort_keys=True) for c in cases}),
            "peer_costs": sorted({c["peer"]["cost"] for c in cases}),
            "q_costs": sorted({c["Q"]["cost"] for c in cases})}


# ---------------------------------------------------------------------------
# H-01 — what a *rational* suboptimum needs: a stag-hunt game form
# ---------------------------------------------------------------------------
def stag_hunt(joint=5.0, safe=4.0, sucker=0.0) -> dict:
    """Two players, action 1 = joint project, 0 = status quo.

    payoff(1,1)=joint, payoff(0,*)=safe, payoff(1,0)=sucker. Unilateral
    deviation is FEASIBLE, unlike the coupled feasibility trap of PR #42.
    """
    pay = {(1, 1): (joint, joint), (0, 0): (safe, safe), (1, 0): (sucker, safe), (0, 1): (safe, sucker)}

    def is_nash(a, b):
        return pay[(a, b)][0] >= pay[(1 - a, b)][0] and pay[(a, b)][1] >= pay[(a, 1 - b)][1]

    nash = [s for s in pay if is_nash(*s)]
    # Harsanyi-Selten risk dominance for 2x2 symmetric coordination games:
    # (0,0) risk-dominates (1,1) iff (safe - sucker)^2 > (joint - safe)^2.
    risk_dominant = "(0,0)" if (safe - sucker) ** 2 > (joint - safe) ** 2 else "(1,1)"
    return {"payoffs": {str(k): v for k, v in pay.items()}, "nash_equilibria": [str(s) for s in nash],
            "pareto_superior": "(1,1)", "risk_dominant": risk_dominant,
            "reading": "(0,0) is an equilibrium that rational players may keep although (1,1) dominates it"}


# ---------------------------------------------------------------------------
# H-02 — the assumed network gap g*E over output b*n
# ---------------------------------------------------------------------------
def gap_ratio(n: int, topology: str, b=10.0, g=0.2) -> float:
    edges = n * (n - 1) // 2 if topology == "dense" else n - 1
    return g * edges / (b * n)


def gap_threshold() -> dict:
    first = next(n for n in range(2, 10_000) if gap_ratio(n, "dense") > 1.0)
    return {"dense_ratio_formula": "0.01*(n-1)", "first_n_gap_exceeds_output": first,
            "star_limit": 0.02, "examples": {n: (round(gap_ratio(n, "dense"), 4), round(gap_ratio(n, "star"), 4))
                                              for n in (5, 10, 20, 40, 101, 102)}}


# ---------------------------------------------------------------------------
# H-03 — censoring versus nesting, separated
# ---------------------------------------------------------------------------
def nested_sum(values):
    if len(values) == 1:
        return values[0]
    m = len(values) // 2
    return nested_sum(values[:m]) + nested_sum(values[m:])


def censoring_vs_nesting(n: int = 4) -> dict:
    profiles = list(product((8, 10), repeat=n))
    out = {}
    for request, label in ((8, "censored_request_8"), (10, "uncensored_request_10")):
        leaves = [tuple(min(request, c) for c in p) for p in profiles]
        out[label] = {"hidden_states": len(profiles),
                      "distinct_flat_branch_reports": len(set(leaves)),
                      "distinct_nested_top_level_sums": len({nested_sum(list(x)) for x in leaves})}
    out["reading"] = ("With censoring both flat and nested reports collapse to 1 value (loss from censoring). "
                      "Without censoring flat reports keep all 2^n states while the nested sum keeps n+1: "
                      "only this second contrast isolates loss attributable to composition.")
    out["bits_lost_by_nesting_without_censoring"] = round(n - math.log2(n + 1), 4)
    return out


# ---------------------------------------------------------------------------
# Figures (plain SVG, no dependencies). Palette: validated reference instance.
# ---------------------------------------------------------------------------
STYLE = """<style>
  .ink{fill:#0b0b0b}.ink2{fill:#52514e}.grid{stroke:#e4e3df}.axis{stroke:#52514e}
  .bg{fill:#fcfcfb}.c1{fill:#2a78d6}.c2{fill:#eb6834}.c3{fill:#1baf7a}.c0{fill:#d7d6d0}
  .l1{stroke:#2a78d6}.l2{stroke:#eb6834}.ref{stroke:#d03b3b}
  text{font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif}
  @media (prefers-color-scheme: dark){
    .ink{fill:#f0efec}.ink2{fill:#c3c2b7}.grid{stroke:#383835}.axis{stroke:#c3c2b7}
    .bg{fill:#1a1a19}.c1{fill:#3987e5}.c2{fill:#d95926}.c3{fill:#199e70}.c0{fill:#4a4a46}
    .l1{stroke:#3987e5}.l2{stroke:#d95926}
  }
</style>"""


def fig_sweep(sw: dict) -> str:
    """Winner per cell for true rate 2.0 (the half where a transfer can help)."""
    cls = {"A_ONLY": "c1", "Q_META_PROTOCOL": "c2", "CONVENTIONAL_DIRECTED": "c3"}
    lab = {"A_ONLY": "A", "Q_META_PROTOCOL": "Q", "CONVENTIONAL_DIRECTED": "D"}
    overheads, qcosts, peers = (0.1, 0.25, 0.5, 0.75, 1.5), (0.05, 0.3, 0.8, 1.5), (0.1, 1.0, 3.0, 5.0)
    cell, gap, left, top = 30, 2, 70, 92
    panel_w = len(qcosts) * (cell + gap) + 18
    w = left + len(peers) * panel_w + 20
    h = top + len(overheads) * (cell + gap) + 104
    dec = lambda v: f"{v:g}".replace(".", ",")
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" '
         f'aria-label="Ganador por celda del barrido de PR 57, tasa real 2,0">{STYLE}',
         f'<rect class="bg" width="{w}" height="{h}" rx="8"/>',
         f'<text class="ink" x="16" y="26" font-size="15" font-weight="600">F-03 · Quién gana en cada celda (tasa real 2,0; 80 de 160 celdas)</text>',
         f'<text class="ink2" x="16" y="46" font-size="12">Las otras 80 celdas (tasa 0,6) las gana A por construcción: ninguna transferencia puede mejorar.</text>',
         f'<text class="ink2" x="16" y="64" font-size="12">Paneles: coste del instrumento dirigido. Filas: overhead h. Columnas: precio de Q.</text>']
    index = {(c["overhead"], c["q_cost"], c["peer_cost"]): c for c in sw["grid"] if c["true_rate"] == 2.0}
    for pi, pc in enumerate(peers):
        x0 = left + pi * panel_w
        s.append(f'<text class="ink" x="{x0}" y="{top - 10}" font-size="12" font-weight="600">dirigido = {dec(pc)}</text>')
        for ri, o in enumerate(overheads):
            y = top + ri * (cell + gap)
            if pi == 0:
                s.append(f'<text class="ink2" x="{left - 8}" y="{y + 19}" font-size="11" text-anchor="end">h = {dec(o)}</text>')
            for ci, qc in enumerate(qcosts):
                x = x0 + ci * (cell + gap)
                win = index[(o, qc, pc)]["winners"]
                k = win[0] if len(win) == 1 else None
                s.append(f'<rect class="{cls.get(k, "c0")}" x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3">'
                         f'<title>h={o:g}, Q={qc:g}, dirigido={pc:g}: {", ".join(win)}</title></rect>')
                s.append(f'<text x="{x + cell / 2}" y="{y + 20}" font-size="12" text-anchor="middle" fill="#fff" font-weight="600">{lab.get(k, "=")}</text>')
        ybot = top + len(overheads) * (cell + gap) + 14
        for ci, qc in enumerate(qcosts):
            s.append(f'<text class="ink2" x="{x0 + ci * (cell + gap) + cell / 2}" y="{ybot}" font-size="10" text-anchor="middle">{dec(qc)}</text>')
    yl = h - 62
    for i, (k, name) in enumerate((("A_ONLY", "A: mantener A"), ("Q_META_PROTOCOL", "Q: Q + metaprotocolo"),
                                   ("CONVENTIONAL_DIRECTED", "D: convencional dirigido"))):
        x = 16 + i * 210
        s.append(f'<rect class="{cls[k]}" x="{x}" y="{yl}" width="14" height="14" rx="3"/>')
        s.append(f'<text class="ink" x="{x + 20}" y="{yl + 12}" font-size="12">{name}</text>')
    s.append(f'<text class="ink2" x="16" y="{h - 28}" font-size="11">Q gana sólo cuando el dirigido cuesta 3 o 5. El brazo convencional con Q equivalente, excluido</text>')
    s.append(f'<text class="ink2" x="16" y="{h - 12}" font-size="11">del barrido, empataría con Q en esas 14 celdas si se le diera el mismo precio.</text>')
    s.append("</svg>")
    return "\n".join(s)


def fig_gap() -> str:
    """Assumed gap as share of output versus n, dense and star."""
    w, h, l, r, t, b = 640, 360, 64, 150, 70, 52
    xmax, ymax = 120, 1.4
    X = lambda n: l + (n / xmax) * (w - l - r)
    Y = lambda v: t + (1 - v / ymax) * (h - t - b)
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" '
         f'aria-label="Brecha supuesta como proporción de la producción frente a n">{STYLE}',
         f'<rect class="bg" width="{w}" height="{h}" rx="8"/>',
         '<text class="ink" x="16" y="26" font-size="15" font-weight="600">H-02 · La brecha supuesta g·E crece sin cota en red densa</text>',
         '<text class="ink2" x="16" y="46" font-size="12">Brecha / producción con b = 10, g = 0,2, α = 0 (misma ecuación en #42, #49 y #54)</text>']
    for v in (0, 0.25, 0.5, 0.75, 1.0, 1.25):
        s.append(f'<line class="grid" x1="{l}" x2="{w - r}" y1="{Y(v):.1f}" y2="{Y(v):.1f}" stroke-width="1"/>')
        s.append(f'<text class="ink2" x="{l - 8}" y="{Y(v) + 4:.1f}" font-size="11" text-anchor="end">{int(v * 100)} %</text>')
    for n in (0, 20, 40, 60, 80, 100, 120):
        s.append(f'<text class="ink2" x="{X(n):.1f}" y="{h - b + 18}" font-size="11" text-anchor="middle">{n}</text>')
    s.append(f'<text class="ink2" x="{(l + w - r) / 2}" y="{h - 12}" font-size="12" text-anchor="middle">n (dimensiones o nodos)</text>')
    s.append(f'<line class="axis" x1="{l}" x2="{w - r}" y1="{Y(0):.1f}" y2="{Y(0):.1f}" stroke-width="1"/>')
    s.append(f'<line class="ref" x1="{l}" x2="{w - r}" y1="{Y(1):.1f}" y2="{Y(1):.1f}" stroke-width="1.5" stroke-dasharray="4 4"/>')
    s.append(f'<text class="ink2" x="{w - r + 6}" y="{Y(1) + 4:.1f}" font-size="11">brecha = producción</text>')
    for topo, cls in (("dense", "l1"), ("star", "l2")):
        pts = " ".join(f"{X(n):.1f},{Y(gap_ratio(n, topo)):.1f}" for n in range(2, xmax + 1))
        s.append(f'<polyline class="{cls}" fill="none" stroke-width="2" points="{pts}"/>')
    s.append(f'<text class="ink" x="{w - r + 6}" y="{Y(gap_ratio(120, "dense")) + 4:.1f}" font-size="12">densa</text>')
    s.append(f'<text class="ink" x="{w - r + 6}" y="{Y(gap_ratio(120, "star")) - 4:.1f}" font-size="12">estrella (→ 2 %)</text>')
    s.append(f'<circle class="c1" cx="{X(102):.1f}" cy="{Y(gap_ratio(102, "dense")):.1f}" r="4"/>')
    s.append(f'<text class="ink" x="{X(102) - 6:.1f}" y="{Y(gap_ratio(102, "dense")) - 10:.1f}" font-size="11" text-anchor="end">n = 102</text>')
    for n in (5, 10, 20, 40):
        s.append(f'<circle class="c1" cx="{X(n):.1f}" cy="{Y(gap_ratio(n, "dense")):.1f}" r="3"><title>n={n}: {gap_ratio(n, "dense"):.0%}</title></circle>')
    s.append('<text class="ink2" x="16" y="62" font-size="11">Puntos: valores de n usados en los PRs (5, 10, 20, 40).</text>')
    s.append("</svg>")
    return "\n".join(s)


def build() -> dict:
    return {"schema": "ACC-INCREMENTAL-AUDIT-COMPANION-v0.1",
            "F04_AG01_net_values": ag01(),
            "F03_sweep_as_published": {k: v for k, v in sweep().items() if k != "grid"},
            "F03_sweep_with_equivalent_arm_same_price": {k: v for k, v in sweep(True).items() if k != "grid"},
            "G01_G02_registry_structure": registry_structure(),
            "H01_stag_hunt_reference": stag_hunt(),
            "H02_gap_threshold": gap_threshold(),
            "H03_censoring_vs_nesting": censoring_vs_nesting(4),
            "evidence": "AUDIT ARITHMETIC ON SYNTHETIC FIXTURES; NO EMPIRICAL CLAIM"}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args(argv)
    result = build()
    text = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    if args.write:
        (HERE / "COMPANION_RESULTS.json").write_text(text, encoding="utf-8")
        (HERE / "figures").mkdir(exist_ok=True)
        (HERE / "figures" / "F03_sweep_winners.svg").write_text(fig_sweep(sweep()), encoding="utf-8")
        (HERE / "figures" / "H02_network_gap.svg").write_text(fig_gap(), encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
