# Example 6: List Slicing
# Slicing works EXACTLY like string slicing — cut out a piece of the list!
# Real life: Like taking a few pages from a notebook.

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
#              0         1        2        3         4          5         6         7

print("All planets:", planets)
print()

print("First 3 planets:", planets[:3])      # Mercury, Venus, Earth
print("Last 3 planets:", planets[-3:])      # Uranus, Neptune (and more)
print("Middle planets:", planets[2:6])      # Earth to Jupiter
print("Every 2nd planet:", planets[::2])    # Mercury, Earth, Jupiter, Uranus
print("Reversed:", planets[::-1])           # Neptune to Mercury

# Slicing creates a COPY — original is unchanged
inner_planets = planets[:4]
print("\nInner planets:", inner_planets)
print("All planets still:", planets)
