# Exercise: 6. Implementar classe Vector(x, y) com __add__, __sub__

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
    

class Vector:
    def __init__(self, x: int, y: int) -> None:
        """Initiate a vector object."""
        self.x = x
        self.y = y

    def __add__(self, other: object) -> tuple:
        """Add two vectors."""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: object) -> tuple:
        """Subtracts two vectors"""
        return Vector(self.x - other.x, self.y - other.y)



p1 = Vector(10, 8)
p2 = Vector(5, 3)

print(p1 - p2)