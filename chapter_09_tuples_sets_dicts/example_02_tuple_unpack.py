# Example 2: Unpacking Tuples
# Unpacking = pulling each value out into its OWN variable.
# Real life: Opening a gift box and taking out each item separately!

# Packing
student_info = ("Arjun", 10, "Grade 5", 92.5)

# Unpacking — each value goes into its own variable
name, age, grade, score = student_info

print(f"Name:  {name}")
print(f"Age:   {age}")
print(f"Grade: {grade}")
print(f"Score: {score}")

# Swap two variables using tuple unpacking!
a = "Hello"
b = "World"
print(f"\nBefore swap: a={a}, b={b}")
a, b = b, a     # Swap in one line!
print(f"After swap:  a={a}, b={b}")
