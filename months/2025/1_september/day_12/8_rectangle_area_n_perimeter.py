# Exercise: 8. Criar método area() e perimeter()

class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        """Initiante a rectangle object."""
        self._width = width
        self._height = height
    
    @property
    def width(self) -> int:
        """Getter: Allow to access the _width as an attribute."""
        return self._width
    
    @property
    def height(self) -> int:
        """Getter: Allow to access the _height as an attribute."""
        return self._height
    
    @width.setter
    def width(self, width: int) -> None:
        """
        Setter: Set's the width value.
        
        Args:
            width (int): Width value.
        """
        if width > 0:
            self._width = width
    
        raise ValueError('The width must be > 0.')
    
    @height.setter
    def height(self, height: int) -> None:
        """
        Setter: Set's the height value.
        
        Args:
            height (int): height value.
        """
        if height > 0:
            self._height = height

        raise ValueError('The height must be > 0.')
    
    def area(self) -> float:
        """
        Returns the rectangle area (width * height).

        Returns:
            area (float): The rectangle area.
        """
        area = self._width * self._height
        return area
    
    def perimeter(self) -> float:
        """
        Returns the rectangle perimeter (2*width + 2*height).

        Returns:
            perimeter (float): The rectangle perimeter.
        """
        perimeter = (2 * self._width) + (2 * self._height)
        return perimeter

rectangle = Rectangle(0, 0)
print(rectangle.se, rectangle.height)

rectangle.width = 1080
rectangle.height = 1920
print(rectangle.width, rectangle.height)

print(rectangle.area())
print(rectangle.perimeter())

