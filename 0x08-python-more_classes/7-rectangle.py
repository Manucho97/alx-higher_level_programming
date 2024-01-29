#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """this represents a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializing this rectangle class
        Args:
            width: represents the width of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: if width or height is not an integer
            ValueError: if width or height is less than 0
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retrieves width attribute"""

        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """retrieves height attribute"""

        return self.__height

    @height.setter
    def height(self, value):
        """sets height attribute"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Returns area of a rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of a rectangle"""

        if self.__height == 0 or self.__width == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self) -> str:
        """presents a diagram of the rectangle defined for an object"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                rectangle += f'{self.print_symbol}'
            if column < self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """prints a text each time an instance is deleted"""
        del self
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
