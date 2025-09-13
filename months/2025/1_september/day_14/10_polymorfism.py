# Exercise: 10. Implementar Dog, Cat, Bird que herdam de Animal
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def make_sound(self) -> None:
        """Make a sound."""
        print("Standard sound.")


class Dog(Animal):
    def __init__(self):
        """Initiante a dog object."""
        super().__init__()
    
    def make_sound(self) -> None:
        """Make a dog sound."""
        print('Au Au.')


class Cat(Animal):
    def __init__(self):
        """Initiate a cat object."""
        super().__init__()

    def make_sound(self) -> None:
        """Make a cat sound."""
        print('Miau.')


class Bird(Animal):
    def __init__(self):
        """Initiate a bird object."""
        super().__init__()

    def make_sound(self) -> None:
        """Make a bird sound."""
        print('Diu fiu.')


animals = [Dog(), Cat(), Bird()]

for animal in animals:
    animal.make_sound()