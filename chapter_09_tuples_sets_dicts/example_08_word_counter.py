# Example 8: Word Counter Using a Dictionary
# Real life: Like when you count how many times a word appears in your essay!

sentence = input("Enter a sentence: ").lower()

# Split into individual words
words = sentence.split()

# Count each word using a dictionary
word_count = {}

for word in words:
    # Remove punctuation from word
    clean_word = word.strip(".,!?;:")

    if clean_word in word_count:
        word_count[clean_word] += 1    # Already seen — increase count
    else:
        word_count[clean_word] = 1     # First time seeing it

# Display results
print(f"\nWord frequencies in your sentence:")
print("-" * 30)
for word, count in sorted(word_count.items()):
    print(f"  '{word}': {count} time(s)")

# Find the most common word
most_common = max(word_count, key=word_count.get)
print(f"\nMost common word: '{most_common}' ({word_count[most_common]} times)")
