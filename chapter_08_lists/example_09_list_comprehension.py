# Example 9: List Comprehensions
# A list comprehension builds a new list in a single, readable line.
#
# GENERAL FORM:
#   [expression   for   item   in   iterable   if   condition]
#        ↑          ↑    ↑      ↑      ↑         ↑       ↑
#    what to        |  loop   |  what to      |   filter
#    put in        "for"  variable  loop over  (optional)
#    the list
#
# COMPARE: traditional loop vs comprehension
#
#   TRADITIONAL:                      COMPREHENSION:
#   result = []                       result = [x**2 for x in range(1,6)]
#   for x in range(1, 6):
#       result.append(x**2)
#
#   Both produce: [1, 4, 9, 16, 25]
#   The comprehension is shorter and is considered more "Pythonic" (idiomatic).

# -------------------------------------------------------
# Basic: no condition, just transform each item
# -------------------------------------------------------
# "For each x in range(1,11), put x**2 into the list."
squares = [x ** 2 for x in range(1, 11)]
print("Squares 1–10:", squares)


# -------------------------------------------------------
# With condition: only include items that pass the filter
# -------------------------------------------------------
# "For each x in range(1,11), IF x is even, put x**2 into the list."
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print("Even squares:", even_squares)


# -------------------------------------------------------
# Works on any iterable, including lists of strings
# -------------------------------------------------------
names   = ["Alice", "Bob", "Amanda", "Charlie", "Andrew", "Diana"]
# "For each name in names, IF it starts with 'A', put name.upper() into the list."
a_names = [name.upper() for name in names if name.startswith("A")]
print("Names starting with A (uppercased):", a_names)


# -------------------------------------------------------
# Advanced: two for clauses (nested loops compressed)
# -------------------------------------------------------
# A 2D list (list of lists) being flattened into a 1D list.
# "For each row in matrix, for each cell in that row, put cell in the list."
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat   = [cell for row in matrix for cell in row]
# Equivalent to:
#   flat = []
#   for row in matrix:
#       for cell in row:
#           flat.append(cell)
print("Flattened matrix:", flat)


# -------------------------------------------------------
# Practical: temperature conversion with zip()
# -------------------------------------------------------
# round(number, decimal_places) rounds to that many decimal places.
celsius_temps = [0, 10, 20, 30, 37, 100]
fahrenheit    = [round((c * 9/5) + 32, 1) for c in celsius_temps]

# zip(list1, list2) pairs up items from two lists side by side:
# zip([0,10,20], [32,50,68]) → (0,32), (10,50), (20,68), ...
# Each time through the loop we unpack the pair into c and f.
print("\nTemperature conversions:")
for c, f in zip(celsius_temps, fahrenheit):
    print(f"  {c}°C = {f}°F")
