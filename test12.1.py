# Sample paragraph
sample_paragraph = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia 
deserunt mollit anim id est laborum.
"""

# Specific word to search for
specific_word = input("Enter the word to search for: ")

# Count occurrences of the specific word
occurrences = sample_paragraph.lower().count(specific_word.lower())

# Replace occurrences with another word
replace_with_word = "REPLACED"
modified_text = sample_paragraph.replace(specific_word, replace_with_word)

# Display results
print(f"Number of occurrences of '{specific_word}': {occurrences}")
print(f"Modified Text:\n{modified_text}")
