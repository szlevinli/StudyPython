# -*- coding: utf8 -*-

import unittest
from overLongWeight import *


class TestOverLongWeight(unittest.TestCase):

    def test_isOverWeight(self):
        self.assertEqual(isOverWeight(0.2, 1, 80), False)
        self.assertEqual(isOverWeight(1, 1, 1), False)
        with self.assertRaises(AssertionError):
            self.assertEqual(isOverWeight(1, 0, 1), False)

if __name__ == '__main__':
    unittest.main()
