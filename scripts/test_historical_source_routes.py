"""Check the boundary: exact historical citations qualify; live failures stay failures."""
from pathlib import Path
import json
import hashlib
import tempfile
import unittest
from unittest.mock import patch

from check_document_integrity import check_document_links
from historical_source_routes import MANIFEST, text_hash


class SourceQualificationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / 'origin').mkdir()
        (self.root / 'origin/old.md').write_text('Original receiver\n', encoding='utf8')
        (self.root / 'review.md').write_text('Preserved [citation](./old.md)\n[live](live.md)\n', encoding='utf8')
        (self.root / 'live.md').write_text('Current destination\n', encoding='utf8')
        self.entry = {'source':'review.md','raw_target':'./old.md','expected_occurrences':1,
            'source_text_sha256_lf':text_hash(self.root/'review.md'), 'source_relative_base':'origin',
            'receiver_text_sha256_lf':text_hash(self.root/'origin/old.md')}
        self.write_manifest()

    def tearDown(self):
        self.temp.cleanup()

    def write_manifest(self):
        path = self.root / MANIFEST
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({'entries':[self.entry]}), encoding='utf8')

    def test_exact_historical_receiver_is_checked(self):
        errors, total, historical = check_document_links(self.root)
        self.assertEqual((errors, total, historical), ([], 2, 1))

    def test_source_change_invalidates_qualification(self):
        with (self.root/'review.md').open('a', encoding='utf8') as handle:
            handle.write('Changed claim\n')
        errors, _, qualified = check_document_links(self.root)
        self.assertTrue(any('historical source changed' in e for e in errors))
        self.assertEqual(qualified, 0)

    def test_new_broken_link_is_not_hidden(self):
        (self.root/'new.md').write_text('[broken](missing.md)\n', encoding='utf8')
        errors, _, qualified = check_document_links(self.root)
        self.assertTrue(any('new.md' in e and 'missing.md' in e for e in errors))
        self.assertEqual(qualified, 1)

    def test_changed_receiver_invalidates_qualification(self):
        (self.root/'origin/old.md').write_text('Different receiver', encoding='utf8')
        errors, _, _ = check_document_links(self.root)
        self.assertTrue(any('receiver missing or changed' in e for e in errors))

    def test_missing_receiver_is_a_failure(self):
        (self.root/'origin/old.md').unlink()
        self.assertTrue(check_document_links(self.root)[0])

    def test_occurrence_count_cannot_expand(self):
        self.entry['expected_occurrences'] = 2
        self.write_manifest()
        self.assertTrue(any('count changed' in e for e in check_document_links(self.root)[0]))

    def test_repository_escape_is_rejected(self):
        self.entry['source_relative_base'] = '..'
        self.write_manifest()
        self.assertTrue(any('escapes repository' in e for e in check_document_links(self.root)[0]))

    def test_repaired_live_link_needs_no_historical_exception(self):
        (self.root/'old.md').write_text('Now a live route', encoding='utf8')
        self.assertTrue(any('no longer needed' in e for e in check_document_links(self.root)[0]))

    def test_missing_manifest_does_not_silently_skip_quote(self):
        (self.root/MANIFEST).unlink()
        self.assertTrue(any('missing link' in e for e in check_document_links(self.root)[0]))

    def test_only_line_endings_are_normalized(self):
        source = self.root/'review.md'
        source.write_bytes(source.read_bytes().replace(b'\r\n', b'\n').replace(b'\n', b'\r\n'))
        self.assertEqual(check_document_links(self.root)[0], [])
        source.write_bytes(source.read_bytes().replace(b'Preserved', b'Preserved '))
        self.assertTrue(check_document_links(self.root)[0])

    def quote_context(self, receiver='origin/old.md'):
        body = (self.root/'review.md').read_bytes().decode('utf8')
        line = body.splitlines()[0]
        digest = lambda value: hashlib.sha256(value.encode('utf8')).hexdigest()
        return [{'source':'review.md','context':body,'context_sha256':digest(body),
                 'links':[{'line':line,'line_sha256':digest(line),
                           'expected_line_occurrences':1,'href':'./old.md',
                           'receiver':receiver}]}]

    def test_upstream_context_and_registry_agree(self):
        with patch('check_document_integrity.SOURCE_QUOTATION_CONTEXTS', self.quote_context()):
            self.assertEqual(check_document_links(self.root), ([], 2, 1))

    def test_requalified_hash_cannot_override_changed_quote_context(self):
        context = self.quote_context()
        with (self.root/'review.md').open('a', encoding='utf8') as handle:
            handle.write('Changed context\n')
        # Change within the old exact context, then refresh only the whole-source hash.
        source = self.root/'review.md'
        source.write_bytes(source.read_bytes().replace(b'Preserved', b'Changed'))
        self.entry['source_text_sha256_lf'] = text_hash(source)
        self.write_manifest()
        with patch('check_document_integrity.SOURCE_QUOTATION_CONTEXTS', context):
            self.assertTrue(any('quote context changed' in e for e in check_document_links(self.root)[0]))

    def test_registry_cannot_override_upstream_receiver(self):
        with patch('check_document_integrity.SOURCE_QUOTATION_CONTEXTS', self.quote_context('live.md')):
            self.assertTrue(any('receiver disagreement' in e for e in check_document_links(self.root)[0]))


if __name__ == '__main__':
    unittest.main()
