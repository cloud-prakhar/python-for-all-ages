# Chapter 7: Strings — Working with Text

---

## What Will You Learn?

- String indexing and slicing
- Essential string methods
- String formatting with f-strings
- Checking string content
- Iterating over strings
- Common string patterns

---

## Strings in Depth

A **string** is an ordered, immutable sequence of characters. In Python, strings are first-class objects with a rich set of built-in methods.

```python
s = "Hello, Python!"
```

**Ordered** — every character has a fixed position (index).
**Immutable** — you cannot change characters in-place; string operations always create a **new** string.

```python
s = "hello"
# s[0] = "H"   # ERROR — strings cannot be mutated
s = "H" + s[1:]  # Create a new string instead
```

---

## Indexing

Each character in a string has a **zero-based index** — counting starts at 0, not 1.

```
 H  e  l  l  o
 0  1  2  3  4
-5 -4 -3 -2 -1    (negative indices count from the end)
```

```python
word = "Hello"
print(word[0])    # H  — first character
print(word[4])    # o  — last character (index 4)
print(word[-1])   # o  — last character (negative index)
print(word[-2])   # l  — second to last
```

---

## Slicing

Slicing extracts a **substring** (a portion of the string).

```python
s[start : stop : step]
```

- `start` — index to begin from (inclusive). Default: 0
- `stop` — index to end at (exclusive). Default: end of string
- `step` — how many characters to skip. Default: 1

```python
text = "Python Programming"

print(text[0:6])     # "Python"      — index 0 to 5
print(text[7:])      # "Programming" — from index 7 to end
print(text[:6])      # "Python"      — from start to index 5
print(text[::2])     # Every other character
print(text[::-1])    # Reverse the string
```

---

## Essential String Methods

| Method | What it Does | Example |
|--------|-------------|---------|
| `.upper()` | All uppercase | `"hello".upper()` → `"HELLO"` |
| `.lower()` | All lowercase | `"HELLO".lower()` → `"hello"` |
| `.title()` | Title case | `"hello world".title()` → `"Hello World"` |
| `.strip()` | Remove leading/trailing whitespace | `"  hi  ".strip()` → `"hi"` |
| `.replace(old, new)` | Replace substring | `"cat".replace("c","b")` → `"bat"` |
| `.split(sep)` | Split into list | `"a,b,c".split(",")` → `["a","b","c"]` |
| `.join(iterable)` | Join list into string | `",".join(["a","b","c"])` → `"a,b,c"` |
| `.find(sub)` | Position of first match (-1 if not found) | `"hello".find("l")` → `2` |
| `.count(sub)` | Count occurrences | `"banana".count("a")` → `3` |
| `.startswith(sub)` | Does it start with? | `"Python".startswith("Py")` → `True` |
| `.endswith(sub)` | Does it end with? | `"file.py".endswith(".py")` → `True` |
| `.isdigit()` | All digits? | `"123".isdigit()` → `True` |
| `.isalpha()` | All letters? | `"abc".isalpha()` → `True` |
| `len(s)` | Length of string | `len("hello")` → `5` |

---

## String Formatting

### f-Strings (Recommended — Python 3.6+)

The clearest and most modern way to embed variables inside strings:

```python
name = "Alice"
score = 94.5

print(f"Name: {name}")
print(f"Score: {score:.1f}%")       # .1f = 1 decimal place
print(f"Next year: {2024 + 1}")     # Expressions work too
print(f"{'centered':^20}")          # Alignment formatting
```

### Format Specifiers

Inside `{}` you can control formatting with `:`:

| Specifier | Meaning | Example |
|-----------|---------|---------|
| `:.2f` | Float with 2 decimal places | `f"{3.14159:.2f}"` → `"3.14"` |
| `:d` | Integer | `f"{42:d}"` → `"42"` |
| `:>10` | Right-align in 10 chars | `f"{'hi':>10}"` → `"        hi"` |
| `:<10` | Left-align in 10 chars | `f"{'hi':<10}"` → `"hi        "` |
| `:^10` | Center in 10 chars | `f"{'hi':^10}"` → `"    hi    "` |
| `:,` | Thousands separator | `f"{1000000:,}"` → `"1,000,000"` |

---

## The `in` Operator with Strings

```python
email = "user@example.com"

print("@" in email)             # True
print("gmail" in email)         # False
print(email.startswith("user")) # True
print(email.endswith(".com"))   # True
```

---

## Iterating Over a String

Strings are iterable — you can loop over each character:

```python
for char in "Python":
    print(char)    # P, y, t, h, o, n — one per line
```

---

## Examples in This Chapter

| File | What it Does |
|------|-------------|
| [example_01_string_basics.py](example_01_string_basics.py) | Indexing and membership |
| [example_02_methods.py](example_02_methods.py) | upper, lower, title, strip |
| [example_03_slicing.py](example_03_slicing.py) | Slicing and indexing |
| [example_04_find_replace.py](example_04_find_replace.py) | find, replace, split |
| [example_05_fstrings.py](example_05_fstrings.py) | f-string formatting |
| [example_06_palindrome.py](example_06_palindrome.py) | Palindrome checker |
| [example_07_word_game.py](example_07_word_game.py) | Word guessing game |
| [example_08_string_stats.py](example_08_string_stats.py) | Count vowels, consonants, words |
| [example_09_caesar_cipher.py](example_09_caesar_cipher.py) | Simple encryption |
| [example_10_name_formatter.py](example_10_name_formatter.py) | Format and validate names |
