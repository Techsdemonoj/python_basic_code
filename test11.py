# Get a full name input from the user
full_name = input("Enter your full name: ")

# Split the full name into individual names
names = full_name.split()

# Reverse the order of first and last names
reversed_name = ' '.join(reversed(names))

# Count the total number of characters in the full name
total_characters = len(full_name)

# Extract initials of the first and last names
first_name_initial = names[0][0].upper()
last_name_initial = names[-1][0].upper()

# Display the results
print(f"Reversed Name: {reversed_name}")
print(f"Total number of characters: {total_characters}")
print(f"Initials: {first_name_initial}{last_name_initial}")
