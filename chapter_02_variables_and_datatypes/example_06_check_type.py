# Example 6: Checking Data Types with type()
# type() is like an X-ray machine — it tells you WHAT is inside a variable!
# Real life: Like reading the label on a box to know what's inside.

age = 9
height = 4.2
name = "Meera"
is_happy = True

print(type(age))        # <class 'int'>
print(type(height))     # <class 'float'>
print(type(name))       # <class 'str'>
print(type(is_happy))   # <class 'bool'>

# Let's make it cleaner to read
print(f"age is of type: {type(age)}")
print(f"height is of type: {type(height)}")
print(f"name is of type: {type(name)}")
print(f"is_happy is of type: {type(is_happy)}")
