# Session 1 Assignment — Solutions
# Covers: Chapters 1–7 | Variables, Operators, Conditions, Loops, Functions, Strings
#
# NOTE FOR TEACHERS: These are reference solutions.
# Students may arrive at correct solutions using different approaches.
# Any working program that produces the correct output should be accepted.

print("=" * 60)
print("SESSION 1 ASSIGNMENT SOLUTIONS")
print("=" * 60)


# ==============================================================
# Question 1 — Variables, Data Types & Operators
# Simple Bill Splitter
# ==============================================================

def q1_bill_splitter():
    """
    Asks user for bill amount, number of people, and tip percentage.
    Prints tip amount, total bill after tip, and per-person share.
    """
    print("\n--- Q1: Bill Splitter ---")

    bill = float(input("Enter total bill amount: Rs. "))
    people = int(input("How many people are splitting? "))
    tip_pct = float(input("Enter tip percentage (e.g. 10 for 10%): "))

    tip_amount = bill * (tip_pct / 100)
    total_bill = bill + tip_amount
    per_person = round(total_bill / people, 2)

    print(f"\nTotal bill    : Rs. {bill:.2f}")
    print(f"Tip ({tip_pct:.0f}%)     : Rs. {tip_amount:.2f}")
    print(f"Bill + tip    : Rs. {total_bill:.2f}")
    print(f"Per person    : Rs. {per_person:.2f}")


# ==============================================================
# Question 2 — Conditions
# Number Classifier
# ==============================================================

def q2_number_classifier():
    """
    Classifies a number as positive/negative/zero, even/odd,
    single-digit, and divisible by 3 and 5.
    """
    print("\n--- Q2: Number Classifier ---")

    n = int(input("Enter an integer: "))

    # Positive, negative, or zero
    if n > 0:
        print(f"{n} is positive.")
    elif n < 0:
        print(f"{n} is negative.")
    else:
        print(f"{n} is zero.")

    # Even or odd (skip if zero)
    if n != 0:
        if n % 2 == 0:
            print(f"{n} is even.")
        else:
            print(f"{n} is odd.")

    # Single-digit: -9 to 9
    if -9 <= n <= 9:
        print(f"{n} is a single-digit number.")
    else:
        print(f"{n} is NOT a single-digit number.")

    # Divisible by both 3 and 5
    if n % 3 == 0 and n % 5 == 0:
        print(f"{n} is divisible by both 3 and 5.")
    else:
        print(f"{n} is NOT divisible by both 3 and 5.")


# ==============================================================
# Question 3 — Loops
# Multiplication Grid (1 through 9)
# ==============================================================

def q3_multiplication_grid():
    """
    Prints a formatted 9x9 multiplication table.
    """
    print("\n--- Q3: Multiplication Grid ---")

    # Header row
    print(f"{'':>4}", end="")
    for col in range(1, 10):
        print(f"{col:>5}", end="")
    print()

    # Divider
    print("-" * 49)

    # Data rows
    for row in range(1, 10):
        print(f"{row:>3} |", end="")
        for col in range(1, 10):
            print(f"{row * col:>5}", end="")
        print()


# ==============================================================
# Question 4 — Functions
# Password Checker
# ==============================================================

def password_checker(password):
    """
    Validates a password against 4 rules:
    - Minimum 8 characters
    - At least one digit
    - At least one uppercase letter
    - At least one lowercase letter

    Returns: (is_valid: bool, issues: list of str)
    """
    issues = []

    if len(password) < 8:
        issues.append("Must be at least 8 characters long")

    if not any(ch.isdigit() for ch in password):
        issues.append("Must contain at least one digit")

    if not any(ch.isupper() for ch in password):
        issues.append("Must contain at least one uppercase letter")

    if not any(ch.islower() for ch in password):
        issues.append("Must contain at least one lowercase letter")

    is_valid = len(issues) == 0
    return (is_valid, issues)


def q4_password_checker_demo():
    """Tests the password_checker function with multiple passwords."""
    print("\n--- Q4: Password Checker ---")

    test_passwords = [
        "abc",               # Too short, no digit, no uppercase
        "password123",       # No uppercase
        "PASSWORD1",         # No lowercase
        "Hello123!",         # All rules satisfied
        "Abcdefgh1",         # Valid: upper + lower + digit + 8+ chars
        "12345678",          # No uppercase, no lowercase
    ]

    for pwd in test_passwords:
        valid, issues = password_checker(pwd)
        status = "VALID" if valid else "INVALID"
        print(f"\nPassword : '{pwd}'")
        print(f"Result   : {status}")
        if issues:
            for issue in issues:
                print(f"  - {issue}")


# ==============================================================
# Question 5 — Strings (Combined Challenge)
# Text Analysis Report
# ==============================================================

def q5_text_analysis():
    """
    Reads a sentence from the user and prints a full text analysis report:
    - Character count (with and without spaces)
    - Word count
    - Reversed sentence
    - Each word reversed in place
    - Vowel counts
    """
    print("\n--- Q5: Text Analysis Report ---")

    sentence = input("Enter a sentence: ")

    # Character counts
    char_total = len(sentence)
    char_no_spaces = len(sentence.replace(" ", ""))

    # Word count
    words = sentence.split()
    word_count = len(words)

    # Reverse entire sentence
    reversed_sentence = sentence[::-1]

    # Reverse each word in place (keep word order)
    words_reversed = " ".join(word[::-1] for word in words)

    # Vowel count (case-insensitive)
    lower_sentence = sentence.lower()
    vowel_counts = {v: lower_sentence.count(v) for v in "aeiou"}

    # Print report
    print(f"\nOriginal         : {sentence}")
    print(f"Characters       : {char_total} ({char_no_spaces} without spaces)")
    print(f"Words            : {word_count}")
    print(f"Reversed sentence: {reversed_sentence}")
    print(f"Words reversed   : {words_reversed}")
    vowel_line = "  ".join(f"{v}={vowel_counts[v]}" for v in "aeiou")
    print(f"Vowel counts     : {vowel_line}")


# ==============================================================
# Run all questions
# ==============================================================

if __name__ == "__main__":
    print("\nRun individual questions by calling their functions.")
    print("Uncomment the question you want to test below:\n")

    # q1_bill_splitter()
    # q2_number_classifier()
    q3_multiplication_grid()    # No input needed — safe to run directly
    q4_password_checker_demo()  # No input needed — safe to run directly
    # q5_text_analysis()
