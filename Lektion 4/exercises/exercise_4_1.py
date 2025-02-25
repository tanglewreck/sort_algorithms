"""foo"""


class Rectangle:
    """A rectangle class"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """compute and return area"""
        return self.width * self.height

    def perimeter(self):
        """return perimeter"""
        return (self.width + self.height) * 2


class Square(Rectangle):
    """Square"""
    def __init__(self, side_length):
        """__init__"""
        super().__init__(side_length, side_length)
        self.side_length = side_length

    def perimeter(self):
        """compute and return perimeter"""
        return 4 * self.side_length


square = Square(5)
print("Area:", square.area())
print("Perimeter:", square.perimeter())
