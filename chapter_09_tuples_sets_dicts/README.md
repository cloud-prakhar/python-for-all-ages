# Chapter 9: Tuples, Sets & Dictionaries

---

## What Will You Learn?

- **Tuples** — immutable sequences
- **Sets** — unordered collections with no duplicates
- **Dictionaries** — key-value data stores
- When to use each collection type
- Common patterns and operations

---

## Tuples

A **tuple** is an ordered, **immutable** sequence. Once created, its contents cannot be changed — no adding, removing, or modifying items.

```python
point = (3, 7)
rgb = (255, 128, 0)
person = ("Alice", 30, "Engineer")
```

### Why use a tuple instead of a list?

| Reason | Explanation |
|--------|-------------|
| **Safety** | Prevents accidental modification of data that shouldn't change |
| **Performance** | Tuples are slightly faster than lists for iteration and creation |
| **Hashability** | Tuples can be used as dictionary keys; lists cannot |
| **Semantic meaning** | Communicates intent — "this data is fixed" |

```python
# Tuple indexing and slicing work like lists
coordinates = (10.5, 20.3, 5.0)
print(coordinates[0])     # 10.5
print(coordinates[1:])    # (20.3, 5.0)
```

### Tuple Packing and Unpacking

```python
# Packing
student = ("Arjun", 20, "Computer Science")

# Unpacking — distribute values into individual variables
name, age, major = student
print(name)    # Arjun
print(age)     # 20

# Swap two variables elegantly
a, b = 10, 20
a, b = b, a    # One line — no temporary variable needed
```

### Single-item Tuple

A tuple with one item requires a trailing comma:
```python
single = (42,)    # This is a tuple
not_tuple = (42)  # This is just an integer in parentheses
```

---

## Sets

A **set** is an **unordered collection of unique items**. Sets are optimized for membership testing and eliminating duplicates.

```python
fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)    # {'apple', 'banana', 'cherry'} — duplicate removed
```

**Key properties:**
- No duplicates — each value appears at most once
- No guaranteed order — don't rely on position
- Items must be **hashable** (strings, numbers, tuples work; lists do not)

### Set Methods

| Method | What it Does |
|--------|-------------|
| `.add(x)` | Add item |
| `.remove(x)` | Remove item (KeyError if missing) |
| `.discard(x)` | Remove item (no error if missing) |
| `.pop()` | Remove and return an arbitrary item |
| `.clear()` | Remove all items |
| `x in set` | Membership check (very fast — O(1)) |
| `len(set)` | Number of items |

### Set Operations

Sets support mathematical set operations:

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A | B)    # Union         — all items from both:  {1,2,3,4,5,6,7,8}
print(A & B)    # Intersection  — items in BOTH:        {4, 5}
print(A - B)    # Difference    — in A but not B:       {1, 2, 3}
print(A ^ B)    # Symmetric diff — in one but not both: {1,2,3,6,7,8}
```

### Removing Duplicates from a List

A common use of sets:

```python
data = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(data))    # Convert to set (removes duplicates), back to list
```

---

## Dictionaries

A **dictionary** stores data as **key: value** pairs. Keys must be unique and hashable; values can be anything.

```python
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "enrolled": True
}
```

Think of a dictionary like a real dictionary — you look up a **word** (key) to get its **definition** (value). Or like a phone book — look up a **name** to get a **number**.

### Accessing Values

```python
print(student["name"])          # Alice — direct access (KeyError if not found)
print(student.get("age"))       # 20    — safe access (returns None if not found)
print(student.get("gpa", 0.0))  # 0.0  — default value if key missing
```

### Modifying Dictionaries

```python
# Add or update
student["email"] = "alice@example.com"   # Add new key
student["age"] = 21                       # Update existing key

# Delete
del student["enrolled"]          # Delete key (KeyError if missing)
student.pop("grade")             # Delete and return value
student.pop("missing", None)     # Safe delete — no error if missing
```

### Iterating Over a Dictionary

```python
d = {"a": 1, "b": 2, "c": 3}

for key in d:                          # Iterate keys
    print(key)

for key, value in d.items():           # Iterate key-value pairs
    print(f"{key}: {value}")

for value in d.values():               # Iterate values only
    print(value)
```

### Dictionary Methods

| Method | What it Does |
|--------|-------------|
| `.keys()` | View of all keys |
| `.values()` | View of all values |
| `.items()` | View of all (key, value) pairs |
| `.get(key, default)` | Get value safely |
| `.pop(key, default)` | Remove and return value |
| `.update(other_dict)` | Merge another dict in |
| `.setdefault(key, val)` | Get key; set default if missing |

### Nested Dictionaries

Dictionaries can contain other dictionaries — ideal for structured data:

```python
employees = {
    "E001": {"name": "Alice", "dept": "Engineering", "salary": 75000},
    "E002": {"name": "Bob",   "dept": "Marketing",   "salary": 60000},
}

print(employees["E001"]["name"])     # Alice
print(employees["E002"]["dept"])     # Marketing
```

### Dictionary Comprehensions

Like list comprehensions, but for dicts:

```python
squares = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

filtered = {k: v for k, v in squares.items() if v > 5}
# {3: 9, 4: 16, 5: 25}
```

---

## Choosing the Right Collection

| Need | Use |
|------|-----|
| Ordered, changeable sequence | `list` |
| Ordered, fixed/immutable sequence | `tuple` |
| Unique items, fast membership test | `set` |
| Key-value lookup | `dict` |
| Dictionary key (must be hashable) | `tuple` (not list) |

---

## Examples in This Chapter

| File | What it Does |
|------|-------------|
| [example_01_tuples.py](example_01_tuples.py) | Creating and using tuples |
| [example_02_tuple_unpack.py](example_02_tuple_unpack.py) | Unpacking tuples |
| [example_03_sets_basics.py](example_03_sets_basics.py) | Creating and using sets |
| [example_04_set_operations.py](example_04_set_operations.py) | Union, intersection, difference |
| [example_05_dict_basics.py](example_05_dict_basics.py) | Creating and reading dictionaries |
| [example_06_dict_methods.py](example_06_dict_methods.py) | Modifying dictionaries |
| [example_07_student_database.py](example_07_student_database.py) | Nested dict — student records |
| [example_08_word_counter.py](example_08_word_counter.py) | Count word frequency |
| [example_09_nested_dict.py](example_09_nested_dict.py) | Deep nested dictionaries |
| [example_10_inventory_system.py](example_10_inventory_system.py) | Inventory management system |
