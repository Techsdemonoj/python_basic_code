import textwrap

# Get a full name input from the user
full_name = input("Enter your full name: ")

# Reverse the order of first and last names
reversed_name = ' '.join(textwrap.wrap(full_name, width=1)[::-1])

# Count the total number of characters in the full name
total_characters = len(full_name)

# Extract initials of the first and last names
first_name_initial = full_name[0].upper()
last_name_initial = full_name.split()[-1][0].upper()

# Display the results
print(f"Reversed Name: {reversed_name}")
print(f"Total number of characters: {total_characters}")
print(f"Initials: {first_name_initial}{last_name_initial}")
