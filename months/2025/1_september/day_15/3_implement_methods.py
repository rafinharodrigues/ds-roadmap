# Exercise: 3. Implementar __lt__, __le__, __gt__, __ge__ para ordenação

class Point:
    def __init__(self, x: int, y: int) -> None:
        """Initiate a point object."""
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """Returns a human friendly object signature."""
        return f'{Point.__name__}: {self.x}, {self.y}'
    
    def __repr__(self) -> str:
        """Returns a technical object signature."""
        return f'{Point.__name__}(x={self.x}, y={self.y})'
    
    def __eq__(self, obj: object):
        """Compares 2 objects."""
        return isinstance(obj, Point) and self.x == obj.x and self.y == obj.y
    
    def __hash__(self) -> int:
        """Returns the hash number that represents the objet."""
        return hash((self.x, self.y))
    
    def __lt__(self, other: object) -> bool:
        """Returns if this object is lower than other."""
        return (self.x, self.y) < (other.x, other.y)
    
    def __le__(self, other: object) -> bool:
        """Returns if this object is lower or equal than other."""
        return (self.x, self.y) <= (other.x, other.y)

    def __gt__(self, other: object) -> bool:
        """Returns if this object is greater than other."""
        return (self.x, self.y) > (other.x, other.y)

    def __ge__(self, other: object) -> bool:
        """Returns if this object is greater or equal than other."""
        return (self.x, self.y) >= (other.x, other.y)

