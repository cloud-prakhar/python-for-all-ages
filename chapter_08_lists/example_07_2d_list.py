# Example 7: 2D Lists (List of Lists)
# A 2D list is like a GRID or TABLE — rows and columns!
# Real life: Your classroom seating chart — row 1, seat 2, etc.

# Classroom seating: 3 rows, 3 seats each
classroom = [
    ["Aarav",  "Bhavna", "Chetan"],   # Row 0
    ["Divya",  "Eshan",  "Farida"],   # Row 1
    ["Gaurav", "Heena",  "Ishan"]     # Row 2
]

# Access a specific student: [row][seat]
print(f"Row 0, Seat 0: {classroom[0][0]}")   # Aarav
print(f"Row 1, Seat 2: {classroom[1][2]}")   # Farida
print(f"Row 2, Seat 1: {classroom[2][1]}")   # Heena

print("\n--- Full Classroom Seating Chart ---")
for row_num, row in enumerate(classroom):
    print(f"Row {row_num + 1}: ", end="")
    for seat_num, student in enumerate(row):
        print(f"[{seat_num + 1}:{student}]", end="  ")
    print()   # New line after each row
