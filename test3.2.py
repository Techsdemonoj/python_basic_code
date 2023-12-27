# Get two integer inputs from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer:"))

# Display the original values
print(f"Original values: num1 = {num1}, num2 = {num2}")

# Swap values using tuple unpacking
num1, num2 = num2, num1

# Display the swapped values
print(f"Swapped values: num1 = {num1}, num2 = {num2}")
