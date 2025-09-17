# Exercise:  6. Testar: temp.celsius = 25; print(temp.fahrenheit)

class Temperature:
    def __init__(self, celsius) -> None:
        """Initiate a temperature object."""
        self.__celsius = celsius

    @property
    def celsius(self) -> float:
        """Allows to read the celsius attibute."""
        return self.__celsius
    
    @property
    def fahrenheit(self) -> float:
        """Convert the celsius value to fahrenheit."""
        fahrenheit = (self.__celsius * 1.8) + 32
        return fahrenheit
    
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
        

temp1 = Temperature(25)

print(temp1.celsius)
print(temp1.fahrenheit)