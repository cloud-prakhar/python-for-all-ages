# Example 6: Dictionary Methods — Add, Update, Delete
# Real life: Managing your contact book on a phone!

contacts = {
    "Arjun": "9876543210",
    "Meera": "9123456789"
}
print("Contacts:", contacts)

# Add a new contact
contacts["Bharat"] = "9988776655"
print("\nAfter adding Bharat:", contacts)

# Update an existing contact (Arjun changed his number)
contacts["Arjun"] = "9000012345"
print("After updating Arjun:", contacts)

# Delete a contact
del contacts["Meera"]
print("After deleting Meera:", contacts)

# Get safely (won't crash if key not found)
number = contacts.get("Zara", "Not found")
print(f"\nZara's number: {number}")

# All keys and values
print("\nAll names:", list(contacts.keys()))
print("All numbers:", list(contacts.values()))
