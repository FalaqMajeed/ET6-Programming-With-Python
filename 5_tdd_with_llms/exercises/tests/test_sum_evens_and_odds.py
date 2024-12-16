#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for adding sum of evens and odds in a list


Test categories:
    - Standard cases: int list, float lists, negative list
    - Edge cases: empty lists, 
    - Defensive tests: wrong input types, assertions

Created on 2024-12-15
Author: Falaq"""


import unittest

from ..sum_evens_and_odds import sum_evens_and_odds
class TestInBoth(unittest.TestCase):
    """Adds the odd and even numbers in a list"""
    def test_add_positive_int(self):
        """adding integers odds and evens"""
        actual = sum_evens_and_odds([1, 2, 3, 4, 5])
        expected = {'even_sum': 6, 'odd_sum': 9}
        self.assertEqual(actual, expected)
    def test_add_positive_float(self):
        """adding float odds and evens"""
        actual = sum_evens_and_odds([1.0, 2.0, 3.0, 4.0, 5.0])
        expected = {'even_sum': 6.0, 'odd_sum': 9.0}
        self.assertEqual(actual, expected)
    def test_add_negative_float(self):
        """adding negative float odds and evens"""
        actual = sum_evens_and_odds([-1.0, -2.0, -3.0, -4.0, -5.0])
        expected = {'even_sum': -6.0, 'odd_sum': -9.0}
        self.assertEqual(actual, expected) 
    def test_add_negative_int(self):
        """adding negative odds and evens"""
        actual = sum_evens_and_odds([-1, -2, -3, -4, -5])
        expected = {'even_sum': -6, 'odd_sum': -9}
        self.assertEqual(actual, expected)
    def test_add_empty(self):
        """adding empty list"""
        actual = sum_evens_and_odds([])
        expected = {'even_sum': 0, 'odd_sum': 0}
        self.assertEqual(actual, expected)  
    def test_add_one(self):
        """adding one number in a list"""
        actual = sum_evens_and_odds([1])
        expected = {'even_sum': 0, 'odd_sum': 1}
        self.assertEqual(actual, expected)
    def test_is_not_list(self):
        """should raise an error if the numbers is not list"""
        with self.assertRaises(AssertionError):
            sum_evens_and_odds("hello")
