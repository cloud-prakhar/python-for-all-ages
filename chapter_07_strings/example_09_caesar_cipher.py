# Example 9: Caesar Cipher — Simple Encryption
# A Caesar cipher shifts each letter by a fixed number of positions in the alphabet.
# Used by Julius Caesar to send secret messages. Shift by 3: A→D, B→E, Z→C.
#
# NEW CONCEPTS: ord() and chr()
#
#   Every character on your keyboard has a NUMBER assigned to it in a system
#   called ASCII (American Standard Code for Information Interchange).
#
#   ord(character) → returns the ASCII number of a character
#   chr(number)    → returns the character for a given ASCII number
#
#   Examples:
#       ord('A') → 65      chr(65) → 'A'
#       ord('B') → 66      chr(66) → 'B'
#       ord('Z') → 90      chr(90) → 'Z'
#       ord('a') → 97      chr(97) → 'a'  (lowercase starts at 97)
#
#   Why is this useful?
#   Shifting a letter = adding to its number, then converting back.
#   'A' is 65. Shift by 3: 65 + 3 = 68 → chr(68) = 'D'. So A→D!
#
# HOW THE SHIFT FORMULA WORKS (the most complex line):
#
#   shifted = (ord(char) - base + shift) % 26 + base
#
#   Trace with char='Z', shift=3, base=ord('A')=65:
#   1. ord('Z')        → 90
#   2. 90 - 65         → 25   (position in alphabet: A=0, B=1, ..., Z=25)
#   3. 25 + 3          → 28   (shift forward by 3)
#   4. 28 % 26         → 2    (wrap around — 26 letters, 28 wraps to 2)
#   5. 2  + 65         → 67   (convert position back to ASCII number)
#   6. chr(67)         → 'C'  (Z shifted by 3 = C — it wraps from Z back to A!)
#
#   The % 26 makes it wrap around after Z so it cycles back to A.

def caesar_encrypt(text, shift):
    """Encrypt text by shifting each letter by 'shift' positions."""
    result = ""
    for char in text:
        if char.isalpha():
            # .isalpha() is True if the character is a letter (not a space or punctuation)
            # base = starting ASCII value: 65 for UPPERCASE, 97 for lowercase
            base    = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)   # Convert number back to character
        else:
            result += char   # Spaces, punctuation — leave them unchanged
    return result


def caesar_decrypt(text, shift):
    """Decrypt by shifting in the opposite direction."""
    return caesar_encrypt(text, -shift)   # A negative shift reverses the encryption


# --- Demonstration ---
original = input("Enter a message to encrypt: ")
shift    = int(input("Enter shift amount (e.g. 3): "))

encrypted = caesar_encrypt(original, shift)
decrypted = caesar_decrypt(encrypted, shift)

print(f"\nOriginal : {original}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
print(f"\n(Verification: original matches decrypted? {original == decrypted})")
