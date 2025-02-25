"""
    exercise_4_5.py
    Uppgift: Hitta felet i koden och rätta
"""

__date__ = "2025-02-25"
__author__ = "mier"
__version__ = 0.1

class Flower:
    """Class docstring"""
    def __init__(self, name: str, color: str):
        """Method docstring"""
        self.name = name
        self.color = color

    def display_info(self):
        """Method docstring"""
        print(f"{self.name} är en {self.color} blomma.")


class Tulip():
    """Class docstring"""
    def __init__(self, name: str, color: str, petals:int ):
        """Method docstring"""
        super().__init__(name, color)
        self.petals = petals

    def display_info(self):
        """Method docstring"""
        print(f"{self.name} är en {self.color} tulpan {self.petals} kronblad.")


tulip = Tulip("Vanlig tulpan", "röd") # 6)
tulip.display_info()
