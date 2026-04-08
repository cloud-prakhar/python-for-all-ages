# Example 6: Default Parameters
# Default values are used when you don't pass an argument.
# Real life: A pizza place assumes you want regular size UNLESS you say otherwise.

def order_pizza(topping, size="medium"):
    print(f"Ordering a {size} pizza with {topping}! 🍕")

# Uses the default size "medium"
order_pizza("cheese")
order_pizza("pepperoni")

# Override the default
order_pizza("mushroom", "large")
order_pizza("veggie", "small")
