"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  ADDIN MANASIYA
ID:      169044620
Email:   mana4620@mylaurier.ca
__updated__ = "2023-02-23"
-------------------------------------------------------
"""
from functions import largest_product

val1 = float(input("First Value: "))
val2 = float(input("Second Value: "))
val3 = float(input("Third Value: "))

product = largest_product(val1, val2, val3)

print(f"largest_product({val1 , val2 , val3}) -> {product}")
