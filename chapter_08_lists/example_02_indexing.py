# Example 2: Accessing Items by Index
# Index = the position number, starting from 0.
# Real life: Like bus seats — seat 0 is the first seat, seat 1 is the second...

students = ["Aarav", "Bhavna", "Chetan", "Divya", "Eshan"]
#              0         1         2         3        4

print("All students:", students)
print()

print(f"First student (index 0): {students[0]}")
print(f"Second student (index 1): {students[1]}")
print(f"Last student (index 4): {students[4]}")
print(f"Last student (index -1): {students[-1]}")    # Shortcut for last!
print(f"Second to last (index -2): {students[-2]}")

# Checking membership
print()
print(f"Is 'Divya' in the class? {'Divya' in students}")
print(f"Is 'Farhan' in the class? {'Farhan' in students}")
