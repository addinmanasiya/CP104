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

# imports
from functions import list_subtraction
from functions import list_of_positives

print("Minuend")
minuend = list_of_positives()
print("\nSubtrahend")
subtrahend = list_of_positives()

print(f"list_subtraction({minuend},{subtrahend} ) ->")
# call function and update list
list_subtraction(minuend, subtrahend)

# print updated list

print(f"minuend after:{minuend}")
