# Example 3: Modulus (%) — The Remainder
# Real life: You have 13 candies and 4 friends.
# Everyone gets 3 candies. How many are LEFT OVER?

total_candies = 13
num_friends = 4

each_gets = total_candies // num_friends   # Floor division — full shares
leftover = total_candies % num_friends     # Remainder — leftover candies

print(f"Total candies: {total_candies}")
print(f"Number of friends: {num_friends}")
print(f"Each friend gets: {each_gets} candies")
print(f"Leftover candies: {leftover}")
print("(You get to keep the leftover ones! 😄)")
