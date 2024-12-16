#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for is in one  function.


Test categories:
    - Standard cases: a string item and two lists
    - Edge cases: empty lists, cases sensitivity
    - Defensive tests: wrong input types, assertions

Created on 2024-12-15
Author: Falaq"""


import unittest

from ..is_in_one import is_in_one
class TestInOne(unittest.TestCase):
    """testing is_in_one function"""
    def test_is_in_both(self):
        """Testing is item in  2 lists"""
        actual = is_in_one('cat', ['cat', 'hat'], ['cat', 'hat'])
        expected = False
        self.assertEqual(actual, expected)
    def test_is_in_one(self):
        """Testing is item in  1 list"""
        actual = is_in_one('lena', ['falaq', 'shafaq','lena'], ['apple', 'banana'])
        expected = True
        self.assertEqual(actual, expected)
    def test_is_in_none(self):
        """Testing is item not in the list"""
        actual = is_in_one('car', ['aero', 'plane', 'ship'], ['yacht', 'jat'])
        expected = False
        self.assertEqual(actual, expected)
    def test_two_list_empty(self):
        """testing if two list empty"""
        actual = is_in_one('hello', [], [])
        expected = False
        self.assertEqual(actual, expected)
    def test_item_empty(self):
        """testing empty item"""
        actual = is_in_one('', ['me', 'you'], ['them','they'])
        expected = False 
        self.assertEqual(actual, expected)
    def test_item_case(self):
        """testing the letter case"""
        actual = is_in_one('Ant', ['ant', 'bat'], ['hat', 'cat'])
    def test_is_not_str(self):
        """should raise an error if the item is not string"""
        with self.assertRaises(AssertionError):
            is_in_one(23, ['he', 'she'], ['they', 'them'])
    def test_is_not_list(self):
        """should raise an error if the list is not list"""
        with self.assertRaises(AssertionError):
            is_in_one('cat', ['he', 'she'], 1123)
