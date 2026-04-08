# Example 3: Function with Return Value
# return sends a result BACK from the function.
# Real life: You send a question to a friend, they send back an ANSWER!

def add_numbers(a, b):
    result = a + b
    return result       # Send the answer back!

def multiply(a, b):
    return a * b        # Can return directly too

# Store the returned value in a variable
sum_result = add_numbers(10, 5)
print(f"10 + 5 = {sum_result}")

product = multiply(4, 6)
print(f"4 x 6 = {product}")

# Use returned value directly in print
print(f"7 + 8 = {add_numbers(7, 8)}")
