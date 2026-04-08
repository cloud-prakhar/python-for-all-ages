# Chapter 5: Loops — Repeating Code

---

## What Will You Learn?

- The `for` loop — iterate over a sequence or range
- The `while` loop — repeat while a condition holds
- `range()` and its parameters
- `break`, `continue`, and `pass`
- Nested loops
- Loop patterns and common use cases

---

## Why Loops?

Imagine you want to print the word "Python" 1000 times. Writing 1000 `print()` statements is impractical. Loops let you repeat a block of code as many times as needed — from 0 times to millions — with just a few lines.

Loops are one of the most fundamental constructs in programming. Almost every real-world program uses them.

---

## The `for` Loop

The `for` loop **iterates over a sequence** — a range of numbers, a string, a list, or any iterable object. It runs the body once for each item in the sequence.

```python
for variable in sequence:
    # body — runs once per item
```

```python
for i in range(5):
    print(i)
# Output: 0  1  2  3  4
```

### The `range()` Function

`range()` generates a sequence of integers. It has three forms:

| Form | Meaning | Example | Produces |
|------|---------|---------|---------|
| `range(stop)` | 0 to stop-1 | `range(5)` | 0,1,2,3,4 |
| `range(start, stop)` | start to stop-1 | `range(2, 6)` | 2,3,4,5 |
| `range(start, stop, step)` | with step | `range(0, 10, 2)` | 0,2,4,6,8 |

A **negative step** goes backwards:
```python
for i in range(10, 0, -1):
    print(i)   # 10, 9, 8, ... 1
```

---

## The `while` Loop

The `while` loop runs **as long as a condition is True**. You use it when you don't know in advance how many iterations you need.

```python
while condition:
    # body — repeats as long as condition is True
```

```python
count = 1
while count <= 5:
    print(count)
    count += 1     # This line is crucial — must move toward ending the loop!
```

**Warning:** If the condition never becomes False, you get an **infinite loop** — the program runs forever. Always ensure the loop body makes progress toward terminating.

---

## `break` — Exit the Loop

`break` immediately exits the entire loop, regardless of the condition.

```python
for i in range(100):
    if i == 5:
        break       # Stop as soon as i reaches 5
    print(i)
# Prints: 0, 1, 2, 3, 4
```

Use case: searching for something — once found, stop looking.

---

## `continue` — Skip to Next Iteration

`continue` skips the rest of the current iteration and moves to the next one.

```python
for i in range(10):
    if i % 2 == 0:
        continue    # Skip even numbers
    print(i)
# Prints: 1, 3, 5, 7, 9
```

---

## `else` on Loops

Python has a unique feature: a `for` or `while` loop can have an `else` block. The `else` runs **only if the loop completed normally** (without hitting a `break`).

```python
for i in range(5):
    if i == 10:
        print("Found 10!")
        break
else:
    print("10 was not found.")   # Runs — loop finished without break
```

---

## Nested Loops

A loop inside another loop. The **inner loop runs completely** for each single iteration of the outer loop.

```python
for row in range(3):        # Outer loop — 3 times
    for col in range(3):    # Inner loop — 3 times per outer iteration
        print(row, col)
# Total iterations: 3 × 3 = 9
```

Common use: processing 2D data like grids, tables, matrices.

---

## Choosing `for` vs `while`

| Situation | Use |
|-----------|-----|
| Know exactly how many times | `for` with `range()` |
| Iterating over a collection | `for item in collection` |
| Repeating until something changes | `while` |
| Waiting for user input | `while` |
| Number of iterations unknown | `while` |

---

## Examples in This Chapter

| File | What it Does |
|------|-------------|
| [example_01_for_loop.py](example_01_for_loop.py) | Basic for loop with range |
| [example_02_count_down.py](example_02_count_down.py) | Countdown timer |
| [example_03_while_loop.py](example_03_while_loop.py) | Basic while loop |
| [example_04_multiplication_table.py](example_04_multiplication_table.py) | Times table generator |
| [example_05_break_continue.py](example_05_break_continue.py) | break and continue |
| [example_06_pattern.py](example_06_pattern.py) | Star pattern (nested loops) |
| [example_07_sum_calculator.py](example_07_sum_calculator.py) | Sum using a loop |
| [example_08_fibonacci.py](example_08_fibonacci.py) | Fibonacci sequence |
| [example_09_number_pyramid.py](example_09_number_pyramid.py) | Number pyramid pattern |
| [example_10_prime_checker.py](example_10_prime_checker.py) | Prime number checker |
