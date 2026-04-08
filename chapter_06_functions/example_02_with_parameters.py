# Example 2: Function with Parameters
# Parameters are like blanks in a template — you fill them in when you call the function!
# Real life: "Make a sandwich with ___" — the blank changes each time.

def greet_student(name, grade):
    print(f"Hello, {name}! Welcome to Grade {grade}!")
    print(f"We're glad you're here, {name}!")

# Call with different arguments
greet_student("Arjun", 3)
print()
greet_student("Meera", 5)
print()
greet_student("Rohan", 2)
