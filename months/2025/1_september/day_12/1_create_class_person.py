# Exercise: 1. Criar classe Person(name, age) com método celebrate_birthday()

class Person:
    def __init__(self, name: str, age: int) -> None:
        """
        Initiate a Person object.
        
        Args:
            name (str): A person name.
            age (int): A person age.
        """
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        """Print a birthday celebration message."""
        print("Happy Birthday!")


josh = Person(name='Josh', age=18)
josh.celebrate_birthday()