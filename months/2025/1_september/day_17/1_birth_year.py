# Exercise: 1. Implementar Person.from_birth_year(name, birth_year) com @classmethod
from datetime import datetime

class Person():
    def __init__(self, name: str, birthdate: datetime) -> None:
        """Initiate a Person object."""
        self.name = name
        self.birth_year = birthdate

    @classmethod
    def from_birth_year(cls, name: str, birth_year: datetime.year) -> str:
        """Initiate a Person object by the given birth year."""
        return cls(name, birth_year)
