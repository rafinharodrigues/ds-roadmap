# Exercise: 3. Car.start() deve chamar engine.start()

class Engine:
    def __init__(self, horsepower: int, type: str) -> None:
        """Initiate an Engine object."""
        self.horsepower = horsepower
        self.type = type

    def start(self) -> None:
        """Start the engine."""
        print('Engine started.')


class Car:
    def __init__(self):
        """Initiate a car object."""
        self.engine = Engine(horsepower=250, type='SUV')

    def start(self) -> None:
        self.engine.start()