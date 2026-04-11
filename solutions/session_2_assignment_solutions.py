# Session 2 Assignment — Solutions
# Covers: Chapters 8–9 | Lists, Tuples, Sets, Dictionaries
#
# NOTE FOR TEACHERS: These are reference solutions.
# Students may arrive at correct solutions using different approaches.
# Any working program that produces the correct output should be accepted.

print("=" * 60)
print("SESSION 2 ASSIGNMENT SOLUTIONS")
print("=" * 60)


# ==============================================================
# Question 1 — Lists
# Task Manager (To-Do List)
# ==============================================================

def q1_task_manager():
    """
    A simple command-line task manager supporting:
    add <task>, done <number>, view, quit
    """
    print("\n--- Q1: Task Manager ---")
    tasks = []

    while True:
        command = input("\nCommand: ").strip()

        if command.lower() == "quit":
            print(f"Goodbye! You have {len(tasks)} task(s) remaining.")
            break

        elif command.lower() == "view":
            if not tasks:
                print("No tasks yet!")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"  {i}. {task}")

        elif command.lower().startswith("add "):
            task_name = command[4:].strip()
            if not task_name:
                print("Task name cannot be empty.")
            else:
                tasks.append(task_name)
                print(f'Task added: "{task_name}"')

        elif command.lower().startswith("done "):
            try:
                num = int(command[5:].strip())
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print(f'Removed: "{removed}"')
                else:
                    print(f"Invalid task number. You have {len(tasks)} task(s).")
            except ValueError:
                print("Please provide a valid number after 'done'.")

        else:
            print("Unknown command. Use: add <task>, done <number>, view, quit")


# ==============================================================
# Question 2 — Lists + Sorting
# Student Score Analysis
# ==============================================================

def q2_score_analysis():
    """
    Analyzes a list of student scores: sorted, top 5, bottom 5,
    median, and count above average.
    """
    print("\n--- Q2: Score Analysis ---")

    scores = [72, 88, 45, 95, 61, 83, 55, 90, 77, 68, 42, 99, 73, 86, 51]

    print(f"Original list  : {scores}")

    sorted_scores = sorted(scores)
    print(f"Sorted (low-hi): {sorted_scores}")

    top_5 = sorted_scores[-5:][::-1]   # Highest 5, descending
    print(f"Top 5 scores   : {top_5}")

    bottom_5 = sorted_scores[:5]
    print(f"Bottom 5 scores: {bottom_5}")

    # Median: middle value of sorted list
    n = len(sorted_scores)
    if n % 2 == 1:
        median = sorted_scores[n // 2]
    else:
        median = (sorted_scores[n // 2 - 1] + sorted_scores[n // 2]) / 2
    print(f"Median score   : {median}")

    average = sum(scores) / len(scores)
    above_avg = sum(1 for s in scores if s > average)
    print(f"Average score  : {average:.1f}")
    print(f"Above average  : {above_avg} student(s)")


# ==============================================================
# Question 3 — Sets
# Job Candidate Skills Analysis
# ==============================================================

def q3_candidate_skills():
    """
    Compares skills of two job candidates against required skills
    using set operations.
    """
    print("\n--- Q3: Candidate Skills ---")

    candidate_a = {"Python", "SQL", "Excel", "Tableau", "Statistics", "Machine Learning", "R"}
    candidate_b = {"Python", "Java", "SQL", "Spark", "Hadoop", "Statistics", "Kafka"}

    required_skills = {"Python", "SQL", "Statistics", "Machine Learning", "Spark"}

    print(f"Candidate A : {candidate_a}")
    print(f"Candidate B : {candidate_b}")
    print(f"Required    : {required_skills}")

    common = candidate_a & candidate_b
    print(f"\nSkills both have          : {common}")

    only_a = candidate_a - candidate_b
    print(f"Only Candidate A has      : {only_a}")

    only_b = candidate_b - candidate_a
    print(f"Only Candidate B has      : {only_b}")

    a_match = len(candidate_a & required_skills)
    b_match = len(candidate_b & required_skills)
    print(f"\nRequired skills met — A: {a_match}, B: {b_match}")
    if a_match > b_match:
        print("Candidate A meets more required skills.")
    elif b_match > a_match:
        print("Candidate B meets more required skills.")
    else:
        print("Both candidates meet the same number of required skills.")

    neither_has = required_skills - (candidate_a | candidate_b)
    if neither_has:
        print(f"\nRequired skills NEITHER has: {neither_has}")
    else:
        print("\nBoth candidates together cover all required skills.")


# ==============================================================
# Question 4 — Dictionaries
# Contact Book
# ==============================================================

def q4_contact_book():
    """
    A contact book with add, search, delete, list, and quit commands.
    Contacts stored as: {name: {"phone": ..., "email": ...}}
    """
    print("\n--- Q4: Contact Book ---")

    contacts = {}

    while True:
        print("\nOptions: add | search | delete | list | quit")
        choice = input("Enter command: ").strip().lower()

        if choice == "quit":
            print("Goodbye!")
            break

        elif choice == "add":
            name = input("Name: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue
            phone = input("Phone: ").strip()
            email = input("Email: ").strip()
            contacts[name] = {"phone": phone, "email": email}
            print(f"Contact '{name}' added.")

        elif choice == "search":
            query = input("Search by name: ").strip().lower()
            results = {n: d for n, d in contacts.items() if query in n.lower()}
            if results:
                for name, info in results.items():
                    print(f"  {name}: {info['phone']} | {info['email']}")
            else:
                print("No contacts found.")

        elif choice == "delete":
            name = input("Enter name to delete: ").strip()
            # Case-insensitive search for the name
            match = next((n for n in contacts if n.lower() == name.lower()), None)
            if match:
                confirm = input(f"Delete '{match}'? (yes/no): ").strip().lower()
                if confirm == "yes":
                    del contacts[match]
                    print(f"'{match}' deleted.")
                else:
                    print("Delete cancelled.")
            else:
                print(f"Contact '{name}' not found.")

        elif choice == "list":
            if not contacts:
                print("No contacts yet.")
            else:
                print("\nAll contacts (alphabetical):")
                for name in sorted(contacts.keys()):
                    info = contacts[name]
                    print(f"  {name}: {info['phone']} | {info['email']}")

        else:
            print("Unknown command.")


# ==============================================================
# Question 5 — Combined Challenge (Lists + Dicts)
# Mini Student Grade Book
# ==============================================================

def letter_grade(average):
    """Returns a letter grade based on the average score."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def display_ranking(students):
    """Prints the student ranking sorted by average score (highest first)."""
    ranked = sorted(students, key=lambda s: s["average"], reverse=True)
    print(f"\n{'Rank':<6} {'Name':<15} {'Average':>8} {'Grade':>6}")
    print("-" * 40)
    for i, s in enumerate(ranked, start=1):
        print(f"{i:<6} {s['name']:<15} {s['average']:>8.1f} {s['grade']:>6}")


def q5_grade_book():
    """
    A mini grade book that:
    - Pre-loads 5 students with scores
    - Calculates averages and letter grades
    - Shows ranking
    - Finds highest/lowest/class average
    - Lets user add a new student
    """
    print("\n--- Q5: Student Grade Book ---")

    # Pre-loaded students
    students = [
        {"name": "Alice",   "scores": [85, 90, 78, 92, 88]},
        {"name": "Bob",     "scores": [70, 65, 72, 68, 75]},
        {"name": "Charlie", "scores": [95, 98, 92, 97, 94]},
        {"name": "Diana",   "scores": [60, 55, 62, 58, 65]},
        {"name": "Ethan",   "scores": [80, 82, 78, 85, 81]},
    ]

    # Calculate average and grade for each student
    for s in students:
        s["average"] = sum(s["scores"]) / len(s["scores"])
        s["grade"] = letter_grade(s["average"])

    display_ranking(students)

    # Statistics
    best = max(students, key=lambda s: s["average"])
    worst = min(students, key=lambda s: s["average"])
    class_avg = sum(s["average"] for s in students) / len(students)

    print(f"\nHighest average : {best['name']} ({best['average']:.1f})")
    print(f"Lowest average  : {worst['name']} ({worst['average']:.1f})")
    print(f"Class average   : {class_avg:.1f}")

    # Add a new student
    print("\n--- Add a New Student ---")
    new_name = input("Student name: ").strip()
    print(f"Enter 5 scores for {new_name}:")
    new_scores = []
    for i in range(1, 6):
        score = float(input(f"  Score {i}: "))
        new_scores.append(score)

    new_student = {"name": new_name, "scores": new_scores}
    new_student["average"] = sum(new_scores) / len(new_scores)
    new_student["grade"] = letter_grade(new_student["average"])
    students.append(new_student)

    print("\n--- Updated Ranking ---")
    display_ranking(students)


# ==============================================================
# Run all questions
# ==============================================================

if __name__ == "__main__":
    print("\nRun individual questions by calling their functions.")
    print("Uncomment the question you want to test below:\n")

    # q1_task_manager()        # Interactive — requires input
    q2_score_analysis()        # No input needed — safe to run directly
    q3_candidate_skills()      # No input needed — safe to run directly
    # q4_contact_book()        # Interactive — requires input
    # q5_grade_book()          # Interactive — requires input
