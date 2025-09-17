# Exercise:  2. Criar @property celsius getter

class Temperature:
    def __init__(self, celsius) -> None:
        """Initiate a temperature object."""
        self.__celsius = celsius

    @property
    def celsius(self) -> float:
        """Allows to read the celsius attibute."""
        return self.__celsius
