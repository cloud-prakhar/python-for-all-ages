# Chapter 3: Operators

---

## What Will You Learn?

- Arithmetic operators (math operations)
- Comparison operators (evaluating relationships between values)
- Logical operators (combining conditions)
- Assignment operators (shortcuts for updating variables)
- Operator precedence (which operations run first)

---

## What is an Operator?

An **operator** is a symbol that performs an operation on one or more values (called **operands**). Operators are the building blocks of expressions — anything that computes a result.

```python
result = 10 + 5    # + is the operator, 10 and 5 are operands
```

---

## Arithmetic Operators

These perform mathematical calculations.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `10 - 4` | `6` |
| `*` | Multiplication | `3 * 4` | `12` |
| `/` | Division | `10 / 2` | `5.0` (always float) |
| `//` | Floor Division | `10 // 3` | `3` (drops decimal) |
| `%` | Modulus (Remainder) | `10 % 3` | `1` |
| `**` | Exponentiation (Power) | `2 ** 8` | `256` |

### Notes on Division

```python
print(10 / 3)    # 3.3333... — true division, always returns float
print(10 // 3)   # 3         — floor division, rounds DOWN
print(10 % 3)    # 1         — remainder after dividing
```

The `%` (modulus) operator is more useful than it looks. Common uses:
- **Check if a number is even or odd:** `n % 2 == 0` → even
- **Distribute items evenly:** leftovers after giving everyone an equal share
- **Wrap around a range:** `(n + 1) % max` → cycles back to 0

---

## Comparison Operators

These compare two values and always return a **Boolean** (`True` or `False`).

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `7 > 3` | `True` |
| `<` | Less than | `2 < 5` | `True` |
| `>=` | Greater than or equal | `5 >= 5` | `True` |
| `<=` | Less than or equal | `3 <= 4` | `True` |

**Common mistake:** `=` assigns a value, `==` compares values. These are completely different.

```python
x = 10       # Assignment: put 10 into x
x == 10      # Comparison: is x equal to 10? Returns True
```

---

## Logical Operators

These combine multiple conditions into a single True/False result.

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `and` | Both must be True | `True and True` | `True` |
| `or` | At least one must be True | `True or False` | `True` |
| `not` | Inverts the boolean | `not True` | `False` |

### Truth Tables

**`and` — both must be True:**

| A | B | A and B |
|---|---|---------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

**`or` — at least one must be True:**

| A | B | A or B |
|---|---|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

---

## Assignment Operators (Shortcuts)

These are shortcuts for updating a variable's value.

| Operator | Long form | Short form |
|----------|-----------|------------|
| `+=` | `x = x + 5` | `x += 5` |
| `-=` | `x = x - 3` | `x -= 3` |
| `*=` | `x = x * 2` | `x *= 2` |
| `/=` | `x = x / 4` | `x /= 4` |
| `//=` | `x = x // 2` | `x //= 2` |
| `%=` | `x = x % 3` | `x %= 3` |
| `**=` | `x = x ** 2` | `x **= 2` |

---

## Operator Precedence

When an expression has multiple operators, Python follows a specific order — similar to BODMAS/PEMDAS in mathematics.

| Priority | Operators |
|----------|-----------|
| Highest | `**` |
| | `*`, `/`, `//`, `%` |
| | `+`, `-` |
| | `==`, `!=`, `<`, `>`, `<=`, `>=` |
| | `not` |
| | `and` |
| Lowest | `or` |

Use parentheses `()` to make your intent explicit and override the default order:

```python
2 + 3 * 4       # 14   (multiplication first)
(2 + 3) * 4     # 20   (addition first due to parentheses)
```

---

## Examples in This Chapter

| File | What it Does |
|------|-------------|
| [example_01_addition.py](example_01_addition.py) | Simple addition |
| [example_02_all_math.py](example_02_all_math.py) | All arithmetic operators |
| [example_03_remainder.py](example_03_remainder.py) | Modulus explained |
| [example_04_comparison.py](example_04_comparison.py) | Comparison operators |
| [example_05_logical.py](example_05_logical.py) | Logical operators |
| [example_06_calculator.py](example_06_calculator.py) | Interactive calculator |
| [example_07_piggy_bank.py](example_07_piggy_bank.py) | Finance tracking story |
