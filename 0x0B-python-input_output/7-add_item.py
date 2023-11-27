#!/usr/bin/python3
"""
This module contains a script that adds all arguments to a Python list,
and then saves them to a file using JSON representation.
"""
import sys


# Importing the necessary functions
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

# The name of the file to save the arguments to
filename = "add_item.json"

try:
    # Try to load the existing list from the file
    items = load_from_json_file(filename)
except FileNotFoundError:
    # If the file doesn't exist, create a new list
    items = []

# Add the command line arguments to the list
items.extend(sys.argv[1:])
# Save the list back to the file
save_to_json_file(items, filename)
