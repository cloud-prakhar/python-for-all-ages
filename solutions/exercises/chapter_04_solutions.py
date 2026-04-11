# Chapter 4 Exercise Solutions — Conditions (If/Elif/Else)
#
# NOTE FOR STUDENTS: Try the exercises yourself first before reading these solutions!
# Understanding WHY the solution works is more important than copying it.

print("=" * 50)
print("CHAPTER 4 EXERCISE SOLUTIONS")
print("=" * 50)


# --------------------------------------------------
# Exercise 1:
# Ask the user their age. If 18 or above → "You can vote!"
# Otherwise → "You cannot vote yet."
# --------------------------------------------------

print("\n--- Exercise 1 ---")

# Always cast input to int when expecting a whole number.
age = int(input("Enter your age: "))

# >= means "greater than OR equal to"
if age >= 18:
    print("You can vote!")
else:
    print("You cannot vote yet.")

# WHY else? If the if condition is False (age < 18),
# Python automatically jumps to the else block.


# --------------------------------------------------
# Exercise 2:
# Ask the user a number. Print if it is positive, negative, or zero.
# --------------------------------------------------

print("\n--- Exercise 2 ---")

number = float(input("Enter a number: "))

# We need 3 branches: positive, negative, and the special case of zero.
# Python checks top-to-bottom and stops at the FIRST True condition.
if number > 0:
    print(f"{number} is POSITIVE")
elif number < 0:
    print(f"{number} is NEGATIVE")
else:
    # If it's not > 0 and not < 0, it must be exactly 0.
    print(f"{number} is ZERO")


# --------------------------------------------------
# Exercise 3:
# Season Finder — ask for month number (1-12), print the season.
# Dec-Feb = Winter, Mar-May = Spring, Jun-Aug = Summer, Sep-Nov = Autumn
# --------------------------------------------------

print("\n--- Exercise 3 ---")

month = int(input("Enter month number (1-12): "))

# We check whether month falls within each season's range.
# 'or' means: if EITHER condition is True, the whole condition is True.
if month == 12 or month == 1 or month == 2:
    season = "Winter"
elif month >= 3 and month <= 5:   # months 3, 4, 5
    season = "Spring"
elif month >= 6 and month <= 8:   # months 6, 7, 8
    season = "Summer"
elif month >= 9 and month <= 11:  # months 9, 10, 11
    season = "Autumn"
else:
    # Handles invalid input (e.g. 0 or 13)
    season = "Invalid month"

print(f"Month {month} → Season: {season}")

# ALTERNATIVE: Python also lets you write "month in [12, 1, 2]" — cleaner!
# if month in [12, 1, 2]: season = "Winter"


# --------------------------------------------------
# Exercise 4:
# Ask the user for a password.
# If it's "python123" → "Access Granted!"
# Otherwise → "Wrong password."
# --------------------------------------------------

print("\n--- Exercise 4 ---")

# == compares two values — True if they are exactly the same.
# Remember: = assigns a value; == compares two values. They are DIFFERENT!
password = input("Enter password: ")

if password == "python123":
    print("Access Granted!")
else:
    print("Wrong password. Try again.")

# SECURITY NOTE: In real programs, passwords are never stored as plain text.
# This is just for practice!


# --------------------------------------------------
# Exercise 5:
# Zoo Ticket Price Calculator
# Age 0-3: Free | Age 4-12: Rs. 50 | Age 13-60: Rs. 100 | 60+: Rs. 40
# --------------------------------------------------

print("\n--- Exercise 5 ---")

visitor_age = int(input("Enter visitor's age: "))

# Each elif checks a range of ages — we go from youngest to oldest.
# Once a condition matches, Python skips all remaining elif/else blocks.
if visitor_age <= 3:
    price = 0
    category = "Child (0-3)"
elif visitor_age <= 12:
    price = 50
    category = "Child (4-12)"
elif visitor_age <= 60:
    price = 100
    category = "Adult (13-60)"
else:
    price = 40
    category = "Senior (60+)"

if price == 0:
    print(f"Category : {category}")
    print("Ticket   : FREE! Enjoy the zoo!")
else:
    print(f"Category : {category}")
    print(f"Ticket   : Rs. {price}")

# WHY this order? If we put age <= 60 before age <= 12, a 10-year-old
# would match the Adult condition first! Always check more specific ranges first.
