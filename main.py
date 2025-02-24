from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI Calculator"}

@app.get("/add")
def add(a: float, b: float):
    return {"operation": "addition", "result": a + b}

@app.get("/subtract")
def subtract(a: float, b: float):
    return {"operation": "subtraction", "result": a - b}

@app.get("/multiply")
def multiply(a: float, b: float):
    return {"operation": "multiplication", "result": a * b}

@app.get("/divide")
def divide(a: float, b: float):
    if b == 0:
        return {"error": "Cannot divide by zero"}
    return {"operation": "division", "result": a / b}
