# Example 4: Looping Through a List
# Real life: A teacher calling out each student's name from the roll call sheet!

animals = ["Lion", "Tiger", "Elephant", "Giraffe", "Zebra"]

# -------------------------------------------------------
# Method 1: Loop directly over items (simplest)
# -------------------------------------------------------
# The loop variable "animal" holds each item in turn.
# No index numbers involved — just the values.
print("Animals in the zoo:")
for animal in animals:
    print(f"  - {animal}")

print()

# -------------------------------------------------------
# Method 2: Loop with index using range(len(...))
# -------------------------------------------------------
# len(animals) → 5 (number of items)
# range(5)     → 0, 1, 2, 3, 4
# animals[i]   → gets the item at position i
print("Animals with their numbers:")
for i in range(len(animals)):
    print(f"  Animal #{i + 1}: {animals[i]}")
    # i + 1 because i starts at 0, but we want to display "Animal #1" not "#0"

print()

# -------------------------------------------------------
# Method 3: enumerate() — the best of both worlds
# -------------------------------------------------------
# enumerate(iterable, start=1) gives you BOTH the index AND the value
# at the same time, without needing range(len(...)).
#
# Each time through the loop, it gives a PAIR: (index, item)
# We unpack that pair into TWO loop variables: index, animal
#
#   for index, animal in enumerate(animals, start=1):
#         ↑       ↑                             ↑
#    index var  value var             start counting at 1 (default is 0)
#
# Iteration 1: index=1, animal="Lion"
# Iteration 2: index=2, animal="Tiger"
# ... and so on
#
# "start=1" is a keyword argument — it tells enumerate to number from 1.
# Without it, the default is start=0.
#
print("Using enumerate:")
for index, animal in enumerate(animals, start=1):
    print(f"  {index}. {animal}")
