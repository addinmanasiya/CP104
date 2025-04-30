"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  ADDIN MANASIYA
ID:      169044620
Email:   mana4620@mylaurier.ca
__updated__ = "2023-03-17"
-------------------------------------------------------
"""

from math import fabs


def total_wins():
    """
    -------------------------------------------------------
    Determine how many times user entered 'blue' and 'grey'
    when asked for winning team
    Use: numBlue, numGrey = total_wins()
    -------------------------------------------------------
    Parameters:
        None
    Returns:
        numBlue - Number of times the user entered 'blue'
        numGrey - Number of times the user entered 'grey'
    ------------------------------------------------------
    """
    numBlue = 0
    numGrey = 0
    print("total_wins() ->")
    winningTeam = input("Enter the winning team: ")
    while winningTeam != "":
        if winningTeam == "blue":
            numBlue += 1
        elif winningTeam == "grey":
            numGrey += 1
        winningTeam = input("Enter the winning team: ")
    return numBlue, numGrey


def is_prime_number(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number.
    Use: is_prime = is_prime_number(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        is_prime - True if number is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    prime = True
    count = 2
    while prime and count < number:
        if number % count == 0:
            prime = False
        count += 1
    return prime


def interest_data(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_data(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    balance = principal_amount
    monthlyRate = (interest_rate / 100) / 12
    month = 0
    print(f"interest_data{principal_amount, interest_rate, payment} ->")
    print(f"Principal: ${principal_amount:.2f}")
    print(f"Interest interest rate: {interest_rate:.2f}%")
    print(f"Monthly payment: ${payment:.2f}")
    print("----------------------------------")
    print("Month Interest   Payment   Balance")
    print("----------------------------------")
    while balance > payment:
        interest = balance * monthlyRate
        balance = balance - payment + interest
        month += 1
        print(f"{month:>5d}{interest:9.2f}{payment:10.2f}{balance:10.2f}")
    month += 1
    interest = balance * monthlyRate
    payment = balance + interest
    balance = balance - balance
    print(f"{month:>5d}{interest:9.2f}{payment:10.2f}{balance:10.2f}")
    return


def count_digits(number):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: digits = count_digits(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        digits - the number of digits in number (int)
    ------------------------------------------------------
    """
    count = 0
    if number == 0:
        count = 1
    else:
        number = fabs(number)
        while number != 0:
            number //= 10
            count += 1
    return count


def sum_of_factors(number):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = sum_of_factors(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        total - the total of number's factors (int)
    ------------------------------------------------------
    """
    count = 1
    total = 0
    while count < number:
        if number % count == 0:
            total += count
        count += 1
    return total
