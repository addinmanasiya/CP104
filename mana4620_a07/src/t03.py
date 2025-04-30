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
from functions import find_indexes
from functions import list_of_positives

# call function to get user input for list
values = list_of_positives()
target = int(input("\nEnter a target number: "))
# call function to get location of indexes
locations = find_indexes(values, target)

# print output
print(f"find_indexes({values},{target}) ->{locations}")
