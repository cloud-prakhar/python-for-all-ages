# Chapter 8: Lists & Arrays

---

## What Will You Learn?

- Creating, accessing, and modifying lists
- List methods and operations
- Sorting and searching
- Slicing lists
- Nested lists (2D arrays)
- List comprehensions
- Common list patterns and algorithms

---

## What is a List?

A **list** is Python's most versatile built-in data structure. It stores an **ordered, mutable collection** of items. Items can be of any type — integers, strings, floats, booleans, even other lists.

In most other programming languages, this is called an **array**. Python's list is more flexible — it can grow, shrink, and hold mixed types.

```python
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40, 50]
mixed = ["Alice", 25, True, 3.14]
empty = []
```

**Ordered** — items maintain the order in which they were added.
**Mutable** — you can add, remove, or change items after creation.
**Dynamic** — lists grow and shrink automatically; no fixed size.

---

## Indexing

Like strings, lists use zero-based indexing.

```python
fruits = ["apple", "banana", "cherry", "date"]
#            0         1         2        3

print(fruits[0])    # apple
print(fruits[-1])   # date  (last item)
print(fruits[-2])   # cherry (second to last)
```

### Modifying by Index

Unlike strings, lists are mutable — you can change items:

```python
fruits[1] = "mango"    # Replace "banana" with "mango"
print(fruits)          # ["apple", "mango", "cherry", "date"]
```

---

## Essential List Methods

| Method | What it Does |
|--------|-------------|
| `.append(x)` | Add item to the end |
| `.insert(i, x)` | Insert item at position i |
| `.extend(iterable)` | Add all items from another list |
| `.remove(x)` | Remove first occurrence of x (error if not found) |
| `.pop(i)` | Remove and return item at index i (default: last) |
| `.clear()` | Remove all items |
| `.index(x)` | Return index of first occurrence of x |
| `.count(x)` | Count occurrences of x |
| `.sort()` | Sort in place (modifies original) |
| `.reverse()` | Reverse in place |
| `.copy()` | Return a shallow copy |
| `len(lst)` | Number of items |
| `sorted(lst)` | Return a new sorted list (original unchanged) |
| `sum(lst)` | Sum all numeric items |
| `min(lst)` / `max(lst)` | Smallest / largest item |

---

## Slicing Lists

List slicing works identically to string slicing:

```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(nums[2:6])     # [2, 3, 4, 5]
print(nums[:4])      # [0, 1, 2, 3]
print(nums[6:])      # [6, 7, 8, 9]
print(nums[::2])     # [0, 2, 4, 6, 8]  — every other
print(nums[::-1])    # [9, 8, 7, ..., 0] — reversed
```

Slicing creates a **new list** — the original is not modified.

---

## Iterating Over Lists

```python
colors = ["red", "green", "blue"]

# Simple iteration
for color in colors:
    print(color)

# With index using enumerate
for i, color in enumerate(colors, start=1):
    print(f"{i}. {color}")
```

---

## Nested Lists (2D Arrays)

A list can contain other lists — creating a grid-like structure.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])        # [1, 2, 3] — first row
print(matrix[1][2])     # 6         — row 1, column 2

# Iterate all cells
for row in matrix:
    for cell in row:
        print(cell, end=" ")
    print()
```

---

## List Comprehensions

A **list comprehension** is a concise way to create a list using a single line. It replaces the pattern of creating an empty list and appending in a loop.

```python
# Traditional way
squares = []
for x in range(1, 6):
    squares.append(x ** 2)

# List comprehension — same result, one line
squares = [x ** 2 for x in range(1, 6)]
# [1, 4, 9, 16, 25]

# With a condition
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
# [4, 16, 36, 64, 100]
```

The general form: `[expression for item in iterable if condition]`

---

## Copying Lists

Be careful with assignment — it creates a **reference**, not a copy:

```python
a = [1, 2, 3]
b = a           # b points to the SAME list as a
b.append(4)
print(a)        # [1, 2, 3, 4] — a was changed too!

# To create an independent copy:
c = a.copy()    # or: c = a[:]  or: c = list(a)
c.append(5)
print(a)        # [1, 2, 3, 4] — a is unchanged
```

---

## Examples in This Chapter

| File | What it Does |
|------|-------------|
| [example_01_create_list.py](example_01_create_list.py) | Creating lists |
| [example_02_indexing.py](example_02_indexing.py) | Accessing items by index |
| [example_03_add_remove.py](example_03_add_remove.py) | Adding and removing items |
| [example_04_loop_list.py](example_04_loop_list.py) | Looping with enumerate |
| [example_05_sort_reverse.py](example_05_sort_reverse.py) | Sorting and reversing |
| [example_06_list_slicing.py](example_06_list_slicing.py) | Slicing lists |
| [example_07_2d_list.py](example_07_2d_list.py) | 2D lists and grids |
| [example_08_shopping_cart.py](example_08_shopping_cart.py) | Interactive shopping cart |
| [example_09_list_comprehension.py](example_09_list_comprehension.py) | List comprehensions |
| [example_10_marks_analyzer.py](example_10_marks_analyzer.py) | Statistical analysis on a list |
