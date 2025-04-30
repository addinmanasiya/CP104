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
from functions import customer_append

# open connection to file
fileName = "customers.txt"
fh = open(fileName, "a", encoding="utf-8")

# define list to append
fields = ['35612', 'David', 'Brown', 237.56, '2008-10-10']

# call function
customer_append(fh, fields)

# close file and print confirmation
fh.close()
print(f"Data: {fields}")
print("data appended to file")
