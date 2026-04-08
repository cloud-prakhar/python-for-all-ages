# Python Keywords Guide

> Python keywords are reserved words that have a fixed, special meaning.
> You **cannot** use them as variable names or function names.
> This guide explains each keyword, what it does, and when you'll first see it in this course.

---

## What Is a Keyword?

A keyword is a word that Python has already claimed for its own use. If you try to name a variable using a keyword, you'll get an error:

```python
for = 10        # SyntaxError — 'for' is a keyword
if = "hello"   # SyntaxError — 'if' is a keyword
```

Python has **35 keywords** in total. You don't need to memorise them all at once — this guide is organised by the chapter in which each one appears.

---

## Quick Reference — All 35 Keywords

| Keyword | One-line meaning |
|---------|-----------------|
| `True` | Boolean value for "yes / on / correct" |
| `False` | Boolean value for "no / off / incorrect" |
| `None` | Represents "nothing" or "no value" |
| `and` | Both conditions must be true |
| `or` | At least one condition must be true |
| `not` | Flip a condition (True → False, False → True) |
| `if` | Run code only if a condition is true |
| `elif` | Check another condition if the previous one was false |
| `else` | Run code when all conditions above were false |
| `for` | Loop over a sequence a known number of times |
| `while` | Keep looping as long as a condition is true |
| `break` | Exit a loop immediately |
| `continue` | Skip the current loop iteration and go to the next |
| `in` | Check if a value exists in a sequence |
| `is` | Check if two variables point to the exact same object |
| `def` | Define (create) a function |
| `return` | Send a value back from a function |
| `pass` | Do nothing — placeholder for empty blocks |
| `global` | Tell Python a variable is from the outer (global) scope |
| `nonlocal` | Tell Python a variable is from the enclosing function's scope |
| `import` | Load a module (extra tools) into your program |
| `from` | Import a specific item from a module |
| `as` | Give an import or exception an alias (nickname) |
| `class` | Define a new type of object (Object-Oriented Programming) |
| `del` | Delete a variable or remove an item from a list/dict |
| `lambda` | Create a small anonymous (unnamed) function in one line |
| `try` | Start a block of code that might cause an error |
| `except` | Handle an error that happened in a `try` block |
| `finally` | Code that always runs after a `try/except` block |
| `raise` | Manually trigger (throw) an error |
| `with` | Manage a resource (like a file) that needs cleanup |
| `assert` | Test that something is true — crash if it isn't |
| `yield` | Pause a function and send a value (generators) |
| `async` | Define a function that can run asynchronously |
| `await` | Wait for an async operation to complete |

---

## Keywords by Chapter

### Chapter 2 — Variables & Data Types

#### `True` and `False`
The two possible values of a **boolean** (bool) data type. Always capitalised.

```python
is_raining = True
has_ticket = False

print(type(True))   # <class 'bool'>
```

> Think of it like a light switch — it's either ON (True) or OFF (False). Nothing in between.

#### `None`
Represents "nothing" or "no value at all". It's Python's way of saying a variable exists but has no meaningful value yet.

```python
result = None          # result exists, but has no value yet
print(result)          # None
print(type(None))      # <class 'NoneType'>
```

> A function that doesn't have a `return` statement automatically returns `None`.

---

### Chapter 3 — Operators

#### `and`
Both conditions on the left **and** right must be `True` for the overall result to be `True`.

```python
age = 20
has_id = True

can_enter = age >= 18 and has_id
print(can_enter)   # True — both are True

# Truth table:
# True  and True  → True
# True  and False → False
# False and True  → False
# False and False → False
```

#### `or`
At least **one** of the conditions must be `True`.

```python
is_weekend = True
is_holiday = False

can_sleep_in = is_weekend or is_holiday
print(can_sleep_in)   # True — one of them is True

# Truth table:
# True  or True  → True
# True  or False → True
# False or True  → True
# False or False → False
```

#### `not`
Flips a boolean value. `True` becomes `False`, and `False` becomes `True`.

```python
is_raining = False
print(not is_raining)   # True — flipped

is_logged_in = True
print(not is_logged_in) # False — flipped
```

> Useful for checking the opposite: "if NOT logged in, redirect to login page."

---

### Chapter 4 — Conditions

#### `if`
Runs a block of code **only if** the condition is `True`.

```python
score = 85

if score >= 90:
    print("Grade: A")   # This runs only when score >= 90
```

> Notice the colon `:` at the end of the `if` line and the 4-space indentation for the block inside.

#### `elif`
Short for "else if". Checks another condition if all previous conditions were `False`. Python tests conditions top-to-bottom and stops at the first `True` one.

```python
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")   # ← This one runs (75 >= 70 is True)
```

#### `else`
Runs when **all** the `if` and `elif` conditions above it were `False`. It has no condition of its own.

```python
score = 45

if score >= 60:
    print("Passed")
else:
    print("Failed")   # ← This runs (45 >= 60 is False)
```

#### `in`
Checks whether a value exists inside a sequence (string, list, tuple, dict, set).

```python
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)   # True
print("mango" in fruits)    # False

name = "Python"
print("y" in name)          # True
print("z" in name)          # False
```

#### `is`
Checks if two variables point to the **exact same object** in memory (not just equal values). Most beginners use `==` to compare values — `is` is for identity checks.

```python
x = None
if x is None:
    print("x has no value yet")

# is vs ==
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # True  — same content
print(a is b)   # False — different objects in memory

# RULE OF THUMB: Use == to compare values. Use 'is' only for None checks.
```

---

### Chapter 5 — Loops

#### `for`
Repeats a block of code for each item in a sequence. You know in advance how many times it will run.

```python
# Loop over a range of numbers
for i in range(1, 6):
    print(i)   # Prints 1, 2, 3, 4, 5

# Loop over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

#### `while`
Keeps repeating a block of code **as long as** a condition is `True`. Use when you don't know in advance how many iterations you need.

```python
count = 1

while count <= 5:
    print(count)
    count += 1    # Important: always move toward the exit condition!
```

> **Warning:** If the condition never becomes `False`, the loop runs forever (infinite loop). Use `Ctrl + C` to stop it.

#### `break`
Exits the loop immediately, regardless of the loop's condition.

```python
for i in range(1, 11):
    if i == 5:
        break          # Stop the loop when i reaches 5
    print(i)           # Prints 1, 2, 3, 4
print("Loop ended early")
```

#### `continue`
Skips the **rest of the current iteration** and jumps to the next one.

```python
for i in range(1, 11):
    if i % 2 == 0:
        continue       # Skip even numbers
    print(i)           # Prints: 1, 3, 5, 7, 9
```

> `break` = exit the whole loop. `continue` = skip this one iteration only.

---

### Chapter 6 — Functions

#### `def`
Defines (creates) a new function. The function body (the indented block below) only runs when you **call** the function by name.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")   # Hello, Alice!
greet("Bob")     # Hello, Bob!
```

#### `return`
Sends a value **back** from the function to the place that called it. After `return`, the function stops.

```python
def square(n):
    return n * n

result = square(5)   # result = 25
print(result + 10)   # 35 — we can use the returned value in expressions
```

> `print()` only shows a value on screen. `return` gives the value back so you can use it in your program.

#### `pass`
A placeholder that does nothing. Useful when Python requires a code block but you haven't written the logic yet.

```python
def coming_soon():
    pass   # Function defined but empty — no error!

if True:
    pass   # Empty if block — valid Python
```

#### `global`
Declares that a variable inside a function refers to the **global** (module-level) variable, not a local one.

```python
counter = 0

def increment():
    global counter     # Without this, counter would be a new local variable
    counter += 1

increment()
increment()
print(counter)   # 2
```

> **Best practice:** Avoid `global` when possible. Pass values in as parameters and use `return` instead — it makes code easier to understand.

---

### Chapter 7 — Strings (and earlier chapters)

#### `import`
Loads a **module** — a file of extra tools and functions — into your program. Python has hundreds of built-in modules.

```python
import math

print(math.pi)           # 3.141592653589793
print(math.sqrt(16))     # 4.0
print(math.ceil(4.3))    # 5
```

#### `from`
Imports a **specific item** from a module, so you can use it directly without the module name prefix.

```python
from math import sqrt, pi

print(sqrt(25))   # 5.0    ← no 'math.' needed
print(pi)         # 3.141592653589793
```

#### `as`
Gives an imported module or item a **nickname** (alias). Common for long module names.

```python
import random as r

print(r.randint(1, 10))   # Random number — shorter to type than random.randint
```

---

### Chapter 9 — Collections

#### `del`
Removes a variable, or deletes an item from a list or dictionary.

```python
# Remove a variable
x = 10
del x
# print(x)   # NameError — x no longer exists

# Remove from a list by index
fruits = ["apple", "banana", "cherry"]
del fruits[1]
print(fruits)   # ["apple", "cherry"]

# Remove from a dictionary by key
person = {"name": "Alice", "age": 25}
del person["age"]
print(person)   # {"name": "Alice"}
```

---

## Keywords You'll Encounter Later

These keywords go beyond the scope of this course. They are listed here so you recognise them when you see them.

| Keyword | Used in | Brief description |
|---------|---------|------------------|
| `class` | Object-Oriented Programming | Define a new type (blueprint for objects) |
| `lambda` | Functional programming | One-line anonymous function: `lambda x: x * 2` |
| `try` / `except` / `finally` | Error handling | Catch and handle runtime errors gracefully |
| `raise` | Error handling | Manually trigger an error |
| `with` | File handling | Open a resource and automatically close it when done |
| `assert` | Testing / debugging | Check that a condition is True — crash with a message if not |
| `yield` | Generators | Pause a function and produce a series of values one at a time |
| `async` / `await` | Asynchronous programming | Run multiple tasks concurrently (advanced) |
| `nonlocal` | Nested functions | Access a variable from an enclosing (but non-global) function |

---

## Common Mistakes with Keywords

| Mistake | What happens | Fix |
|---------|-------------|-----|
| `if = 5` | `SyntaxError` — `if` is reserved | Rename: `if_condition = 5` |
| `for = "loop"` | `SyntaxError` | Rename: `loop_count = ...` |
| `true` / `false` / `none` | `NameError` — wrong capitalisation | Use `True`, `False`, `None` (capital first letter) |
| `x is 5` | Works but wrong tool | Use `x == 5` to compare values |
| Function returns `None` | Forgot `return` statement | Add `return value` inside the function |

---

## Quick Reference by Chapter

| Chapter | Keywords introduced |
|---------|-------------------|
| Ch 2 | `True`, `False`, `None` |
| Ch 3 | `and`, `or`, `not` |
| Ch 4 | `if`, `elif`, `else`, `in`, `is` |
| Ch 5 | `for`, `while`, `break`, `continue` |
| Ch 6 | `def`, `return`, `pass`, `global` |
| Ch 7 | `import`, `from`, `as` |
| Ch 9 | `del` |
| Beyond course | `class`, `lambda`, `try`, `except`, `finally`, `raise`, `with`, `assert`, `yield`, `async`, `await`, `nonlocal` |
