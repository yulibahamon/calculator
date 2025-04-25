from fastapi import FastAPI
from pydantic import BaseModel, field_validator
from typing import List

class SumRequest(BaseModel):
    numbers: List[float]

class CalculateRequest(BaseModel):
    num1: float
    num2: float
    operation: str
    
    @field_validator('operation')
    @classmethod
    def validate_operation(cls, operation):
        valid_operations = ["subtract", "multiplication", "division", "power"]
        if operation not in valid_operations:
            raise ValueError(f"Operación no válida. Operaciones permitidas: {', '.join(valid_operations)}")
        return operation

class CalculateResponse(BaseModel):
    result: float
    operation: str