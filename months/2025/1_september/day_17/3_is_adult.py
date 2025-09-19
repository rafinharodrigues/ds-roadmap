# Exercise: 3. Adicionar @staticmethod is_adult(age) -> bool
from datetime import datetime

class Person():
    def __init__(self, name: str, birthdate: datetime) -> None:
        """Initiate a Person object."""
        self.name = name
        self.birth_year = birthdate

    @classmethod
    def from_birth_year(cls, name: str, birth_year: datetime.year) -> object:
        """Initiate a Person object by the given birth year."""
        return cls(name, birth_year)
    
    @classmethod
    def from_string(cls, name_age_string: str) -> object:
        """Initiate a Person object by the string name_age"""
        name, age = name_age_string.split('_')
        return cls(name, age)
    
    @staticmethod
    def is_adult(age: int) -> bool:
        """Check if is an adult by the given age."""
        return True if age >= 18 else False