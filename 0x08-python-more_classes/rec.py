#!/usr/bin/python3
'''A module that defines a rectangle'''


class Rectangle:
    '''Represents a Rectangle'''

    def __init__(self, width=0, height=0):
        '''Initializing the rectangle
        Args:
            Width: represents the width of the rectangle
            Height: represents the height of the rectangle
        Raises:
            TypeErro: if width or height is not an integer
            ValueError: if width or height is less than 0
        '''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''Retrieves width attribute of a rectangle'''
        return self.__width
    
    @width.setter
    def width(self, value):
        '''sets width attribute of a rectangle'''
        if not isinstance(self, int):
            raise TypeError('self must be an integer')
        if self < 0:
            raise ValueError('self must be >= 0')
        
        self.__width = value

    @property
    def height(self):
        '''Retrieves width of a rectangle'''
        return self.__height
    
    @height.setter
    def height(self, value):
        '''Sets the height attribute of a rectangle'''
        if not isinstance(self, int):
            raise TypeError('self must be an integer')
        if self < 0:
            raise ValueError('self must be >= 0')
        
        self.__height = value
