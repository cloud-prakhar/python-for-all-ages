# Chapter 9 Exercise Solutions — Tuples, Sets & Dictionaries
#
# NOTE FOR STUDENTS: Try the exercises yourself first before reading these solutions!
# Understanding WHY the solution works is more important than copying it.

print("=" * 50)
print("CHAPTER 9 EXERCISE SOLUTIONS")
print("=" * 50)


# --------------------------------------------------
# Exercise 1 (Tuples):
# Tuple of 7 days of the week.
# Print: first day, last day, weekdays (Mon-Fri) using slicing.
# --------------------------------------------------

print("\n--- Exercise 1 (Tuples) ---")

# A tuple is defined with regular parentheses ().
# Like a list, but IMMUTABLE — you cannot change its contents after creation.
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

print(f"First day        : {days[0]}")      # Monday — index 0
print(f"Last day         : {days[-1]}")     # Sunday — index -1

# Weekdays are Monday to Friday = indices 0 to 4 → slice [0:5]
# (stop=5 is EXCLUDED, so we get indices 0,1,2,3,4 = Mon-Fri)
weekdays = days[0:5]
print(f"Weekdays (Mon-Fri): {weekdays}")

# WHY a tuple here? Days of the week never change — they are FIXED data.
# Tuples signal "this data is constant" to anyone reading your code.
# They are also slightly faster than lists for read-only data.


# --------------------------------------------------
# Exercise 2 (Tuples):
# Tuple for a map point (latitude, longitude). Unpack into two variables.
# --------------------------------------------------

print("\n--- Exercise 2 (Tuples) ---")

# Tuples are perfect for coordinates — they are a fixed pair that belongs together.
location = (28.6139, 77.2090)   # New Delhi, India

# Tuple unpacking: assigns each element to a separate variable in one line.
# This is much cleaner than: lat = location[0]; lon = location[1]
latitude, longitude = location

print(f"Location  : {location}")
print(f"Latitude  : {latitude}° N")
print(f"Longitude : {longitude}° E")
print(f"City      : New Delhi, India")

# BONUS: You can unpack any iterable (tuples, lists, strings) this way.
# The number of variables on the left MUST match the number of items on the right.


# --------------------------------------------------
# Exercise 3 (Sets):
# boys = {"Arjun", "Rohan", "Bharat"}
# girls = {"Priya", "Rohan", "Meera"}
# Print union, intersection, unique to boys.
# --------------------------------------------------

print("\n--- Exercise 3 (Sets) ---")

# A set is defined with curly braces {}.
# Sets only store UNIQUE values — no duplicates allowed.
# Sets have NO guaranteed order — you cannot use index like set[0].
boys = {"Arjun", "Rohan", "Bharat"}
girls = {"Priya", "Rohan", "Meera"}

print(f"Boys  : {boys}")
print(f"Girls : {girls}")

# Union (|) = all names from BOTH sets (each name appears only once)
union = boys | girls
print(f"\nUnion (all names)       : {union}")

# Intersection (&) = names that appear in BOTH sets
intersection = boys & girls
print(f"Intersection (in both)  : {intersection}")    # {"Rohan"}

# Difference (-) = names in boys that are NOT in girls
unique_to_boys = boys - girls
print(f"Unique to boys          : {unique_to_boys}")  # {"Arjun", "Bharat"}

# VENN DIAGRAM ANALOGY:
# Union      = the entire area of both circles combined
# Intersection = only the overlapping area in the middle
# Difference = left circle minus the middle (only what's exclusive to the left)


# --------------------------------------------------
# Exercise 4 (Sets):
# List with duplicates: [1, 2, 2, 3, 3, 3, 4, 5, 5]
# Convert to set to remove duplicates. Print how many unique numbers.
# --------------------------------------------------

print("\n--- Exercise 4 (Sets) ---")

numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 5, 5]
print(f"Original list          : {numbers_with_duplicates}")
print(f"Length (with dupes)    : {len(numbers_with_duplicates)}")

# Converting a list to a set automatically removes all duplicates.
unique_numbers = set(numbers_with_duplicates)
print(f"Unique numbers (set)   : {unique_numbers}")
print(f"Count of unique numbers: {len(unique_numbers)}")

# If you need a list back (e.g. to sort it), convert back to list:
unique_list = sorted(list(unique_numbers))
print(f"Back as sorted list    : {unique_list}")

# IMPORTANT: Sets are unordered, so the output order may vary.
# Use sorted() if you need a specific order.


# --------------------------------------------------
# Exercise 5 (Dictionaries):
# Dictionary of 5 countries and populations.
# Print the country with the highest population.
# --------------------------------------------------

print("\n--- Exercise 5 (Dictionaries) ---")

# A dictionary stores KEY: VALUE pairs inside curly braces {}.
# Here: key = country name (str), value = population (int)
populations = {
    "China": 1_412_000_000,
    "India": 1_400_000_000,
    "USA": 331_000_000,
    "Indonesia": 275_000_000,
    "Pakistan": 225_000_000,
}

print("Country populations:")
for country, pop in populations.items():
    # .items() gives us (key, value) pairs to loop over
    print(f"  {country:<12}: {pop:>15,}")   # :, formats numbers with commas

# max() with key= lets us find the key with the maximum value
most_populous = max(populations, key=populations.get)
print(f"\nMost populous country: {most_populous} ({populations[most_populous]:,})")

# HOW max(populations, key=populations.get) works:
# max() looks at each key in the dictionary.
# key=populations.get tells it: "compare by the VALUE for each key, not the key itself."
# It finds the key whose value is the largest.


# --------------------------------------------------
# Exercise 6 (Dictionaries):
# Build a quiz using a dictionary. Keys = questions, values = answers.
# Ask the user each question, check their answer, keep score.
# --------------------------------------------------

print("\n--- Exercise 6 (Dictionaries) ---")

# Each key is a question string; each value is the correct answer string.
quiz = {
    "What is the capital of India?": "New Delhi",
    "How many days are in a leap year?": "366",
    "What does CPU stand for?": "Central Processing Unit",
    "Which planet is closest to the Sun?": "Mercury",
}

score = 0           # Accumulator — starts at 0 and increases for each correct answer
total = len(quiz)   # Total number of questions

print("=== QUIZ TIME! ===\n")

# .items() gives us each question-answer pair
for question, correct_answer in quiz.items():
    user_answer = input(f"Q: {question}\nYour answer: ")

    # .strip() removes accidental spaces; .lower() ignores capitalisation differences
    if user_answer.strip().lower() == correct_answer.lower():
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The answer was: {correct_answer}\n")

# Final score
print(f"=== QUIZ COMPLETE! ===")
print(f"Your score: {score}/{total}")

# Convert to percentage for a nice result
percentage = (score / total) * 100
print(f"Percentage: {percentage:.0f}%")

if percentage == 100:
    print("Perfect score! Excellent!")
elif percentage >= 75:
    print("Great job!")
elif percentage >= 50:
    print("Good effort — keep studying!")
else:
    print("Keep practising — you'll get there!")
