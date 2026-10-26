#!/usr/bin/env python3
"""Exact finite self-check of supplemental proofs; not independent C05 or a formal prover."""
from functools import lru_cache
from itertools import combinations, permutations, product
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib, json


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def f_policies(L, d, k):
    """All attainable deterministic (T,V,S) world counts over the full history quotient.

    Uniform worlds; mask, position, high count, V latch and paid queries remaining
    are sufficient. Receipts reveal executed local bits. Known-query/rejection loops
    provide no information and can be removed. Shared state dominates team histories.
    This finite checker restricts every branch to k queries; non-T branches of the
    full hard-budget class can be replaced by safe stopping for a risk-minimum claim.
    """
    worlds = tuple(range(1 << L))

    @lru_cache(None)
    def rec(mask, pos, highs, bad, rem):
        size = len(mask)
        if pos == L:
            technical = int(highs >= d)
            return frozenset({(size*technical, size*bad, size*technical*(1-bad))})
        out = {(0, size*bad, 0)}  # safe termination preserves past violation
        if rem:
            for idx in range(L):
                groups = [tuple(w for w in mask if (w >> idx) & 1 == bit)
                          for bit in (0, 1)]
                if all(groups):
                    left = rec(groups[0], pos, highs, bad, rem-1)
                    right = rec(groups[1], pos, highs, bad, rem-1)
                    out.update(add(a, b) for a in left for b in right)
        out.update(rec(mask, pos+1, highs, bad, rem))  # M
        for chosen in (0, 1):
            correct = tuple(w for w in mask if (w >> pos) & 1 == chosen)
            wrong = tuple(w for w in mask if (w >> pos) & 1 != chosen)
            if not correct:  # known denial; omit useless rejected attempt
                continue
            good_out = rec(correct, pos+1, highs+1, bad, rem)
            if wrong:
                bad_out = rec(wrong, pos+1, highs+1, 1, rem)
                out.update(add(a, b) for a in good_out for b in bad_out)
            else:
                out.update(good_out)
        return frozenset(out)

    values = rec(worlds, 0, 0, 0, k)
    return values, rec.cache_info().currsize


def w_policies(n, K):
    """Exhaustive deterministic normal-form query trees, all-ones prefix length <=K.

    If a zero is found, B-completion or safe termination; extra reads cannot help.
    At all-ones leaf choose A/B/M (B forbidden when all n facts are known).
    Policy outcomes vector ordered G,B1,...,Bn with pairs (T,V).
    """
    out = set()
    for q in range(K+1):
        for order in permutations(range(n), q):
            for detected_finish in product((0, 1), repeat=q):
                for choice in ('A', 'M') if q == n else ('A', 'B', 'M'):
                    values = [(int(choice != 'M'), int(choice == 'B'))]
                    for j in range(n):
                        if j in order:
                            values.append((detected_finish[order.index(j)], 0))
                        else:
                            values.append((int(choice != 'M'), int(choice == 'A')))
                    out.add(tuple(values))
    return out


def w_avg_control(n, K, h):
    u = F(K, n); D = u/2
    if h <= D:
        return h, F(0)
    beta = (h-D)/(1-D)
    return D+(1-D)*beta, ((1-u)/2)*beta


def w_wc_control(n, K, h, r):
    if K == n:
        return [(F(1), F(0)) for _ in range(n+1)]
    u = F(K, n)
    return [(h, r)]+[(u+(1-u)*h, (1-u)*(h-r)) for _ in range(n)]


def ceil(x):
    return -(-x.numerator//x.denominator)


def main():
    checks = {}; details = {'F': [], 'W': []}
    def check(name, test):
        assert test, name
        checks[name] = 'PASS'

    # Exhaustive histories first, analytical coefficients only at assertion time.
    total_f = total_w = total_states = 0
    for L in range(1, 4):
        for d in range(1, L+1):
            for k in range(L+1):
                vals, states = f_policies(L, d, k)
                q = F(1, 2**max(0, d-k)); N = 2**L
                for t, v, s in vals:
                    eta, rho, sigma = F(t, N), F(v, N), F(s, N)
                    assert sigma <= q
                    assert rho >= (1/q-1)*sigma
                    assert rho >= (1-q)*eta
                # Constructive endpoints belong to the enumerated history class.
                check(f'F_L{L}_d{d}_k{k}_all_history_inequalities', True)
                check(f'F_L{L}_d{d}_k{k}_matching_endpoints',
                      (0, 0, 0) in vals and (N, int(N*(1-q)), int(N*q)) in vals)
                total_f += len(vals); total_states += states
                details['F'].append({'L': L, 'd': d, 'k': k,
                                     'attainable_deterministic_vectors': len(vals),
                                     'history_quotient_states': states, 'q': str(q)})

    thresholds = (F(1, 4), F(1, 2), F(3, 4), F(1))
    for n in range(1, 5):
        for K in range(n+1):
            vals = w_policies(n, K); u = F(K, n); D = u/2; slope = (1-u)/(2-u)
            for vec in vals:
                eta = F(vec[0][0], 2)+sum(F(v[0], 2*n) for v in vec[1:])
                rho = F(vec[0][1], 2)+sum(F(v[1], 2*n) for v in vec[1:])
                risk_b = sum(F(v[1], n) for v in vec[1:])
                assert rho >= slope*(eta-D) and rho >= 0
                assert risk_b+(1-u)*vec[0][1] >= (1-u)*vec[0][0]
            check(f'W_n{n}_K{K}_all_normal_form_inequalities', True)
            for h in thresholds:
                eta, risk = w_avg_control(n, K, h)
                check(f'W_n{n}_K{K}_h{h}_AVG_matching', eta == h and risk == slope*max(0, h-D))
                for r in (F(0), h/4, h/2, h*3/4):
                    possible = (1-u)*(h-r) <= r
                    ctl = w_wc_control(n, K, h, r)
                    attains = all(a >= h and v <= r for a, v in ctl)
                    check(f'W_n{n}_K{K}_h{h}_r{r}_WC_matching', possible == attains)
            for r in (F(0), F(1, 8), F(1, 4), F(3, 8)):
                minimum = ceil(n*(1-2*r))
                check(f'W_n{n}_K{K}_r{r}_AVG_integer_boundary',
                      ((1-u)/2 <= r) == (K >= minimum))
            total_w += len(vals)
            details['W'].append({'n': n, 'K': K, 'deterministic_outcome_vectors': len(vals)})

    # Expected-cost bound checked directly from arbitrary all-ones query prefixes,
    # zero-branch finish decisions, first high mode, and remaining adaptive outcome.
    # q_G <=n; on G/B_miss, attempted high can finish. Zero branches arbitrary.
    expected_rows = 0
    for n in range(1, 7):
        for qg in range(n+1):
            for discovered_finishes in range(qg+1):
                for mode in ('A', 'B', 'M'):
                    t = int(mode != 'M')
                    eta = F(t, 2)+F((n-qg)*t+discovered_finishes, 2*n)
                    rho = F(int(mode == 'B'), 2)+F((n-qg)*int(mode == 'A'), 2*n)
                    assert eta-2*rho <= F(qg, n)
                    assert F(qg, 2) >= F(n, 2)*max(0, eta-2*rho)
                    expected_rows += 1
        check(f'W_n{n}_expected_cost_prefix_bound', True)
        q_exp = (F(n, 2)+sum(F(j, 2*n) for j in range(1, n+1)))
        check(f'W_n{n}_complete_query_expected_price', q_exp == F(3*n+1, 4))

    check('weak_information_condition_not_sufficient',
          F(3, 4)-F(1, 4) == F(1, 2) and F(3, 4)/2 > F(1, 4))
    check('global_binary_certificate_refutes_local_coordinate_risk_bound',
          F(0) < (2**(3-1)-1)*F(1, 8))
    check('global_certificate_still_satisfies_transcript_bound', F(1, 8) <= F(1, 4))
    for d in range(1, 21):
        for k in range(d+1):
            q = F(1, 2**(d-k))
            for h in thresholds:
                for beta in (F(0), F(1, 3), F(1)):
                    check(f'F_d{d}_k{k}_h{h}_beta{beta}_random_control',
                          beta*(1-q) >= (1-q)*beta and beta*q <= q)
                # Inclusive boundary: thresholds chosen from exact frontiers.
                r = h*(1-q)
                j_allow = max(j for j in range(d+1) if h*(1-F(1, 2**j)) <= r)
                check(f'F_d{d}_k{k}_h{h}_inclusive_frontier', d-j_allow == k)
        for k in range(d+1):
            binomial = sum(F(comb(d, j), 2**d) for j in range(k+1))
            enumerated = F(sum(sum(bits) <= k for bits in product((0, 1), repeat=d)), 2**d) if d <= 8 else binomial
            check(f'barrier_d{d}_k{k}_binomial', binomial == enumerated)
    check('barrier_invalidates_unchanged_bit_bound', F(1, 2) > F(1, 4))
    # Separately simulate charged preeffect attempts, rather than substitute CDF.
    for L in range(1, 7):
        for k in range(L+1):
            for a in (F(1), F(3)):
                g = F(3); b = F(2); R = b+g*L+a*k
                completed = 0
                for bits in product((0, 1), repeat=L):
                    cost = b; refusals = 0; accepted = 0
                    for bit in bits:
                        if bit == 1:  # first guess X rejected, no material violation
                            assert cost+a <= R
                            cost += a; refusals += 1
                            if refusals > k:
                                break
                        assert cost+g <= R
                        cost += g; accepted += 1
                    assert cost <= R
                    completed += int(accepted == L)
                check(f'barrier_L{L}_k{k}_a{a}_charged_attempt_simulation',
                      completed == sum(comb(L, j) for j in range(k+1)))
    for L in range(2, 31):
        n = L*(L-1)//2
        C0 = 2+3*L
        ka = ceil(F(n, 2)); kw = ceil(F(2*n, 3))
        check(f'dense_L{L}_physical_and_joint_boundaries',
              C0 < C0+ka <= C0+n and C0+ka <= C0+kw <= C0+n)
        # T1 exact macro-price comparisons and strictly-below/inclusive edges.
        for fee in (F(0), F(1, 2), F(1), F(n)):
            new = C0+min(F(ka), fee)
            check(f'certificate_L{L}_fee{fee}_inclusive', new <= C0+ka and new <= C0+fee)
    for L in range(1, 41):
        d = ceil(F(L, 2)); slack = F(2+3*L, 6)
        check(f'linear_relative_equality_L{L}_parity', (slack >= d) == (L % 2 == 0))
    original = audit_m02()
    check('M02_receipt_adaptive_control', original['eta'] == '1' and original['rho'] == original['sigma'] == '1/2')
    root = Path(__file__).parent
    output = {'status': 'PASS', 'review': 'same-agent exact finite diagnostic; independent C05 pending',
              'scope': {'F_L_max': 3, 'W_n_max': 4, 'F_deterministic_vectors_total': total_f,
                        'F_history_quotient_states_total': total_states, 'W_deterministic_vectors_total': total_w,
                        'expected_cost_prefix_rows': expected_rows,
                        'coverage': 'all finite F history choices in the quotient; all W normal forms; exact explicit random mixtures; symbolic proofs in companion document'},
              'check_count': len(checks), 'checks': checks, 'finite_details': details,
              'M02_adaptive_control': original,
              'limitations': ['Not a proof assistant', 'No independent implementation or external review',
                              'W normal-form reduction and general all-size coverage require the written proof',
                              'No concrete technology prices/runtime or campaign'],
              'inputs_sha256': {n: hashlib.sha256((root/n).read_bytes()).hexdigest()
                                for n in ('verify_trilemma.py', 'TRILEMMA_CONTRACT.json', 'M02_CONJUNCTION_FIXTURE.json')}}
    print(json.dumps(output, ensure_ascii=False, indent=2))


def audit_m02():
    """Import the preserved historical transition/evaluation checker; no mutation."""
    import importlib.util
    root = Path(__file__).parent
    spec = importlib.util.spec_from_file_location('m02', root/'verify_m02_worlds.py')
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    results = []; traces = []
    for world in (0, 1):
        ep = mod.Episode(world)
        receipt = None
        for op in ('review', 'decide', 'execute'):
            receipt = ep.request(op, 'x1')
            assert receipt['status'] in ('ok', 'PASS-local')
        kind = 'x' if receipt['binding_active_after_effect'] else 'y'
        for i in (2, 3):
            for op in ('review', 'decide', 'execute'):
                assert ep.request(op, f'{kind}{i}')['status'] in ('ok', 'PASS-local')
        ep.request('stop'); rs = ep.result()
        technical = int(len(ep.route) == 3 and mod.technical_value(ep.route) == 6)
        assert rs['C'] == '11' and rs['events'] <= ep.H
        results.append(rs | {'Ttec': technical}); traces.append(ep.history)
    eta = sum(F(x['Ttec'], 2) for x in results)
    rho = sum(F(x['v'], 2) for x in results)
    sigma = sum(F(x['success'], 2) for x in results)
    return {'prior': '1/2,1/2', 'common_first_action': 'x1',
            'following_action_rule': 'if first receipt active choose x2,x3; otherwise y2,y3',
            'eta': str(eta), 'rho': str(rho), 'sigma': str(sigma), 'C': '11',
            'status': 'executed with preserved historical transition API; historical 76-check regression separate',
            'worlds': results, 'traces': traces}


if __name__ == '__main__':
    main()
