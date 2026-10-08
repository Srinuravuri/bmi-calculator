import math


def calculate_bmi():
    print("--- BMI CALCULATOR ---")
    name = input("Enter your name: ")

    try:
        weight = float(input("Enter your weight in pounds: "))
        height = float(input("Enter your height in inches: "))
    except ValueError:
        print("Error: Please enter valid numeric values for weight and height.")
        return

    if not math.isfinite(weight) or not math.isfinite(height) or weight <= 0 or height <= 0:
        print("Error: Please enter valid positive inputs.")
        return

    bmi = (weight * 703) / (height * height)
    name = name.strip() or "Friend"
    print(f"\n{name}, your BMI is: {bmi:.2f}\n")

    if bmi < 18.5:
        category = "Underweight"
        risk = "Minimal"
    elif bmi < 25:
        category = "Normal weight"
        risk = "Minimal"
    elif bmi < 30:
        category = "Overweight"
        risk = "Increased"
    elif bmi < 35:
        category = "Obese"
        risk = "High"
    elif bmi < 40:
        category = "Severely obese"
        risk = "Very high"
    else:
        category = "Morbidly obese"
        risk = "Extremely high"

    print(f"Category: {category}")
    print(f"Health Risk: {risk}")
    print("\n*Disclaimer: This is a general screening number, not medical advice.*")


if __name__ == "__main__":
    calculate_bmi()
