# Example 10: Name Formatter and Validator
# A common real-world task: clean, validate, and format user-entered names.
# This example ties together: strip, title, isalpha, split, join, f-strings.

def format_name(raw_name):
    """
    Clean and format a name string.
    Returns (formatted_name, is_valid, error_message).
    """
    # Step 1: Strip leading/trailing whitespace
    name = raw_name.strip()

    if not name:
        return None, False, "Name cannot be empty."

    # Step 2: Check for invalid characters (only letters and spaces allowed)
    for char in name:
        if not (char.isalpha() or char == " "):
            return None, False, f"Invalid character found: '{char}'"

    # Step 3: Remove extra internal spaces
    parts = name.split()
    if len(parts) < 2:
        return None, False, "Please enter at least a first and last name."

    # Step 4: Title-case each part
    formatted = " ".join(part.title() for part in parts)
    return formatted, True, "OK"


def generate_username(formatted_name):
    """Generate a username from first and last name."""
    parts = formatted_name.split()
    first = parts[0].lower()
    last  = parts[-1].lower()
    return f"{first}.{last}"


def generate_initials(formatted_name):
    """Generate initials from a formatted name."""
    return ".".join(part[0].upper() for part in formatted_name.split()) + "."


# --- Run it ---
print("=== Name Formatter ===")
raw = input("Enter your full name: ")

name, valid, message = format_name(raw)

if valid:
    username = generate_username(name)
    initials = generate_initials(name)

    print(f"\nFormatted name : {name}")
    print(f"Username       : {username}")
    print(f"Initials       : {initials}")
    print(f"Email suggestion: {username}@example.com")
else:
    print(f"\nError: {message}")
