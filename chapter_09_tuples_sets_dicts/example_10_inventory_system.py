# Example 10: Inventory Management System
# A practical application combining dictionaries, tuples, and sets.
# Simulates a simple store inventory with add, remove, restock, and report features.

# Inventory: {item_name: {"qty": int, "price": float, "category": str}}
inventory = {
    "apple":     {"qty": 50,  "price": 0.99,  "category": "Fruit"},
    "banana":    {"qty": 30,  "price": 0.49,  "category": "Fruit"},
    "milk":      {"qty": 20,  "price": 2.49,  "category": "Dairy"},
    "bread":     {"qty": 15,  "price": 3.99,  "category": "Bakery"},
    "cheddar":   {"qty": 8,   "price": 5.99,  "category": "Dairy"},
    "orange":    {"qty": 3,   "price": 1.29,  "category": "Fruit"},
}

LOW_STOCK_THRESHOLD = 10   # Warn if qty drops below this


def add_item(name, qty, price, category):
    if name in inventory:
        inventory[name]["qty"] += qty
        print(f"  Updated '{name}': added {qty} units (new total: {inventory[name]['qty']}).")
    else:
        inventory[name] = {"qty": qty, "price": price, "category": category}
        print(f"  New item '{name}' added to inventory.")


def sell_item(name, qty):
    if name not in inventory:
        print(f"  '{name}' not found in inventory.")
        return
    if inventory[name]["qty"] < qty:
        print(f"  Insufficient stock. Only {inventory[name]['qty']} '{name}' available.")
        return
    inventory[name]["qty"] -= qty
    revenue = qty * inventory[name]["price"]
    print(f"  Sold {qty}x '{name}' for ${revenue:.2f}.")
    if inventory[name]["qty"] < LOW_STOCK_THRESHOLD:
        print(f"  ⚠ LOW STOCK WARNING: only {inventory[name]['qty']} '{name}' left!")


def inventory_report():
    categories = set(item["category"] for item in inventory.values())

    print("\n" + "=" * 55)
    print("                  INVENTORY REPORT")
    print("=" * 55)

    for category in sorted(categories):
        print(f"\n  [{category}]")
        for name, data in inventory.items():
            if data["category"] == category:
                stock_flag = " ⚠ LOW" if data["qty"] < LOW_STOCK_THRESHOLD else ""
                print(f"    {name:<12} qty:{data['qty']:<6} price:${data['price']:.2f}{stock_flag}")

    total_value = sum(d["qty"] * d["price"] for d in inventory.values())
    print(f"\n  Total inventory value: ${total_value:,.2f}")
    print("=" * 55)


# --- Demo ---
inventory_report()

print("\n--- Transactions ---")
sell_item("apple", 45)
sell_item("orange", 2)
add_item("mango", 40, 1.79, "Fruit")
add_item("milk", 30, 2.49, "Dairy")

inventory_report()
