#!/usr/bin/python3
"""
Module 3-say_my_name
Defines a function that prints "My name is <first name> <last name>"
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>"
    Arguments:
    first_name: string
    last_name: string
    """
    try:
        if type(first_name) is not str:
            raise TypeError("first_name must be a string")
        if type(last_name) is not str:
            raise TypeError("last_name must be a string")
        print(f"My name is {first_name} {last_name}", end="")
    except NameError:
        print("NameError: name '{}' is not defined".format(first_name))
