#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for is in both function.


Test categories:
    - Standard cases: a string item and two lists
    - Edge cases: empty lists, cases sensitivity
    - Defensive tests: wrong input types, assertions

Created on 2024-12-15
Author: Falaq"""


import unittest

from ..is_in_both import is_in_both
class TestInBoth(unittest.TestCase):
    """testing is_in_both function"""
    def test_is_in_both1(self):
        """Testing is item in  2 lists"""
        actual = is_in_both('cat', ['cat', 'hat'], ['cat', 'hat'])
        expected = True
        self.assertEqual(actual, expected)
    def test_one_both(self):
        """testing if item in only one list"""
        actual = is_in_both('lena', ['falaq', 'shafaq','lena'], ['apple', 'banana'])
        expected = False
        self.assertEqual(actual, expected)
    def test_not_both(self):
        """testing if item is not in both list"""
        actual = is_in_both('you', ['I', 'Me', 'They'], ['They', 'cat', 'mat'])
        expected = False
        self.assertEqual(actual, expected)
    def test_one_list_empty(self):
        """testing if one list is empty"""
        actual = is_in_both('hey', ['hey', 'hello'],[])
        expected = False
        self.assertEqual(actual, expected)
    def test_two_list_empty(self):
        """testing if two list empty"""
        actual = is_in_both('hello', [], [])
        expected = False
        self.assertEqual(actual, expected)
    def test_item_empty(self):
        """testing empty item"""
        actual = is_in_both('', ['me', 'you'], ['them','they'])
        expected = False 
        self.assertEqual(actual, expected)
    def test_item_case(self):
        """testing the letter case"""
        actual = is_in_both('Ant', ['ant', 'bat'], ['hat', 'cat'])
    def test_is_not_str(self):
        """should raise an error if the item is not string"""
        with self.assertRaises(AssertionError):
            is_in_both(23, ['he', 'she'], ['they', 'them'])
    def test_is_not_list(self):
        """should raise an error if the item is not string"""
        with self.assertRaises(AssertionError):
            is_in_both('cat', ['he', 'she'], 1123)
