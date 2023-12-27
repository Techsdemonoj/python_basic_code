import numpy as np

def fahrenheit_to_celsius(fahrenheit):
    return np.deg2rad(fahrenheit)

def celsius_to_fahrenheit(celsius):
    return np.rad2deg(celsius)

# Get temperature and unit from the user
temperature = float(input("Enter temperature: "))
unit = input("Enter unit (F for Fahrenheit, C for Celsius): ").upper()

# Perform the conversion based on the user's input
if unit == "F":
    celsius_temperature = fahrenheit_to_celsius(temperature)
    print(f"{temperature} degrees Fahrenheit is equal to {celsius_temperature:.2f} degrees Celsius.")
elif unit == "C":
    fahrenheit_temperature = celsius_to_fahrenheit(temperature)
    print(f"{temperature} degrees Celsius is equal to {fahrenheit_temperature:.2f} degrees Fahrenheit.")
else:
    print("Invalid unit. Please enter 'F' or 'C'.")
