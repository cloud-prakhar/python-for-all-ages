# Example 4: Find and Replace
# Real life: Like "Find and Replace" in Microsoft Word!
# Change every "cat" to "dog" in a sentence.

story = "The cat sat on the mat. The cat chased the rat."

print("Original:", story)

# Replace "cat" with "dog"
new_story = story.replace("cat", "dog")
print("Modified:", new_story)

# Find where a word is
position = story.find("mat")
print(f"'mat' starts at position: {position}")

# Split a sentence into words
words = story.split(" ")   # Split by space
print(f"Number of words: {len(words)}")
print(f"Words: {words}")
