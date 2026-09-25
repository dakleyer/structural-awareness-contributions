"""Serious P6 repair search for 00K A6 / 00G.

This layer hardens the source-independence test against a realistic shortcut:
counting distinct immediate source IDs. Distinct leaf sources can still share one
material upstream root. The strong peer therefore resolves transitive dependency,
not message/source labels alone.
"""
from dataclasses import dataclass
from enum import Enum


class Disposition(Enum):
    PRESERVE = "PRESERVE"
    TRANSITION = "TRANSITION"
    REQUALIFY = "REQUALIFY"


@dataclass(frozen=True)
class Claim:
    agent_id: str
    org_id: str
    source_id: str
    signed: bool = True
    fresh: bool = True
    confidence: float = 0.95
    time_bucket: int = 1
    content_variant: str = "v1"


@dataclass(frozen=True)
class Graph:
    parent: dict[str, str | None]


AGENTS = [f"A{i}" for i in range(6)]
ORGS = [f"O{i}" for i in range(6)]
VARIANTS = ["v1", "v2", "v3", "v1", "v2", "v3"]


def false_hidden_dependency():
    sources = [f"S{i}" for i in range(6)]
    claims = [
        Claim(AGENTS[i], ORGS[i], sources[i], True, True, 0.95, i % 3, VARIANTS[i])
        for i in range(6)
    ]
    parent = {s: f"M{i % 2}" for i, s in enumerate(sources)}
    parent.update({"M0": "ROOT_N", "M1": "ROOT_N", "ROOT_N": None})
    return claims, Graph(parent)


def genuine_independent():
    sources = [f"S{i}" for i in range(6)]
    claims = [
        Claim(AGENTS[i], ORGS[i], sources[i], True, True, 0.95, i % 3, VARIANTS[i])
        for i in range(6)
    ]
    parent = {s: f"ROOT_{i}" for i, s in enumerate(sources)}
    parent.update({f"ROOT_{i}": None for i in range(6)})
    return claims, Graph(parent)


def blind_signature(claims):
    return tuple(
        (
            c.agent_id,
            c.org_id,
            c.signed,
            c.fresh,
            c.confidence,
            c.time_bucket,
            c.content_variant,
        )
        for c in claims
    )


def identity_quorum(claims, q=3):
    return (
        Disposition.TRANSITION
        if len({c.agent_id for c in claims}) >= q
        else Disposition.PRESERVE
    )


def org_diversity(claims, q=3):
    return (
        Disposition.TRANSITION
        if len({c.org_id for c in claims}) >= q
        else Disposition.PRESERVE
    )


def direct_source_count(claims, q=3):
    return (
        Disposition.TRANSITION
        if len({c.source_id for c in claims}) >= q
        else Disposition.PRESERVE
    )


def confidence_weighted(claims, threshold=4.0):
    return (
        Disposition.TRANSITION
        if sum(c.confidence for c in claims) >= threshold
        else Disposition.PRESERVE
    )


def temporal_diversity(claims, q=2):
    return (
        Disposition.TRANSITION
        if len({c.time_bucket for c in claims}) >= q
        else Disposition.PRESERVE
    )


def content_diversity(claims, q=2):
    return (
        Disposition.TRANSITION
        if len({c.content_variant for c in claims}) >= q
        else Disposition.PRESERVE
    )


def human_committee(claims, q=4):
    return (
        Disposition.TRANSITION
        if len([c for c in claims if c.signed and c.fresh]) >= q
        else Disposition.PRESERVE
    )


def trusted_org_reputation(claims, score=0.99, threshold=0.9):
    return Disposition.TRANSITION if score >= threshold else Disposition.PRESERVE


def root_of(source, graph):
    seen = set()
    cur = source
    while True:
        if cur in seen:
            return None
        seen.add(cur)
        if cur not in graph.parent:
            return None
        nxt = graph.parent[cur]
        if nxt is None:
            return cur
        cur = nxt


def material_root_count(claims, graph):
    roots = []
    for c in claims:
        r = root_of(c.source_id, graph)
        if r is None:
            return None
        roots.append(r)
    return len(set(roots))


def dependency_graph_peer(claims, graph, q=2):
    n = material_root_count(claims, graph)
    if n is None:
        return Disposition.REQUALIFY
    return Disposition.TRANSITION if n >= q else Disposition.PRESERVE


def effective_sample_size_peer(claims, graph, q=2):
    return dependency_graph_peer(claims, graph, q)


def missing_graph():
    claims, g = false_hidden_dependency()
    parent = dict(g.parent)
    parent.pop("S3")
    return claims, Graph(parent)


def cyclic_graph():
    claims, g = false_hidden_dependency()
    parent = dict(g.parent)
    parent["ROOT_N"] = "M0"
    return claims, Graph(parent)
