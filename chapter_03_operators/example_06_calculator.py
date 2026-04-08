# Example 6: Mini Calculator
# Real life: Let's build our own calculator!
#
# NEW CONCEPTS IN THIS EXAMPLE:
#
# 1) NESTED FUNCTION CALLS — float(input(...))
#    You already know input() asks the user to type something.
#    You already know float() converts text to a decimal number.
#    Here we combine them: float(input("Enter a number: "))
#
#    Python evaluates this INSIDE-OUT:
#      Step 1: input("Enter the first number: ") runs first → user types "7.5" → returns the STRING "7.5"
#      Step 2: float("7.5") runs on that result            → converts to the NUMBER 7.5
#
#    Why do we need float()?
#    Because input() ALWAYS returns a string — even if the user types a number.
#    "7.5" (string) ≠ 7.5 (number). You can't do math with a string.
#    float() converts it to a real number we can calculate with.
#
# 2) FORMAT SPECIFIER :.2f inside f-strings
#    {num1 / num2:.2f} means:
#      - Calculate num1 / num2
#      - Display the result as a float (f) with exactly 2 decimal places (.2)
#    Example: 7.5 / 2 = 3.75  →  displays as  3.75
#    Example: 10 / 3 = 3.333… →  displays as  3.33
#    See: reference/python_symbols_guide.md for more on format specifiers.

num1 = float(input("Enter the first number: "))   # string → float
num2 = float(input("Enter the second number: "))  # string → float

print(f"\n--- Results ---")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")

# Guard against dividing by zero — this would crash the program!
if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2:.2f}")  # :.2f → 2 decimal places
else:
    print("Cannot divide by zero!")
