# Example 4: Calling a Function Inside a Loop
# Real life: The teacher greets each student as they walk into class!
#
# PREVIEW: Lists (covered fully in Chapter 8)
#
#   students = ["Aarav", "Diya", "Kunal", "Sneha", "Vikram"]
#
#   A LIST is a way to store multiple values in one variable.
#   Square brackets [ ] create a list.
#   Each item is separated by a comma.
#   You can loop over a list with: for item in list_name:
#
#   This is a sneak peek — Chapter 8 covers lists in full detail.
#   For now, just think of it as: "a collection of names I can loop through."

def greet(name):
    # "name" is the parameter — it receives a different value each call
    print(f"Good morning, {name}! Ready to learn Python?")

# A list holds multiple names in one place
students = ["Aarav", "Diya", "Kunal", "Sneha", "Vikram"]

print("Teacher greeting the class:")
print("=" * 40)

for student in students:
    # Loop variable "student" takes each name from the list in order:
    # First iteration:  student = "Aarav"
    # Second iteration: student = "Diya"
    # ... and so on
    greet(student)   # We call greet() and pass the current student's name
