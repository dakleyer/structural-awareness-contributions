"""K-02 extension (round 19): composability of B certificates on random trees.

Usage: python3 -B k02_b_composability_fuzz.py <studies/intrinsic-abcd-economics-v0.1>
Expected on main 51fc686: 3 000 single-question cases with 0 over-promises;
2 299 two-question cases where the sum of two valid B over-promises the joint
gain in 214. Writes nothing.
"""
import sys, random
sys.path.insert(0, sys.argv[1])
import intrinsic_abcd as m
random.seed(11); over=0; n_cases=0; joint_over=0; joint_cases=0
for _ in range(3000):
    n=random.choice([2,4,8,16]); bits=tuple(random.randint(0,1) for _ in range(n))
    cap=random.choice([None, 8*n, 8*n+1, 8*n+2, 8*n+3])
    w=m.balanced_tree(bits, cap_root=cap, base=8, upper=random.choice([1,2,3]))
    extra=random.choice([1,2,3])
    t=f"source-{random.randrange(n)}"
    b=m.upstream_B(w,t,now=0,ttl=5,extra=extra)
    cur=m.deliver(w,m.base_demand(w)); gain=m.deliver(w,m.selected_demand(w,t,extra=extra))-cur
    n_cases+=1; over+= b.delivered_if_requested>gain
    # joint: two distinct targets
    t2=f"source-{random.randrange(n)}"
    if t2!=t:
        b2=m.upstream_B(w,t2,now=0,ttl=5,extra=extra)
        d=m.base_demand(w); d[t]+=extra; d[t2]+=extra
        jg=m.deliver(w,d)-cur; joint_cases+=1; joint_over+= (b.delivered_if_requested+b2.delivered_if_requested)>jg
print(f"single-question cases: {n_cases}, B over-promises: {over}")
print(f"two-question cases: {joint_cases}, sum of two valid B over-promises joint gain: {joint_over}")
