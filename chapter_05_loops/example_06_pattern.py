# Example 6: Draw a Star Pattern with Loops
# Real life: Like drawing rows of stars on your art project!
# Nested loops = a loop INSIDE another loop.

rows = 5

print("--- Triangle Pattern ---")
for i in range(1, rows + 1):     # Outer loop: rows
    for j in range(i):            # Inner loop: stars in that row
        print("*", end=" ")
    print()   # Move to next line after each row

print("\n--- Square Pattern ---")
for i in range(rows):
    for j in range(rows):
        print("*", end=" ")
    print()
