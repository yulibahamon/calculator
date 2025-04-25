from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

class SumRequest(BaseModel):
    numbers: List[float]