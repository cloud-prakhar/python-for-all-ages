# Example 8: Interactive Shopping Cart
# Real life: Adding items to your online shopping cart!

cart = []

print("=== WELCOME TO PYTHON STORE! ===")
print("Commands: add / remove / view / done")
print()

while True:
    action = input("What do you want to do? ").lower().strip()

    if action == "add":
        item = input("What item to add? ").strip()
        cart.append(item)
        print(f"✅ '{item}' added to cart!")

    elif action == "remove":
        if len(cart) == 0:
            print("Your cart is empty!")
        else:
            item = input("What item to remove? ").strip()
            if item in cart:
                cart.remove(item)
                print(f"🗑️ '{item}' removed from cart.")
            else:
                print(f"'{item}' is not in your cart.")

    elif action == "view":
        if len(cart) == 0:
            print("Your cart is empty!")
        else:
            print(f"\n🛒 Your Cart ({len(cart)} items):")
            for i, item in enumerate(cart, 1):
                print(f"  {i}. {item}")
            print()

    elif action == "done":
        print(f"\n🎉 Order placed! You bought {len(cart)} items:")
        for item in cart:
            print(f"  - {item}")
        break

    else:
        print("Invalid command. Try: add / remove / view / done")
