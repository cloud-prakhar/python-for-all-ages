# Chapter 3 Exercise Solutions — Operators
#
# NOTE FOR STUDENTS: Try the exercises yourself first before reading these solutions!
# Understanding WHY the solution works is more important than copying it.

print("=" * 50)
print("CHAPTER 3 EXERCISE SOLUTIONS")
print("=" * 50)


# --------------------------------------------------
# Exercise 1:
# You have 50 rupees. You spend 18 on a pencil box and 12 on an eraser.
# How much money do you have left?
# --------------------------------------------------

print("\n--- Exercise 1 ---")

starting_money = 50
pencil_box_cost = 18
eraser_cost = 12

# Subtract both purchases from the starting amount.
money_left = starting_money - pencil_box_cost - eraser_cost

print(f"Starting money : Rs. {starting_money}")
print(f"Pencil box     : Rs. {pencil_box_cost}")
print(f"Eraser         : Rs. {eraser_cost}")
print(f"Money left     : Rs. {money_left}")

# WHY variables? We could write 50 - 18 - 12 directly,
# but using descriptive names makes the code much easier to read and change.


# --------------------------------------------------
# Exercise 2:
# 29 students, 4 groups.
# How many complete groups? How many students are left over?
# Use // and % operators.
# --------------------------------------------------

print("\n--- Exercise 2 ---")

students = 29
groups = 4

# // is integer (floor) division — gives the whole number of groups
complete_groups = students // groups

# % is the modulus (remainder) operator — gives what's left over
leftover_students = students % groups

print(f"Total students   : {students}")
print(f"Number of groups : {groups}")
print(f"Complete groups  : {complete_groups}")    # 7
print(f"Students left over: {leftover_students}") # 1

# ANALOGY: Think of dividing pizza. 29 slices ÷ 4 people = 7 slices each,
# with 1 slice left over. // gives 7, % gives 1.


# --------------------------------------------------
# Exercise 3:
# Ask the user for two numbers.
# Print whether the first is greater than, less than, or equal to the second.
# --------------------------------------------------

print("\n--- Exercise 3 ---")

# input() returns a string — we need float() so we can compare decimal numbers too.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# > and < are comparison operators — they return True or False.
if num1 > num2:
    print(f"{num1} is GREATER THAN {num2}")
elif num1 < num2:
    print(f"{num1} is LESS THAN {num2}")
else:
    print(f"{num1} is EQUAL TO {num2}")

# NOTE: We're using if/elif/else here — that's Chapter 4!
# This is a preview of how operators combine with conditions.


# --------------------------------------------------
# Exercise 4:
# has_ticket = True, is_above_height = False
# Print: "Can you ride the ride?" using 'and' logic.
# --------------------------------------------------

print("\n--- Exercise 4 ---")

has_ticket = True
is_above_height = False

# 'and' means BOTH conditions must be True to ride.
# If either one is False, the result is False.
can_ride = has_ticket and is_above_height

print(f"Has ticket        : {has_ticket}")
print(f"Is above height   : {is_above_height}")
print(f"Can you ride?     : {can_ride}")

# TRUTH TABLE for 'and':
# True  and True  → True   ← can ride
# True  and False → False  ← needs to be taller
# False and True  → False  ← needs a ticket
# False and False → False  ← needs both

# TRY: Change is_above_height = True and run again — now can_ride becomes True!


# --------------------------------------------------
# Exercise 5:
# Calculate the area of a rectangle.
# Ask the user for length and width. Area = length * width.
# --------------------------------------------------

print("\n--- Exercise 5 ---")

# float() allows decimal inputs like 5.5 metres
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# The formula for area of a rectangle is simple: length × width
area = length * width

# :.2f in the f-string means "show exactly 2 decimal places"
print(f"Length : {length} units")
print(f"Width  : {width} units")
print(f"Area   : {area:.2f} square units")
