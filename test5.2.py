import textwrap

# Get a string input from the user
input_string = input("Enter a string: ")

# Reverse the string using the textwrap module
reversed_string = textwrap.dedent(input_string)[::-1]

# Display the reversed string
print(f"Reversed String: {reversed_string}")
