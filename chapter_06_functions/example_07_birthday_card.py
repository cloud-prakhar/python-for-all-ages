# Example 7: Birthday Card Generator
# Real life: Write a function to generate a custom birthday card for anyone!

def birthday_card(name, age):
    print("*" * 35)
    print("*    🎂 HAPPY BIRTHDAY! 🎂       *")
    print("*" * 35)
    print(f"*  Dear {name}!")
    print(f"*  You are turning {age}!")
    print(f"*  May all your {age} wishes come true!")
    print("*  Have a super awesome day!")
    print("*" * 35)
    print()

# Generate cards for multiple people!
birthday_card("Aryan", 8)
birthday_card("Priya", 10)
birthday_card("Grandma", 65)
