# Example 3: Sets — No Duplicates!
# Real life: Class attendance — each student is marked ONCE.

# Creating a set
class_present = {"Arjun", "Meera", "Bharat", "Arjun", "Meera"}
print("Students present:", class_present)   # Arjun and Meera appear only once!
print(f"Number of unique students: {len(class_present)}")

# Adding to a set
class_present.add("Priya")
print("After adding Priya:", class_present)

# Try adding a duplicate
class_present.add("Arjun")    # Already there — nothing changes
print("After adding Arjun again:", class_present)

# Removing from a set
class_present.remove("Bharat")   # Bharat went home sick
print("After removing Bharat:", class_present)

# Checking membership
print()
print(f"Is Priya present? {'Priya' in class_present}")
print(f"Is Bharat present? {'Bharat' in class_present}")
