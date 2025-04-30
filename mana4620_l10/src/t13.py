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
# Imports
from functions import file_copy

# open connection to files
fileName = "words.txt"
fileName2 = "new_words.txt"
fh_1 = open(fileName, "r", encoding="utf-8")
fh_2 = open(fileName2, "a", encoding="utf-8")

# get input
print("Copying 'words.txt' to 'new_words.txt'")

# call function
file_copy(fh_1, fh_2)

# close files
fh_1.close()
fh_2.close()
