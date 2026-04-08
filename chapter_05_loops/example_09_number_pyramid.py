# Example 9: Number Pyramid Pattern
# Builds on nested loops — the inner loop depends on the outer loop's variable.
# This example prints multiple patterns to show how changing the logic
# creates completely different shapes.

rows = int(input("Enter number of rows (e.g. 5): "))

print("\n--- Pattern 1: Right-aligned triangle ---")
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n--- Pattern 2: Number repetition ---")
for i in range(1, rows + 1):
    print((str(i) + " ") * i)

print("\n--- Pattern 3: Multiplication diamond column ---")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(i * j, end="\t")
    print()
