# Example 5: f-Strings (Formatted Strings)
# f-strings let you put variables INSIDE a string easily.
# Just put an f before the quotes and wrap variables in { }!
# Real life: Like filling in blanks in a letter template.

name = "Ananya"
age = 9
city = "Bangalore"
score = 95.5

# Old way (harder)
print("My name is " + name + " and I am " + str(age) + " years old.")

# f-string way (much easier!)
print(f"My name is {name} and I am {age} years old.")
print(f"I live in {city}.")
print(f"My score is {score:.1f}%")     # .1f = 1 decimal place
print(f"Next year I will be {age + 1} years old!")

# You can do math inside {}!
apples = 12
friends = 4
print(f"Each friend gets {apples // friends} apples.")
