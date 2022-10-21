#!/usr/bin/python3
"""Creating module with square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits the attributes of the Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize class Rectangle"""
        self.size = size
        super().__init__(self.size, self.size, x, y, id)

    def __str__(self):
        """Returns a string"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        attributes = ["id", "size", "x", "y"]
        for attri, arg in zip(attributes, args):
            setattr(self, attri, arg)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """return dictionary representation"""
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
