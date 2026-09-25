from __future__ import annotations

import math
import unittest

from full_cube_model import Model, Inquiry, all_targets, construct, signature


class TestFullCube(unittest.TestCase):

    def test_signature_000000(self):
        target = (0, 0, 0, 0, 0, 0)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_000001(self):
        target = (0, 0, 0, 0, 0, 1)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_000010(self):
        target = (0, 0, 0, 0, 1, 0)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_000011(self):
        target = (0, 0, 0, 0, 1, 1)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_000100(self):
        target = (0, 0, 0, 1, 0, 0)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_000101(self):
        target = (0, 0, 0, 1, 0, 1)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_000110(self):
        target = (0, 0, 0, 1, 1, 0)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_000111(self):
        target = (0, 0, 0, 1, 1, 1)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_001000(self):
        target = (0, 0, 1, 0, 0, 0)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_001001(self):
        target = (0, 0, 1, 0, 0, 1)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_001010(self):
        target = (0, 0, 1, 0, 1, 0)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_001011(self):
        target = (0, 0, 1, 0, 1, 1)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_001100(self):
        target = (0, 0, 1, 1, 0, 0)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_001101(self):
        target = (0, 0, 1, 1, 0, 1)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_001110(self):
        target = (0, 0, 1, 1, 1, 0)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_001111(self):
        target = (0, 0, 1, 1, 1, 1)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_010000(self):
        target = (0, 1, 0, 0, 0, 0)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_010001(self):
        target = (0, 1, 0, 0, 0, 1)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_010010(self):
        target = (0, 1, 0, 0, 1, 0)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_010011(self):
        target = (0, 1, 0, 0, 1, 1)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_010100(self):
        target = (0, 1, 0, 1, 0, 0)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_010101(self):
        target = (0, 1, 0, 1, 0, 1)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_010110(self):
        target = (0, 1, 0, 1, 1, 0)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_010111(self):
        target = (0, 1, 0, 1, 1, 1)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_011000(self):
        target = (0, 1, 1, 0, 0, 0)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_011001(self):
        target = (0, 1, 1, 0, 0, 1)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_011010(self):
        target = (0, 1, 1, 0, 1, 0)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_011011(self):
        target = (0, 1, 1, 0, 1, 1)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_011100(self):
        target = (0, 1, 1, 1, 0, 0)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_011101(self):
        target = (0, 1, 1, 1, 0, 1)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_011110(self):
        target = (0, 1, 1, 1, 1, 0)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_011111(self):
        target = (0, 1, 1, 1, 1, 1)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_100000(self):
        target = (1, 0, 0, 0, 0, 0)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_100001(self):
        target = (1, 0, 0, 0, 0, 1)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_100010(self):
        target = (1, 0, 0, 0, 1, 0)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_100011(self):
        target = (1, 0, 0, 0, 1, 1)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_100100(self):
        target = (1, 0, 0, 1, 0, 0)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_100101(self):
        target = (1, 0, 0, 1, 0, 1)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_100110(self):
        target = (1, 0, 0, 1, 1, 0)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_100111(self):
        target = (1, 0, 0, 1, 1, 1)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_101000(self):
        target = (1, 0, 1, 0, 0, 0)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_101001(self):
        target = (1, 0, 1, 0, 0, 1)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_101010(self):
        target = (1, 0, 1, 0, 1, 0)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_101011(self):
        target = (1, 0, 1, 0, 1, 1)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_101100(self):
        target = (1, 0, 1, 1, 0, 0)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_101101(self):
        target = (1, 0, 1, 1, 0, 1)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_101110(self):
        target = (1, 0, 1, 1, 1, 0)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_101111(self):
        target = (1, 0, 1, 1, 1, 1)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_110000(self):
        target = (1, 1, 0, 0, 0, 0)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_110001(self):
        target = (1, 1, 0, 0, 0, 1)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_110010(self):
        target = (1, 1, 0, 0, 1, 0)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_110011(self):
        target = (1, 1, 0, 0, 1, 1)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_110100(self):
        target = (1, 1, 0, 1, 0, 0)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_110101(self):
        target = (1, 1, 0, 1, 0, 1)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_110110(self):
        target = (1, 1, 0, 1, 1, 0)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_110111(self):
        target = (1, 1, 0, 1, 1, 1)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_111000(self):
        target = (1, 1, 1, 0, 0, 0)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_111001(self):
        target = (1, 1, 1, 0, 0, 1)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_111010(self):
        target = (1, 1, 1, 0, 1, 0)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_111011(self):
        target = (1, 1, 1, 0, 1, 1)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_111100(self):
        target = (1, 1, 1, 1, 0, 0)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_111101(self):
        target = (1, 1, 1, 1, 0, 1)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_111110(self):
        target = (1, 1, 1, 1, 1, 0)
        self.assertEqual(signature(construct(target)), target)

    def test_signature_111111(self):
        target = (1, 1, 1, 1, 1, 1)
        self.assertEqual(signature(construct(target)), target)

    def test_all_64_signatures_are_realized(self):
        realized = {signature(construct(tuple(t))) for t in all_targets()}
        self.assertEqual(len(realized), 64)
        self.assertEqual(realized, {tuple(t) for t in all_targets()})

    def test_counting_argument_requires_six_boolean_coordinates(self):
        required_classes = 64
        min_boolean_coordinates = math.ceil(math.log2(required_classes))
        self.assertEqual(min_boolean_coordinates, 6)
        self.assertLess(2 ** 5, required_classes)
        self.assertEqual(2 ** 6, required_classes)

    def test_one_conjunction_bit_is_enough_only_for_pass_fail_not_full_signature(self):
        models = [construct(tuple(t)) for t in all_targets()]
        pass_fail = {int(all(signature(m))) for m in models}
        self.assertEqual(pass_fail, {0, 1})
        # One bit recognizes the all-six-pass set, but cannot recover 64 diagnostic signatures.
        self.assertEqual(len(pass_fail), 2)
        self.assertEqual(len({signature(m) for m in models}), 64)

    def test_p2_and_p3_share_the_same_inquiry_object_semantics(self):
        # P2 false / P3 true: same unresolved issue, unbounded search, but not material-to-action.
        m01 = construct((1, 0, 1, 1, 1, 1))
        self.assertTrue(m01.inquiry.unresolved)
        self.assertTrue(m01.inquiry.cyclic_progress)
        self.assertFalse(m01.inquiry.material_to_action)
        self.assertEqual(signature(m01)[1:3], (0, 1))

        # P2 true / P3 false: same unresolved issue, bounded process, but material state is promoted.
        m10 = construct((1, 1, 0, 1, 1, 1))
        self.assertTrue(m10.inquiry.unresolved)
        self.assertFalse(m10.inquiry.cyclic_progress)
        self.assertTrue(m10.inquiry.material_to_action)
        self.assertEqual(signature(m10)[1:3], (1, 0))


if __name__ == "__main__":
    unittest.main()
