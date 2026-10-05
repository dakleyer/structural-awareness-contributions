"""Content-integrity verifier for frozen R01 oracle Stage-0 artifacts.

The manifest pins Git blob object IDs. This is independent of branch movement:
a later commit may contain the same frozen bytes, but changing a frozen file
without explicitly revising the manifest makes verification fail.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Mapping


class IntegrityError(ValueError):
    pass


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


SUPPORTED_FREEZE_SCHEMAS = {
    "R01-C02-FREEZE-MANIFEST-0.4",
    "R01-C02-FREEZE-MANIFEST-0.5",
}


def verify_freeze_manifest(root: Path, manifest: Mapping[str, Any]) -> dict[str, Any]:
    if manifest.get("schema") not in SUPPORTED_FREEZE_SCHEMAS:
        raise IntegrityError("unsupported freeze manifest schema")
    files = manifest.get("files")
    if not isinstance(files, list) or not files:
        raise IntegrityError("freeze manifest requires files")

    checked = []
    seen = set()
    for entry in files:
        if not isinstance(entry, Mapping):
            raise IntegrityError("freeze manifest file entry must be an object")
        rel = entry.get("path")
        expected = entry.get("git_blob_sha1")
        if not isinstance(rel, str) or not rel or rel.startswith("/") or ".." in Path(rel).parts:
            raise IntegrityError(f"invalid frozen path: {rel!r}")
        if rel in seen:
            raise IntegrityError(f"duplicate frozen path: {rel}")
        seen.add(rel)
        if not isinstance(expected, str) or len(expected) != 40:
            raise IntegrityError(f"invalid git blob id for {rel}")

        path = root / rel
        if not path.is_file():
            raise IntegrityError(f"frozen file missing: {rel}")
        actual = git_blob_sha1(path.read_bytes())
        if actual != expected:
            raise IntegrityError(
                f"frozen file drift: {rel}: expected {expected}, actual {actual}"
            )
        checked.append({"path": rel, "git_blob_sha1": actual})

    return {
        "status": "PASS",
        "manifest_schema": manifest["schema"],
        "files_checked": len(checked),
        "files": checked,
    }


def load_and_verify(root: Path, manifest_path: Path) -> dict[str, Any]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    return verify_freeze_manifest(root, manifest)
