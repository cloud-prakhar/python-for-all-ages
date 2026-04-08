# Example 9: Nested Dictionaries
# Dictionaries can contain other dictionaries as values.
# This creates a hierarchy — like a JSON structure used in real APIs and databases.

# A company org chart: department → employee ID → employee info
company = {
    "Engineering": {
        "E001": {"name": "Alice Chen",   "role": "Backend Engineer",   "salary": 95000, "years": 4},
        "E002": {"name": "Raj Patel",    "role": "Frontend Engineer",  "salary": 88000, "years": 2},
        "E003": {"name": "Sara Kim",     "role": "DevOps Engineer",    "salary": 92000, "years": 6},
    },
    "Marketing": {
        "M001": {"name": "James Brown",  "role": "Marketing Manager",  "salary": 78000, "years": 5},
        "M002": {"name": "Priya Nair",   "role": "Content Strategist", "salary": 65000, "years": 1},
    },
    "Finance": {
        "F001": {"name": "Tom Harris",   "role": "CFO",                "salary": 130000,"years": 10},
        "F002": {"name": "Linda Zhou",   "role": "Accountant",         "salary": 72000, "years": 3},
    },
}

# --- Access specific employee ---
print("Employee E002:")
emp = company["Engineering"]["E002"]
print(f"  Name  : {emp['name']}")
print(f"  Role  : {emp['role']}")
print(f"  Salary: ${emp['salary']:,}")

# --- List all employees in a department ---
print("\nEngineering Team:")
for emp_id, info in company["Engineering"].items():
    print(f"  [{emp_id}] {info['name']} — {info['role']}")

# --- Find highest paid employee across all departments ---
highest_salary = 0
top_employee   = ""
top_dept       = ""

for dept, employees in company.items():
    for emp_id, info in employees.items():
        if info["salary"] > highest_salary:
            highest_salary = info["salary"]
            top_employee   = info["name"]
            top_dept       = dept

print(f"\nHighest paid: {top_employee} ({top_dept}) — ${highest_salary:,}/year")

# --- Company-wide statistics ---
all_salaries = [
    info["salary"]
    for employees in company.values()
    for info in employees.values()
]
print(f"Total employees: {len(all_salaries)}")
print(f"Average salary : ${sum(all_salaries) // len(all_salaries):,}")
