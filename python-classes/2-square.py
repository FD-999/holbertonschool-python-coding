#!/usr/bin/python3
"""Fuad babaaa"""


class Square:
    """fd bababaaa"""

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """ASJJAJFDSJF"""
        return self.__size ** 2
