# Example 4: Multiplication Table Generator
# Real life: Your math homework — but Python does it in seconds!

number = int(input("Which multiplication table do you want? "))

print(f"\n--- {number} Times Table ---")
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i:2} = {result}")
