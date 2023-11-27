#!/usr/bin/python3
"""
This is the "101-locked_class" module.

The 101-locked_class module defines the LockedClass class.
"""


class LockedClass:
    """
    This is the LockedClass class.

    The LockedClass class prevents the user
    from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name.
    """

    __slots__ = ['first_name']
