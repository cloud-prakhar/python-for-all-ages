# Example 7: Sum Calculator Using a Loop
# Real life: Adding up all your weekly allowance money to see the total!

total = 0
count = 5

print(f"Let's add {count} numbers together!")
for i in range(1, count + 1):
    number = int(input(f"Enter number {i}: "))
    total = total + number

print(f"\nYou entered {count} numbers.")
print(f"Their total sum is: {total}")
print(f"Their average is: {total / count:.2f}")
