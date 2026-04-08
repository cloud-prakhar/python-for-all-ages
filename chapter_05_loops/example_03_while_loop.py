# Example 3: While Loop
# Real life: Keep eating until you're full!
# A while loop keeps going AS LONG AS the condition is True.

hunger_level = 5   # 5 means very hungry, 0 means full

print("Starting to eat...")
while hunger_level > 0:
    print(f"Eating... hunger level: {hunger_level} 🍕")
    hunger_level = hunger_level - 1   # Gets less hungry each time

print("I'm full! Hunger level:", hunger_level)
print("Time to stop eating!")
