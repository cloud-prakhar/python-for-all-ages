# Example 7: Piggy Bank Story
# Real life: Track your savings and spending like a real piggy bank!

piggy_bank = 50        # Starting savings in Rs.
pocket_money = 20      # Weekly pocket money
spent_on_snacks = 15   # Money spent
spent_on_pencils = 8   # Money spent

# Add money
piggy_bank = piggy_bank + pocket_money
print(f"After pocket money: Rs. {piggy_bank}")

# Spend money
piggy_bank = piggy_bank - spent_on_snacks - spent_on_pencils
print(f"After buying snacks and pencils: Rs. {piggy_bank}")

# Check if I can afford a book that costs Rs. 55
book_cost = 55
print(f"Can I buy the book (Rs. {book_cost})? {piggy_bank >= book_cost}")
