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

from functions import file_header

file_handle = open("students.txt", "r", encoding="utf-8")
file_header(file_handle, 5)
file_handle.close()
