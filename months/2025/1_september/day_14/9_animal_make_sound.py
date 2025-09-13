# Exercise: 9. Criar classe Animal com método make_sound()
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