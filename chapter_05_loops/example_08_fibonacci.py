# Example 8: Fibonacci Sequence
# The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Each number is the SUM of the two numbers before it.
# Found in nature: flower petals, seashell spirals, sunflower seeds.
#
# NEW CONCEPT: Multiple assignment and simultaneous swap
#
#   a, b = 0, 1
#
#   This assigns TWO variables at once in a single line.
#   It's equivalent to:
#       a = 0
#       b = 1
#   Just shorter and more convenient.
#
# THE TRICKY PART — this line inside the loop:
#
#   a, b = b, a + b
#
#   This is a SIMULTANEOUS assignment. Here is what happens:
#
#   Step 1: Python evaluates the RIGHT side COMPLETELY first:
#           b      → current value of b (e.g. 1)
#           a + b  → current value of a + b (e.g. 0 + 1 = 1)
#           So the right side produces the pair: (1, 1)
#
#   Step 2: Python THEN assigns to the left side:
#           a gets the first value  → a = 1
#           b gets the second value → b = 1
#
#   WHY does this matter? If Python did it one at a time (left to right):
#       a = b        → a becomes 1
#       b = a + b    → b becomes 1 + 1 = 2  ← WRONG! a was already changed
#
#   Simultaneous assignment avoids this bug — the right side is fully
#   calculated before anything on the left side is changed.
#
# TRACE through the first 5 iterations:
#   Start:    a=0,  b=1   → prints 0,  then a=1,  b=1
#   i=1:      a=1,  b=1   → prints 1,  then a=1,  b=2
#   i=2:      a=1,  b=2   → prints 1,  then a=2,  b=3
#   i=3:      a=2,  b=3   → prints 2,  then a=3,  b=5
#   i=4:      a=3,  b=5   → prints 3,  then a=5,  b=8

n = int(input("How many Fibonacci numbers do you want to see? "))

if n <= 0:
    print("Please enter a positive number.")
elif n == 1:
    print("0")
else:
    a, b = 0, 1   # Multiple assignment: a starts at 0, b starts at 1

    print(f"Fibonacci sequence ({n} terms):")
    for i in range(n):
        print(a, end="  ")        # Print current value of a
        a, b = b, a + b           # Simultaneous: new a = old b, new b = old a + old b

    print()   # Move to a new line after all numbers are printed

    print(f"\nThe {n}th Fibonacci number is: {a}")
