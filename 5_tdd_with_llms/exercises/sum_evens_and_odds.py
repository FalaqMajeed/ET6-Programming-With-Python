""" Sum Evens and Odds

Write a function that takes a list of numbers 
and returns a dictionary with sums of the even and odd numbers in the list.

"""
def sum_evens_and_odds(numbers: list) -> dict:
    """
    Takes a list and returns a dictionary with sums of the even and odd numbers in the list.

    Args:
        numbers (list): List of numbers (int or float).

    Returns:
        dict: Sum of odd and even numbers.

    Raises:
        AssertionError: When `numbers` is not a list.
        AssertionError: When any item in `numbers` is not an int or float.

    Examples:
        >>> sum_evens_and_odds([1, 2, 3, 4, 5])
        {'even_sum': 6, 'odd_sum': 9}
        >>> sum_evens_and_odds([])
        {'even_sum': 0, 'odd_sum': 0}
        >>> sum_evens_and_odds([1.0, 2.0, 3.0, 4.0, 5.0])
        {'even_sum': 6.0, 'odd_sum': 9.0}
    """
    assert isinstance(numbers, list), "Input must be a list."
    even_sum = 0
    odd_sum = 0

    for number in numbers:
        assert isinstance(number, (int, float)), "All items in the list must be int or float."
        if number % 2 == 0:
            even_sum += number
        else:
            odd_sum += number

    return {'even_sum': even_sum, 'odd_sum': odd_sum}
