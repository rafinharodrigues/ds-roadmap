# Exercise: 10. Adicionar validação: raio deve ser positivo

class Circle:
    def __init__(self, radius: int) -> None:
        """Initiate a circle object."""
        self.__radius = radius

    @property
    def radius(self) -> int:
        """Getter: Allow to access __radius as an attribute."""
        return self.__radius
    
    @radius.setter
    def radius(self, radius: int) -> None:
        """
        Setter: Set's the radius values checking if it is a positive 
                value
        """
        if radius > 0:
            self.__radius = radius
        else:
            raise ValueError('The radius value must be > 0.')
        

circle = Circle(10)

print(circle.radius)
circle.radius = 0
circle.radius = 20
print(circle.radius)