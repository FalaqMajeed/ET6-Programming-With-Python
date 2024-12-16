""" Inclusive Or

Write a function that takes in a string and two lists of strings. 
It will return true if the item is in _at least one_ of the lists.

"""
def sort_numbers(num: list[float | int])-> list[float | int]:
    """Sort in ascending order
    arg: 
    num (list): list of numbers(float,int)
    Return: sorted list
    Raises:
    AssertionError: if num is not list
    AssertionError: if num element are not int or float
  
>>> sort_numbers([5, 6, 7, 1])
[1, 5, 6, 7]
>>> sort_numbers([1, 2, 3, 4])
[1, 2, 3, 4]
>>> sort_numbers([1.0, 1.0, 4.5, 2.0])
[1.0, 1.0, 2.0, 4.5]
"""
    assert isinstance(num, list), "Input must be a list."
    assert all(isinstance(x, (int, float)) for x in num), "All elements must be int or float."
    return sorted(num)
