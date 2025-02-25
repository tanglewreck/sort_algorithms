"""
    exercise_4.4.py
    Date: 2025-02-25
"""
class Flower:
    """Class docstring"""
    def __init__(self, name, color):
        """Method docstring"""
        self.name = name
        self.color = color
        self.species = "generisk blomma"

    def display_info(self):
        """Method docstring"""
        print(f"{self.name} är en {self.color} blomma.")


    def __str__(self):
        return f"{self.name}: {self.color}"


class Rose(Flower):
    """Class docstring"""
    def __init__(self, name, color, fragrance):
        """Method docstring"""
        super().__init__(name, color)
        self.fragrance = fragrance
        self.species = "ros"


    def display_info(self):
        """Method docstring"""
        print(f"{self.name} är en {self.color} {self.species} som doftar {self.fragrance}.")


    def __add__(self, other):
        """Method docstring"""
        return f"{self.name} + {other.name}"


    def __str__(self):
        return f"{self.name} är en {self.color} {self.species} som doftar {self.fragrance}"


rose = Rose("Ros", "röd", "sött")
maskros = Flower("maskros", "gul")

print(rose)
print(rose + maskros)
