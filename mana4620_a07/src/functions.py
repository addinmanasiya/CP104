"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  ADDIN MANASIYA
ID:      169044620
Email:   mana4620@mylaurier.ca
__updated__ = "2023-03-24"
-------------------------------------------------------
"""


def list_of_factors(number):
    """
    -------------------------------------------------------
    Takes an integer parameter and returns a list of the factors
    that make up that number
    Use: factors = list_of_factors(number)
    -------------------------------------------------------
    Parameters:
        number - The number to find factors for (int > 0)
    Returns:
        factors - List of all factors for numbers
    ------------------------------------------------------
    """
    count = 1
    factors = []
    while count < number:
        if number % count == 0:
            factors.append(count)
        count += 1
    return factors


def list_of_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: number_list = list_of_positives()
    -------------------------------------------------------
    Returns:
        number_list - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    numbers = []
    num = int(input("Enter a positive number: "))
    while num != 0:
        if num > 0:
            numbers.append(num)
        num = int(input("Enter a positive number: "))
    return numbers


def find_indexes(numbers, target_number):
    """
    -------------------------------------------------------
    Finds the indexes of target_number in numbers.
    Use: index_list = find_indexes(numbers, target_number)
    -------------------------------------------------------
    Parameters:
        numbers - list of values (list)
        target_number - value to look for in num_list (*)
    Returns:
        index_list - list of indexes of target_number (list of int)
    -------------------------------------------------------
    """
    locations = []
    for i in range(len(numbers)):
        if numbers[i] == target_number:
            locations.append(i)
    return locations


def list_subtraction(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtraction(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(len(subtrahend) + 1):
        for i in minuend:
            if i in subtrahend:
                minuend.remove(i)
    return


def check_sorted(numbers):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = check_sorted(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list)
    Returns:
        in_order - True if numbers is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    index = -1
    in_order = True
    i = 1
    while i < len(numbers) and in_order == True:
        if numbers[i] < numbers[i - 1]:
            index = i
            in_order = False
        i += 1
    return in_order, index
