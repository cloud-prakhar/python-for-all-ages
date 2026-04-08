# Example 5: Break and Continue
# break = STOP the loop immediately (like the STOP button)
# continue = SKIP this step, go to the next (like skipping a song)
# Real life: Checking a bag of apples — skip bad ones, stop when bag is empty.

print("--- BREAK example ---")
print("Looking for the number 5 in a list:")
for num in range(1, 11):
    if num == 5:
        print(f"Found 5! Stopping the search.")
        break          # Stop the entire loop
    print(f"Checking {num}... not 5.")

print("\n--- CONTINUE example ---")
print("Printing only ODD numbers from 1 to 10:")
for num in range(1, 11):
    if num % 2 == 0:
        continue       # Skip even numbers
    print(num, end=" ")
print()  # new line
