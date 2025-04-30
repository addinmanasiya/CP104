"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  ADDIN MANASIYA
ID:      169044620
Email:   mana4620@mylaurier.ca
__updated__ = "2023-04-07"
-------------------------------------------------------
"""

from functions import extract_integers

file_handle = open("numbers.txt", "r", encoding="utf-8")

number_list = extract_integers(file_handle)

print(number_list)

file_handle.close()
