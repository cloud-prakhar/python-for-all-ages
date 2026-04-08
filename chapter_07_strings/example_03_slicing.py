# Example 3: String Slicing and Indexing
# Slicing means cutting out a piece of the string!
# Real life: Like cutting a slice from a loaf of bread 🍞

word = "STRAWBERRY"
#       0123456789

print(word[0])       # S — first character
print(word[4])       # W
print(word[-1])      # Y — last character
print(word[-3])      # R — 3rd from end

# Slicing: [start : stop]  (stop is NOT included)
print(word[0:5])     # STRAW — characters 0 to 4
print(word[5:])      # BERRY — from index 5 to end
print(word[:5])      # STRAW — from beginning to index 4
print(word[::2])     # Every 2nd character: SRWER
print(word[::-1])    # Reverse the string: YRREWARTS
