# Method 1: Using basic arithmetic operations
def calculate_simple_interest1(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

# Get user input
principal1 = float(input("Enter the principal amount: "))
rate1 = float(input("Enter the interest rate per annum: "))
time1 = float(input("Enter the time in years: "))

# Calculate and display simple interest
interest1 = calculate_simple_interest1(principal1, rate1, time1)
print(f"Simple Interest : {interest1}")
