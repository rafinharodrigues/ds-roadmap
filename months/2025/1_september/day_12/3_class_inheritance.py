# Exercise: Criar classe Student(Person) que herda de Person + grade attribute

class Person:
    def __init__(self, name: str, birthdate: str) -> None:
        """Initiate a Person object."""
        self.name = name
        self.birthdate = birthdate


class Student(Person):
    def __init__(self, name: str, birthdate: str, grade: str) -> None:
        super().__init__(name, birthdate)
        self.grade = grade