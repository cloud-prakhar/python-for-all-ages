# Chapter 6: Functions — Reusable Blocks of Code

---

## What Will You Learn?

- Defining and calling functions
- Parameters, arguments, and return values
- Default parameter values
- Returning multiple values
- Variable scope (local vs global)
- Introduction to recursion

---

## What is a Function?

A **function** is a named, reusable block of code that performs a specific task. Instead of writing the same logic over and over, you define it once as a function and call it by name whenever needed.

Functions are the foundation of **good software design**. They allow you to:
- **Avoid repetition** — write once, use many times (DRY: Don't Repeat Yourself)
- **Organize code** — break a large program into logical, manageable pieces
- **Test in isolation** — verify each piece works before combining them
- **Reuse across projects** — a well-written function can be used in other programs

---

## Defining a Function

```python
def function_name(parameters):
    """Optional docstring describing what this function does."""
    # function body
    return result    # optional
```

- `def` — keyword that starts a function definition
- `function_name` — the name you give it (use snake_case)
- `parameters` — optional input variables (comma-separated)
- `return` — sends a value back to the caller (if omitted, function returns `None`)

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")    # Calling the function
greet("Bob")
```

---

## Parameters vs Arguments

These two terms are often confused:

- **Parameter** — the variable name in the function definition: `def greet(name)`
- **Argument** — the actual value you pass when calling: `greet("Alice")`

---

## Return Values

Functions can send back a result using `return`. The calling code can store or use this value.

```python
def add(a, b):
    return a + b

result = add(3, 4)    # result = 7
print(add(10, 20))    # prints 30
```

The difference between `print()` and `return`:
- `print()` displays something on screen — it doesn't produce a value you can use
- `return` produces a value the rest of your code can work with

```python
def double(n):
    return n * 2

x = double(5)        # x = 10, can use it later
y = double(5) + 3    # y = 13, works in expressions
```

---

## Default Parameter Values

You can assign a **default value** to a parameter. If the caller doesn't provide that argument, the default is used.

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")              # Hello, Alice!
greet("Bob", "Good morning") # Good morning, Bob!
```

Parameters with defaults must come **after** parameters without defaults.

---

## Returning Multiple Values

Python functions can return multiple values as a tuple:

```python
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 8, 2, 9])
print(low, high)    # 1  9
```

---

## Variable Scope

**Scope** refers to where a variable can be accessed in your code.

- **Local variable** — created inside a function, only accessible within that function
- **Global variable** — created outside all functions, accessible everywhere

```python
x = 10           # Global variable

def my_function():
    y = 20       # Local variable
    print(x)     # Can access global x
    print(y)     # Can access local y

my_function()
print(x)         # Works — x is global
# print(y)       # ERROR — y is local to my_function
```

Best practice: avoid modifying global variables inside functions. Pass values in via parameters and return results instead.

---

## Introduction to Recursion

A **recursive function** is one that calls itself. Every recursive function needs:
1. A **base case** — the condition where it stops calling itself
2. A **recursive case** — the call to itself, making progress toward the base case

```python
def factorial(n):
    if n == 0:          # Base case
        return 1
    return n * factorial(n - 1)   # Recursive case

print(factorial(5))   # 120  (5 × 4 × 3 × 2 × 1)
```

Recursion is elegant but can be hard to follow at first. Trace through the calls step by step on paper to build intuition.

---

## Examples in This Chapter

| File | What it Does |
|------|-------------|
| [example_01_first_function.py](example_01_first_function.py) | Your first function |
| [example_02_with_parameters.py](example_02_with_parameters.py) | Function with inputs |
| [example_03_return_value.py](example_03_return_value.py) | Function that returns a value |
| [example_04_greet_everyone.py](example_04_greet_everyone.py) | Calling function in a loop |
| [example_05_calculator_functions.py](example_05_calculator_functions.py) | Calculator using functions |
| [example_06_default_parameters.py](example_06_default_parameters.py) | Default parameter values |
| [example_07_birthday_card.py](example_07_birthday_card.py) | Birthday card generator |
| [example_08_multiple_returns.py](example_08_multiple_returns.py) | Returning multiple values |
| [example_09_scope.py](example_09_scope.py) | Local vs global scope |
| [example_10_recursion.py](example_10_recursion.py) | Recursion with factorial |
