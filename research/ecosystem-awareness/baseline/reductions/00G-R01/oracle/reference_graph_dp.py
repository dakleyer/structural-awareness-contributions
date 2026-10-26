"""Dynamic-programming DAG reference cross-check for the R01 oracle.

This implementation does not enumerate all complete paths. It uses a frozen
topological order and retains tied optimum path identifiers.
"""

from __future__ import annotations

from typing import Any, Mapping


def evaluate_graph_dp(graph: Mapping[str, Any]) -> dict[str, Any]:
    nodes_raw = graph.get("nodes")
    edges_raw = graph.get("edges")
    order = graph.get("topological_order")
    start = graph.get("start")
    terminals = graph.get("terminals")
    if not isinstance(nodes_raw, list) or not nodes_raw:
        raise ValueError("DP graph nodes must be non-empty")
    if not isinstance(edges_raw, list):
        raise ValueError("DP graph edges must be a list")
    if not isinstance(order, list) or not order:
        raise ValueError("DP graph requires topological_order")
    if not isinstance(start, str) or not isinstance(terminals, list) or not terminals:
        raise ValueError("DP graph start/terminals required")

    nodes = {}
    for item in nodes_raw:
        nid = item.get("id")
        benefit, adm = item.get("benefit", 0), item.get("admissible")
        if not isinstance(nid, str) or not nid or nid in nodes:
            raise ValueError("DP node ids must be unique strings")
        if type(benefit) is not int or benefit < 0:
            raise ValueError("DP node benefit must be non-negative integer")
        if type(adm) is not bool:
            raise ValueError("DP node admissible must be boolean")
        nodes[nid] = (benefit, adm)

    if set(order) != set(nodes) or len(order) != len(nodes):
        raise ValueError("topological_order must contain each node exactly once")
    index = {nid: i for i, nid in enumerate(order)}
    if start not in nodes or any(t not in nodes for t in terminals):
        raise ValueError("DP start/terminal missing")
    edges_from = {nid: [] for nid in nodes}
    for edge in edges_raw:
        src, dst = edge.get("from"), edge.get("to")
        benefit, adm = edge.get("benefit", 0), edge.get("admissible")
        if src not in nodes or dst not in nodes:
            raise ValueError("DP edge endpoint missing")
        if index[src] >= index[dst]:
            raise ValueError("edge violates declared topological order")
        if type(benefit) is not int or benefit < 0:
            raise ValueError("DP edge benefit must be non-negative integer")
        if type(adm) is not bool:
            raise ValueError("DP edge admissible must be boolean")
        edges_from[src].append((dst, benefit, adm))

    neg = None
    best: dict[str, int | None] = {nid: neg for nid in nodes}
    paths: dict[str, set[tuple[str, ...]]] = {nid: set() for nid in nodes}
    start_benefit, start_adm = nodes[start]
    if start_adm:
        best[start] = start_benefit
        paths[start].add((start,))

    for src in order:
        if best[src] is None:
            continue
        for dst, edge_benefit, edge_adm in edges_from[src]:
            node_benefit, node_adm = nodes[dst]
            if not edge_adm or not node_adm:
                continue
            score = best[src] + edge_benefit + node_benefit
            proposed = {path + (dst,) for path in paths[src]}
            if best[dst] is None or score > best[dst]:
                best[dst] = score
                paths[dst] = proposed
            elif score == best[dst]:
                paths[dst].update(proposed)

    terminal_scores = [(t, best[t]) for t in terminals if best[t] is not None]
    if not terminal_scores:
        return {
            "reference_status": "NOT_ESTABLISHED",
            "optimum_J": None,
            "optimum_path_ids": [],
            "states_processed": len(order),
        }
    optimum = max(score for _, score in terminal_scores)
    optimum_paths = set()
    for terminal, score in terminal_scores:
        if score == optimum:
            optimum_paths.update(paths[terminal])
    return {
        "reference_status": "ESTABLISHED",
        "optimum_J": optimum,
        "optimum_path_ids": sorted(">".join(path) for path in optimum_paths),
        "states_processed": len(order),
    }
