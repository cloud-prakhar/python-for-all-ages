# Chapter 8 Exercise Solutions — Lists & Arrays
#
# NOTE FOR STUDENTS: Try the exercises yourself first before reading these solutions!
# Understanding WHY the solution works is more important than copying it.

print("=" * 50)
print("CHAPTER 8 EXERCISE SOLUTIONS")
print("=" * 50)


# --------------------------------------------------
# Exercise 1:
# Create a list of 5 favorite foods. Print the list and its length.
# --------------------------------------------------

print("\n--- Exercise 1 ---")

# A list is defined with square brackets []. Items are separated by commas.
# Lists can hold any type of data — here we use strings.
favorite_foods = ["Pizza", "Biryani", "Dosa", "Pasta", "Mangoes"]

print(f"My favorite foods : {favorite_foods}")
print(f"Number of foods   : {len(favorite_foods)}")   # len() counts the items

# WHY lists? A list lets us store MANY values under ONE variable name.
# Without lists we'd need: food1, food2, food3 ... which is messy.


# --------------------------------------------------
# Exercise 2:
# List [5, 3, 8, 1, 9, 2, 7]. Sort it, print. Reverse it, print.
# --------------------------------------------------

print("\n--- Exercise 2 ---")

numbers = [5, 3, 8, 1, 9, 2, 7]
print(f"Original list : {numbers}")

# .sort() sorts the list IN PLACE (modifies the original list directly).
# It does NOT return a new list — it returns None.
numbers.sort()
print(f"Sorted        : {numbers}")   # [1, 2, 3, 5, 7, 8, 9]

# .reverse() reverses the list IN PLACE (modifies the original list).
numbers.reverse()
print(f"Reversed      : {numbers}")   # [9, 8, 7, 5, 3, 2, 1]

# KEY DIFFERENCE:
# .sort()   → permanently changes the list (lowest to highest by default)
# .reverse()→ permanently flips the order of the list
# sorted()  → returns a NEW sorted list without changing the original
# If you want to keep the original, use sorted() instead of .sort().


# --------------------------------------------------
# Exercise 3:
# Start with empty "friends" list. Ask user to add 4 friend names.
# Then print all friends.
# --------------------------------------------------

print("\n--- Exercise 3 ---")

friends = []   # Empty list — we'll fill it using .append()

print("Enter 4 friend names:")
for i in range(1, 5):
    friend_name = input(f"  Friend {i}: ")
    friends.append(friend_name)   # .append() adds an item to the END of the list

print(f"\nYour friends: {friends}")
print(f"Total friends: {len(friends)}")

# HOW .append() works:
# friends = []
# friends.append("Rohan")   → friends = ["Rohan"]
# friends.append("Priya")   → friends = ["Rohan", "Priya"]
# Each call adds one item to the right end of the list.


# --------------------------------------------------
# Exercise 4:
# planets list — print 3rd planet, last planet, planets 2-5, planets in reverse.
# --------------------------------------------------

print("\n--- Exercise 4 ---")

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# Indexing starts at 0, so the 3rd planet is at index 2.
print(f"3rd planet      : {planets[2]}")      # Earth

# Index -1 is always the last item in any list.
print(f"Last planet     : {planets[-1]}")     # Neptune

# Slicing: planets[start:stop] — stop index is EXCLUDED.
# Planets 2 through 5 = indices 1, 2, 3, 4 → slice [1:5]
print(f"Planets 2 to 5  : {planets[1:5]}")   # Venus, Earth, Mars, Jupiter

# [::-1] reverses the list — same trick as with strings!
print(f"Planets reversed: {planets[::-1]}")

# MEMORY AID for slicing:
# planets[1:5] → start at index 1 (Venus), stop BEFORE index 5 (Jupiter is index 4)


# --------------------------------------------------
# Exercise 5:
# List of 10 numbers. Find largest, smallest, sum, and average.
# --------------------------------------------------

print("\n--- Exercise 5 ---")

# A fixed list of 10 numbers for this exercise.
my_numbers = [45, 12, 78, 34, 90, 23, 67, 5, 89, 56]

# Python's built-in functions max(), min(), sum() work on any list of numbers.
largest = max(my_numbers)
smallest = min(my_numbers)
total = sum(my_numbers)
average = total / len(my_numbers)   # average = sum ÷ count

print(f"Numbers  : {my_numbers}")
print(f"Largest  : {largest}")
print(f"Smallest : {smallest}")
print(f"Sum      : {total}")
print(f"Average  : {average:.1f}")   # :.1f = 1 decimal place

# WHY use built-ins? max(), min(), sum() are cleaner and faster than
# writing your own loops for these very common operations.


# --------------------------------------------------
# Exercise 6:
# Create a 3x3 tic-tac-toe grid (2D list). Print it nicely.
# --------------------------------------------------

print("\n--- Exercise 6 ---")

# A 2D list is a list that contains other lists — a "list of rows".
# Each inner list is one row of the grid.
grid = [
    ["X", "O", "X"],   # Row 0
    ["O", "X", "O"],   # Row 1
    ["X", " ", "O"],   # Row 2
]

# To access a specific cell: grid[row][column]
# Example: grid[0][1] → "O" (row 0, column 1)

print("  Tic-Tac-Toe Board:")
print("  +---------+")
for row in grid:
    # " | ".join(row) connects the items in the row with " | " between them
    print(f"  | {' | '.join(row)} |")
    print("  +---------+")

# HOW join() WORKS:
# row = ["X", "O", "X"]
# " | ".join(row) → "X | O | X"
# The separator " | " is placed BETWEEN every item.
