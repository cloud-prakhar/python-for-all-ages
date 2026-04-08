# Example 8: Nested Conditions
# Nested if = an if statement inside another if statement.
# Use this when a second decision depends on the first one being true.
# Real life: A cinema — first check if you have a ticket, THEN check your age for the film rating.

has_ticket = True
age = 14
film_rating = "PG-13"   # Options: "G", "PG-13", "R"

if has_ticket:
    print("Ticket verified. Checking film rating eligibility...")

    if film_rating == "G":
        print("All ages welcome. Enjoy the show!")

    elif film_rating == "PG-13":
        if age >= 13:
            print("You're old enough for this PG-13 film. Enjoy!")
        else:
            print("This film is rated PG-13. You need to be at least 13.")

    elif film_rating == "R":
        if age >= 17:
            print("Restricted film access granted.")
        else:
            print("You must be 17+ for R-rated films.")

else:
    print("No ticket found. Please purchase a ticket first.")
