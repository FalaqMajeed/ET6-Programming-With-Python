#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for is in sort number function.


Test categories:
    - Standard cases: a sorted and unsorted list
    - Edge cases: same item , negative
    - Defensive tests: wrong input types, assertions

Created on 2024-12-15
Author: Falaq"""


import unittest

from ..sort_numbers import sort_numbers
class TestSortNumbers(unittest.TestCase):
    """"""
    def test_int(self):
        """test unsorted int"""
        actual = sort_numbers([5, 6, 7, 1])
        expected = sort_numbers([1, 5, 6, 7])
        self.assertEqual(actual, expected)
    def test_sorted(self):
        """test sorted num"""
        actual = sort_numbers([1, 2, 3])
        expected = sort_numbers([1, 2, 3])
        self.assertEqual(actual,expected)
    def test_float(self):
        """test float"""
        actual = sort_numbers([1.0, 5.0, 3])
        expected = sort_numbers([1.0, 3, 5.0])
        self.assertEqual(actual,expected)
    def test_negative(self):
        """test negative list"""
        actual = sort_numbers([-1.0, 5.0, -3])
        expected = sort_numbers([-3, -1.0, 5.0])
        self.assertEqual(actual,expected)
    def test_same(self):
        """test if same num"""
        actual = sort_numbers([-1.0, -1.0, -1.0])
        expected = sort_numbers([-1.0, -1.0, -1.0])
        self.assertEqual(actual,expected)
    def test_all_num(self):
        """raise an error in not int or float"""
        with self.assertRaises(AssertionError):
            sort_numbers(['cat', 'mat'])
    def test_is_not_list(self):
        """raise an error if not list"""
        with self.assertRaises(AssertionError):
            sort_numbers("hello")
