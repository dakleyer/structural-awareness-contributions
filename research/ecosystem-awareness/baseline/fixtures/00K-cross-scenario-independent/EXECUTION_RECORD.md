# Independent cross-scenario kernel execution record

**Planned regression count:** 6  
**Evidence class:** independent symbolic reimplementation, supplemental to the 101 core 00K tests.

The implementation shares no helper code with A1–A6. It tests:

- P4 on 00H and 00J;
- P5 on 00I and 00H; and
- P6 on 00G and 00F.

A passing CI result is evidence of cross-scenario semantic reuse, not universal validity.
