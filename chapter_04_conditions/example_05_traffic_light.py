# Example 5: Traffic Light Simulator
# Real life: What do you do at a traffic light?
#
# NEW CONCEPT: Method chaining — input(...).lower()
#
#   You already know input() returns a string.
#   Strings have built-in tools called METHODS you can use on them.
#   A method is called by putting a dot (.) after the value, then the method name.
#
#   .lower() converts ALL characters in a string to lowercase.
#   Examples:  "RED".lower()   → "red"
#              "Green".lower() → "green"
#              "YELLOW".lower()→ "yellow"
#
#   WHY use .lower() here?
#   If the user types "Red", "RED", or "red" — they all mean the same thing.
#   Without .lower(), we'd have to check all three variations separately.
#   With .lower(), we convert to lowercase once and compare only to "red".
#
#   METHOD CHAINING — two methods in a row:
#   input("...").lower()
#   ↑                  ↑
#   Step 1: get user   Step 2: call .lower() on whatever input() returned
#   input returns → "RED"  →  .lower() converts → "red"
#
#   Methods always act on whatever is to their LEFT of the dot.

light = input("What color is the traffic light? (red/yellow/green): ").lower()

if light == "red":
    print("STOP! 🔴 Wait for the green light.")
elif light == "yellow":
    print("SLOW DOWN! 🟡 Get ready to stop or go.")
elif light == "green":
    print("GO! 🟢 It is safe to cross.")
else:
    print("That is not a valid traffic light color!")
