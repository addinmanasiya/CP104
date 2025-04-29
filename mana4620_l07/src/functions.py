"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  ADDIN MANASIYA
ID:      169044620
Email:   mana4620@mylaurier.ca
__updated__ = "2023-03-11"
-------------------------------------------------------
"""
from random import randint


def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    num = randint(1, high)
    guess = int(input("Guess: "))
    count = 1
    while guess != num:
        if guess > num:
            print("Too high, try again.")
            count += 1
        elif guess < num:
            print("Too low, try again.")
            count += 1
        guess = int(input("Guess: "))
    print("Congratulations")
    return count


def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """
    power = 1
    exponent = 0
    while power < target:
        power = 2**exponent
        exponent = exponent + 1
    return power


def sum_squares(target):
    """
    -------------------------------------------------------
    Determines the sum of squares closest to, and greater than or
    equal to, a target value.
    Use: final = sum_squares(target)
    -------------------------------------------------------
    Parameters:
        target - target value (int >= 0)
    Returns:
        final - the final sum of squares >= target (int)
    -------------------------------------------------------
    """
    final = 0
    sum = 0
    while final <= target:
        final += (sum**2)
        sum += 1
    return final


def meal_costs():
    """
    -------------------------------------------------------
    Asks a user the costs of breakfast, lunch, and supper for each
    day the user was away. Assumes there is at least one day, and
    after entering data for each day asks the user whether they want
    to enter data for another day. Calculates total costs for meals.
    Use: b_total, l_total, s_total, a_total = meal_costs()
    -------------------------------------------------------
    Returns:
        b_total - total breakfasts cost (float)
        l_total - total lunches cost (float)
        s_total - total suppers cost (float)
        a_total - all meals cost (float)
    ------------------------------------------------------
    """
    b_total, l_total, s_total, a_total, day = 0, 0, 0, 0, 1
    bcost, lcost, scost, daytotal = 0, 0, 0, 0
    away = "Y"

    while away == "Y":
        print(f"For Day {day}")
        day += 1
        print("")
        bcost = float(input("How much was breakfast? $"))
        lcost = float(input("How much was lunch? $"))
        scost = float(input("How much was supper? $"))
        daytotal = bcost + lcost + scost
        b_total += bcost
        l_total += lcost
        s_total += scost
        print(f"Your total for the day was ${daytotal:.2f}")
        print("")
        away = input("Were you away for another day (Y/N)? ")

    a_total = b_total + l_total + s_total
    return b_total, l_total, s_total, a_total


def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """
    # constants
    TAXRATE = 0.03625
    OVERTIMERATE = 1.5
    OVERTIMEHOURS = 40
    # declare variables
    total = 0
    average = 0
    count = 0
    # ask for employee ID
    employeeID = int(input("Employee ID: "))
    # start while loop
    while employeeID != 0:
        hourlyWage = float(input("Hourly wage rate: "))
        hoursWorked = float(input("Hours worked: "))
        if hoursWorked > 40:
            overtimeRate = hourlyWage * OVERTIMERATE
            overtimeHours = hoursWorked - OVERTIMEHOURS
            overtimePay = overtimeHours * overtimeRate
            regularPay = 40 * hourlyWage
            netPayment = overtimePay + regularPay
        else:
            netPayment = hourlyWage * hoursWorked
        netPayment = netPayment - (netPayment * TAXRATE)
        print(f"Net payment for employee {employeeID}: ${netPayment:,.2f}")
        total = total + netPayment
        count = count + 1
        employeeID = int(input("\nEmployee ID: "))
    average = total / count
    return total, average
