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

from functions import text_analyze

uppr, lowr, dgts, whtspc = text_analyze(
    'Python uses whitespace indentation, rather than curly brackets or keywords, to delimit blocks.')

print(f"({uppr}, {lowr}, {dgts}, {whtspc})")
