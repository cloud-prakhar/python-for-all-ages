# Example 4: Grade Checker
# Real life: What grade did you get on your test?
#
# NEW CONCEPT: int(input(...)) — nested function call
#
#   input() always returns a STRING — even if the user types a number.
#   We need an INTEGER to compare with >= 90, >= 80, etc.
#   So we wrap input() inside int() to convert immediately:
#
#     int( input("Enter your test score (0-100): ") )
#          ↑                                         ↑
#          └─ Step 2: convert the string to an int  ─┘
#               ↑
#               └─ Step 1: ask the user, get a string back
#
#   Python evaluates inside-out: input() first, then int() on the result.
#   If the user types  85  → input() gives "85" → int("85") gives 85

score = int(input("Enter your test score (0-100): "))

if score >= 90:
    grade   = "A+"
    message = "Outstanding! You're a star!"
elif score >= 80:
    grade   = "A"
    message = "Excellent work! Keep it up!"
elif score >= 70:
    grade   = "B"
    message = "Good job! Practice a little more."
elif score >= 60:
    grade   = "C"
    message = "You passed! Study harder next time."
elif score >= 40:
    grade   = "D"
    message = "Don't give up! Ask your teacher for help."
else:
    grade   = "F"
    message = "Needs improvement. Let's study together!"

print(f"\nYour score: {score}")
print(f"Your grade: {grade}")
print(message)
