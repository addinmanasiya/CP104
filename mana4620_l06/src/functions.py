"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  ADDIN MANASIYA
ID:      169044620
Email:   mana4620@mylaurier.ca
__updated__ = "2023-03-06"
-------------------------------------------------------
"""


def sum_even(num):
    """
    -------------------------------------------------------
    Sums and returns the total of all even numbers from 2 to num (inclusive).
    Use: total = sum_even(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int > 0)
    Returns:
        total - sum of all even numbers from 2 to num (int)
    ------------------------------------------------------
    """
    total = 0
    for i in range(2, num+1, 2):
        total = total+i
    return total


def draw_rectangle(height, width, char):
    """
    -------------------------------------------------------
    Prints a rectangle of height and width characters using
    the char character.
    Use: draw_rectangle(height, width, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(height):
        print(f"{char}"*width)
    return


def bottles_of_beer(n):
    """
    -------------------------------------------------------
    Prints n verses of the song "99 Bottles of Beer on the Wall".
    Use: bottles_of_beer(n)
    -------------------------------------------------------
    Parameters:
        n - number of verses of the song to print (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(n - 2, -1, -1):
        print(f"{n} bottles of beer on the wall, {n} bottles of beer.")
        n = n - 1
        print(
            f"Take one down, pass it around, {n} bottles of beer on the wall.")
        print("--")
    print("1 bottle of beer on the wall, 1 bottle of beer.")
    print("Take one down, pass it around, no more bottles of beer on the wall!")
    return


def treadmill(burnt_per_minute, start, end, inc):
    """
    -------------------------------------------------------
    Calculates and prints calories burnt on a treadmill over
    a given time range.
    Use: treadmill(burnt_per_minute, start, end, inc)
    -------------------------------------------------------
    Parameters:
        burnt_per_minute - calories burnt per minute (float > 0)
        start - start time in minutes (int > 0)
        end - end time in minutes (int >= start)
        inc - increment in minutes (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    for e in range(start, end + 1, inc):
        burnt = e * burnt_per_minute
        print(f"Calories burned after {e} minutes: {burnt}")
    return


def statistics(n):
    """
    -------------------------------------------------------
    Asks a user to enter n values, then calculates and returns
    the minimum, maximum, total, and average of those values.
    Use: minimum, maximum, total, average = statistics(n)
    -------------------------------------------------------
    Parameters:
        n - number of values to process (int > 0)
    Returns:
        minimum - smallest of n values (float)
        maximum - largest of n values (float)
        total - total of n values (float)
        average - average of n values (float)
    ------------------------------------------------------
    """
    value = float(input("First value: "))
    minimum, maximum, total, average = value, value, value, 0
    for f in range(n - 1):
        value = float(input("Next value: "))
        if value < minimum:
            minimum = value
        if value > maximum:
            maximum = value
        total += value
    average = total / n
    return minimum, maximum, total, average
