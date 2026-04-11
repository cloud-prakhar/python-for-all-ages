# Chapter 5 Exercise Solutions — Loops
#
# NOTE FOR STUDENTS: Try the exercises yourself first before reading these solutions!
# Understanding WHY the solution works is more important than copying it.

print("=" * 50)
print("CHAPTER 5 EXERCISE SOLUTIONS")
print("=" * 50)


# --------------------------------------------------
# Exercise 1:
# Print numbers from 1 to 20 using a for loop.
# --------------------------------------------------

print("\n--- Exercise 1 ---")

# range(1, 21) generates numbers starting at 1 and stopping BEFORE 21.
# That means: 1, 2, 3, ... 20. The stop value is EXCLUDED.
for i in range(1, 21):
    print(i, end=" ")   # end=" " prints a space instead of a newline
print()                 # Print a blank line after the row

# WHY range(1, 21) and not range(1, 20)?
# range(start, stop) goes UP TO but NOT INCLUDING stop.
# To include 20, we need stop = 21.


# --------------------------------------------------
# Exercise 2:
# Print all even numbers from 2 to 30 using range with a step.
# --------------------------------------------------

print("\n--- Exercise 2 ---")

# range(start, stop, step) — step of 2 means skip every other number.
# Starting at 2 and stepping by 2 gives us: 2, 4, 6, 8 ... 30.
for num in range(2, 31, 2):
    print(num, end=" ")
print()

# ALTERNATIVE: You could start at 1, step by 1, and check if num % 2 == 0.
# But the step approach is more efficient and cleaner.


# --------------------------------------------------
# Exercise 3:
# Ask the user for a number and print its multiplication table (1 to 10).
# --------------------------------------------------

print("\n--- Exercise 3 ---")

base = int(input("Enter a number for its multiplication table: "))

print(f"\n--- Multiplication Table for {base} ---")
for multiplier in range(1, 11):
    result = base * multiplier
    # :>3 right-aligns the result in a field of 3 characters for neat columns
    print(f"  {base} x {multiplier:>2} = {result:>3}")


# --------------------------------------------------
# Exercise 4:
# Use a while loop to keep asking the user to guess a number between 1-5.
# Secret number is 3. Print "Correct!" when they guess right.
# --------------------------------------------------

print("\n--- Exercise 4 ---")

secret_number = 3
guess = 0           # Start with a value that is not the secret

# The while loop keeps running AS LONG AS the condition is True.
# Once guess == secret_number, the condition becomes False and the loop ends.
while guess != secret_number:
    guess = int(input("Guess a number between 1 and 5: "))
    if guess != secret_number:
        print("Not quite! Try again.")

print("Correct! You guessed it!")

# WHY while instead of for? We don't know ahead of time how many guesses
# the user needs — it could be 1 guess or 10. Use while when the number
# of iterations is unknown.


# --------------------------------------------------
# Exercise 5:
# Print a number triangle using nested loops:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# --------------------------------------------------

print("\n--- Exercise 5 ---")

# Outer loop controls the rows: row 1, row 2, ... row 5
for row in range(1, 6):
    # Inner loop prints numbers from 1 up to the current row number
    for num in range(1, row + 1):
        print(num, end=" ")
    print()  # Move to the next line after each row

# HOW IT WORKS (trace through):
# row=1: inner loop runs for num in range(1, 2) → prints: 1
# row=2: inner loop runs for num in range(1, 3) → prints: 1 2
# row=3: inner loop runs for num in range(1, 4) → prints: 1 2 3
# ... and so on


# --------------------------------------------------
# Exercise 6:
# Find the sum of all numbers from 1 to 100 using a loop.
# --------------------------------------------------

print("\n--- Exercise 6 ---")

# We use an "accumulator" — start at 0 and add each number as we loop.
total = 0

for n in range(1, 101):   # 1 to 100 inclusive (stop = 101)
    total += n             # Same as: total = total + n

print(f"Sum of 1 to 100 = {total}")
# The answer should be 5050!

# BONUS — The mathematical shortcut (Gauss's formula):
# sum = n * (n + 1) / 2 = 100 * 101 / 2 = 5050
gauss_sum = 100 * 101 // 2
print(f"Gauss formula check: {gauss_sum}")   # Also 5050!

# WHY += ? It's shorthand for total = total + n. The variable grows
# (accumulates) with each iteration of the loop — that's why it's called
# an accumulator pattern.
