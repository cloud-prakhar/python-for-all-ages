# Chapter 6 Exercise Solutions — Functions
#
# NOTE FOR STUDENTS: Try the exercises yourself first before reading these solutions!
# Understanding WHY the solution works is more important than copying it.

print("=" * 50)
print("CHAPTER 6 EXERCISE SOLUTIONS")
print("=" * 50)


# --------------------------------------------------
# Exercise 1:
# Write a function called "say_goodbye" that prints "Goodbye! See you tomorrow!"
# Call it 3 times.
# --------------------------------------------------

print("\n--- Exercise 1 ---")

# def keyword defines a function. The function body is indented under it.
# A function with no parameters just runs the same code every time it's called.
def say_goodbye():
    print("Goodbye! See you tomorrow!")

# Calling the function 3 times — we only wrote the logic once!
say_goodbye()
say_goodbye()
say_goodbye()

# WHY functions? If we decide to change the message, we only change it in
# ONE place (inside the function), not in all 3 call locations.


# --------------------------------------------------
# Exercise 2:
# Write a function called "square(number)" that returns number * number.
# Call it with 5, 8, and 12 and print the results.
# --------------------------------------------------

print("\n--- Exercise 2 ---")

# This function takes one INPUT (number) and returns one OUTPUT (the square).
# 'return' sends the result back to wherever the function was called from.
def square(number):
    return number * number

# We capture the returned value in a variable and then print it.
result_5 = square(5)
result_8 = square(8)
result_12 = square(12)

print(f"square(5)  = {result_5}")    # 25
print(f"square(8)  = {result_8}")    # 64
print(f"square(12) = {result_12}")   # 144

# IMPORTANT: return is different from print!
# print() just displays on screen — you can't use it in a calculation.
# return sends the value back — you CAN do: total = square(5) + square(3)


# --------------------------------------------------
# Exercise 3:
# Write a function "is_even(number)" that returns True if even, False if odd.
# Test it with numbers 1 through 10.
# --------------------------------------------------

print("\n--- Exercise 3 ---")

def is_even(number):
    # The modulus operator % gives the remainder after division.
    # If number % 2 == 0 (no remainder), the number is even.
    return number % 2 == 0

# Test all numbers from 1 to 10 using a loop
for n in range(1, 11):
    result = is_even(n)
    label = "even" if result else "odd"   # Ternary expression — works like if/else in one line
    print(f"  {n:>2} → {label}")

# HOW does number % 2 == 0 work?
# 4 % 2 = 0  (no remainder) → True  → even
# 7 % 2 = 1  (remainder 1)  → False → odd
# The comparison (== 0) already produces True or False, so we return it directly.


# --------------------------------------------------
# Exercise 4:
# Write a function "max_of_three(a, b, c)" that returns the largest of 3 numbers.
# Test it with at least 3 different sets of numbers.
# --------------------------------------------------

print("\n--- Exercise 4 ---")

def max_of_three(a, b, c):
    # Compare a against b first, then the winner against c.
    if a >= b and a >= c:
        return a       # a is the largest
    elif b >= a and b >= c:
        return b       # b is the largest
    else:
        return c       # c must be the largest

print(f"max_of_three(3, 7, 5)   = {max_of_three(3, 7, 5)}")    # 7
print(f"max_of_three(10, 2, 8)  = {max_of_three(10, 2, 8)}")   # 10
print(f"max_of_three(4, 4, 9)   = {max_of_three(4, 4, 9)}")    # 9
print(f"max_of_three(6, 6, 6)   = {max_of_three(6, 6, 6)}")    # 6 (all equal)

# BONUS: Python has a built-in max() function that can do this:
print(f"Using built-in max(): {max(3, 7, 5)}")
# But writing it yourself is great practice for understanding comparisons!


# --------------------------------------------------
# Exercise 5:
# Write a function "school_report(name, score)" that prints a report card.
# Include: student name, score, and a grade (A/B/C/D/F) based on the score.
# --------------------------------------------------

print("\n--- Exercise 5 ---")

def school_report(name, score):
    """
    Prints a formatted report card for a student.

    name  - student's name (string)
    score - their score out of 100 (number)
    """
    # Determine grade based on score range
    if score >= 90:
        grade = "A"
        remark = "Outstanding!"
    elif score >= 80:
        grade = "B"
        remark = "Well done!"
    elif score >= 70:
        grade = "C"
        remark = "Good effort!"
    elif score >= 60:
        grade = "D"
        remark = "Keep practising!"
    else:
        grade = "F"
        remark = "Please see your teacher."

    # Print the formatted report card
    print("-" * 35)
    print(f"  SCHOOL REPORT CARD")
    print("-" * 35)
    print(f"  Student : {name}")
    print(f"  Score   : {score}/100")
    print(f"  Grade   : {grade}")
    print(f"  Remark  : {remark}")
    print("-" * 35)

# Test the function with different students and scores
school_report("Rohan", 95)
school_report("Sneha", 78)
school_report("Arjun", 55)
