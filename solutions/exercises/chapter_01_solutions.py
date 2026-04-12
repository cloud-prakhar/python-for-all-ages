# Chapter 1 Exercise Solutions — Setup & First Programs
#
# NOTE FOR STUDENTS: Try the exercises yourself first before reading these solutions!
# Understanding WHY the solution works is more important than copying it.
##
print("=" * 50)
print("CHAPTER 1 EXERCISE SOLUTIONS")
print("=" * 50)


# --------------------------------------------------
# Exercise 1:
# Print your full name on one line and your city on the next line.
# --------------------------------------------------

print("\n--- Exercise 1 ---")

# We use two separate print() calls — each one moves to the next line automatically.
print("Arjun Sharma")
print("Mumbai")

# WHY: Every print() call ends with a newline by default.
# If you wanted them on the same line, you'd use print(..., end=" ")


# --------------------------------------------------
# Exercise 2:
# Print a short story about yourself using at least 4 print() statements.
# --------------------------------------------------

print("\n--- Exercise 2 ---")

# Each print() is one sentence/line in the story.
print("My name is Arjun and I am 12 years old.")
print("I live in Mumbai with my family.")
print("I love playing cricket and reading books.")
print("My dream is to become a software engineer!")

# TIP: You can print anything you like here — there is no single "right" answer.
# As long as you have at least 4 print() calls, your solution is correct!


# --------------------------------------------------
# Exercise 3:
# Ask the user for their name AND their favorite color.
# Then print: "Hello [name]! [color] is a great color!"
# --------------------------------------------------

print("\n--- Exercise 3 ---")

# input() pauses the program and waits for the user to type something.
# The text typed is stored in a variable so we can use it later.
name = input("What is your name? ")
color = input("What is your favorite color? ")

# f-string lets us embed variables directly inside the string using {}
print(f"Hello {name}! {color} is a great color!")


# --------------------------------------------------
# Exercise 4:
# Print this pattern exactly:
# ***
# ***
# ***
# --------------------------------------------------

print("\n--- Exercise 4 ---")

# Option 1: Three separate print statements (simplest approach)
print("***")
print("***")
print("***")

# Option 2 (bonus — using a loop — covered in Chapter 5):
# for i in range(3):
#     print("***")

# WHY: Both are correct. The loop version is better when the pattern is large
# because you only need to change one number instead of many lines.


# --------------------------------------------------
# Exercise 5:
# Print a mini menu for a restaurant with at least 3 food items.
# Format it nicely with a header and borders!
# --------------------------------------------------

print("\n--- Exercise 5 ---")

# We use a separator line to create borders — the * 30 repeats the string 30 times.
print("=" * 30)
print("   KRISHNA'S KITCHEN — MENU   ")
print("=" * 30)
print("  1. Paneer Butter Masala  Rs.180")
print("  2. Dal Tadka             Rs.120")
print("  3. Butter Naan           Rs.40")
print("  4. Mango Lassi           Rs.80")
print("=" * 30)

# TIP: The spaces before each item are just regular spaces inside the string.
# You can use as many as you like to align things nicely.
