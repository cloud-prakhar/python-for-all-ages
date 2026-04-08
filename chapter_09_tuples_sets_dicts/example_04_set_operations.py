# Example 4: Set Operations — Union, Intersection, Difference
# Real life: Two friend groups — who's in BOTH? Who's in ONLY one?
#
# SET OPERATORS — Python uses symbols for set math operations.
# These symbols are the same as in mathematics (Venn diagrams).
#
#   |   Union            — everyone from BOTH sets (no duplicates)
#   &   Intersection     — only items that appear in BOTH sets
#   -   Difference       — items in the LEFT set but NOT in the right set
#   ^   Symmetric diff   — items in ONE set but not in BOTH
#
# These operators are overloaded — the same symbols mean different things
# depending on what type of data you use them on:
#   5 | 3   → bitwise OR on integers (different topic)
#   {1,2} | {2,3} → set union
#
# Python knows which meaning to use based on the type (set vs int).

football_team = {"Arjun", "Bharat", "Chetan", "Divya", "Eshan"}
cricket_team  = {"Divya", "Eshan", "Farida", "Gaurav", "Heena"}

print("Football team:", football_team)
print("Cricket team: ", cricket_team)
print()

# | UNION — combine both sets, remove duplicates
# "Give me everyone who plays football OR cricket (or both)"
all_players = football_team | cricket_team
print(f"All players (union |):              {all_players}")

# & INTERSECTION — only items in BOTH sets
# "Give me everyone who plays football AND cricket"
both_teams = football_team & cricket_team
print(f"In both teams (intersection &):     {both_teams}")

# - DIFFERENCE — in left set but NOT in right set
# "Give me football players who do NOT play cricket"
only_football = football_team - cricket_team
print(f"Only in football (difference -):    {only_football}")

# ^ SYMMETRIC DIFFERENCE — in one set but NOT in both
# "Give me players who play exactly ONE sport (not both)"
one_sport_only = football_team ^ cricket_team
print(f"Exactly one sport (symmetric diff ^): {one_sport_only}")
