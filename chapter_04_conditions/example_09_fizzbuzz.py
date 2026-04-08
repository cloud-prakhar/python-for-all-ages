# Example 9: FizzBuzz
# A classic programming challenge used in interviews.
# Rule: For numbers 1 to 30:
#   - If divisible by both 3 and 5 → print "FizzBuzz"
#   - If divisible by 3 only        → print "Fizz"
#   - If divisible by 5 only        → print "Buzz"
#   - Otherwise                     → print the number
#
# Key insight: check the most specific condition (divisible by BOTH) FIRST.

for number in range(1, 31):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
