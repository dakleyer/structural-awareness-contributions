"""Evaluators use raw worlds, issuer records and histories, not candidate state.

These are algorithmically separate, same-author semantic evaluators, not
independently validated domain oracles.
"""
from itertools import product

def entailed(evidence, required):
    worlds = [w for w in product((0, 1), repeat=3)
              if all(e == -1 or e == w[i] for i, e in enumerate(evidence))]
    return all(all(w[j] == 1 for j in required) for w in worlds)

def timely(events, budget):
    clock = 0
    response_finished = False
    for kind, duration in events:
        for _ in range(duration):
            clock += 1
        if kind == 'respond':
            response_finished = clock <= budget
    return response_finished

def permitted_by_issuers(scopes, revoked, caps, actions):
    batch = [i for i in range(3) if actions & (1 << i)]
    for issuer in range(3):
        if revoked[issuer]:
            return False
        if len(batch) > caps[issuer]:
            return False
        for item in batch:
            if not scopes[issuer] & (1 << item):
                return False
    return True

def bad_execution(events, output):
    # No counters, qualification tokens or candidate tickets are inspected.
    # Reconstruct the segment preceding each actual execution backwards.
    for i, ran in enumerate(output):
        if not ran:
            continue
        for prior in reversed(events[:i]):
            if prior in ('C', 'X'):
                return True
            if prior == 'Q':
                break
        else:
            return True
    return False

def unrelated_roots(edges, a, b):
    def roots(node):
        pending, visited, leaves = [node], set(), set()
        while pending:
            current = pending.pop()
            if current in visited:
                continue
            visited.add(current)
            incoming = [u for u, v in edges if v == current]
            if incoming:
                pending.extend(incoming)
            else:
                leaves.add(current)
        return leaves
    return roots(a).isdisjoint(roots(b))
