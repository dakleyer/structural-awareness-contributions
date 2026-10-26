import itertools, math
from functools import lru_cache

def setup(L, eps_int):
    worlds = list(itertools.product((0, 1), repeat=L))
    routes = list(itertools.product('mxy', repeat=L))
    def admissible(r, w):
        for ch, b in zip(r, w):
            if ch == 'x' and b != 0: return False
            if ch == 'y' and b != 1: return False
        return True
    def delivers(r, w):
        n_m = sum(1 for ch in r if ch == 'm')
        return admissible(r, w) and n_m <= eps_int
    return worlds, routes, admissible, delivers

def best_success(L, eps_int, tmax):
    worlds, routes, admissible, delivers = setup(L, eps_int)
    n = len(worlds)
    adm = [[admissible(r, w) for w in worlds] for r in routes]
    dlv = [[delivers(r, w) for w in worlds] for r in routes]
    full = (1 << n) - 1
    def mask_of(vec):
        m = 0
        for i, v in enumerate(vec):
            if v: m |= (1 << i)
        return m
    adm_m = [mask_of(a) for a in adm]
    dlv_m = [mask_of(d) for d in dlv]
    @lru_cache(maxsize=None)
    def f(S, t):
        # best number of worlds (within S) delivered correctly
        stop = max(bin(S & d).count('1') for d in dlv_m)
        if t == 0 or S == 0:
            return stop
        best = stop
        seen = set()
        for a in adm_m:
            yes = S & a; no = S & ~a
            if yes == 0 or no == 0:
                continue
            key = (min(yes, no), max(yes, no))
            if key in seen: continue
            seen.add(key)
            v = f(yes, t - 1) + f(no, t - 1)
            if v > best: best = v
        return best
    return [f(full, t) / n for t in range(tmax + 1)]

print('A. Route-membership oracle (a human approves or rejects a whole route), exact optimum over adaptive trees')
for L, eps in [(2, 0), (3, 0), (3, 1)]:
    d = L - eps
    res = best_success(L, eps, L + 1)
    bound = [min(1.0, 2 ** (t - d)) for t in range(L + 2)]
    ok = all(res[t] <= bound[t] + 1e-12 for t in range(L + 2))
    tight = all(abs(res[t] - bound[t]) < 1e-12 for t in range(L + 2))
    print(f' L={L} eps={eps} b*={d}')
    print('  optimum   ', [round(x, 4) for x in res])
    print('  2^(t-b*)  ', [round(x, 4) for x in bound])
    print('  Lemma 1 holds:', ok, ' tight at every t:', tight)

def p_correct(k, q):
    # bit with k noisy queries, each correct w.p. q, Bayes majority, ties random
    if k == 0: return 0.5
    s = 0.0
    for i in range(k + 1):
        pr = math.comb(k, i) * q ** i * (1 - q) ** (k - i)
        if 2 * i > k: s += pr
        elif 2 * i == k: s += 0.5 * pr
    return s

def best_alloc(L, t, q):
    best = 0.0
    for alloc in itertools.product(range(t + 1), repeat=L):
        if sum(alloc) != t: continue
        p = 1.0
        for k in alloc: p *= p_correct(k, q)
        best = max(best, p)
    return best

def H(q):
    return 0.0 if q in (0.0, 1.0) else -q * math.log2(q) - (1 - q) * math.log2(1 - q)

print()
print('B. Noisy judge on each bit, accuracy q, L=3 bits, queries t needed for success >= 3/4')
for q in [0.5, 0.6, 0.75, 0.9, 0.99, 1.0]:
    need = None
    for t in range(0, 61):
        if best_alloc(3, t, q) >= 0.75:
            need = t; break
    cap = 1 - H(q)
    lb = 3 / cap if cap > 0 else float('inf')
    print(f' q={q:<5} capacity per query={cap:.3f} bits   queries needed (exact)={need}   crude capacity estimate 3/capacity={lb:.1f}')
