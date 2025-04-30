"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  ADDIN MANASIYA
ID:      169044620
Email:   mana4620@mylaurier.ca
__updated__ = "2023-03-25"
-------------------------------------------------------
"""

from functions import validate_code

category, digits, qualifiers = validate_code('BFG9000x7')

print(f"({category}, {digits}, {qualifiers})")
