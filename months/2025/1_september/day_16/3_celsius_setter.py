# Exercise:  3. Implementar @celsius.setter com validação (>= -273.15)

class Temperature:
    def __init__(self, celsius) -> None:
        """Initiate a temperature object."""
        self.__celsius = celsius

    @property
    def celsius(self) -> float:
        """Allows to read the celsius attibute."""
        return self.__celsius
    
    @celsius.setter
    def set_celsius(self, value: float) -> None:
        """Getter: sett the celsius value with validation."""
        if isinstance(value, float):
            if value >= -273.15:
                self.__celsius = value
            else:
                return "The celsius value must be >= -273.15."
        else:
            raise TypeError("The celsius value must be float.")

