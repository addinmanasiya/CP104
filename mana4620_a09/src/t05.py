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

from functions import student_data

students = open("students.txt", "r", encoding="utf-8")


l_id, h_id, avg = student_data(students)
print(f"({l_id}, {h_id}, {avg:.2f})")

students.close()
