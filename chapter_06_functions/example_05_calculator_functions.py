# Example 5: Calculator Using Functions
# Real life: A real calculator has separate buttons for +, -, *, /
# Each button is like a function!

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

# Use the calculator functions
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"\nAddition:       {add(num1, num2)}")
print(f"Subtraction:    {subtract(num1, num2)}")
print(f"Multiplication: {multiply(num1, num2)}")
print(f"Division:       {divide(num1, num2)}")
