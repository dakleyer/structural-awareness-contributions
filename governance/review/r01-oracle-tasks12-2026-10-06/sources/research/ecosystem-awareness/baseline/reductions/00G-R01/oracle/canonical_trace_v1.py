"""R01 reuse of Canonical Trace v1.

Source implementation:
research/ecosystem-awareness/baseline/fixtures/RS-00E-Q1a/canonical_trace_v1.py

The serialization rules are preserved so R01 can interoperate with the existing
corpus harness evidence. This utility is not a technology or EA implementation.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import PurePosixPath
from typing import Any, Mapping

CANONICALIZATION_VERSION = "CTv1"
EXCLUDED_FIELDS = frozenset({"run_id", "wall_clock_timestamp", "host_process_id", "temporary_output_path"})
PATH_FIELDS = frozenset({"repository_path", "file_path", "artifact_path", "source_path"})


class CanonicalTraceError(ValueError):
    pass


def _normalise_path(value: str) -> str:
    raw = value.replace("\\", "/")
    if raw.startswith("/") or (len(raw) >= 2 and raw[1] == ":"):
        raise CanonicalTraceError(f"absolute/local path is forbidden: {value!r}")
    parts = PurePosixPath(raw).parts
    if ".." in parts:
        raise CanonicalTraceError(f"parent traversal is forbidden: {value!r}")
    norm = PurePosixPath(*[p for p in parts if p not in ("", ".")]).as_posix()
    return "." if norm == "" else norm


def _normalise(value: Any, *, path: tuple[str, ...] = (), set_like_rules=None) -> Any:
    rules = set_like_rules or {}
    if value is None or isinstance(value, (str, bool)):
        return value
    if isinstance(value, int) and not isinstance(value, bool):
        return value
    if isinstance(value, float):
        raise CanonicalTraceError("CTv1 forbids JSON floating-point numbers; use normalized decimal strings")
    if isinstance(value, dict):
        out = {}
        for key in sorted(value):
            if not isinstance(key, str):
                raise CanonicalTraceError("object keys must be strings")
            if key in EXCLUDED_FIELDS:
                continue
            child = value[key]
            if key in PATH_FIELDS and child is not None:
                if not isinstance(child, str):
                    raise CanonicalTraceError(f"path field {key!r} must be a string")
                child = _normalise_path(child)
            out[key] = _normalise(child, path=path + (key,), set_like_rules=rules)
        return out
    if isinstance(value, (list, tuple)):
        items = [_normalise(x, path=path + ("[]",), set_like_rules=rules) for x in value]
        if path in rules:
            stable_key = rules[path]
            items = sorted(items, key=lambda x: x[stable_key])
        return items
    raise CanonicalTraceError(f"unsupported trace type {type(value).__name__}")


def canonical_trace_bytes(trace: Mapping[str, Any], *, set_like_rules=None) -> bytes:
    prepared = dict(trace)
    prepared["canonicalization_version"] = CANONICALIZATION_VERSION
    normalised = _normalise(prepared, set_like_rules=set_like_rules)
    return json.dumps(normalised, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


def canonical_trace_sha256(trace: Mapping[str, Any], *, set_like_rules=None) -> str:
    return hashlib.sha256(canonical_trace_bytes(trace, set_like_rules=set_like_rules)).hexdigest()
