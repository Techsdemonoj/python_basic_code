from string import Template

# Get user information
name = input("Enter your name: ")
age = input("Enter your age: ")
favorite_color = input("Enter your favorite color: ")

# Create a template and substitute variables
template = Template("Hello, $name! You are $age years old, and your favorite color is $color.")
message = template.substitute(name=name, age=age, color=favorite_color)

# Display the user information
print(message)
