def search_and_replace(paragraph, search_word, replace_word):
    # Search for the specific word and count occurrences
    occurrences = paragraph.lower().count(search_word.lower())

    # Replace all occurrences of the word
    modified_paragraph = paragraph.replace(search_word, replace_word)

    return occurrences, modified_paragraph


def main():
    # Given paragraph
    given_paragraph = "Python is commonly used for developing websites and software, task automation, data analysis, and data visualization. Since it's relatively easy to learn, Python has been adopted by many non-programmers such as accountants and scientists, for a variety of everyday tasks, like organizing finances in python"

    # Specific word to search for
    specific_word = "python"

    # Word to replace with
    replace_word = "replace_with"

    # Search for the specific word and replace in the given paragraph
    occurrences, modified_paragraph = search_and_replace(given_paragraph, specific_word, replace_word)

    # Display results
    print(f"Occurrences of '{specific_word}': {occurrences}")
    print("Modified Paragraph:")
    print(modified_paragraph)


if __name__ == "__main__":
    main()
