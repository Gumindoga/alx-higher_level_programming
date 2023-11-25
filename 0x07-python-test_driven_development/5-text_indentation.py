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
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not text:
        return

    chars = ""
    split = []
    for char in text:
        chars += char
        if char in ".?:":
            split.append(chars.strip())
            chars = ""

    if chars:
        split.append("".join(chars).strip())

    for line in split[:-1]:
        print(line)
        print("")
    print(split[-1], end="")
