# Example 2: All Math Operators
# Real life: You use all of these every day without knowing it!
#
# WHY CURLY BRACES { } IN THE PRINT STATEMENTS?
#   Look at this line:   print(f"{a} + {b} = {a + b}")
#
#   The "f" before the opening quote makes this an f-STRING (formatted string).
#   Inside an f-string, anything you put between { } is NOT printed as text —
#   instead, Python EVALUATES it and inserts the RESULT.
#
#   So:   f"{a} + {b} = {a + b}"
#   With a=20, b=6, Python reads this as:
#         "20" + " + " + "6" + " = " + "26"
#   And prints:  20 + 6 = 26
#
#   { } in an f-string = "put the VALUE of this expression here"
#   Text outside { }   = printed exactly as written
#
#   Without f-strings, you'd have to write:
#       print(str(a) + " + " + str(b) + " = " + str(a + b))
#   f-strings are much cleaner!
#
#   See: reference/python_symbols_guide.md for the full symbols guide.

a = 20
b = 6

print(f"{a} + {b} = {a + b}")      # Addition        → 20 + 6 = 26
print(f"{a} - {b} = {a - b}")      # Subtraction     → 20 - 6 = 14
print(f"{a} * {b} = {a * b}")      # Multiplication  → 20 * 6 = 120
print(f"{a} / {b} = {a / b}")      # Division        → 20 / 6 = 3.3333... (always a float)
print(f"{a} // {b} = {a // b}")    # Floor Division  → 20 // 6 = 3 (drops the decimal part)
print(f"{a} % {b} = {a % b}")      # Modulus/Remainder → 20 % 6 = 2 (what's left after division)
print(f"2 ** 10 = {2 ** 10}")      # Exponentiation  → 2^10 = 1024
