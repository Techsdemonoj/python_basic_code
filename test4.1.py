# Method 2: Using a function with named parameters
def calculate_simple_interest2(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest


# Get user input
principal2 = float(input("Enter the principal amount: "))
rate2 = float(input("Enter the interest rate per annum: "))
time2 = float(input("Enter the time in years: "))

# Calculate and display simple interest
interest2 = calculate_simple_interest2(principal=principal2, rate=rate2, time=time2)
print(f"Simple Interest : {interest2}")
