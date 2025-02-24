"""exercise_4.2 doc string"""
class Shape:
    """Class doc string"""
    def __init__(self, color):
        """__init__ doc string"""
        self.color = color


    def display_color(self):
        """Method doc string"""
        print(f"This shape is {self.color}.")


    def __str__(self):
        """Return string representation of the object"""
        return str(self.color)


class Circle(Shape):
    """Class doc string"""
    def __init__(self, color, radius):
        """Method doc string"""
        super().__init__(color)
        self.radius = radius

    def display_radius(self):
        """Method doc string"""
        print(f"The radius of this circle is {self.radius}.")

    def __str__(self):
        """Return string representation of the object"""
        return f"{str(self.color)}, {str(self.radius)}"



def main():
    """main"""
    circle = Circle("Red", 5)
    circle.display_color()
    circle.display_radius()
    print(str(circle))


if __name__ == "__main__":
    main()
