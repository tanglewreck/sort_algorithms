"""exercise_4.3 doc string"""


class Animal:
    """Class doc string"""
    def __init__(self, name="Generic animal") -> None:
        """Method doc string"""
        self.name = name
        self.sound = "nothing"
        self.class_name = "Animal"

    def make_sound(self) -> str:
        """Method doc string"""
        # print(f"{self.name} says {self.sound}")
        return self.sound

    def __str__(self) -> str:
        """Method doc string"""
        if self.class_name[0] in ['A', 'E', 'I', 'O', 'U', 'Y']:
            article = "An"
        else:
            article = "A"
        return f"{article} {self.class_name} says '{self.sound}'"


class Dog(Animal):
    """Class doc string"""
    def __init__(self, name: str = None) -> None:
        """Method doc string"""
        super().__init__(name)
        self.sound = "woof"
        self.class_name = "Dog"


class Cat(Animal):
    """Class doc string"""
    def __init__(self, name: str = None) -> None:
        super().__init__(name)
        self.sound = "meow"
        self.class_name = "Cat"


def main() -> None:
    """function doc string"""
    # Print what (a generic) animal of each class says
    print(str(Animal()))
    print(str(Dog()))
    print(str(Cat()))
    print()

    # Create an animal object and print what it says
    animal = Animal()
    print(f"{animal.name} says '{animal.make_sound()}'")

    # Create a dog object and print what it says
    dog = Dog("Buddy")
    print(f"{dog.name} says '{dog.make_sound()}'")

    # Create a cat object and print what it says
    cat = Cat("Pussy")
    print(f"{cat.name} says '{cat.make_sound()}'")


if __name__ == "__main__":
    main()
