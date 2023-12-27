from collections import Counter

# Get a string input from the user
input_string = input("Enter a string: ")

# Get a character to count from the user
character_to_count = input("Enter a character to count: ")

# Check if the user entered exactly one character
if len(character_to_count) == 1:
    # Use Counter to count occurrences of the specified character in the string
    char_count = Counter(input_string)
    count = char_count[character_to_count]

    # Display the result
    print(f"The character '{character_to_count}' appears {count} times in the string.")
else:
    print("Please enter exactly one character.")


