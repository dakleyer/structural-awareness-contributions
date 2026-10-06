"""Canonical Trace v1 reference helper for RS-00E-Q1a.

This module is a fixture/harness utility, not an EA runtime implementation.
It implements the evidence-serialization rules pre-registered in
pre_registration_v0.5.md.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import PurePosixPath
from typing import Any, Mapping

CANONICALIZATION_VERSION = "CTv1"

EXCLUDED_FIELDS = frozenset({
    "run_id",
    "wall_clock_timestamp",
    "host_process_id",
    "temporary_output_path",
})

PATH_FIELDS = frozenset({
    "repository_path",
    "file_path",
    "artifact_path",
    "source_path",
})


class CanonicalTraceError(ValueError):
    """Raised when a trace cannot conform to Canonical Trace v1."""


def _normalise_path(value: str) -> str:
    # Convert separator syntax but never accept an absolute/local-machine path.
    raw = value.replace("\\", "/")
    if raw.startswith("/") or (len(raw) >= 2 and raw[1] == ":"):
        raise CanonicalTraceError(f"absolute/local path is forbidden: {value!r}")
    parts = PurePosixPath(raw).parts
    if ".." in parts:
        raise CanonicalTraceError(f"parent traversal is forbidden: {value!r}")
    norm = PurePosixPath(*[p for p in parts if p not in ("", ".")]).as_posix()
    return "." if norm == "" else norm


def _normalise(
    value: Any,
    *,
    path: tuple[str, ...] = (),
    set_like_rules: Mapping[tuple[str, ...], str] | None = None,
) -> Any:
    rules = set_like_rules or {}

    if value is None or isinstance(value, (str, bool)):
        return value

    if isinstance(value, int) and not isinstance(value, bool):
        return value

    if isinstance(value, float):
        raise CanonicalTraceError(
            "Canonical Trace v1 forbids JSON floating-point numbers; "
            "encode non-integral measurements as normalized decimal strings."
        )

    if isinstance(value, dict):
        out: dict[str, Any] = {}
        for key in sorted(value.keys()):
            if not isinstance(key, str):
                raise CanonicalTraceError("object keys must be strings")
            if key in EXCLUDED_FIELDS:
                continue
            child = value[key]
            if key in PATH_FIELDS and child is not None:
                if not isinstance(child, str):
                    raise CanonicalTraceError(f"path field {key!r} must be a string")
                child = _normalise_path(child)
            out[key] = _normalise(
                child,
                path=path + (key,),
                set_like_rules=rules,
            )
        return out

    if isinstance(value, (list, tuple)):
        items = [
            _normalise(item, path=path + ("[]",), set_like_rules=rules)
            for item in value
        ]
        if path in rules:
            stable_key = rules[path]
            try:
                items = sorted(items, key=lambda x: x[stable_key])
            except (TypeError, KeyError) as exc:
                raise CanonicalTraceError(
                    f"set-like collection at {path!r} requires mapping items "
                    f"with stable key {stable_key!r}"
                ) from exc
        return items

    raise CanonicalTraceError(
        f"unsupported trace type {type(value).__name__}; "
        "use JSON-compatible values only"
    )


def canonical_trace_bytes(
    trace: Mapping[str, Any],
    *,
    set_like_rules: Mapping[tuple[str, ...], str] | None = None,
) -> bytes:
    """Return Canonical Trace v1 bytes.

    The function adds/overwrites canonicalization_version with CTv1 in the
    canonicalized copy. It never mutates the caller's mapping.
    """
    if not isinstance(trace, Mapping):
        raise CanonicalTraceError("trace root must be a mapping/object")

    prepared = dict(trace)
    prepared["canonicalization_version"] = CANONICALIZATION_VERSION
    normalised = _normalise(prepared, set_like_rules=set_like_rules)

    text = json.dumps(
        normalised,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )
    return text.encode("utf-8")


def canonical_trace_sha256(
    trace: Mapping[str, Any],
    *,
    set_like_rules: Mapping[tuple[str, ...], str] | None = None,
) -> str:
    return hashlib.sha256(
        canonical_trace_bytes(trace, set_like_rules=set_like_rules)
    ).hexdigest()
