# Example 1: Tuples — The Locked List
# Real life: Your date of birth — it NEVER changes!

birthday = (2016, 3, 15)   # (year, month, day)
print("My birthday:", birthday)
print("Year:", birthday[0])
print("Month:", birthday[1])
print("Day:", birthday[2])

# You CAN read from a tuple
coordinates = (28.6, 77.2)   # Latitude and Longitude of Delhi
print(f"\nDelhi's coordinates: {coordinates}")
print(f"Latitude: {coordinates[0]}")

# Tuples can be looped
colors = ("red", "green", "blue")
print("\nTraffic light colors:")
for color in colors:
    print(f"  - {color}")

# Trying to change a tuple will FAIL (uncomment to see the error)
# birthday[0] = 2020   # This would raise a TypeError!
print("\nTuples cannot be changed — they are LOCKED! 🔒")
