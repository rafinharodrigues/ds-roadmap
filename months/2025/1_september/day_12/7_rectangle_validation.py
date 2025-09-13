# Exercise: 7. Adicionar getters/setters com validação (width > 0)

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


rectangle = Rectangle(0, 0)
print(rectangle.se, rectangle.height)

rectangle.width = 0
rectangle.height = 0
print(rectangle.width, rectangle.height)

