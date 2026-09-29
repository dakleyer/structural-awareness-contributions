"""Candidate mechanisms and deliberate mutants. No evaluator imports."""

def support(evidence, required, mutant=False):
    positive = sum(1 << i for i, value in enumerate(evidence) if value == 1)
    wanted = sum(1 << i for i in required)
    return bool(positive) if mutant else positive & wanted == wanted

def schedule(durations, budget, response, mutant=False):
    spent = 0
    events = []
    reserve = 0 if mutant else response
    for duration in durations:
        if spent + duration + reserve > budget:
            break
        events.append(('observe', duration))
        spent += duration
    events.append(('respond', response))
    return events

def disposition(established, unknown, required, authorized, mutant='none'):
    if not authorized:
        return False
    if mutant == 'unknown_is_permission':
        return required <= established | unknown
    if mutant == 'all_unknown_blocks':
        return not unknown and required <= established
    if mutant == 'ignore_unknown':
        return required <= established
    return required <= established and not required & unknown

def delegation(scopes, revoked, caps, actions, mutant='none'):
    token = 7
    if mutant == 'union':
        token = 0
    for scope in scopes:
        token = token | scope if mutant == 'union' else token & scope
    active = True if mutant == 'revocation' else not any(revoked)
    capacity = 3 if mutant == 'cap' else min(caps)
    return active and token & actions == actions and actions.bit_count() <= capacity

def execution(events, policy='atomic'):
    observed = 0
    qualified = None
    ticket = False
    output = []
    for event in events:
        if event == 'C':
            observed += 1
        elif event == 'Q':
            qualified = observed
        elif event == 'R' and policy == 'record_qualifies':
            qualified = observed
        elif event == 'K':
            ticket = qualified == observed
        if event == 'A':
            allowed = qualified == observed
            if policy == 'cached':
                allowed = ticket
            elif policy == 'open':
                allowed = True
            elif policy == 'hold':
                allowed = False
            output.append(allowed)
        else:
            output.append(False)
    return output

def independent(edges, a, b, mutant='none'):
    if mutant == 'names':
        return a != b
    parents = {i: [u for u, v in edges if v == i] for i in range(5)}
    if mutant == 'parents':
        return not set(parents[a]) & set(parents[b])
    masks = []
    for i in range(5):
        value = 0
        for parent in parents[i]:
            value |= masks[parent]
        masks.append(value if parents[i] else 1 << i)
    return not masks[a] & masks[b]
