"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  ADDIN MANASIYA
ID:      169044620
Email:   mana4620@mylaurier.ca
__updated__ = "2023-02-23"
-------------------------------------------------------
"""
from functions import day_of_the_week

day_number = int(input("Please enter a number between 1 and 7: "))
day = day_of_the_week(day_number)
print(f"day_of_the_week({day_number})  ->  {day}")
