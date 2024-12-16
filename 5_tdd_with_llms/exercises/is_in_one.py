#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Is in one

Write a function that takes in a string and two lists of strings. 
It will return true if the item is in _only one_ of the lists.

"""
def is_in_one(item:str,list1:list,list2:list) -> bool:
    """Returns true if the item is in one  only of the list

    Args:
        item (str): the input string
        list1 (list): the input list 1
        list2 (list): the input list 2
  Returns: true if the string is in one list
  Raises:
  AssertionError: if the item is not string
  AssertionError: if the list1 is not a list
  AssertionError: if the list2 is not a ist
>>> is_in_one('cat', ['cat', 'hat'], ['cat', 'bat'])
False
>>> is_in_one('lena', ['falaq', 'shafaq','lena'], ['apple', 'banana'])
True
>>> is_in_one('car', ['aero', 'plane', 'ship'], ['yacht', 'jat'])
False
"""
    assert isinstance(item, str)
    assert isinstance(list1, list)
    assert isinstance(list2, list)
    if item in list1 and item in list2:
      return False
    elif item in list1:
      return True
    elif item in list2:
      return True
    else:
      return False
