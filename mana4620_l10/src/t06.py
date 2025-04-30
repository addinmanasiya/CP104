"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  ADDIN MANASIYA
ID:      169044620
Email:   mana4620@mylaurier.ca
__updated__ = "2023-03-31"
-------------------------------------------------------
"""

from functions import number_stats

fileName = "numbers.txt"
fh = open(fileName, "r", encoding="utf-8")

smallest, largest, total, average = number_stats(fh)
print(
    f"Smallest: {smallest}\nLargest: {largest}\nTotal: {total:.2f}\nAverage: {average:.2f}")
