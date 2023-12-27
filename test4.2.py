# Method 3: Using a class
class SimpleInterestCalculator:
    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time

    def calculate_simple_interest(self):
        interest = (self.principal * self.rate * self.time) / 100
        return interest

# Get user input
principal3 = float(input("Enter the principal amount: "))
rate3 = float(input("Enter the interest rate per annum: "))
time3 = float(input("Enter the time in years: "))

# Create an instance of the SimpleInterestCalculator class
calculator = SimpleInterestCalculator(principal3, rate3, time3)

# Calculate and display simple interest
interest3 = calculator.calculate_simple_interest()
print(f"Simple Interest (Method 3): {interest3}")
