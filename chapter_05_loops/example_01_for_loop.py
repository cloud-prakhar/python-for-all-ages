# Example 1: Basic For Loop
# Real life: Ring the school bell once for each class period (5 times).
#
# HOW THE FOR LOOP WORKS:
#   for <loop_variable> in <sequence>:
#       <body>
#
# WHAT IS "period" HERE?
#   "period" is called the LOOP VARIABLE (also called the iterator variable).
#   Python creates it automatically when the loop starts.
#   Each time the loop runs, Python takes the NEXT value from the sequence
#   and puts it into "period". Then the body runs using that value.
#
#   Loop run 1: period = 1  → prints "RING! Period 1 begins!"
#   Loop run 2: period = 2  → prints "RING! Period 2 begins!"
#   Loop run 3: period = 3  → prints "RING! Period 3 begins!"
#   ... and so on until the sequence is exhausted.
#
# CAN I USE A DIFFERENT NAME?
#   Yes! The loop variable name is your choice — pick something meaningful.
#   These all work exactly the same:
#       for period in range(1, 6):     ← meaningful name (recommended)
#       for i in range(1, 6):          ← "i" is the most common short name
#       for x in range(1, 6):          ← also common for math-style loops
#       for banana in range(1, 6):     ← works, but confusing — avoid this!
#
#   RULE: name the loop variable after WHAT EACH ITEM REPRESENTS.
#   If you're looping through periods → call it "period"
#   If you're looping through students → call it "student"
#   If you're just counting → "i" or "count" is fine

print("School Bell Schedule:")

for period in range(1, 6):
    # range(1, 6) generates: 1, 2, 3, 4, 5
    # Note: range STOPS BEFORE 6 — the end number is NOT included!
    print(f"RING! Period {period} begins!")

print("\nSchool day done!")


# -------------------------------------------------------
# range(start, stop, step) — three parameters
# -------------------------------------------------------
# start : where to begin (included)
# stop  : where to end   (NOT included — stops just before)
# step  : how much to add each time (default is 1)

print("\nCounting by 2s (step = 2):")
for number in range(0, 11, 2):   # 0, 2, 4, 6, 8, 10
    # Here "number" is the loop variable — it takes each value: 0, 2, 4, 6, 8, 10
    print(number, end=" ")        # end=" " prints a space instead of a new line
print()                           # This print() adds the missing new line at the end


# -------------------------------------------------------
# The loop variable only exists DURING the loop.
# After the loop ends, it holds the LAST value it had.
# -------------------------------------------------------
print(f"\nAfter the loop, 'number' still holds its last value: {number}")
