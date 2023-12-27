# Initialize an empty shopping cart
cart = []

# Get prices of items from the user until they are done
while True:
    item_price = input("Enter the price of the item (or 'done' to finish): ")

    if item_price.lower() == 'done':
        break

    try:
        # Convert input to float and add to the cart
        item_price = float(item_price)
        cart.append(item_price)
    except ValueError:
        print("Invalid input. Please enter a valid price.")

# Calculate and print the total cost of items in the cart
if cart:
    total_cost = sum(cart)
    print(f"Total cost of items in the cart: ${total_cost:.2f}")
else:
    print("Your shopping cart is empty.")
