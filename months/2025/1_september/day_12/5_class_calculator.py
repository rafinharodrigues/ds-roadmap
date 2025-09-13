# Exercise: 5. Criar classe Calculator com métodos estáticos para +, -, *, /

class Calculator:
    def __init__(self, name: str) -> None:
        """Initiate a calculator object"""
        self.name = name

    @staticmethod
    def sum(value1: float, value2: float) -> float:
        """
        Sum 2 given values.

        Args:
            value1 (float): First number to sum.
            value2 (float): Second number to sum with the first one.

        Returns:
            result (float): The result sum number.
        """
        if isinstance(value1,float):
            if isinstance(value2,float):
                result = value1 + value2
                return result
            
        raise TypeError('The value numbers must be a float instance.')
    
    @staticmethod
    def sub(value1: float, value2: float) -> float:
        """
        Subtracts a value from a number.

        Args:
            value1 (float): First number to subtract.
            value2 (float): Second number to subtract from the first one.

        Returns:
            result (float): The final number. Result of the subtraction.
        """
        if isinstance(value1,float):
            if isinstance(value2, float):
                result = value1 - value2
                return result
            
        raise TypeError('The value numbers must be a float instance.')
    
    @staticmethod
    def mult(value1: float, value2: float) -> float:
        """
        Multiply 2 numbers.

        Args:
            value1 (float): First number to multiply.
            value2 (float): Second number to multiply with the first one.

        Returns:
            result (float): The final number. Result of the operation.
        """
        if isinstance(value1,float):
            if isinstance(value2, float):
                result = value1 * value2
                return result
            
        raise TypeError('The value numbers must be a float instance.')
        
    @staticmethod
    def div(value1: float, value2: float) -> float:
        """
        Divide two numbers.

        Args:
            value1 (float): The number to be divided.
            value2 (float): The number to divide the first one.

        Returns:
            result (float): The final number. Result of the operation.
        """
        if isinstance(value1,float):
            if isinstance(value2, float):
                result = value1 / value2
                return result
            
        raise TypeError('The value numbers must be a float instance.')
    
calculator1 = Calculator('calculadora1')
print(calculator1.sum(1.0, 4.0))
print(calculator1.sub(5.0, 5.0))
print(calculator1.mult(5.0, 5.0))
print(calculator1.div(5.0, 5.0))