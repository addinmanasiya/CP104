"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  ADDIN MANASIYA
ID:      169044620
Email:   mana4620@mylaurier.ca
__updated__ = "2023-03-10"
-------------------------------------------------------
"""


def factorial_calculator(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = factorial_calculator(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """
    product = 1
    for i in range(1, number + 1):
        product = product * i
    return product


def cal_burned(per_min, minutes):
    """
    -------------------------------------------------------
    Prints a table of the number of calories burned every five 
    minutes given the number of calories burned per minute
    Use: cal_burned(per_min, minutes)
    -------------------------------------------------------
    Parameters:
        per_min - Calories burned per minute on treadmill (float > 0)
        minutes - Minutes spent running on treadmill (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    for min in range(5, minutes + 1, 5):
        caloriesBurned = min * per_min
        print(f"{min:>2d}:{caloriesBurned:7.1f}")
    return


def open_triangle_print(rows):
    """
    -------------------------------------------------------
    Print a triangle of # characters with an empty center
    Use: open_triangle_print(rows)
    -------------------------------------------------------
    Parameters:
        rows - The number of rows in the open triangle
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(rows):
        triangle = '#' + " " * i + "#"
        print(triangle)
    return


def mult_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: mult_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    answer = 0
    print("   ", end='')
    for num in range(start_num, stop_num + 1):
        print(f"{num:>5d}", end='')
    print()
    print("   -------------------------")
    for i in range(start_num, stop_num + 1):
        print(f"{i:>2d}|", end='')
        for j in range(start_num, stop_num + 1):
            answer = i * j
            print(f"   {answer:>2d}", end='')
        print("")
    return


def total_range(start_value, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum count values from start_value by increment.
    Use: sum_of_range = total_range(symbol, start_value, increment, count)
    -------------------------------------------------------
    Parameters:
        start_value - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        sum_of_range - the sum of the range (float)
    ------------------------------------------------------
    """
    total = 0
    for i in range(count):
        total = total + start_value
        start_value = start_value + increment
    return total
