# Example 9: Variable Scope — Local vs Global
# Scope determines WHERE a variable can be accessed.
# Local  = only inside the function where it was created.
# Global = created outside all functions, accessible everywhere.

global_greeting = "Hello"    # Global variable

def show_scope():
    local_message = "I only exist inside this function."   # Local variable
    print(global_greeting)    # Can READ the global variable
    print(local_message)

show_scope()
print(global_greeting)        # Works — global
# print(local_message)        # ERROR — local_message doesn't exist out here


# --- Why this matters: avoid accidental side effects ---

total = 0   # Global counter

def bad_approach(x):
    global total    # Declaring intent to modify the global
    total += x      # Modifying a global inside a function — fragile design

def good_approach(current_total, x):
    return current_total + x   # Better: pass in, return out — no hidden state

bad_approach(10)
bad_approach(5)
print(f"\nBad approach total: {total}")

result = 0
result = good_approach(result, 10)
result = good_approach(result, 5)
print(f"Good approach total: {result}")

print("\nLesson: prefer passing values in and returning results out.")
print("Reserve globals for true constants (values that never change).")
