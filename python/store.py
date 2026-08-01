print("☆✼★ Welcome to my Store ★✼☆")
print("Mcdonalds\n Chicken\n Door\n yummy chips\n Chair\n Microphone")

print("Simple sales strategy: buy 3 or more items and get 10% off!")

# Ask the user for the quantity and unit price
quantity = int(input("How many items do you want? "))
unit_price = float(input("What is the unit price? "))

# Calculate the subtotal
subtotal = quantity * unit_price

# Apply a discount if the customer buys 3 or more items
discount = 0
if quantity >= 3:
    discount = subtotal * 0.10
    print("You get a 10% discount!")

# Calculate the final total
total_amount = subtotal - discount

# Print the bill
print("Subtotal: $" + str(subtotal))
print("Discount: $" + str(discount))
print("Total amount: $" + str(total_amount))
