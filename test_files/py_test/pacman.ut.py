"""
Unit tests for pacman.py
Last Modified: April 29, 2019
"""

import os
import sys
import time
import unittest
from pacman import pacman

class AllTests(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(pacman("test_files/py_test/generic.txt"), (6, 1, 27))

    def test_edge(self):
        self.assertEqual(pacman("test_files/py_test/edge.txt"), (-1, -1, 0))

    def test_runtime(self):
        self.assertEqual(pacman("test_files/py_test/runtime.txt"), (2142, 147, 148))

if __name__ == '__main__':
    for testClass in [AllTests]:
        print('\n\nTest Class: {}\n'.format(testClass.__name__))
        suite = unittest.TestLoader().loadTestsFromTestCase(testClass)
        result = unittest.TextTestRunner(verbosity=0).run(suite)
