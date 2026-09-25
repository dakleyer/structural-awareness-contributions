# 00K historical A1–A3 fixture variants

**Status:** preserved historical executable sources. These are not the current canonical A1–A3 fixtures and are not part of the [379-test campaign](../00K-SUITE/README.md).

The six Python files in these three directories reproduce the original repository blobs byte for byte. They were removed on 25 September 2026 with commit messages describing them as duplicate ablation variants. Their inputs and assertions differ from the current fixtures, so they remain distinct evidence and are preserved here without changing the current harnesses.

| Historical fixture | Original source commit before removal | Tests | Distinct question |
|---|---|---:|---|
| [A1 / 00J](./A1-00J/test_A1_00J.py) and [model](./A1-00J/ablation_A1_00J.py) | [`348edcbc`](https://github.com/dakleyer/structural-awareness-contributions/tree/348edcbcfb2ffac81088599bf7bfc7f706642f3b/research/ecosystem-awareness/baseline/fixtures/00K-A1-P1-00J) | 11 | Unsupported enforcement versus legitimate grant, including fresh lineage with different proposition support. |
| [A2 / 00E](./A2-00E/test_A2_00E.py) and [model](./A2-00E/ablation_A2_00E.py) | [`8af3969`](https://github.com/dakleyer/structural-awareness-contributions/tree/8af3969b45bfd95d2cb7ac84af30333669a4b421/research/ecosystem-awareness/baseline/fixtures/00K-A2-P2-00E) | 11 | Bounded closure, unbounded search and a positive control where resolution arrives. |
| [A3 / 00F](./A3-00F/test_A3_00F.py) and [model](./A3-00F/ablation_A3_00F.py) | [`465c892`](https://github.com/dakleyer/structural-awareness-contributions/tree/465c89271464c0c90f70681fab0f5018f5130907/research/ecosystem-awareness/baseline/fixtures/00K-A3-P3-00F) | 10 | Unresolved HOLD, open/closed controls and native interlock. |

Run these three historical variants from this directory with pytest installed:

```bash
python -m pytest -q A1-00J A2-00E A3-00F
```

**Replay on 25 September 2026:** 32/32 passed. This is a separate archival replay, not 32 additional canonical tests. The current fixtures contain more developed controls, but their success does not make the earlier assertions byte-identical or erase their provenance.
