# Exercise: 1. Criar hierarquia: Shape -> Circle, Rectangle, Triangle

class Shape:
    def __init__(self, kind: str) -> None:
        """Initiate a shape object."""
        self.kind = kind

class Circle(Shape):
    def __init__(self, kind: str, radius: int) -> None:
        """Initiate a circle object."""
        super().__init__(kind)
        self.radius = radius

class Rectangle(Shape):
    def __init__(self, kind: str, width: int, height: int) -> None:
        """Inititate a rectangle object."""
        super().__init__(kind)
        self.width = width
        self.height = height

class Triangle(Shape):
    def __init__(self, kind: str, side_size1: int, side_size2: int, side_size3: int) -> None:
        """Initiate a triangle object."""
        super().__init__(kind)
        self.side_size1 = side_size1
        self.side_size2 = side_size2
        self.side_size3 = side_size3