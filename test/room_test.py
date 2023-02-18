#!/usr/bin/env python3
import unittest
import src.room as room


class TestEntity(unittest.TestCase):

    def setUp(self):
        description = "Test Room"
        self.room_ = room.Room(description)

    def test_get_room_properties(self):
        self.assertEqual(self.room_.description, "Test Room")
        self.assertEqual(self.room_.num_foes, -1)
        self.assertFalse(self.room_.treasure)

if __name__ == "__main__":
    unittest.main()