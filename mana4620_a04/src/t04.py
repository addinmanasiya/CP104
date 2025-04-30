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
from functions import colour_mix

rgb_colour1 = input("First colour: ")
rgb_colour2 = input("Second colour: ")

rgb_colour = colour_mix(rgb_colour1, rgb_colour2)

print(f"colour_mix(rgb_colour1,rgb_colour2)  ->{rgb_colour}")
