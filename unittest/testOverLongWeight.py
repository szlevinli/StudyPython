# -*- coding: utf8 -*-

import unittest
from overLongWeight import *


class Test_overLongWeight(unittest.TestCase):

    def test_isOverWeight(self):
        self.assertEqual(isOverWeight(0.2, 1), False)
        self.assertEqual(isOverWeight(100, 1), True)
        self.assertEqual(isOverWeight(100, 3), False)
        self.assertEqual(isOverWeight(500, 5.5), True)
        self.assertEqual(isOverWeight(1, 1, 1), False)
        self.assertEqual(isOverWeight(10, 2, 4), True)

    def test_isOverLong(self):
        self.assertEqual(isOverLong(100, 100, 80), False)
        self.assertEqual(isOverLong(100, 100, 100), False)
        self.assertEqual(isOverLong(100, 100, 100.00001), True)
        self.assertEqual(isOverLong(-10, 180, 0), True)
        self.assertEqual(isOverLong(1, 1, 1, 1, 3), False)
        self.assertEqual(isOverLong(1, 1, 1, 0.9, 3), True)
        self.assertEqual(isOverLong(1, 1, 1, 1, 2.9), True)

if __name__ == '__main__':
    unittest.main()
