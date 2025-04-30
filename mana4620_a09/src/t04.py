"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  ADDIN MANASIYA
ID:      169044620
Email:   mana4620@mylaurier.ca
__updated__ = "2023-04-06"
-------------------------------------------------------
"""

from functions import add_numbers

fh_read = open("wilde.txt", "r", encoding="utf-8")
fh_write = open("wilde_numbered.txt", "w", encoding="utf-8")

add_numbers(fh_read, fh_write)

fh_read.close()
fh_write.close()
