print("☆✼★ Welcome to my Store ★✼☆")
print("Here is our menu:")

# Store ALL product names in one list
names = ["burger", "chips", "drink", "cookie"]

# Store ALL product prices in a second list
prices = [5.00, 2.00, 3.00, 1.50]

# Start with a total of 0
running_total = 0.0

# Let the customer order again and again
while True:
    # Show the menu with codes
    for i in range(len(names)):
        print(f"{i}: {names[i]} - ${prices[i]:.2f}")

    # Ask the customer for a product code
    code = int(input("Enter the product code (0, 1, 2, or 3): "))

    # Validate the code before using it
    while code < 0 or code >= len(names):
        print("Invalid code. Please try again.")
        code = int(input("Enter the product code (0, 1, 2, or 3): "))

    # Look up the product name and price using the code
    product_name = names[code]
    product_price = prices[code]

    # Ask for the quantity
    quantity = int(input("How many do you want? "))

    # Calculate the total price for this purchase
    total_price = product_price * quantity
    running_total += total_price

    # Print the result for this order
    print(f"You bought {quantity} {product_name}(s)")
    print(f"Total price for this order: ${total_price:.2f}")

    # Ask if the customer wants to order again
    again = input("Do you want to order again? (yes/no): ").lower().strip()
    if again != "yes":
        break

# Print the final total
print(f"Final total: ${running_total:.2f}")
