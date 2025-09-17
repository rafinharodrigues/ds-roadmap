# Exercise: 12. Implementar __len__ para retornar total de elementos

from math import sqrt

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

    def __add__(self, other: object) -> 'Vector':
        """Add two vectors."""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: object) -> 'Vector':
        """Subtracts two vectors"""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: object) -> 'Vector':
        """Multiply two vectors"""
        return Vector(self.x * other, self.y * other)

    def __rmul__(self, other: object) -> 'Vector':
        """Multiply two vectors"""
        return self.__mul__(other)

    def __truediv__(self, other: float) -> 'Vector':
        """Divide a vector."""
        if other == 0:
            return ZeroDivisionError('Can not use zero for division.')
        else:
            return Vector(self.x / other, self.y / other)
            
    def __neg__(self) -> 'Vector':
        """Turn a vector into negative."""
        return Vector(-self.x, -self.y)
    
    def __abs__(self) -> float:
        """Turn a vector into negative."""
        return sqrt(self.x ** 2 + self.y ** 2)
    

class Matrix():
    def __init__(self, data: list[list[float]]) -> None:
        """Init a matrix object."""
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    def __getitem__(self, index: list[int, int]) -> float:
        """Get an item from the matrix giving an index."""
        if self.rows == 1:
            return self.data[0][index[1]]
        else:
            return self.data[index[0]][index[1]]

    def __setitem__(self, value: float, index: list[int, int]) -> float:
        """Set a value to the matrix giving an index."""
        if self.rows == 1:
            valueRemoved = self.data[0][index[1]]
            self.data[0][index[1]] = value
            return valueRemoved
        else:
            valueRemoved = self.data[index[0]][index[1]]
            self.data[index[0]][index[1]] = value
            return valueRemoved

    def __len__(self) -> int:
        """Get the matrix length."""
        return self.rows


m1 = Matrix([])

print(m1.__len__())