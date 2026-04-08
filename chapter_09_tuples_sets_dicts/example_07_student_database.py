# Example 7: Student Database using Dictionaries
# Real life: Like the school's student records system!
#
# This example uses NESTED DICTIONARIES:
# The outer dictionary maps student ID → another dictionary of their details.
#
#   students["S001"]             → {"name": "Arjun Sharma", "grade": 5, ...}
#   students["S001"]["name"]     → "Arjun Sharma"
#   students["S001"]["score"]    → 92
#
# Think of it as: outer key gets you to a student's "folder",
# inner key gets you to a specific field in that folder.
#
# NEW CONCEPT: lambda as a sort key
#
#   max(students, key=lambda sid: students[sid]['score'])
#
#   max() normally finds the largest item in a collection.
#   When you pass key=..., it uses THAT function to determine what to compare.
#
#   "students" here is a dictionary — looping over a dict gives you its KEYS.
#   So max() loops over "S001", "S002", "S003", "S004".
#   For each key (sid), the lambda looks up students[sid]['score'].
#   max() then picks the key whose score is the highest.
#
#   lambda sid: students[sid]['score']
#   is equivalent to:
#       def get_score(sid):
#           return students[sid]['score']
#
#   lambda is used here because this function is only needed once,
#   so creating a named def function would be unnecessary clutter.

students = {
    "S001": {"name": "Arjun Sharma",  "grade": 5, "score": 92, "sport": "Cricket"},
    "S002": {"name": "Priya Patel",   "grade": 4, "score": 88, "sport": "Swimming"},
    "S003": {"name": "Rohan Mehta",   "grade": 5, "score": 75, "sport": "Football"},
    "S004": {"name": "Ananya Singh",  "grade": 3, "score": 95, "sport": "Dance"},
}


def show_student(student_id):
    if student_id in students:
        s = students[student_id]     # s is a shortcut to the inner dictionary
        print(f"\n--- Student Record: {student_id} ---")
        print(f"Name:  {s['name']}")   # s['name'] is the same as students[student_id]['name']
        print(f"Grade: {s['grade']}")
        print(f"Score: {s['score']}")
        print(f"Sport: {s['sport']}")
    else:
        print(f"Student {student_id} not found!")


def top_scorer():
    # max() over a dict loops over its KEYS.
    # key=lambda sid: students[sid]['score'] → compare by each student's score.
    best_id = max(students, key=lambda sid: students[sid]['score'])
    return students[best_id]['name'], students[best_id]['score']   # return two values


# Loop over the dictionary — "sid" is each student ID key: "S001", "S002", ...
print("=== STUDENT DATABASE ===")
for sid in students:
    show_student(sid)

# Unpack the two returned values into name and score
name, score = top_scorer()
print(f"\nTop scorer: {name} with {score} marks!")
