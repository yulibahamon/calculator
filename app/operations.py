from app.errors import DivisionByZeroError

class Calculator:
    
    def sum(numbers) -> float:
        """suma números de una lista."""
        if not numbers:
            raise ValueError("La lista no puede estar vacía")
        if len(numbers) < 2:
            raise ValueError("Se requieren al menos dos números para sumar")
        return sum(numbers)
    
    def subtract(num1, num2):
        """Resta num1 menos num2"""
        return num1 - num2

    def multiply(num1, num2):
        """Multiplica num1 por num2"""
        return num1 * num2
    
    def divide(num1, num2):
        """Divide  numeraod Num1 por Denominadofr num2  
            DivisionByZeroError: Si el denominador es cero.
        """
        if num2 == 0:
            raise DivisionByZeroError("No se puede dividir por cero")
        return num1 / num2
    
    def power(num1, num2):
        """Calcula la potencia de un número num1 aelevado a num2"""
        return num1 ** num2

