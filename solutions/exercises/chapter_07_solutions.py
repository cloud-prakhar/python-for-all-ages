# Chapter 7 Exercise Solutions — Strings
#
# NOTE FOR STUDENTS: Try the exercises yourself first before reading these solutions!
# Understanding WHY the solution works is more important than copying it.

print("=" * 50)
print("CHAPTER 7 EXERCISE SOLUTIONS")
print("=" * 50)


# --------------------------------------------------
# Exercise 1:
# sentence = "Python is amazing!"
# Print: first character, last character, the word "amazing"
# --------------------------------------------------

print("\n--- Exercise 1 ---")

sentence = "Python is amazing!"

# Index 0 is always the first character.
first_char = sentence[0]

# Index -1 is always the last character — negative indices count from the end.
last_char = sentence[-1]

# "Python is amazing!" — count the characters:
# "Python is " is 10 characters (P=0 ... space=9), then "amazing" starts at index 10.
# We want "amazing" which is 7 letters: indices 10 to 16 (stop is exclusive, so use 17).
word_amazing = sentence[10:17]

print(f"First character : '{first_char}'")    # P
print(f"Last character  : '{last_char}'")     # !
print(f"Word 'amazing'  : '{word_amazing}'")  # amazing

# HOW TO FIND THE RIGHT INDICES:
# You can use .find() to locate a word:
start = sentence.find("amazing")
end = start + len("amazing")
print(f"Using .find()   : '{sentence[start:end]}'")  # same result


# --------------------------------------------------
# Exercise 2:
# Ask for the user's full name.
# Print it in UPPERCASE, lowercase, Title Case.
# Print total character count (including spaces).
# --------------------------------------------------

print("\n--- Exercise 2 ---")

full_name = input("Enter your full name: ")

# String methods return a NEW string — they do not change the original.
print(f"Uppercase   : {full_name.upper()}")
print(f"Lowercase   : {full_name.lower()}")
print(f"Title Case  : {full_name.title()}")
print(f"Total chars : {len(full_name)}")   # len() counts ALL characters including spaces

# WHY .title()? It capitalises the first letter of EVERY word.
# "alice smith" → "Alice Smith"
# This is useful for formatting names entered in any case by the user.


# --------------------------------------------------
# Exercise 3:
# Ask the user for a sentence.
# Print it reversed. Check if it's a palindrome (ignore case).
# --------------------------------------------------

print("\n--- Exercise 3 ---")

text = input("Enter a sentence or word: ")

# [::-1] is a slice with step -1 — it reads the string backwards.
reversed_text = text[::-1]
print(f"Original : {text}")
print(f"Reversed : {reversed_text}")

# A palindrome reads the same forwards and backwards.
# We use .lower() to ignore case — "Racecar" and "racecar" should both work.
is_palindrome = text.lower() == reversed_text.lower()

if is_palindrome:
    print(f"'{text}' IS a palindrome!")
else:
    print(f"'{text}' is NOT a palindrome.")

# Test examples:
# "racecar" reversed is "racecar" → palindrome
# "madam"   reversed is "madam"   → palindrome
# "Python"  reversed is "nohtyP"  → NOT a palindrome


# --------------------------------------------------
# Exercise 4:
# Ask the user for a sentence.
# Split it into words and print each word with its length.
# --------------------------------------------------

print("\n--- Exercise 4 ---")

user_sentence = input("Enter a sentence: ")

# .split() breaks a string into a list of words, splitting on spaces by default.
words = user_sentence.split()

print(f"\nWord breakdown for: '{user_sentence}'")
print("-" * 30)
for word in words:
    # len(word) counts the characters in each word.
    # :<15 left-aligns the word in 15 characters so the numbers line up.
    print(f"  {word:<15} ({len(word)} letters)")

print(f"\nTotal words: {len(words)}")

# HOW .split() WORKS:
# "Hello World Python" → ["Hello", "World", "Python"]
# It removes extra spaces automatically.


# --------------------------------------------------
# Exercise 5:
# Username formatter: first letter of first name + full last name, all lowercase.
# Example: "Alice" + "Smith" → "asmith"
# Then print email: username@school.edu
# --------------------------------------------------

print("\n--- Exercise 5 ---")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Step 1: Take the first letter of the first name using index [0]
# Step 2: Add the full last name
# Step 3: Make the whole thing lowercase with .lower()
username = (first_name[0] + last_name).lower()

# The email is just the username with "@school.edu" added.
email = username + "@school.edu"

print(f"\nFirst name : {first_name}")
print(f"Last name  : {last_name}")
print(f"Username   : {username}")
print(f"Email      : {email}")

# EXAMPLE RUN:
# First name: Alice  | Last name: Smith
# first_name[0]  → "A"
# "A" + "Smith"  → "ASmith"
# .lower()       → "asmith"
# email          → "asmith@school.edu"
