#!/usr/bin/env python3
import unittest
from src.hero import Hero


class TestHero(unittest.TestCase):

    def setUp(self):
        self.hero_ = Hero()

    def test_get_hero_properties(self):
        self.assertEqual(self.hero_.hp, 10)
        self.assertEqual(self.hero_.dice, 3)
        self.assertFalse(self.hero_.treasure)

    def test_hero_hit(self):
        self.hero_.hit()
        self.assertEqual(self.hero_.hp, 9)


if __name__ == "__main__":
    unittest.main()
