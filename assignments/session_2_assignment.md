# Session 2 Assignment

**Covers:** Chapters 8–9 | Lists, Tuples, Sets, Dictionaries

**Instructions:**
- Complete all 5 questions
- Each answer should be a working Python program saved as a `.py` file
- Test your code before submitting — it must run without errors
- Add comments explaining your logic

---

## Question 1 — Lists

Write a program that simulates a **task manager (To-Do List)**.

The program must support these commands in a loop:
- `add <task>` — add a task to the list
- `done <number>` — mark task at that position as done (remove it)
- `view` — display all current tasks numbered from 1
- `quit` — exit the program

Rules:
- Validate that the task number exists before removing it
- Show a message if the list is empty when viewing
- When adding, reject empty task names

**Example interaction:**
```
Command: add Buy groceries
✅ Task added: "Buy groceries"
Command: add Finish assignment
✅ Task added: "Finish assignment"
Command: view
  1. Buy groceries
  2. Finish assignment
Command: done 1
🗑 Removed: "Buy groceries"
Command: quit
Goodbye! You have 1 task(s) remaining.
```

---

## Question 2 — Lists + Sorting

Given the following list of student scores:

```python
scores = [72, 88, 45, 95, 61, 83, 55, 90, 77, 68, 42, 99, 73, 86, 51]
```

Write a program (no user input needed) that:
1. Prints the original list
2. Prints the sorted list (low to high)
3. Prints the top 5 scores
4. Prints the bottom 5 scores
5. Calculates and prints the median score
6. Prints how many scores are above the average

---

## Question 3 — Sets

Write a program that:
1. Creates two sets of at least 6 items each, representing the **skills** of two job candidates:
   - `candidate_a` and `candidate_b`
2. Defines a set of `required_skills` (at least 5 skills)
3. Prints:
   - Skills both candidates have in common
   - Skills only candidate A has
   - Skills only candidate B has
   - Which candidate meets more of the required skills (show the count for each)
   - Any required skill that NEITHER candidate has

---

## Question 4 — Dictionaries

Build a **contact book** program that lets the user:
- `add` — add a new contact (name, phone, email)
- `search` — search by name (partial match allowed)
- `delete` — delete a contact by name
- `list` — list all contacts alphabetically
- `quit` — exit

Requirements:
- Store contacts as a dictionary: `{name: {"phone": ..., "email": ...}}`
- Search should be case-insensitive
- Display a clear message when a contact is not found
- Confirm before deleting

---

## Question 5 — Combined Challenge (Lists + Dicts)

Write a **mini student grade book** program.

The program should manage student records using a list of dictionaries. Each record:
```python
{"name": "Alice", "scores": [85, 90, 78, 92, 88]}
```

Functionality:
1. Start with at least 5 pre-loaded students
2. Calculate and display each student's average score and letter grade
3. Print the class ranking (sorted by average, highest first)
4. Find and display:
   - The student with the highest average
   - The student with the lowest average
   - The overall class average
5. Allow the user to add a new student (name + 5 scores via input)
   and re-display the full updated ranking
