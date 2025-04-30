"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  ADDIN MANASIYA
ID:      169044620
Email:   mana4620@mylaurier.ca
__updated__ = "2023-04-06"
-------------------------------------------------------
"""


def file_header(file_handle, count):
    """
    -------------------------------------------------------
    Prints first count lines of file_handle. Line numbering starts at 0.
    If length of file is shorter than count, stops printing after
    last line of file.
    Use: file_header(file_handle, count)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
        count - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    i = 0
    line = file_handle.readline().strip()
    while line != "" and i != count:
        print(line)
        line = file_handle.readline().strip()
        i += 1
    return


def extract_integers(file_handle):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: number_list = extract_integers(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        number_list - a list of integers from file_handle (list of int)
    -------------------------------------------------------
    """
    i = 0
    numbers = []
    for lines in file_handle:
        num = lines.strip().split(",")
        for i in num:
            if i.isdigit():
                numbers.append(int(i))
    return numbers


def text_stats(file_handle):
    """
    -------------------------------------------------------
    Evaluates the contents of a file by counting upper-case letters,
    lower-case letters, digits, and white-spaces (including end-of-line
    characters).
    Use: ucount, lcount, dcount, wcount = text_stats(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        ucount - The number of upper-case letters in the file (int)
        lcount - The number of lower-case letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of white-space characters in the file (int)
    -------------------------------------------------------
    """
    ucount, lcount, dcount, wcount = 0, 0, 0, 0
    for line in file_handle:
        for i in line:
            if i.isupper():
                ucount += 1
            elif i.islower():
                lcount += 1
            elif i.isdigit():
                dcount += 1
            elif i.isspace():
                wcount += 1
    return ucount, lcount, dcount, wcount


def add_numbers(fh_read, fh_write):
    """
    -------------------------------------------------------
    Adds line numbers to a file. Contents of fh_write contain contents
    of fh_read where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.
    Use: add_numbers(fh_read, fh_write)
    -------------------------------------------------------
    Parameters:
        fh_read - file to read (file - open for reading)
        fh_write - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """
    i = 0
    for line in fh_read:
        fh_write.write(f"[{i}] {line}")
        i += 1
    return


def student_data(file_handle):
    """
    -------------------------------------------------------
    Get information from a file of file_handle and grades.
    Use: l_id, h_id, avg = student_data(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - student information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    -------------------------------------------------------
    """
    l_id, h_id = "", ""
    lowest, highest, count, total, avg = 100, 0, 0, 0, 0
    line = file_handle.readline().strip()
    while line != "":
        data = line.split(",")
        if int(data[3]) < lowest:
            lowest = int(data[3])
            l_id = data[2]
        if int(data[3]) > highest:
            highest = int(data[3])
            h_id = data[2]
        count += 1
        total += int(data[3])
        line = file_handle.readline().strip()
    avg = total / count
    return l_id, h_id, avg
