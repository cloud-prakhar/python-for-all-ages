# Example 5: Sorting and Reversing
# Real life: Arranging books on a shelf alphabetically, or scores from high to low!

names = ["Zara", "Arjun", "Meera", "Bharat", "Kavya"]
scores = [78, 95, 62, 88, 71]

print("Original names:", names)
names.sort()                 # Sort alphabetically
print("Sorted names:", names)

print()
print("Original scores:", scores)
scores.sort()                # Sort numbers from low to high
print("Sorted (low to high):", scores)
scores.sort(reverse=True)    # Sort from high to low
print("Sorted (high to low):", scores)

print()
fruits = ["mango", "apple", "cherry"]
print("Original:", fruits)
fruits.reverse()             # Just flip the order
print("Reversed:", fruits)

# sorted() — creates a NEW sorted list without changing original
original = [3, 1, 4, 1, 5, 9, 2, 6]
new_sorted = sorted(original)
print("\nOriginal:", original)
print("Sorted copy:", new_sorted)
