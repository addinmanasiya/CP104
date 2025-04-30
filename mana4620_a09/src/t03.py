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

from functions import text_stats

file_handle = open("addresses.txt", "r", encoding="utf-8")

ucount, lcount, dcount, wcount = text_stats(file_handle)

print(f"({ucount}, {lcount}, {dcount}, {wcount})")

file_handle.close()
