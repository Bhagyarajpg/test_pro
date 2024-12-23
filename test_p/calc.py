from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import math

app = FastAPI()

class CalculationRequest(BaseModel):
    operation: str
    numbers: List[float]
#testing calculator program
@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Calculator API!"}
#sample calculator project created by bhagyaraj
#changes added from local
@app.post("/calculate/")
def calculate(request: CalculationRequest):
    try:
        if request.operation == "add":
            result = sum(request.numbers)
        elif request.operation == "subtract":
            result = request.numbers[0] - sum(request.numbers[1:])
        elif request.operation == "multiply":
            result = math.prod(request.numbers)
        elif request.operation == "divide":
            try:
                result = request.numbers[0]
                for num in request.numbers[1:]:
                    result /= num
            except ZeroDivisionError:
                raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
        elif request.operation == "power":
            result = math.pow(request.numbers[0], request.numbers[1])
        else:
            raise HTTPException(status_code=400, detail="Invalid operation.")

        return {"operation": request.operation, "numbers": request.numbers, "result": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
