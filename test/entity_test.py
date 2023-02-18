#!/usr/bin/env python3
import unittest
from src.entity import Entity

class TestEntity(unittest.TestCase):

    def setUp(self):
        self.entity_= Entity()
        self.entity_.hp = 5
        self.entity_.dice = 3

    def test_get_entity_properties(self):
        self.assertEqual(self.entity_.hp, 5)
        self.assertEqual(self.entity_.dice, 3)
        self.assertFalse(self.entity_.treasure)


if __name__ == "__main__":
    unittest.main()