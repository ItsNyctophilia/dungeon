#!/usr/bin/env python3
import unittest
from src.monster import Monster


class TestMonster(unittest.TestCase):

    def setUp(self):
        name = "Test Name"
        description = "Test Description"
        self.monster_ = Monster(name, description)
        self.monster_.hp = 5
        self.monster_.dice = 3

    def test_get_monster_properties(self):
        self.assertEqual(self.monster_.name, "Test Name")
        self.assertEqual(self.monster_.description, "Test Description")
        self.assertEqual(self.monster_.hp, 5)
        self.assertEqual(self.monster_.dice, 3)
        self.assertFalse(self.monster_.treasure)

    def test_monster_hit(self):
        self.monster_.hit()
        self.assertEqual(self.monster_.hp, 4)


if __name__ == "__main__":
    unittest.main()
