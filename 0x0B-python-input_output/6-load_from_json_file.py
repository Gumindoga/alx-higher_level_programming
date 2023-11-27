#!/usr/bin/python3
"""
Module for loading an object from a file using JSON
"""
import json


def load_from_json_file(filename):
    """
    Function that creates an Object from a “JSON file”
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())
