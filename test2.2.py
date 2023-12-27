import numpy as np

# Get temperature in Fahrenheit from the user
fahrenheit_temperature = float(input("Enter temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius using numpy
celsius_temperature = np.degrees(fahrenheit_temperature)

# Display the result
print(f"{fahrenheit_temperature} degrees Fahrenheit is equal to {celsius_temperature:.2f} degrees Celsius.")
