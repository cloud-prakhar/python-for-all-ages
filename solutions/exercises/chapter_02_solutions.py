# Chapter 2 Exercise Solutions — Variables & Data Types
#
# NOTE FOR STUDENTS: Try the exercises yourself first before reading these solutions!
# Understanding WHY the solution works is more important than copying it.

print("=" * 50)
print("CHAPTER 2 EXERCISE SOLUTIONS")
print("=" * 50)


# --------------------------------------------------
# Exercise 1:
# Create variables for: name (str), age (int), height (float), loves_coding (bool)
# Print them all with nice labels.
# --------------------------------------------------

print("\n--- Exercise 1 ---")

# Each variable holds a different type of data.
# str  → text (always in quotes)
# int  → whole number (no decimal point)
# float → number with a decimal point
# bool → only True or False (capital T/F, no quotes)
name = "Priya"
age = 14
height = 5.4        # in feet
loves_coding = True

print(f"Name        : {name}")
print(f"Age         : {age}")
print(f"Height      : {height} ft")
print(f"Loves coding: {loves_coding}")

# BONUS: You can always check the type of any variable using type()
print(f"Type of name         : {type(name)}")
print(f"Type of age          : {type(age)}")
print(f"Type of height       : {type(height)}")
print(f"Type of loves_coding : {type(loves_coding)}")


# --------------------------------------------------
# Exercise 2:
# Ask the user for their name and age.
# Store them in variables and print a greeting using those variables.
# --------------------------------------------------

print("\n--- Exercise 2 ---")

# input() always returns a STRING — even if the user types a number.
# So we use int() to convert the age to an actual number.
user_name = input("What is your name? ")
user_age = int(input("How old are you? "))

# Now we can do math with user_age because it's an int.
print(f"Hello, {user_name}! You are {user_age} years old.")
print(f"Next year you will be {user_age + 1}!")

# WHY int()? Without it, user_age would be a string like "14",
# and "14" + 1 would cause a TypeError in Python.


# --------------------------------------------------
# Exercise 3:
# Create a variable called "temperature" with value 37.5
# Print: "My temperature is 37.5 degrees. Am I sick? True/False"
# (Sick means temperature > 37.0)
# --------------------------------------------------

print("\n--- Exercise 3 ---")

temperature = 37.5

# A comparison like temperature > 37.0 evaluates to a Boolean (True or False).
# We store it in a variable so we can print it clearly.
is_sick = temperature > 37.0

print(f"My temperature is {temperature} degrees. Am I sick? {is_sick}")

# WHY: Comparisons always produce a bool result.
# 37.5 > 37.0 is True. 36.5 > 37.0 would be False.


# --------------------------------------------------
# Exercise 4:
# Use type() to check the type of: 42, 3.14, "hello", True
# Print the type of each.
# --------------------------------------------------

print("\n--- Exercise 4 ---")

# type() tells you what kind of data a value is.
# These are the 4 core data types in Python for beginners.
print(f"type(42)      = {type(42)}")       # <class 'int'>
print(f"type(3.14)    = {type(3.14)}")     # <class 'float'>
print(f'type("hello") = {type("hello")}') # <class 'str'>
print(f"type(True)    = {type(True)}")     # <class 'bool'>

# NOTICE: The output says <class 'int'> — everything in Python is an "object".
# For now, just remember: int = whole number, float = decimal, str = text, bool = True/False.


# --------------------------------------------------
# Exercise 5:
# Create a "My Dream Job" card using variables.
# Include: job name, salary, is_fun (bool), hours_per_day (int)
# --------------------------------------------------

print("\n--- Exercise 5 ---")

job_name = "Game Developer"
salary = 1_500_000       # 15 lakh — the _ is just for readability, Python ignores it
is_fun = True
hours_per_day = 8

print("=" * 35)
print("       MY DREAM JOB CARD        ")
print("=" * 35)
print(f"  Job          : {job_name}")
print(f"  Salary       : Rs. {salary:,} per year")   # :, adds thousand separators
print(f"  Is it fun?   : {is_fun}")
print(f"  Hours/day    : {hours_per_day}")
print("=" * 35)

# TIP: salary:,  in the f-string formats the number with commas: 1,500,000
# This is a format specifier — you will learn more in Chapter 7 (Strings).
