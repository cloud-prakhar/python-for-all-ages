# Chapter 2: Variables & Data Types

---

## What Will You Learn?

- What a variable is and how to create one
- The 4 fundamental data types in Python
- Type conversion and checking types
- How Python stores data in memory (conceptually)

---

## What is a Variable?

A **variable** is a named container that holds a value. When you create a variable, Python reserves a spot in memory and labels it with the name you choose. You can then read that value, change it, or use it in calculations — anytime in your program.

```python
score = 95
print(score)    # 95

score = 100     # Update the value
print(score)    # 100
```

Variables make your programs flexible. Instead of hardcoding the number `95` everywhere, you store it in `score` — and if it changes, you only update it in one place.

### Variable Naming Rules

| Rule | Example |
|------|---------|
| Use letters, numbers, underscores only | `first_name`, `score1` |
| Cannot start with a number | `1name` is invalid |
| No spaces (use `_` instead) | `my_score` not `my score` |
| Case-sensitive | `Score` and `score` are different variables |
| Cannot use reserved words | `if`, `for`, `while` are reserved |

### Good Naming Conventions

- Use **descriptive names**: `total_price` not `tp`
- Use **snake_case** for variables: `first_name`, `user_age`
- Avoid single letters (except in short loops): `i`, `j`, `k` are okay in loops

---

## The 4 Core Data Types

Python automatically detects what kind of data you're storing. You don't need to declare the type — Python figures it out.

### 1. Integer (`int`) — Whole Numbers

Integers are numbers without a decimal point. They can be positive, negative, or zero.

```python
age = 25
temperature = -10
year = 2024
population = 1_400_000_000   # Underscores for readability (optional)
```

### 2. Float (`float`) — Decimal Numbers

Floats are numbers with a decimal point. They're used whenever precision matters.

```python
price = 49.99
pi = 3.14159
body_temp = 98.6
percentage = 87.5
```

**Note:** `10 / 3` in Python always produces a float (`3.3333...`), even if the result is "whole". Use `//` for integer division.

### 3. String (`str`) — Text

A string is any sequence of characters enclosed in single or double quotes. Strings can contain letters, numbers, spaces, symbols — anything.

```python
name = "Alice"
message = 'Hello, World!'
sentence = "Python was created in 1991."
empty = ""          # An empty string is valid
```

**String facts:**
- Strings are **ordered** — each character has a position
- Strings are **immutable** — you can't change individual characters; you create new strings
- You can use `"double"` or `'single'` quotes — both are valid

### 4. Boolean (`bool`) — True or False

Booleans represent one of two values: `True` or `False`. They're the result of comparisons and conditions.

```python
is_logged_in = True
has_permission = False
is_adult = age >= 18    # Evaluates to True or False
```

**Important:** `True` and `False` must be capitalized. `true` or `false` will cause an error.

---

## Type Conversion

Sometimes you need to convert a value from one type to another.

```python
# String to integer
age_str = "25"
age_int = int(age_str)      # 25 (integer)

# Integer to string
score = 95
score_str = str(score)      # "95" (string)

# String to float
price_str = "19.99"
price = float(price_str)    # 19.99 (float)

# Integer to float
x = float(5)                # 5.0

# Float to integer (truncates decimal — does NOT round)
y = int(3.9)                # 3 (not 4!)
```

This is crucial when reading user input — `input()` always returns a **string**, so you must convert it if you need a number.

```python
age = int(input("Enter your age: "))   # Convert string input to int
```

---

## Checking Data Types

Use `type()` to inspect the type of any value or variable.

```python
print(type(42))         # <class 'int'>
print(type(3.14))       # <class 'float'>
print(type("hello"))    # <class 'str'>
print(type(True))       # <class 'bool'>
```

---

## Multiple Assignment

Python lets you assign multiple variables in one line:

```python
x, y, z = 10, 20, 30
name, age = "Alice", 25
a = b = c = 0           # All three get the value 0
```

---

## Examples in This Chapter

| File | What it Does |
|------|-------------|
| [example_01_variables.py](example_01_variables.py) | Creating and updating variables |
| [example_02_integers.py](example_02_integers.py) | Working with integers |
| [example_03_floats.py](example_03_floats.py) | Working with decimal numbers |
| [example_04_strings.py](example_04_strings.py) | Working with text |
| [example_05_booleans.py](example_05_booleans.py) | True and False values |
| [example_06_check_type.py](example_06_check_type.py) | Using type() to inspect data |
| [example_07_my_profile.py](example_07_my_profile.py) | Complete profile card |
