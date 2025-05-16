from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Basic Calculator API")

# Request model
class Operation(BaseModel):
    a: float
    b: float

# Response model
class Result(BaseModel):
    result: float

@app.get("/")
def read_root():
    return {"message": "Calculator API is running"}

@app.post("/add", response_model=Result)
def add(operation: Operation):
    return {"result": operation.a + operation.b}

@app.post("/subtract", response_model=Result)
def subtract(operation: Operation):
    return {"result": operation.a - operation.b}

@app.post("/multiply", response_model=Result)
def multiply(operation: Operation):
    return {"result": operation.a * operation.b}

@app.post("/divide", response_model=Result)
def divide(operation: Operation):
    if operation.b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"result": operation.a / operation.b}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=10000, reload=True)
