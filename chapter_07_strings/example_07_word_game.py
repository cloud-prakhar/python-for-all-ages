# Example 7: Word Guessing Game (Mini)
# Real life: Hangman-style game — the computer knows a word, you guess it!

secret = "python"
hint = "_" * len(secret)    # Show blanks: ______

print("=== WORD GUESSING GAME ===")
print(f"The word has {len(secret)} letters.")
print(f"Hint: {hint}")
print()

attempts = 4   # Number of guesses allowed

for attempt in range(1, attempts + 1):
    guess = input(f"Attempt {attempt}/{attempts} — Guess the full word: ").lower()

    if guess == secret:
        print(f"🎉 CORRECT! The word was '{secret}'! You got it!")
        break
    else:
        # Show which letters are correct
        result = ""
        for i in range(len(secret)):
            if i < len(guess) and guess[i] == secret[i]:
                result += secret[i]
            else:
                result += "_"
        print(f"Not quite! Here's your hint: {result}")
else:
    print(f"Game over! The word was '{secret}'. Better luck next time!")
