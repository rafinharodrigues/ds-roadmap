# Exercise: 4. Implementar método is_valid() para cada forma

from abc import ABC, abstractmethod
from math import sqrt


class Shape(ABC):
    def __init__(self, kind: str) -> None:
        """Initiate a shape object."""
        self.kind = kind

    @abstractmethod
    def calculate_area(self):
        """Calculate the shape area."""
        pass

    @abstractmethod
    def is_valid(self):
        """Check if the shapes are valid."""
        pass

class Circle(Shape):
    def __init__(self, kind: str, radius: int) -> None:
        """Initiate a circle object."""
        super().__init__(kind)
        self.radius = radius

    def calculate_area(self):
        """
        Calculate the circle area.

        Returns:
            area (float): The calculated area.
        """
        area = 3.14 * (self.radius ** 2)
        return area
    
    def is_valid(self) -> bool:
        """
        Check if the given circle radius is valid.
        
        Returns:
            (bool): True if valid, False if not.
        """
        if self.radius > 0:
            return True
        else:
            return False 

class Rectangle(Shape):
    def __init__(self, kind: str, width: int, height: int) -> None:
        """Inititate a rectangle object."""
        super().__init__(kind)
        self.width = width
        self.height = height

    def calculate_area(self):
        """
        Calculate the ractangle area.

        Returns:
            area (int): The calculated area.
        """
        area = self.width * self.height
        return area
    
    def is_valid(self) -> bool:
        """
        Check if the width and height is valid.
        
        Returns:
            (bool): True if valid, False if not.
        """
        if self.width > 0 and self.height > 0:
            return True
        else:
            return False 

class Triangle(Shape):
    def __init__(self, kind: str, side_size1: int, side_size2: int, side_size3: int) -> None:
        """Initiate a triangle object."""
        super().__init__(kind)
        self.side_size1 = side_size1
        self.side_size2 = side_size2
        self.side_size3 = side_size3
    
    def calculate_area(self):
        """
        Calculate the triangle area.

        Returns:
            area (float): The calculated area.
        """
        peri = (self.side_size1 + self.side_size2 + self.side_size3) / 2 
        area = sqrt(peri * (peri - self.side_size1) * (peri - self.side_size2) * (peri - self.side_size3))
        return area
    
    def is_valid(self) -> bool:
        """
        Check if the given triangle sides are valid.
        
        Returns:
            (bool): True if valid, False if not.
        """
        if self.side_size1 > 0 and self.side_size2 > 0 and self.side_size3 > 0: 
            if self.side_size1 + self.side_size2 > self.side_size3:
                return True
            elif self.side_size2 + self.side_size3 > self.side_size1:
                return True
            elif self.side_size1 + self.side_size3 > self.side_size2:
                return True
            else:
                return False
        else:
            return False

         
    
class Square(Rectangle):
    def __init__(self, kind: str, width: int, height: int):
        """Inititate a square object."""
        super().__init__(kind, width, height)
        self.width = width
        self.height = height

    def calculate_area(self):
        """
        Calculate the square area.

        Returns:
            area (float): The calculated area.
        """
        area = self.width * self.height
        return area

    def is_valid(self) -> bool:
        """
        Check if the square sides are valid.
        
        Returns:
            (bool): True if valid, False if not.
        """
        if self.width > 0 and self.height > 0:
            return True
        else:
            return False 
