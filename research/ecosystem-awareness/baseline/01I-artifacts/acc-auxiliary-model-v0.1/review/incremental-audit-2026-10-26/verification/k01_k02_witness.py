"""K-02 witness and K-01 cost-versus-size table (round 17).

Usage: python3 -B k01_k02_witness.py <studies/intrinsic-abcd-economics-v0.1>
K-02: root bottleneck 129, A = 128; B for source-3 and for source-8 are each
valid and promise 1; together they promise 2, the joint gain is 1.
K-01: with default costs, B stops being cheaper than targeted inspection at
n = 128 leaves (tie at 3.00). Writes nothing.
"""
import sys; sys.path.insert(0, sys.argv[1])
import intrinsic_abcd as m
n=16
bits=tuple(1 if k in (3,8,12) else 0 for k in range(n))
# K-02: two individually valid B's sharing a root bottleneck with headroom 1
w=m.balanced_tree(bits, cap_root=129)
cur=m.deliver(w, m.base_demand(w))
b3=m.upstream_B(w,"source-3",now=5,ttl=10); b8=m.upstream_B(w,"source-8",now=5,ttl=10)
ok3=m.receiver_B_valid(m.public_outline(w),b3,"source-3",now=6); ok8=m.receiver_B_valid(m.public_outline(w),b8,"source-8",now=6)
d=m.base_demand(w); d["source-3"]+=2; d["source-8"]+=2
joint=m.deliver(w,d)-cur
print("current A:",cur,"| B3:",b3.delivered_if_requested,ok3[0],"| B8:",b8.delivered_if_requested,ok8[0],"| sum promised:",b3.delivered_if_requested+b8.delivered_if_requested,"| actual joint gain:",joint)
# K-01: cost vs depth, current constants
c=m.Costs()
for n in (4,16,64,128,256,1024):
    bits=tuple([1]+[0]*(n-1)); w=m.balanced_tree(bits)
    L=len(m.path_to(w,"source-0")); N=m.node_count(w)
    cB=L*c.b_issuance_per_path_node+c.b_transmission+c.b_maintenance
    print(f"n={n:5d} L={L:3d} N={N:5d}  C_B={cB:6.2f}  C_target={c.target_observation:.2f}  C_full={N*c.full_node:7.1f}  B<target? {cB<c.target_observation}")
