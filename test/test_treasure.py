#!/usr/bin/env python3
import unittest
import src.treasure as treasure


class TestTreasure(unittest.TestCase):

    def setUp(self):
        name = "Test Treasure"
        description = "Test Description"
        self.treasure_ = treasure.Treasure(name, description)

    def test_treasure_properties(self):
        self.assertEqual(self.treasure_.name, "Test Treasure")
        self.assertEqual(self.treasure_.description, "Test Description")

    def test_get_treasure(self):
        self.treasure_ = treasure.get_treasure()
        self.assertTrue(self.treasure_)


if __name__ == "__main__":
    unittest.main()
