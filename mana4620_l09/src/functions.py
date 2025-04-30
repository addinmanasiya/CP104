"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  ADDIN MANASIYA
ID:      169044620
Email:   mana4620@mylaurier.ca
__updated__ = "2023-03-25"
-------------------------------------------------------
"""


def validate_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code and prints whether the various parts are valid.
    A product code has three parts:
        The first three letters describe the product category and must
        all be in upper case.
        The next four digits are the product ID.
        The remaining characters describe the product's qualifiers,
        such as colour, size, etc. and always begins with an uppercase letter.
    Use: category, digits, qualifiers = validate_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a product code (str)
    Returns:
        category - True if three upper-case characters, False otherwise
        digits - True if four digits, False otherwise
        qualifiers - True if starts with 1 upper-case letter, False otherwise
    -------------------------------------------------------
    """
    category, digits, qualifiers = False, False, False
    if (len(product_code) >= 3):
        if product_code[0:3].isupper():
            category = True

    if (len(product_code) >= 7):
        if product_code[3:7].isdigit():
            digits = True

    if (len(product_code) == 9):
        if product_code[7].isupper():
            qualifiers = True

    return category, digits, qualifiers


def is_hydroxide(chemical):
    """
    -------------------------------------------------------
    Determines if a chemical formula is a hydroxide.
    Use: hydroxide = is_hydroxide(chemical)
    -------------------------------------------------------
    Parameters:
        chemical - a chemical formula (str)
    Returns:
        hydroxide - True if chemical is a hydroxide (ends in 'OH'),
            False otherwise (boolean)
    -------------------------------------------------------
    """
    hydroxide = False
    if chemical.endswith("OH"):
        hydroxide = True
    return hydroxide


def parse_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code. A product code has three parts:
        The first three letters describe the product category
        The next four digits are the product ID
        The remaining characters describe the product's qualifiers
    Use: pc, pi, pq = parse_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a valid product code (str)
    Returns:
        pc - the category part of product_code (str)
        pi - the id part of product_code (str)
        pq - the qualifier part of product_code (str)
    -------------------------------------------------------
    """
    pc = product_code[0:3]
    pi = product_code[3:7]
    pq = product_code[7:100]
    return pc, pi, pq


def password_strength(password):
    """
    -------------------------------------------------------
    Checks the strength of a given password. A password is
    strong if it contains at least eight characters, has a
    combination of upper-case and lower-case letters, and
    includes digits. Prints one or more of:
        not long enough - if password less than 8 characters
        no digits - if password has no digits
        no upper case - if password has no upper case letters
        no lower case - if password has no lower case letters
    Use: password_strength(password)
    -------------------------------------------------------
    Parameters:
        password - the password to be checked (str)
    Returns:
        None
    ------------------------------------------------------
    """
    upper, digits, lower = False, False, False
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    nums = "0123456789"
    i, c, k = 0, 0, 0
    if len(password) < 8:
        print("not long enough")

    while not upper and i < len(password):
        if (password[i] in uppercase):
            upper = True
        i += 1

    while not lower and c < len(password):
        if (password[c] in lowercase):
            lower = True
        c += 1

    while not digits and k < len(password):
        if (password[k] in nums):
            digits = True
        k += 1

    if not digits:
        print("no digits")

    if not upper:
        print("no upper case")

    if not lower:
        print("no lower case")
    return


def text_analyze(txt):
    """
    -------------------------------------------------------
    Analyzes txt and returns the number of uppercase letters,
    lowercase letters, digits, and number of whitespaces in txt.
    Use: uppr, lowr, dgts, whtspc = text_analyze(txt)
    -------------------------------------------------------
    Parameters:
        txt - the text to be analyzed (str)
    Returns:
        uppr - number of uppercase letters in txt (int >= 0)
        lowr - number of lowercase letters in txt (int >= 0)
        dgts - number of digits in txt (int >= 0)
        whtspc - number of white spaces in the text (spaces, tabs, linefeeds) (int >= 0)
    ------------------------------------------------------
    """
    uppr, lowr, dgts, whtspc = 0, 0, 0, 0
    for i in txt:
        if i.isupper():
            uppr += 1
        elif i.islower():
            lowr += 1
        elif i.isdigit():
            dgts += 1
        elif i.isspace():
            whtspc += 1
    return uppr, lowr, dgts, whtspc
