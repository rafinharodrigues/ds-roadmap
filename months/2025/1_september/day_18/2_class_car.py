# Exercise: 2. Implementar classe Car que compõe Engine (não herda)

class Engine:
    def __init__(self, horsepower: int, type: str) -> None:
        """Initiate an Engine object."""
        self.horsepower = horsepower
        self.type = type


class Car:
    def __init__(self):
        """Initiate a car object."""
        self.engine = Engine(horsepower=250, type='SUV')