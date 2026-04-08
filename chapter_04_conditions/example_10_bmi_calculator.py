# Example 10: BMI Calculator
# BMI (Body Mass Index) is used to assess whether a person's weight
# is healthy relative to their height.
# Formula: BMI = weight (kg) / height (m) ^ 2
# This example combines user input, arithmetic, and multi-branch conditions.

print("=== BMI Calculator ===")
print()

weight_kg = float(input("Enter your weight in kilograms (e.g. 70): "))
height_m  = float(input("Enter your height in meters (e.g. 1.75): "))

if height_m <= 0 or weight_kg <= 0:
    print("Invalid input. Height and weight must be positive numbers.")
else:
    bmi = weight_kg / (height_m ** 2)

    print(f"\nYour BMI: {bmi:.1f}")

    if bmi < 18.5:
        category = "Underweight"
        advice   = "Consider consulting a nutritionist for a balanced diet plan."
    elif bmi < 25.0:
        category = "Normal weight"
        advice   = "Great! Maintain your healthy lifestyle."
    elif bmi < 30.0:
        category = "Overweight"
        advice   = "Regular exercise and a balanced diet can help."
    else:
        category = "Obese"
        advice   = "Please consult a healthcare professional."

    print(f"Category: {category}")
    print(f"Advice  : {advice}")
