import unittest

from canonical_trace_v1 import (
    CANONICALIZATION_VERSION,
    CanonicalTraceError,
    canonical_trace_bytes,
    canonical_trace_sha256,
)


class CanonicalTraceV1Tests(unittest.TestCase):
    def test_key_order_does_not_change_bytes(self):
        a = {"b": 2, "a": 1}
        b = {"a": 1, "b": 2}
        self.assertEqual(canonical_trace_bytes(a), canonical_trace_bytes(b))

    def test_excluded_runtime_fields_do_not_change_hash(self):
        a = {"step": 1, "run_id": "A", "wall_clock_timestamp": "t1"}
        b = {"step": 1, "run_id": "B", "wall_clock_timestamp": "t2"}
        self.assertEqual(canonical_trace_sha256(a), canonical_trace_sha256(b))

    def test_semantic_array_order_is_preserved(self):
        a = {"events": [{"id": "a"}, {"id": "b"}]}
        b = {"events": [{"id": "b"}, {"id": "a"}]}
        self.assertNotEqual(canonical_trace_bytes(a), canonical_trace_bytes(b))

    def test_declared_set_like_collection_is_sorted(self):
        rules = {("sources",): "id"}
        a = {"sources": [{"id": "b"}, {"id": "a"}]}
        b = {"sources": [{"id": "a"}, {"id": "b"}]}
        self.assertEqual(
            canonical_trace_bytes(a, set_like_rules=rules),
            canonical_trace_bytes(b, set_like_rules=rules),
        )

    def test_repository_path_is_posix_normalised(self):
        a = {"repository_path": "fixtures\\RS-00E-Q1a\\trace.json"}
        b = {"repository_path": "fixtures/RS-00E-Q1a/trace.json"}
        self.assertEqual(canonical_trace_bytes(a), canonical_trace_bytes(b))

    def test_absolute_path_is_rejected(self):
        with self.assertRaises(CanonicalTraceError):
            canonical_trace_bytes({"file_path": "/tmp/trace.json"})

    def test_float_is_rejected(self):
        with self.assertRaises(CanonicalTraceError):
            canonical_trace_bytes({"score": 0.5})

    def test_canonicalization_version_is_present(self):
        out = canonical_trace_bytes({"step": 1}).decode("utf-8")
        self.assertIn(
            f'"canonicalization_version":"{CANONICALIZATION_VERSION}"',
            out,
        )


if __name__ == "__main__":
    unittest.main()
