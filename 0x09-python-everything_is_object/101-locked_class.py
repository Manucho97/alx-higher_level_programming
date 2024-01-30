#!/usr/bin/python3
"""defines a locked class"""


class LockedClass:
    """Only first_name attribute allowed """

    __slots__ = ["first_name"]
