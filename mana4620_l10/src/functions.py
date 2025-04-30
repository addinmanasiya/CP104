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


def customer_record(fh, n):
    """
    -------------------------------------------------------
    Find the n-th record in a comma-delimited sequential file.
    Records are numbered starting with 0.
    Use: result = customer_record(fh, n)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        n - the number of the record to return (int > 0)
    Returns:
        result - a list of the fields of the n-th record if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    line = fh.readline().strip()
    count = 0
    result = []
    while line != "":
        data = line.split(",")
        if count == n:
            result = data
        count += 1
        line = fh.readline().strip()
    return result


def customer_append(fh, fields):
    """
    -------------------------------------------------------
    Appends a customer record to a comma-delimited sequential file.
    Use: customer_append(fh, fields)
    -------------------------------------------------------
    Parameters:
        fh - file to add to (file handle - already open for appending)
        fields - a list of the field data to append to the file (list)
    Returns:
       None
    -------------------------------------------------------
    """
    line = ""
    for i in fields:
        line = line + str(i) + ","
    fh.write(f"{line[:-1]}\n")
    return


def number_stats(fh):
    """
    -------------------------------------------------------
    Returns statistics on the numbers in a file.
    Assumes file is not empty.
    Use: smallest, largest, total, average = number_stats(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        smallest - smallest number (int)
        largest - largest number (int)
        total - sum of all the numbers in the file (int)
        average - average of all the numbers (float)
    ------------------------------------------------------
    """
    line = fh.readline().strip()
    smallest, largest, total, average, count = 100, 0, 0.00, 0.00, 0
    while line != "":
        num = int(line)
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
        total += num
        count += 1
        line = fh.readline().strip()
    average = total / count
    return smallest, largest, total, average


def count_frequency_word(fh, word):
    """
    -------------------------------------------------------
    Counts the number of appearances of word in fh.
    Case is significant - line in file must match word in case.
    Use: count = count_frequency_word(fh, word)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        word - the word to search for it in fh (str)
    Returns:
        count - the number of appearance of word in fh (int)
    ------------------------------------------------------
    """
    count = 0
    for line in fh:
        line = line.strip()
        if line == word:
            count += 1
    return count


def file_copy(fh_1, fh_2):
    """
    -------------------------------------------------------
    Copies the contents of fh_1 to fh_2.
    Any contents of fh_2 are overwritten.
    Use: file_copy(fh_1, fh_2)
    -------------------------------------------------------
    Parameters:
        fh_1 - source file (file handle - already open for reading)
        fh_2 - target file (file handle - already open for writing)
    Returns:
        None
    ------------------------------------------------------
    """
    fh_2.truncate(0)
    for line in fh_1:
        line = line.strip()
        fh_2.write(f"{line}\n")
    return
