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
from functions import level_of_pollution

air_quality_index = int(input("Enter AQI: "))
pollution_level = level_of_pollution(air_quality_index)
print(f"level_of_pollution({air_quality_index}) -> {pollution_level} ")
