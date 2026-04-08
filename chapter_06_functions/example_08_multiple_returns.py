# Example 8: Returning Multiple Values
# A Python function can return multiple values packed as a tuple.
# The caller can unpack them into separate variables.

def analyze_numbers(numbers):
    """Return the min, max, sum, and average of a list of numbers."""
    total = sum(numbers)
    count = len(numbers)
    return min(numbers), max(numbers), total, round(total / count, 2)


def divide_with_remainder(dividend, divisor):
    """Return both the quotient and the remainder."""
    quotient  = dividend // divisor
    remainder = dividend %  divisor
    return quotient, remainder


# --- Using analyze_numbers ---
data = [45, 82, 17, 93, 66, 51, 38]

smallest, largest, total, average = analyze_numbers(data)

print(f"Data   : {data}")
print(f"Minimum: {smallest}")
print(f"Maximum: {largest}")
print(f"Sum    : {total}")
print(f"Average: {average}")

# --- Using divide_with_remainder ---
print()
q, r = divide_with_remainder(47, 5)
print(f"47 ÷ 5 = {q} remainder {r}")
