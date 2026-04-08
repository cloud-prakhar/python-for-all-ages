# Example 6: Higher or Lower Number Game
# Real life: Like the "guess my number" game you play with friends!

secret_number = 42
guess = int(input("Guess the secret number (between 1 and 100): "))

if guess == secret_number:
    print("🎉 You got it! The secret number IS 42!")
elif guess > secret_number:
    print(f"Too HIGH! The secret number is less than {guess}.")
else:
    print(f"Too LOW! The secret number is more than {guess}.")
