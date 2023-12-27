# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Get temperature in Fahrenheit from the user
fahrenheit_temperature = float(input("Enter temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius
celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature)

# Display the result
print(f"{fahrenheit_temperature} degrees Fahrenheit is equal to {celsius_temperature:.2f} degrees Celsius.")
