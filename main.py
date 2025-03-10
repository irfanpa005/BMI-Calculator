from fastapi import FastAPI, Form, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(debug=True)

# Function to calculate BMI
def calculate_bmi(height: float, weight: float) -> float:
    if height <= 0 or weight <= 0:
        raise ValueError("Height and weight must be greater than zero.")
    return round(weight / ((height / 100) ** 2), 2)

# Function to classify BMI category
def bmi_category(bmi: float) -> str:
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"


# API endpoint using Form input
@app.post("/calculate-bmi")
def get_bmi(
    name: str = Form(...),
    age: int = Form(...),
    gender: str = Form(...),
    height: float = Form(...),
    weight: float = Form(...)
):
    try:
        if age <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Age must be greater than zero."
            )

        if gender.lower() not in ["male", "female", "other"]:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid gender. Use 'Male', 'Female', or 'Other'."
            )
        
        bmi_value = calculate_bmi(height, weight)
        category = bmi_category(bmi_value)

        return {
            "name": name,
            "age": age,
            "gender": gender,
            "height": height,
            "weight": weight,
            "bmi": bmi_value,
            "category": category
        }

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific origins if necessary
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)
