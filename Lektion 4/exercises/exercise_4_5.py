"""
    exercise_4_5.py
    Uppgift: Hitta felet i koden och rätta
"""


__date__ = "2025-02-25"
__author__ = "mier"
__version__ = 0.1


class Flower:
    """Class docstring"""
    def __init__(self, name: str, color: str = None) -> None:
        """Method docstring"""
        self.name = name
        self.color = color
        self.species = "generisk blomma"

    def display_info(self) -> None:
        """Method docstring"""
        print(f"{self.name} är en {self.color} blomma.")

    def __str__(self) -> str:
        return f"{self.name}:  {self.color}"

    def __repr__(self) -> str:
        return f"{self.name} är en {self.species}"


class Tulip(Flower):
    """Class docstring"""
    def __init__(self, name: str, color: str, petals: int) -> None:
        """Method docstring"""
        super().__init__(name, color)
        self.petals = petals
        self.species = "tulpan"

    def display_info(self) -> None:
        """Method docstring"""
        print(str(self))

    def __str__(self) -> str:
        return f"{self.name} är en {self.color} "\
               f"{self.species} med {self.petals} kronblad"


generic_flower = Flower("generic flower", "generic colour")
# breakpoint()
tulip = Tulip("Vanlig tulpan", "röd", 6)
print(tulip)
tulip.display_info()
