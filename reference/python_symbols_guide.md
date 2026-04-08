# Python Symbols Guide — When to Use What

> Read this before starting Chapter 2. Refer back to it whenever a symbol confuses you.

Python uses several different types of brackets and symbols — each with a specific meaning
depending on the context. This guide explains what each one does and when you'll see it.

---

## ( ) — Parentheses

Parentheses serve **three different jobs** in Python:

### 1. Calling a Function

When you write a name followed by `()`, you are **calling** (running) that function.
Whatever goes inside the parentheses is the **input** you give to the function.

```python
print("Hello")       # Calling print(), giving it the text "Hello"
len("Python")        # Calling len(), giving it the string "Python"
int("25")            # Calling int(), converting the string "25" to the number 25
input("Your name: ") # Calling input(), giving it the prompt text
```

The rule: **name + `()` = call the function**.
No parentheses = you're just referring to the function, not running it.

### 2. Grouping Math (like in real mathematics)

```python
result = (2 + 3) * 4   # Add first, then multiply → 20
result = 2 + 3 * 4     # Multiply first (default) → 14
```

### 3. Creating a Tuple (a locked list)

```python
point      = (10, 20)          # A tuple with two numbers
rgb_color  = (255, 128, 0)     # Red, Green, Blue values
date       = (2024, 12, 25)    # Year, Month, Day
```

You'll learn tuples fully in Chapter 9.

---

## [ ] — Square Brackets

Square brackets serve **two jobs** in Python:

### 1. Creating a List

```python
fruits   = ["apple", "banana", "cherry"]   # A list of strings
scores   = [85, 92, 78, 95]                # A list of integers
mixed    = ["Alice", 25, True]             # A list of mixed types
empty    = []                              # An empty list
```

You'll learn lists fully in Chapter 8.

### 2. Accessing an Item by Position (Indexing)

Once you have a list or a string, square brackets let you reach into it and get a
specific item using its **index** (position number, starting from 0).

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # apple   ← first item (index 0)
print(fruits[1])   # banana  ← second item (index 1)
print(fruits[-1])  # cherry  ← last item (negative index)

name = "Python"
print(name[0])     # P  ← first character
print(name[2])     # t  ← third character
```

Square brackets after a variable name = **"give me the item at this position"**.

### 3. Slicing (Getting a Range of Items)

```python
word = "Python"
print(word[0:3])   # Pyt   ← characters from index 0 up to (not including) 3
print(word[2:])    # thon  ← from index 2 to the end
```

---

## { } — Curly Braces

Curly braces have **three different uses** in Python. The context tells you which one it is.

### 1. Inside an f-String: Placeholder for a Variable

When a string starts with `f"..."`, the `{}` inside it are **placeholders** — slots where
Python inserts the actual value of a variable.

```python
name  = "Alice"
score = 95

print(f"Hello, {name}!")          # Hello, Alice!
print(f"Your score is {score}.")  # Your score is 95.
print(f"Next year: {2024 + 1}")   # Next year: 2025  ← expressions work too!
```

The `f` before the opening quote is what tells Python "this is an f-string — look for `{}`
placeholders and replace them with values."

Without the `f`, curly braces are printed literally:
```python
print("Hello, {name}!")   # Hello, {name}!  ← not substituted, no f prefix
print(f"Hello, {name}!")  # Hello, Alice!   ← substituted, has f prefix
```

### 2. Creating a Dictionary (key: value pairs)

```python
person = {"name": "Alice", "age": 25, "city": "London"}
#          key      value    key   value  key      value
```

Notice the **colon `:`** separating each key from its value — that's what makes this a
dictionary, not a set. You'll learn dictionaries in Chapter 9.

### 3. Creating a Set (unique items, no duplicates)

```python
colors  = {"red", "green", "blue"}   # A set — no colons, no key:value pairs
numbers = {1, 2, 3, 4, 5}
```

No colons = it's a set. With colons = it's a dictionary.
You'll learn sets in Chapter 9.

---

## Summary Table

| Symbol | What it looks like | What it means |
|--------|--------------------|---------------|
| `name()` | Name followed by `()` | Call (run) a function |
| `(a, b)` | Values separated by commas in `()` | Tuple — locked sequence |
| `(2 + 3) * 4` | Math inside `()` | Grouping — controls calculation order |
| `[a, b, c]` | Values in `[]` | List — ordered, changeable collection |
| `word[0]` | Variable name + `[number]` | Index — get item at that position |
| `word[1:4]` | Variable name + `[x:y]` | Slice — get a range of items |
| `f"{name}"` | `{}` inside `f"..."` | f-string placeholder — insert variable value |
| `{k: v}` | Key-colon-value in `{}` | Dictionary |
| `{a, b, c}` | Values (no colons) in `{}` | Set |

---

## : — The Colon

The colon appears in several places with different roles:

| Context | Example | Meaning |
|---------|---------|---------|
| End of `if`/`for`/`while`/`def` | `if x > 0:` | Starts an indented block |
| Dictionary | `{"name": "Alice"}` | Separates a key from its value |
| f-string format spec | `f"{score:.2f}"` | Format the value (see below) |
| Slice | `word[1:4]` | Separates start and end of a range |

---

## :.2f — Format Specifiers Inside f-Strings

Inside f-string `{}` placeholders, you can add a colon `:` followed by formatting
instructions to control how a value is displayed.

```python
price = 9.9876543

print(f"{price}")         # 9.9876543  ← raw value
print(f"{price:.2f}")     # 9.99       ← rounded to 2 decimal places
print(f"{price:.0f}")     # 10         ← rounded to 0 decimal places
print(f"{price:10.2f}")   # "      9.99"  ← 10 characters wide, right-aligned
```

The format: `{variable_name : width . decimal_places f}`
- `f` at the end means "float" (decimal number)
- The number before the `.` is the total width
- The number after the `.` is decimal places

Common ones you'll see:
- `:.2f` → 2 decimal places (e.g. prices: `9.99`)
- `:.1f` → 1 decimal place (e.g. temperatures: `36.6`)
- `:,` → thousands separator (e.g. `1,000,000`)
- `:<10` → left-align in 10 characters
- `:>10` → right-align in 10 characters

---

## . — The Dot (Method Calls)

When you see a dot after a variable name, it means you're calling a **method** —
a function that belongs to that specific type of object.

```python
name = "alice"
name.upper()     # Call the upper() method on the string "alice" → "ALICE"
name.title()     # Call the title() method → "Alice"

fruits = ["banana", "apple", "cherry"]
fruits.sort()    # Call the sort() method on the list
fruits.append("mango")  # Call append() on the list
```

Think of it as: **the object owns the method**. The dot is how you access what it owns.

Method chaining — calling multiple methods in a row:
```python
user_input = input("Enter: ").strip().lower()
#                              ↑             ↑
#                   remove spaces    make lowercase
```
Each method runs left to right on the result of the previous one.

---

## Quick Reference by Chapter

| Chapter | New symbols introduced |
|---------|----------------------|
| Ch 1 | `print()`, `input()` — parentheses for function calls |
| Ch 2 | `f"{}"` — f-string placeholders |
| Ch 3 | Arithmetic operators `+ - * / // % **` |
| Ch 4 | `:` after `if`/`elif`/`else`, indentation block |
| Ch 5 | `range()`, `:` after `for`/`while` |
| Ch 6 | `def name():` — defining functions |
| Ch 7 | String slicing `[start:stop:step]`, `:.2f` format specs |
| Ch 8 | `[...]` lists, `[index]` indexing |
| Ch 9 | `(...)` tuples, `{...}` sets, `{key: value}` dicts |
