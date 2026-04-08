# Example 10: Recursion — Functions That Call Themselves
# Recursion: a function solves a problem by solving a smaller version of
# the same problem, then combining the results.
#
# Every recursive function needs:
#   1. Base case  — when to STOP (no more recursive calls)
#   2. Recursive case — call itself with a simpler/smaller input

# --- Example 1: Factorial ---
# factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
# factorial(n) = n * factorial(n-1)

def factorial(n):
    if n == 0:                     # Base case: factorial(0) = 1
        return 1
    return n * factorial(n - 1)   # Recursive case

print("Factorials:")
for i in range(8):
    print(f"  {i}! = {factorial(i)}")


# --- Example 2: Sum of digits ---
# sum_digits(1234) = 1 + 2 + 3 + 4 = 10

def sum_digits(n):
    n = abs(n)            # Handle negative numbers
    if n < 10:            # Base case: single digit
        return n
    return n % 10 + sum_digits(n // 10)   # Last digit + recurse on rest

print("\nSum of digits:")
for num in [0, 7, 123, 9999, 54321]:
    print(f"  sum_digits({num}) = {sum_digits(num)}")


# --- Example 3: Power function ---
# power(2, 8) = 2^8 = 256

def power(base, exp):
    if exp == 0:          # Base case: anything^0 = 1
        return 1
    return base * power(base, exp - 1)

print("\nPowers:")
print(f"  2^10 = {power(2, 10)}")
print(f"  3^5  = {power(3, 5)}")
