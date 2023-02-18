#!/usr/bin/env python3
import unittest
from src.menu import Menu


class TestMenu(unittest.TestCase):

    def setUp(self):
        self.menu_ = Menu()
        self.menu_.add_selection("Test 1")
        self.menu_.add_selection("Test 2")
        self.menu_.add_selection("Test 3")

    def test_get_menu_properties(self):
        self.assertEqual(self.menu_.selections[0], "Test 1")
        self.assertEqual(self.menu_.selections[1], "Test 2")
        self.assertEqual(self.menu_.selections[2], "Test 3")

    def test_menu_has_function(self):
        self.assertTrue(self.menu_.has_selection("Test 2"))

    def test_menu_replace_function(self):
        self.menu_.replace_selection("Test Replace", 1)
        self.assertEqual(self.menu_.selections[1], "Test Replace")

    def test_menu_delete_function(self):
        self.menu_.del_selection("Test 2")
        self.assertFalse(self.menu_.has_selection("Test 2"))


if __name__ == "__main__":
    unittest.main()
