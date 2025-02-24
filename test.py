def calculate_bmi(height: float, weight: float) -> float:
    return round(weight / ((height/100) ** 2), 2)


print(calculate_bmi(169,76))