# Exercise: 2. Adicionar __eq__ e __hash__ para comparação de pontos

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

p1 = Point(10, 2)
p2 = Point(10, 2)

print(p1.__eq__(p2))
print(p1.__hash__() == p2.__hash__())