# Chapter 4: Making Decisions — if / elif / else

---

## What Will You Learn?

- The `if`, `elif`, and `else` statements
- How Python evaluates conditions
- Nested conditions (if inside if)
- Compound conditions using `and` / `or`
- The concept of control flow

---

## What is Control Flow?

By default, Python runs code **top to bottom**, one line at a time. But real programs need to make decisions — run different code depending on the situation. This is called **control flow** — directing the program's path based on conditions.

The `if` statement is the most fundamental way to control what code runs.

---

## The `if` Statement

```python
if condition:
    # This block runs ONLY if condition is True
    statement_1
    statement_2
```

- The `condition` is any expression that evaluates to `True` or `False`
- The colon `:` at the end is required
- The **indented block** below is the body — Python uses indentation (4 spaces) to define which lines belong inside the `if`

```python
temperature = 38.5

if temperature > 37.5:
    print("You have a fever.")
    print("Please rest and drink water.")
```

---

## The `if-else` Statement

When you want to do one thing if a condition is true, and something **different** if it's false:

```python
if condition:
    # Runs when condition is True
else:
    # Runs when condition is False
```

```python
age = 16

if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote yet.")
```

---

## The `if-elif-else` Chain

When you have **more than two possible outcomes**, use `elif` (short for "else if"):

```python
if condition_1:
    # Runs if condition_1 is True
elif condition_2:
    # Runs if condition_1 is False AND condition_2 is True
elif condition_3:
    # Runs if condition_1 and condition_2 are False AND condition_3 is True
else:
    # Runs if NONE of the above conditions are True
```

Python checks each condition **in order**, top to bottom. The moment one is True, it runs that block and **skips all the rest**.

```python
score = 82

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")
```

---

## Nested Conditions

You can put an `if` statement **inside** another `if` statement. This is called **nesting**.

```python
has_ticket = True
is_vip = False

if has_ticket:
    print("Access granted to the event.")
    if is_vip:
        print("Welcome to the VIP lounge!")
    else:
        print("Enjoy the general seating area.")
else:
    print("No ticket — entry denied.")
```

Use nesting when you need to check a secondary condition only after a primary one is already confirmed. Avoid deeply nested code (more than 2–3 levels) as it becomes hard to read.

---

## Compound Conditions

You can combine multiple conditions using `and` / `or`:

```python
age = 20
has_id = True

# Both conditions must be True
if age >= 18 and has_id:
    print("Entry allowed.")

# At least one condition must be True
if age >= 18 or has_id:
    print("Possible entry.")
```

---

## Indentation — A Python Fundamental

Unlike most languages that use `{}` to group code, Python uses **indentation**. The standard is **4 spaces** per level.

```python
if True:
    print("Inside the if")          # 4 spaces — inside the block
    print("Also inside")            # 4 spaces — also inside
print("Outside the if")             # 0 spaces — back outside
```

An `IndentationError` means your spacing is inconsistent. Always use spaces, not tabs, or be consistent — never mix.

---

## One-line (Ternary) Conditions

For simple true/false assignments, Python has a compact one-line form:

```python
# Long form
if x > 0:
    label = "positive"
else:
    label = "non-positive"

# One-liner (ternary expression)
label = "positive" if x > 0 else "non-positive"
```

---

## Examples in This Chapter

| File | What it Does |
|------|-------------|
| [example_01_simple_if.py](example_01_simple_if.py) | Basic if statement |
| [example_02_if_else.py](example_02_if_else.py) | if and else |
| [example_03_elif.py](example_03_elif.py) | Multiple conditions with elif |
| [example_04_grade_checker.py](example_04_grade_checker.py) | Grade system |
| [example_05_traffic_light.py](example_05_traffic_light.py) | Traffic light simulator |
| [example_06_number_game.py](example_06_number_game.py) | Higher or lower |
| [example_07_age_checker.py](example_07_age_checker.py) | Amusement park ride check |
| [example_08_nested_conditions.py](example_08_nested_conditions.py) | Nested if statements |
| [example_09_fizzbuzz.py](example_09_fizzbuzz.py) | Classic FizzBuzz problem |
| [example_10_bmi_calculator.py](example_10_bmi_calculator.py) | BMI calculator |
