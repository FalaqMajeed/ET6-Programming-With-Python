""" Is in

Write a function that takes in a string and two lists of strings. 
It will return true if the item is in _at least one_ of the lists.

"""
def is_in(item:str,list1:list,list2:list) -> bool:
    """Returns true if the item is in at least one  of the list

    Args:
      item (str): the input string
      list1 (list): the input list 1
      list2 (list): the input list 2
  Returns: true if the string is in the list
  Raises:
  AssertionError: if the item is not string
  AssertionError: if the list1 is not a list
  AssertionError: if the list2 is not a ist
    
>>> is_in('cat', ['cat', 'hat'], ['cat', 'bat'])
True
>>> is_in('lena', ['falaq', 'shafaq','lena'], ['apple', 'banana'])
True
>>> is_in('Hey', ['hello', 'hi'], ['this','there'])
False
"""
    assert isinstance(item, str)
    assert isinstance(list1, list)
    assert isinstance(list2, list)
    return item in list1 or item in list2
