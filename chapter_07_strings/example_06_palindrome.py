# Example 6: Palindrome Checker
# A palindrome reads the same forwards and backwards!
# Real life: "racecar", "level", "madam", "civic"

def is_palindrome(word):
    # METHOD CHAINING: word.lower().strip()
    # .lower()  → converts all letters to lowercase  ("Racecar" → "racecar")
    # .strip()  → removes spaces from both ends      ("  racecar  " → "racecar")
    # They chain left to right: lower() runs first, strip() runs on the result.
    word = word.lower().strip()

    # SLICE [::-1] reverses a string.
    # Slice syntax: [start : stop : step]
    # [::-1] means: start from end, stop at beginning, step -1 (go backwards)
    # "racecar"[::-1] → "racecar"
    reversed_word = word[::-1]

    return word == reversed_word   # True if original equals its reverse

# Test some words
test_words = ["racecar", "hello", "level", "python", "madam", "banana"]

for word in test_words:
    if is_palindrome(word):
        print(f"'{word}' IS a palindrome! ✅")
    else:
        print(f"'{word}' is NOT a palindrome. ❌")

# Let the user try their own word
user_word = input("\nEnter a word to check: ")
if is_palindrome(user_word):
    print(f"🎉 '{user_word}' is a palindrome!")
else:
    print(f"'{user_word}' is not a palindrome.")
