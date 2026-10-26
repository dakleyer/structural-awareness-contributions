"""Qualify exact historical source-relative citations without hiding live links."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import urllib.parse

MANIFEST = 'governance/review/HISTORICAL_SOURCE_RELATIVE_LINKS_2026-10-25.json'


def text_hash(path):
    value = path.read_bytes().decode('utf8').replace('\r\n', '\n')
    return hashlib.sha256(value.encode('utf8')).hexdigest()


def inside(root, relative):
    target = (root / relative).resolve()
    if not target.is_relative_to(root.resolve()):
        raise ValueError('qualification escapes repository: ' + relative)
    return target


def qualified_routes(root: Path, extract_targets):
    manifest = root / MANIFEST
    if not manifest.exists():
        return {}, []
    result, errors = {}, []
    try:
        entries = json.loads(manifest.read_text(encoding='utf8'))['entries']
        if not isinstance(entries, list):
            raise ValueError('qualification entries must be a list')
        for item in entries:
            source = inside(root, item['source'])
            raw = item['raw_target']
            key = (item['source'], raw)
            if key in result or not isinstance(raw, str) or ':' in raw or raw.startswith(('#', '/', '//')):
                raise ValueError('invalid or duplicate qualified route')
            if text_hash(source) != item['source_text_sha256_lf']:
                raise ValueError('historical source changed: ' + item['source'])
            count = item['expected_occurrences']
            if type(count) is not int or count < 1 or extract_targets(source.read_text(encoding='utf8')).count(raw) != count:
                raise ValueError('historical citation count changed: ' + item['source'])
            route = urllib.parse.unquote(raw.split('#', 1)[0].split('?', 1)[0])
            if (source.parent / route).resolve().exists():
                raise ValueError('qualification no longer needed for direct route: ' + raw)
            receiver = inside(root, (Path(item['source_relative_base']) / route).as_posix())
            if not receiver.is_file() or text_hash(receiver) != item['receiver_text_sha256_lf']:
                raise ValueError('qualified receiver missing or changed: ' + raw)
            result[key] = {'receiver': receiver, 'expected_occurrences': count}
    except (ValueError, KeyError, TypeError, OSError) as exc:
        return {}, ['historical source qualification: ' + str(exc)]
    return result, errors
