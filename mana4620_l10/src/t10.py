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

from functions import count_frequency_word

fileName = "words.txt"
fh = open(fileName, "r", encoding="utf-8")

print("file 'words.txt' open for reading")
word = input("Word to count: ")

count = count_frequency_word(fh, word)

fh.close()
print(f"{word} appears {count} time(s)")
