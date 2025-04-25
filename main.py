from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import math
from app.models import SumRequest
from app.operations import Calculator


app = FastAPI()

@app.post("/api/sum")
async def sum_numbers(data: SumRequest ):
    try:
        result = Calculator.sum(data.numbers)
        return {"result": result, "operation": "sum"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))  
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error interno")