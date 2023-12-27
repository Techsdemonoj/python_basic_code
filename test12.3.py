def is_palindrome(input_string):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_string = "".join(input_string.split()).lower()

    # Iterate through the characters from both ends
    left, right = 0, len(cleaned_string) - 1
    while left < right:
        if cleaned_string[left] != cleaned_string[right]:
            return False
        left += 1
        right -= 1

    return True


def main():
    # Prompt the user for input
    user_input = input("Enter a string: ")

    # Check if the input is a palindrome
    if is_palindrome(user_input):
        print("The input is a palindrome!")
    else:
        print("The input is not a palindrome.")


if __name__ == "__main__":
    main()
