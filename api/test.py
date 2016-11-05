#!/usr/bin/env python3
import unittest

class TestTestingFramework(unittest.TestCase):
    def test_math(self):
        self.assertEqual(1, 1)

    def test_english(self):
        self.assertEqual('word', 'word')

if __name__ == '__main__':
    unittest.main()
