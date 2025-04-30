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

from functions import matrix_stats

smallest, largest, total, average = matrix_stats(
    [[4, 3.5, 2.25], [6.1, 9.3, 4.5]])

print(f"({smallest}, {largest}, {total}, {average})")
