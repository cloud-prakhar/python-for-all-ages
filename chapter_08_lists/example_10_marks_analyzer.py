# Example 10: Student Marks Analyzer
# A realistic application: process a list of exam scores and generate a report.
# Demonstrates: list methods, comprehensions, sorting, lambda, and functions.
#
# NEW CONCEPT 1: lambda — a one-line anonymous function
#
#   lambda x: x[1]
#
#   "lambda" creates a tiny function WITHOUT giving it a name.
#   It's useful when you need a simple function just once (e.g. as a sort key).
#
#   lambda x: x[1]  is equivalent to:
#       def get_second(x):
#           return x[1]
#
#   Usage in sorted():
#       sorted(students, key=lambda x: x[1], reverse=True)
#       → Sort the students list.
#       → For each student (a tuple like ("Alice", 88)), use x[1] (the score) as the sort key.
#       → reverse=True means highest first.
#
# NEW CONCEPT 2: _ (underscore) as a "don't care" variable
#
#   scores = [score for _, score in students]
#
#   Each item in "students" is a tuple like ("Alice", 88).
#   When we unpack it, we get two values: the name and the score.
#   We only NEED the score here — not the name.
#   Using _ signals: "I'm unpacking this position but I don't use its value."
#   It's a Python convention for "intentionally ignored value."
#   Name: _     Score: score
#
# NEW CONCEPT 3: Inline return (compact if)
#
#   if score >= 90: return "A+"
#
#   This is a valid one-liner in Python — the if and its body on the same line.
#   It works but is only readable for very short bodies.
#   You will more commonly see it written as separate lines.

def letter_grade(score):
    if score >= 90: return "A+"
    if score >= 80: return "A"
    if score >= 70: return "B"
    if score >= 60: return "C"
    if score >= 50: return "D"
    return "F"


def analyze_marks(students):
    """
    students: list of (name, score) tuples
    Returns a detailed analysis report as a dictionary.
    """
    # Unpack each tuple — _ means "ignore the name, just give me the score"
    scores  = [score for _, score in students]

    total   = sum(scores)
    count   = len(scores)
    average = total / count
    highest = max(scores)
    lowest  = min(scores)
    passed  = [s for s in scores if s >= 50]
    failed  = [s for s in scores if s < 50]

    # sorted() with key=lambda x: x[1]
    # → sort each tuple ("Name", score) by its second element (the score)
    # → reverse=True → highest score first
    ranked = sorted(students, key=lambda x: x[1], reverse=True)

    return {
        "count"    : count,
        "average"  : round(average, 2),     # round(number, decimal_places)
        "highest"  : highest,
        "lowest"   : lowest,
        "pass_rate": f"{len(passed)/count*100:.1f}%",
        "ranked"   : ranked,
    }


# --- Data: list of (name, score) tuples ---
students = [
    ("Alice",   88),
    ("Bob",     72),
    ("Charlie", 45),
    ("Diana",   95),
    ("Ethan",   61),
    ("Fiona",   83),
    ("George",  39),
    ("Hannah",  77),
]

results = analyze_marks(students)

print("=" * 45)
print("         STUDENT PERFORMANCE REPORT")
print("=" * 45)
print(f"  Total students : {results['count']}")
print(f"  Class average  : {results['average']}")
print(f"  Highest score  : {results['highest']}")
print(f"  Lowest score   : {results['lowest']}")
print(f"  Pass rate      : {results['pass_rate']}")
print()

# Header row: :<5 means left-align in 5 characters, :<12 in 12 characters, etc.
print(f"  {'Rank':<5} {'Name':<12} {'Score':<8} {'Grade'}")
print("  " + "-" * 35)

# enumerate(results["ranked"], 1) → gives (1, first_student), (2, second_student), ...
# (name, score) → unpacking the tuple from each list item
for rank, (name, score) in enumerate(results["ranked"], 1):
    print(f"  {rank:<5} {name:<12} {score:<8} {letter_grade(score)}")

print("=" * 45)
