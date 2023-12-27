# Get a full name input from the user
full_name = input("Enter your full name: ")

# Split the full name into individual words
words = full_name.split()

# Extract the first character from each word and convert to uppercase
initials = ''.join(word[0].upper() for word in words)

# Display the result
print(f"The initials of '{full_name}' are: {initials}")
