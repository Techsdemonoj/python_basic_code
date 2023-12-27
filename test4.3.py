import numpy as np

# Method 4: Using numpy for basic arithmetic
def calculate_simple_interest_numpy(principal, rate, time):
    interest = np.multiply(np.multiply(principal, rate, dtype=float), time, dtype=float) / 100
    return interest

# Get user input
principal4 = float(input("Enter the principal amount: "))
rate4 = float(input("Enter the interest rate per annum: "))
time4 = float(input("Enter the time in years: "))

# Calculate and display simple interest using numpy
interest4 = calculate_simple_interest_numpy(principal4, rate4, time4)
print(f"Simple Interest (Method 4): {interest4}")
