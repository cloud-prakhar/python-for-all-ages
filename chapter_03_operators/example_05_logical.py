# Example 5: Logical Operators (and, or, not)
# Real life: "Can I go out to play?"
# Mom says: "Yes IF your homework is done AND it's not raining."

homework_done = True
is_raining = False
has_permission = True

# AND: BOTH must be True
can_play_outside = homework_done and (not is_raining)
print(f"Can I play outside? {can_play_outside}")

# OR: at least ONE must be True
can_play = homework_done or has_permission
print(f"Can I play at all? {can_play}")

# NOT: flips True to False and False to True
print(f"Is it NOT raining? {not is_raining}")
print(f"Is homework NOT done? {not homework_done}")
