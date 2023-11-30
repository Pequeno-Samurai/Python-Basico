# Ask user for their name and remove whitespace from str and capitalize user's name.
name = input("Type your name: ").strip().title()

#split user's name into first and last name.
first, last = name.split(" ")

# Writes the first name and last name of user.
print(f"First name: {first}\nLast name: {last}")