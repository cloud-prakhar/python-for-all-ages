# Example 4: Strings (Text)
# Strings are any text wrapped in quotes.
# Real life: Like words in a book or messages you send to friends!

# You can use single OR double quotes — both work the same way
first_name = "Arjun"
last_name  = 'Sharma'
favorite_food = "Pizza"
hobby      = "drawing"

print("First name:", first_name)
print("Last name:", last_name)

# -------------------------------------------------------
# JOINING STRINGS — Concatenation with +
# -------------------------------------------------------
# You can stick strings together using +
# Real life: like connecting two pieces of a name tag
full_name = first_name + " " + last_name
print("Full name:", full_name)

# -------------------------------------------------------
# F-STRINGS — the clean way to mix variables and text
# -------------------------------------------------------
# An f-string starts with the letter f right before the opening quote: f"..."
# Inside the string, anything you put between { } gets REPLACED by the
# actual value of that variable or expression.
#
# Think of { } as a blank space you fill in:
#   "My name is ___ and I love ___."
#   "My name is {first_name} and I love {favorite_food}."
#
# Python sees f"My name is {first_name}" and replaces {first_name} with "Arjun"
# Result: "My name is Arjun"
#
# WHY use f-strings instead of + ?
#   With + :  "My name is " + first_name + " and I love " + favorite_food + "!"
#   With f:   f"My name is {first_name} and I love {favorite_food}!"
#   f-strings are shorter, easier to read, and less error-prone.

print(f"My name is {first_name} and I love {favorite_food}!")
print(f"I enjoy {hobby} in my free time.")

# You can even do calculations inside the { }
age = 10
print(f"I am {age} years old. Next year I will be {age + 1}.")
