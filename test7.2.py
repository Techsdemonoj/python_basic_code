try:
    # Get an integer input from the user
    user_input = int(input("Enter an integer: "))

    # Check if the input is odd or even using bitwise AND
    if user_input & 1 == 0:
        print(f"{user_input} is an even number.")
    else:
        print(f"{user_input} is an odd number.")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
