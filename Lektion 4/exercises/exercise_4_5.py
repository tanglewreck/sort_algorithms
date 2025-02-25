"""
    exercise_4_5.py
    Uppgift: Hitta felet i koden och rätta
"""

__date__ = "2025-02-25"
__author__ = "mier"
__version__ = 0.1

class Flower:
    """Class docstring"""
    def __init__(self, name: str, color: str = None):
        """Method docstring"""
        self.name = name
        self.color = color
        self.species = "generisk blomma"

    def display_info(self):
        """Method docstring"""
        print(f"{self.name} är en {self.color} blomma.")

    def __str__(self):
        return f"{self.name}:  {self.color}"

    def __repr__(self):
        return f"{self.name} är en {self.species}"


class Tulip(Flower):
    """Class docstring"""
    def __init__(self, name: str, color: str, petals: int):
        """Method docstring"""
        super().__init__(name, color)
        self.petals = petals

    def display_info(self):
        """Method docstring"""
        print(f"{self.name} är en {self.color} tulpan med {self.petals} kronblad.")

    def __str__(self):
        return f"{self.name} är en {self.color} {self.species} som har {self.petals} kronblad"


generic_flower = Flower("generic flower", "generic colour")
# breakpoint()
tulip = Tulip("Vanlig tulpan", "röd", 6)
print(tulip)
tulip.display_info()
