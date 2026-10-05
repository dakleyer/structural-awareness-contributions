"""Exhaustive DAG/path reference cross-check for the R01 oracle.

This is an internal algorithmic cross-check over a graph representation, separate
from the explicit-trajectory reference used by the current Stage-0 cases.
"""

from __future__ import annotations

from typing import Any, Mapping


def _validate(graph: Mapping[str, Any]):
    nodes_raw = graph.get("nodes")
    edges_raw = graph.get("edges")
    start = graph.get("start")
    terminals = graph.get("terminals")
    if not isinstance(nodes_raw, list) or not nodes_raw:
        raise ValueError("graph nodes must be non-empty")
    if not isinstance(edges_raw, list):
        raise ValueError("graph edges must be a list")
    if not isinstance(start, str) or not isinstance(terminals, list) or not terminals:
        raise ValueError("graph start/terminals required")

    nodes = {}
    for item in nodes_raw:
        nid = item.get("id")
        benefit = item.get("benefit", 0)
        adm = item.get("admissible")
        if not isinstance(nid, str) or not nid or nid in nodes:
            raise ValueError("graph node ids must be unique strings")
        if type(benefit) is not int or benefit < 0:
            raise ValueError("graph node benefits must be non-negative integers")
        if type(adm) is not bool:
            raise ValueError("graph node admissible must be boolean")
        nodes[nid] = {"benefit": benefit, "admissible": adm}
    if start not in nodes or any(t not in nodes for t in terminals):
        raise ValueError("graph start/terminal must name existing nodes")

    adjacency = {nid: [] for nid in nodes}
    for edge in edges_raw:
        src, dst = edge.get("from"), edge.get("to")
        benefit, adm = edge.get("benefit", 0), edge.get("admissible")
        if src not in nodes or dst not in nodes:
            raise ValueError("edge endpoint missing from nodes")
        if type(benefit) is not int or benefit < 0:
            raise ValueError("graph edge benefits must be non-negative integers")
        if type(adm) is not bool:
            raise ValueError("graph edge admissible must be boolean")
        adjacency[src].append((dst, benefit, adm))
    return nodes, adjacency, start, set(terminals)


def evaluate_graph_exhaustive(graph: Mapping[str, Any]) -> dict[str, Any]:
    nodes, adjacency, start, terminals = _validate(graph)
    if not nodes[start]["admissible"]:
        return {
            "reference_status": "NOT_ESTABLISHED",
            "optimum_J": None,
            "optimum_path_ids": [],
            "paths_examined": 0,
        }

    rows = []
    stack = [(start, (start,), nodes[start]["benefit"], {start})]
    while stack:
        node, path, score, visited = stack.pop()
        if node in terminals:
            rows.append((path, score))
            continue
        for dst, edge_benefit, edge_admissible in adjacency[node]:
            if dst in visited:
                raise ValueError("exhaustive DAG reference encountered a cycle")
            if not edge_admissible or not nodes[dst]["admissible"]:
                continue
            stack.append(
                (
                    dst,
                    path + (dst,),
                    score + edge_benefit + nodes[dst]["benefit"],
                    visited | {dst},
                )
            )

    if not rows:
        return {
            "reference_status": "NOT_ESTABLISHED",
            "optimum_J": None,
            "optimum_path_ids": [],
            "paths_examined": 0,
        }
    optimum = max(score for _, score in rows)
    ids = sorted(">".join(path) for path, score in rows if score == optimum)
    return {
        "reference_status": "ESTABLISHED",
        "optimum_J": optimum,
        "optimum_path_ids": ids,
        "paths_examined": len(rows),
    }
