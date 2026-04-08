# Example 5: Dictionary Basics
# A dictionary stores KEY: VALUE pairs.
# Real life: A real dictionary — look up a word (KEY) to get its meaning (VALUE).

# Create a dictionary
capitals = {
    "India":   "New Delhi",
    "France":  "Paris",
    "Japan":   "Tokyo",
    "Brazil":  "Brasilia",
    "Germany": "Berlin"
}

# Access by key
print(f"Capital of India:   {capitals['India']}")
print(f"Capital of Japan:   {capitals['Japan']}")
print(f"Capital of France:  {capitals['France']}")

print()
print("All capitals:")
for country, capital in capitals.items():
    print(f"  {country} → {capital}")

# Check if a key exists
print()
print(f"Is 'India' in dict? {'India' in capitals}")
print(f"Is 'Australia' in dict? {'Australia' in capitals}")
