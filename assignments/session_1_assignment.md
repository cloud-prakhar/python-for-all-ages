# Session 1 Assignment

**Covers:** Chapters 1–7 | Variables, Operators, Conditions, Loops, Functions, Strings

**Instructions:**
- Complete all 5 questions
- Each answer should be a working Python program saved as a `.py` file
- Test your code before submitting — it must run without errors
- Add comments explaining your logic

---

## Question 1 — Variables, Data Types & Operators

Write a program that acts as a **simple bill splitter**.

The program should:
1. Ask the user for the total bill amount (e.g. 1250.00)
2. Ask how many people are splitting the bill
3. Ask for the tip percentage (e.g. 10 for 10%)
4. Calculate and print:
   - Tip amount
   - Total bill after tip
   - Amount each person pays (rounded to 2 decimal places)

**Example output:**
```
Total bill    : Rs. 1250.00
Tip (10%)     : Rs. 125.00
Bill + tip    : Rs. 1375.00
Per person    : Rs. 275.00
```

---

## Question 2 — Conditions

Write a **number classifier** program.

Ask the user to enter an integer, then print ALL of the following that apply:
- Whether it is positive, negative, or zero
- Whether it is even or odd (skip if zero)
- Whether it is a single-digit number (−9 to 9)
- Whether it is divisible by both 3 and 5

**Example output (for input 15):**
```
15 is positive.
15 is odd.
15 is NOT a single-digit number.
15 is divisible by both 3 and 5.
```

---

## Question 3 — Loops

Write a program that prints a **multiplication grid** for numbers 1 through 9.

The output should look like a formatted table with aligned columns.

**Expected output:**
```
      1    2    3    4    5    6    7    8    9
  1   1    2    3    4    5    6    7    8    9
  2   2    4    6    8   10   12   14   16   18
  3   3    6    9   12   15   18   21   24   27
  ...
  9   9   18   27   36   45   54   63   72   81
```

**Hint:** Use nested loops and `end=""` with print to control spacing.

---

## Question 4 — Functions

Write a function called `password_checker(password)` that validates a password and returns a descriptive result.

Rules:
- Minimum 8 characters long
- Must contain at least one digit
- Must contain at least one uppercase letter
- Must contain at least one lowercase letter

The function should return a **tuple**: `(is_valid, list_of_issues)`.

Then write code to test it with at least 4 different passwords (including valid and invalid ones) and print the results clearly.

---

## Question 5 — Strings (Combined Challenge)

Write a program that reads a sentence from the user and produces a **text analysis report**:

1. Total character count (with and without spaces)
2. Word count
3. The sentence reversed (character by character)
4. The sentence with every word reversed in place (e.g. "Hello World" → "olleH dlroW")
5. Count of each vowel (a, e, i, o, u) — case-insensitive

**Example input:** `"Python is awesome"`

**Example output:**
```
Original         : Python is awesome
Characters       : 18 (15 without spaces)
Words            : 3
Reversed sentence: emosewa si nohtyP
Words reversed   : nohtyP si emosewa
Vowel counts     : a=1  e=2  i=1  o=1  u=0
```
