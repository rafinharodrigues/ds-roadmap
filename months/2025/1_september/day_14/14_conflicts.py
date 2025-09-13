# Exercise: 14. Resolver conflitos de métodos usando super()

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def make_sound(self) -> None:
        """Make a sound."""
        print("Standard sound.")

class Flyable():
    def __init__(self) -> None:
        """Initiate a flyable object."""
        pass

    def fly(self) -> None:
        """Start's flying."""
        print('Flying.')


class Swimmable():
    def __init__(self) -> None:
        """Inititante a swimmable object."""
        pass

    def swim(self) -> None:
        """Start's swimming."""
        print('Swimming.')


class Duck(Animal, Flyable, Swimmable):
    def __init__(self) -> None:
        """Initiate a duck object."""
        super().__init__()