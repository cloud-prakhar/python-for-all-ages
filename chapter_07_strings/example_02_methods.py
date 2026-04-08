# Example 2: String Methods
# Methods are like tools you can use ON a string.
# Real life: Like pressing formatting buttons in a word processor!

sentence = "hello, my name is priya!"

print(sentence.upper())    # HELLO, MY NAME IS PRIYA!
print(sentence.lower())    # hello, my name is priya!
print(sentence.title())    # Hello, My Name Is Priya!
print(sentence.capitalize()) # Hello, my name is priya!

# Count and find
print(sentence.count("a"))        # How many "a"s?
print(sentence.find("name"))      # What position does "name" start at?
print(sentence.startswith("hello")) # Does it start with "hello"?

# Strip whitespace (very useful for cleaning user input)
messy = "   lots of spaces   "
print(f"Before: '{messy}'")
print(f"After:  '{messy.strip()}'")
