# Example 2: Rocket Countdown!
# Real life: Like the countdown before a rocket launches. 10... 9... 8... Blast off!
#
# NEW CONCEPT 1: import — using a module
#
#   Python comes with many pre-built tools called MODULES.
#   A module is like a toolbox — it contains ready-made functions.
#   To use a module, you must first IMPORT it:
#
#       import time
#
#   After this line, you can use anything from the "time" module
#   by writing:  time.something()
#   The dot means "look inside the time module and use this tool."
#
#   "time" is a built-in Python module that deals with time-related functions.
#
# NEW CONCEPT 2: time.sleep(seconds)
#
#   time.sleep(0.5) pauses your program for 0.5 seconds (half a second).
#   The number inside the parentheses is how many seconds to pause.
#   time.sleep(1) = pause for 1 second
#   time.sleep(2) = pause for 2 seconds
#
# NEW CONCEPT 3: range(10, 0, -1) — counting DOWN with a negative step
#
#   range(start, stop, step) with a NEGATIVE step counts backwards:
#       range(10, 0, -1) produces: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
#   Stop is still NOT included — so it stops at 1, not 0.
#
#   Think of step as "how much to ADD each time."
#   Normally step=1 means go up: 0, 1, 2, 3...
#   step=-1 means go down: 10, 9, 8, 7...

import time   # Load the time module so we can use time.sleep()

print("ROCKET LAUNCH COUNTDOWN!")
print("=========================")

for i in range(10, 0, -1):   # i takes values: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
    print(f"{i}...")
    time.sleep(0.5)           # Pause for half a second between each number

print("BLAST OFF!!!")
