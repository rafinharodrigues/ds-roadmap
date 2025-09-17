# Exercise: 1. Implementar classe Point(x, y) com __init__, __str__, __repr__

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
    
p1 = Point(10, 2)

print(repr(p1))