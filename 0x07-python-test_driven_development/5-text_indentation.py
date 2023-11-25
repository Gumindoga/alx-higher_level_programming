#!/usr/bin/python3
"""
Module 5-text_indentation
Defines a function that prints a text with 2 new lines after: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    Arguments:
    text: string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')
    if text == "":
        print("")
        return
    else:
        print("\n".join([line.strip() for line in text.split('\n')]), end="")
