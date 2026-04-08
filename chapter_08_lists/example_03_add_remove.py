# Example 3: Adding and Removing Items
# Real life: Adding items to your grocery bag and removing them as you pick them up!

grocery = ["milk", "bread", "eggs"]
print("Starting grocery list:", grocery)

# Add to the END of the list
grocery.append("butter")
print("After append('butter'):", grocery)

# Add at a SPECIFIC position
grocery.insert(1, "cheese")   # Put cheese at index 1 (second position)
print("After insert(1, 'cheese'):", grocery)

# Remove a specific item
grocery.remove("bread")
print("After remove('bread'):", grocery)

# Remove and get the LAST item (like picking it up from the bag)
last_item = grocery.pop()
print(f"Picked up: {last_item}")
print("After pop():", grocery)

# Remove by index
grocery.pop(0)   # Remove the first item
print("After pop(0):", grocery)
