"""M28-04 evidence and L-02 (round 23): expiry handling in requalify.

Usage: python3 -B m28_04_requalify_probe.py <studies/mathematical-lineage-social-agentic-v0.1 on PR #60>

M28-04: requalify(retained, certificate) has no decision-time argument, so it
can only compare expires_before with the retained event time (t = 1). It also
accepts expires_before == 1 at t == 1, an endpoint convention that is not stated.
L-02: expires_before = NaN reaches ADMISSIBLE_FOR_NEW_REVIEW (NaN < 1 is False),
and a missing, None or text expires_before raises TypeError instead of
returning CERTIFICATE_UNSUPPORTED. Expected on PR #60 8cd78d58: exactly that.
Writes nothing.
"""
import sys

sys.path.insert(0, sys.argv[1])
import test_theme18_online_context as t  # noqa: E402

rec = t.capture_pre_admission("new-route", permitted=True, capture_enabled=True)
base = {"verified": True, "source_scope": "route-v1", "target_event": "new-route"}


def run(cert):
    try:
        return t.requalify(rec, cert)
    except Exception as exc:
        return f"RAISES {type(exc).__name__}"


code = t.requalify.__code__
print("event time:", rec["time"], "| requalify parameters:", code.co_varnames[:code.co_argcount])
for eb in (0, 1, 2, 3):
    print(f"expires_before={eb!r}:", run(dict(base, expires_before=eb)))
print("expires_before missing:", run(base))
for eb in (None, float("nan"), "3"):
    print(f"expires_before={eb!r}:", run(dict(base, expires_before=eb)))
