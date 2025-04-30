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
from functions import customer_record

fh = open("customers.txt", "r", encoding="utf-8")
print("Find record n")
n = int(input("Enter a record number: "))
print(customer_record(fh, n))
fh.close
