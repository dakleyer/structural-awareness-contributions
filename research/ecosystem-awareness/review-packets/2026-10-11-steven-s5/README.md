# Steven Zhao S5 / UC-21 — External-review packet (11 October 2026)

**Status:** third-party-reviewable, reviewer-authored technical evidence; **not** a signed independent audit, an admitted UC-4 campaign, DDS Stage B/C validation, a native AWS/RDS run, or an FG-TIDA adopted specification.

[Download the complete executable audit ZIP](./Steven_UC21_Test_Based_Specification_Audit_FULL_REPRODUCIBLE_2026-10-11.zip) (123,884 bytes).

**Integrity:** SHA-256 `9ea1ac54378018e60809f6dff63613fc41d6c0cf53c4ac952345f1e927c51bb8` (verify after download).

## Reproduce offline

Extract the ZIP; in its single top-level directory, run with Python 3.9+ (standard library only):

```bash
python3 verify_archive.py
python3 run_all.py
```

The ZIP includes `AUDIT_REPORT.md`, `README.md`, the frozen S5 decision module/fixture, reviewer-authored replay scripts, raw traces, 18 focused cases, 15 additional probes, a 6,480-row **synthetic** sensitivity grid, a claim/evidence matrix, UC-4 governance proposal, and GitHub Markdown comment draft. The additional synthetic combinations are **not** individually admitted scenario-conformance results.

The original Steven S5 harness and his complete CI/mutation suite are **not included or executed** in this offline package. For those, consult the [original model pinned by commit](https://github.com/zhaoxinghua09-cell/silent-failure-catalog/tree/b59a686b887c2a2545dd22808fb67e629bc95f18/examples/S5-Qregister) and the steps in the ZIP's internal README. Original example code is credited to Steven Zhao under the scope of his MIT licence; the package does not reproduce copyright-reserved catalog prose.

**Scientific purpose:** test-based specification discovery for the frozen UC-21 S5/Step Functions-style queued-repair challenge. Fair conventional solutions receive full credit. Later, independently reviewed candidate specifications are a separate research product and are not conferred by the experiment or the existence of this repository entry.

[UC-21 use case and six scenarios](https://github.com/FG-TIDA/use-cases/issues/21) · [Nelson's UC-4 experimental cycle](https://github.com/FG-TIDA/use-cases/issues/4)
