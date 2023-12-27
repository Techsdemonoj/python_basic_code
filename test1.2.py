import numpy as np

# Function to calculate the area of a circle
def calculate_circle_area(radius):
    # Formula for the area of a circle: Area = π * radius^2
    area = np.pi * radius**2
    return area

# Get the radius from the user
 
radius = float(input("Enter the radius of the circle: "))

# Calculate the area of the circle
area = calculate_circle_area(radius)

# Display the result
print(f"The area of the circle with radius {radius} is: {area}")
