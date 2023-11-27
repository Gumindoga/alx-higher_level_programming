#!/usr/bin/python3
"""
This module contains a function that appends a new string after each line
containing a specific string in a file.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Append a new string after each line containing a specific string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for.
        new_string (str): The new string to append.

    Returns:
        None
    """
    with open(filename, "r+") as f:
        lines = f.readlines()
        f.seek(0)
        f.truncate()
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
