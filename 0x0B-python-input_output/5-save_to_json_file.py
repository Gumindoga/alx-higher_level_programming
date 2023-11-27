#!/usr/bin/python3
"""
Module for saving an object to a file using JSON
"""


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a text file,
    using a JSON representation
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))