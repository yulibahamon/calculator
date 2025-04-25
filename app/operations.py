from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from typing import List

class Calculator:
    
    def sum(numbers) -> float:
        if not numbers:
            raise ValueError("La lista no puede estar vacía")
        if len(numbers) < 2:
            raise ValueError("Se requieren al menos dos números para sumar")
        return sum(numbers)


