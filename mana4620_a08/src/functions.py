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


def insert_spaces(sentence):
    """
    -------------------------------------------------------
    Create a new sentence with added space between words. Words start
    with upper-case characters.
    Use: spaced_sentence = insert_spaces(sentence)
    -------------------------------------------------------
    Parameters:
        sentence - sentence that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is uppercase. sentence has at least one
            character (str)
    Returns:
        spaced_sentence - new sentence in which the words are separated
            by spaces and only the first word starts with
            an uppercase character (str)
    -------------------------------------------------------
    """
    spaced_sentence = sentence[0]
    for i in sentence[1:]:
        if i.isupper():
            spaced_sentence += " " + i.lower()
        else:
            spaced_sentence += i
    return spaced_sentence


def string_pluralizer(string):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', replace
            the 'y' with 'ies'
        - otherwise add 's'
    Use: pluralized_string = string_pluralizer(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        pluralized_string - a pluralized_string version of string (str)
    -------------------------------------------------------
    """
    if len(string) != 0:
        if string[-1] == "s" or string[-2:] == "sh" or string[-2:] == "ch":
            string += "es"
        elif string[-1] == "y" and string[-2:] != "ay" and string[-2:] != "oy":
            string = string[:-1] + "ies"
        else:
            string += "s"
    return string


def common_postfix(str1, str2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: postfix = common_postfix(str1, str2)
    -------------------------------------------------------
    Parameters:
        str1 - first string for ending comparison (str)
        str2 - second string for ending comparison (str)
    Returns:
        postfix - the longest common ending of str1 and str2 (str)
    -------------------------------------------------------
    """
    postfix = ""
    while not str1.endswith(str2):
        str2 = str2[1:]
    postfix = str2
    return postfix


def check_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: is_valid = check_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        is_valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """
    x = list(isbn.split('-'))

    if len(x) != 5 or len(x) != 17:
        is_valid = False

    for i in x:
        if not i.isdigit():
            is_valid = False
    if not (x[0] == "978" or x[0] == '979') or len(x[-1]) != 1:
        is_valid = False
    elif isbn.count("--") > 0:
        is_valid = False
    else:
        is_valid = True
    return is_valid


def check_word_chain(words):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: is_word_chain = check_word_chain(words)
    -------------------------------------------------------
    Parameters:
        words - a of strings (list of str, len > 1)
    Returns:
        is_word_chain - True if words is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    is_word_chain = True
    c = 0
    while c != (len(words) - 1):
        if words[c + 1][0] == words[c][-1]:
            is_word_chain = True
        else:
            is_word_chain = False
        c += 1
    return is_word_chain
