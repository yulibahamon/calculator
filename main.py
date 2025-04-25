from fastapi import FastAPI, HTTPException
from app.models import SumRequest, CalculateRequest, CalculateResponse
from app.operations import Calculator
from app.errors import DivisionByZeroError


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
    
@app.post("/api/calculate", response_model=CalculateResponse)
async def calculate(request: CalculateRequest):
    """Realiza operaciones entre dos números.

        Escribe cualquiera de las siguientes operaciones en el campo 'operation':
        - subtract
        - multiplication
        - division
        - power

        Retorna la operación y el resultado de la operación realizada."""
    try:
        if request.operation == "subtract":
            result = Calculator.subtract(request.num1, request.num2)
        if request.operation == "multiplication":
            result = Calculator.multiply(request.num1, request.num2)
        elif request.operation == "division":
            result = Calculator.divide(request.num1, request.num2)
        elif request.operation == "power":
            result = Calculator.power(request.num1, request.num2)
        
        return CalculateResponse(result=result, operation=request.operation)
    
    except DivisionByZeroError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error interno del servidor")
