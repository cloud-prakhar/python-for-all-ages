# Example 7: Amusement Park Ride Checker
# Real life: Can you ride the rollercoaster? You need to be tall enough AND old enough!

name = input("What is your name? ")
age = int(input("How old are you? "))
height_cm = int(input("How tall are you in cm? "))

min_age = 7
min_height = 120   # cm

print(f"\nChecking if {name} can ride the rollercoaster...")

if age >= min_age and height_cm >= min_height:
    print("✅ You CAN ride the rollercoaster! Hold on tight! 🎢")
elif age < min_age:
    print(f"❌ Sorry, you must be at least {min_age} years old.")
elif height_cm < min_height:
    print(f"❌ Sorry, you must be at least {min_height} cm tall.")
