# Example 10: Prime Number Checker
# A prime number is divisible ONLY by 1 and itself.
# Examples: 2, 3, 5, 7, 11, 13, 17, 19, 23...
# This example shows a practical loop that uses break and else.

def is_prime(n):
    """Return True if n is a prime number, False otherwise."""
    if n < 2:
        return False              # 0 and 1 are not prime

    for divisor in range(2, int(n ** 0.5) + 1):
        # We only need to check up to the square root of n.
        # If n has a factor larger than sqrt(n), the other factor is smaller.
        if n % divisor == 0:
            return False          # Found a divisor — not prime
    return True                   # No divisors found — it's prime


# Part 1: Check a single number
num = int(input("Enter a number to check if it's prime: "))
if is_prime(num):
    print(f"{num} IS a prime number.")
else:
    print(f"{num} is NOT a prime number.")

# Part 2: List all primes up to a limit
limit = int(input("List all primes up to: "))
primes = [n for n in range(2, limit + 1) if is_prime(n)]

print(f"\nPrime numbers up to {limit}:")
print(primes)
print(f"Total primes found: {len(primes)}")
