"""
    exercise_4_6.py
    Uppgift: Skapa en klass Animal med attributen name och species.

"""


__date__ = "2025-02-25"
__author__ = "mier"
__version__ = 0.1


class Animal:
    """Class docstring"""
    def __init__(self, name: str = "generic animal",
                 species: str = "generic species",
                 sound: str = "silence") -> None:
        """Method docstring"""
        self.name = name
        self.species = species
        self.sound = sound

    def makes_sound(self, sound: str = None) -> None:
        """Method docstring"""
        if sound:
            self.sound = sound
            return self.sound
        return None

    def __str__(self):
        """Method docstring"""
        return f"{self.name} is a(n) {self.species} "\
               f"that makes the sound {self.sound}"


def info():
    """Function docstring"""
    print()
    print(f"date: {__date__}")
    print(f"author: {__author__}")
    print(f"version: {__version__}")


def main() -> None:
    """Function docstring"""
    a_generic_animal = Animal()
    cheetah = Animal("flashy", "cheetah", "MEOW")
    elephant = Animal("Dummbboo", "elephant", "tooooooooot")
    print(a_generic_animal)
    print(elephant)
    print(cheetah)


if __name__ == "__main__":
    main()
    # info()
