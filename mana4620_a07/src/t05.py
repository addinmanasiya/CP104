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
from functions import check_sorted
from functions import list_of_positives

# call function and print return value
values = list_of_positives()
in_order, index = check_sorted(values)

print(f"check_sorted({values}) ->{in_order}, {index}")
