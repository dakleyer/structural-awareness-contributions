"""Source-agnostic presentation of L08 grid results, no extra simulations/theory.

Reads a completed L08 JSON trace, validates identity and conditional results,
and generates a portable machine-readable and Markdown summary with matrix
cells and price-front memberships. All totals derive from recorded outputs.
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import argparse
import json
from typing import Any, Mapping

LABELS={
    "BOUNDARY_DOMINATES_ON_ERRORS_AND_MISSED_CANDIDATES":"B",
    "DOMAIN_FACTS_DOMINATES_ON_ERRORS_AND_MISSED_CANDIDATES":"D",
    "TIE_ON_ERRORS_AND_MISSED_CANDIDATES":"T",
    "INCOMPARABLE_ERROR_VS_MISSED_OPPORTUNITY_TRADEOFF":"I",
}
FAIR={
    "SOURCE_BOUNDARY_ONLY",
    "QUALIFIED_DOMAIN_FACTS_ONLY",
    "BOTH_SOURCE_AND_DOMAIN",
    "CONVENTIONAL_TARGETED",
}


def summarize(report:Mapping[str,Any])->dict[str,Any]:
    if report.get("schema")!="ACC-L08-CALIBRATED-PAIRED-EVIDENCE-v0.1":
        raise ValueError("incorrect input laboratory output schema")
    panels=report.get("panels",[])
    if not panels:
        raise ValueError("no experimental panels")
    clean=[]
    total=0
    for panel in panels:
        cells=panel["cells"]
        if not cells or len(cells)!=panel["count_cells"]:
            raise ValueError("missing grid records")
        source_grid=sorted({x["assumed_accuracy_of_qualified_source"] for x in cells},
                           key=lambda x:float(__import__('fractions').Fraction(x)))
        domain_grid=sorted({x["assumed_per_domain_observation_accuracy"] for x in cells},
                           key=lambda x:float(__import__('fractions').Fraction(x)))
        if len(cells)!=len(source_grid)*len(domain_grid):
            raise ValueError("incomplete source/domain grid")
        by_pair={
            (c["assumed_accuracy_of_qualified_source"],
             c["assumed_per_domain_observation_accuracy"]):c
            for c in cells
        }
        if len(by_pair)!=len(cells):
            raise ValueError("duplicate source/domain grid cell")
        matrix=[]
        for source in source_grid:
            row=[]
            for domain in domain_grid:
                cell=by_pair[(source,domain)]
                status=cell["matched_two_axis_source_vs_scoped_domain"]
                if status not in LABELS:
                    raise ValueError("unsupported comparison verdict")
                row.append(LABELS[status])
            matrix.append({"source_accuracy":source,"values":row})
        memberships={}
        for contract in report["price_contracts"]:
            count=Counter()
            for cell in cells:
                if contract not in cell["three_axis_fronts_by_price_contract"]:
                    raise ValueError("missing price profile from a cell")
                values=cell["three_axis_fronts_by_price_contract"][contract]["three_axis_pareto_front"]
                if not set(values)<=FAIR:
                    raise ValueError("diagnostic policy in authoritative fair front")
                count.update(values)
            memberships[contract]={k:count[k] for k in sorted(FAIR)}
        two=Counter()
        for cell in cells:
            v=cell["two_axis_front_no_price"]
            if not set(v)<=FAIR:
                raise ValueError("invalid no-price fair front")
            two.update(v)
        actual=Counter(x["matched_two_axis_source_vs_scoped_domain"] for x in cells)
        if dict(actual)!=panel["counts_by_two_axis_source_vs_scoped_domain"]:
            raise ValueError("report count disagrees with the cell-derived count")
        endpoints={}
        for s,d in (("1","1/2"),("1/2","1"),("1","1")):
            if (s,d) not in by_pair:
                continue
            cell=by_pair[(s,d)]
            endpoints[s+"|"+d]={
                "two_axis_result":LABELS[cell["matched_two_axis_source_vs_scoped_domain"]],
                "B":{k:cell["instrumental_arms"]["SOURCE_BOUNDARY_ONLY"][k]
                     for k in ("invalid_proposals","missed_valid_opportunities")},
                "scoped_domain":{k:cell["instrumental_arms"]["QUALIFIED_DOMAIN_FACTS_ONLY"][k]
                     for k in ("invalid_proposals","missed_valid_opportunities")},
                "directed":{k:cell["instrumental_arms"]["CONVENTIONAL_TARGETED"][k]
                     for k in ("invalid_proposals","missed_valid_opportunities")},
            }
        total+=len(cells)
        clean.append({
            "panel":panel["id"],
            "cells":len(cells),
            "q_accuracy_rows":source_grid,
            "domain_accuracy_columns":domain_grid,
            "labels":"B=boundary-dominant; D=scoped-domain-dominant; T=tie; I=incomparable",
            "classification_matrix":matrix,
            "two_axis_verdict_counts":dict(sorted(actual.items())),
            "without_price_pareto_membership":{k:two[k] for k in sorted(FAIR)},
            "three_axis_membership_by_price_contract":memberships,
            "critical_endpoints":endpoints,
        })
    return {
        "schema":"ACC-L08-PORTABLE-SUMMARY-v0.1",
        "source_manifest_sha256":report["manifest_sha256"],
        "total_regimes":len(clean),
        "total_grid_cells":total,
        "paired_evaluations":report["total_paired_cell_evaluations"],
        "price_contracts":report["price_contracts"],
        "panels":clean,
        "purpose":"CONDITIONAL_RESULT_MAP_AND_COST_SENSITIVITY_ONLY",
        "independent_real_world_source_accuracy_evidence":"NOT_AVAILABLE",
        "source_semantics_unchanged":report["source_original_public_policies_unchanged"],
        "objectives_not_collapsed":"NO_SCALARIZATION_OF_ERRORS_MISSES_COST_OR_HUMAN_WELFARE",
    }


def as_markdown(result:Mapping[str,Any])->str:
    lines=[
        "# L-08 — mapa condicional y costes de los experimentos finitos",
        "",
        "El resultado no determina qué precisión existe en el mundo real ni demuestra prioridad causal FH-C.",
        f"**Evaluaciones emparejadas:** {result['paired_evaluations']}. "
        f"**Celdas de precisión:** {result['total_grid_cells']}. "
        f"**Contratos de coste:** {len(result['price_contracts'])}.",
        "",
        "**Leyenda:** B = domina cualificación de fuentes en errores y omisiones; "
        "D = dominan hechos cualificados; T = empate; I = incomparables.",
        "",
    ]
    for p in result["panels"]:
        lines+=["## "+p["panel"],"",
                "| Q \\ dominio |"+"|".join(p["domain_accuracy_columns"])+"|",
                "|---|"+"|".join("---" for _ in p["domain_accuracy_columns"])+"|"]
        for row in p["classification_matrix"]:
            lines.append("| "+row["source_accuracy"]+" |"+"|".join(row["values"])+"|")
        lines+=["","### Comprobaciones y precios",""]
        lines+=["| Clase | Celdas |","|---|---:|"]
        for name,n in p["two_axis_verdict_counts"].items():
            lines.append("| "+name+" | "+str(n)+" |")
        lines+=["","La pertenencia al frente de Pareto no es una cuota de mercado: "
                "puede haber varios brazos no dominados en una celda.",""]
        lines+=["| Política | Frente SIN precio |"+"|".join(result["price_contracts"])+"|",
                "|---|---:|"+"|".join("---:" for _ in result["price_contracts"])+"|"]
        for arm,value in p["without_price_pareto_membership"].items():
            line="| "+arm+" | "+str(value)
            for price in result["price_contracts"]:
                line+=" | "+str(p["three_axis_membership_by_price_contract"][price][arm])
            lines.append(line+" |")
        lines+=["","### Casos extremos","",
                "| Precisión Q / hechos | Resultado | B: errores / perdidas | Hechos: errores / perdidas | Convencional dirigido: errores / perdidas |",
                "|---|---|---:|---:|---:|"]
        for key,v in p["critical_endpoints"].items():
            def fmt(item):
                return str(item["invalid_proposals"])+"/"+str(item["missed_valid_opportunities"])
            lines.append("| "+key+" | "+v["two_axis_result"]+" | "+fmt(v["B"])+" | "+
                         fmt(v["scoped_domain"])+" | "+fmt(v["directed"])+" |")
        lines.append("")
    lines += [
        "**Límites:** los costes de adquisición no se convierten en alimentos ni en bienestar; "
        "la exactitud de cada uno de tres sensores no equivale a la exactitud de una única declaración B. "
        "Las diferencias son propiedades de este generador sintético y de sus supuestos, no de una "
        "tecnología comercial ni un contrato institucional.","",
    ]
    return "\n".join(lines)


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input",type=Path)
    parser.add_argument("--json",type=Path)
    parser.add_argument("--markdown",type=Path)
    args=parser.parse_args(argv)
    report=summarize(json.loads(args.input.read_text(encoding="utf-8")))
    compact=json.dumps(report,ensure_ascii=False,indent=2,sort_keys=True)+"\n"
    md=as_markdown(report)
    if args.json:
        args.json.write_text(compact,encoding="utf-8")
    if args.markdown:
        args.markdown.write_text(md,encoding="utf-8")
    if not args.json and not args.markdown:
        print(md)
    return 0


if __name__=="__main__":
    raise SystemExit(main())
