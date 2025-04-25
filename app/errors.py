class DivisionByZeroError(Exception):
    """Error que se lanza cuando se intenta dividir por cero."""
    def __init__(self, message="No se puede dividir por cero"):
        self.message = message
        super().__init__(self.message)
        
    def __str__(self):
        return self.message


