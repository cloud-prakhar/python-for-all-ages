# Example 8: String Statistics
# Analyze a piece of text — count vowels, consonants, spaces, words, sentences.
# This is a realistic text-processing task similar to what word processors do.
#
# NEW CONCEPT: Generator expressions inside sum()
#
#   sum(1 for ch in text if ch in vowels)
#
#   This is a compact way to COUNT items that meet a condition.
#   Break it down in plain English:
#       "For each character (ch) in text,
#        IF that character is in vowels,
#        count it as 1.
#        Then sum up all those 1s."
#
#   It's equivalent to this longer version:
#       count = 0
#       for ch in text:
#           if ch in vowels:
#               count += 1
#       vowel_count = count
#
#   The expression inside sum(...) is called a GENERATOR EXPRESSION.
#   Think of it as a mini for-loop that produces values on demand.
#   We use it here purely for counting — it's a common Python pattern.
#
# NEW CONCEPT: for label, value in stats.items()
#
#   stats is a DICTIONARY (covered in Chapter 9 — preview here).
#   .items() gives you all key-value pairs from the dictionary.
#   label, value = the two parts of each pair (key and value).
#   This is called UNPACKING — pulling two values out at once.

def analyze_text(text):
    vowels     = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    # sum(1 for ch in text if ch in vowels)
    # → count every character that appears in the vowels string
    vowel_count     = sum(1 for ch in text if ch in vowels)
    consonant_count = sum(1 for ch in text if ch in consonants)
    space_count     = text.count(" ")
    digit_count     = sum(1 for ch in text if ch.isdigit())  # .isdigit() = True if '0'-'9'
    word_count      = len(text.split())                       # split() splits on spaces → list of words
    sentence_count  = text.count(".") + text.count("!") + text.count("?")
    char_count      = len(text)
    char_no_spaces  = len(text.replace(" ", ""))              # remove spaces, then count

    # Return a dictionary of results (label → number)
    return {
        "characters (with spaces)"   : char_count,
        "characters (without spaces)": char_no_spaces,
        "vowels"                     : vowel_count,
        "consonants"                 : consonant_count,
        "digits"                     : digit_count,
        "spaces"                     : space_count,
        "words"                      : word_count,
        "sentences"                  : sentence_count,
    }


text  = input("Enter a sentence or paragraph:\n> ")
stats = analyze_text(text)

print("\n--- Text Analysis ---")
# stats.items() gives pairs: ("vowels", 3), ("words", 5), etc.
# label = the description, value = the number
for label, value in stats.items():
    print(f"  {label:<30}: {value}")   # :<30 = left-align in 30 characters (for neat columns)
