# Practice Question #11
#
# Use the existing "products_1.csv" file:
#
# Product,Price,Quantity
# Laptop,80000,5
# Mouse,2500,20
# Keyboard,5000,10
#
# Use csv.DictReader() to read the CSV file.
#
# Then:
# - Calculate the total value of each product.
# - Total value = Price × Quantity
# - Print the product name and its total value.

import csv

with open ("products_1.csv", "r", newline="") as z: # Open CSV file in read mode.
    reader = csv.DictReader(z) # Use csv.DictReader() to read the CSV file.
    for row in reader: # Use for loop to iterate through the rows.
        price = int(row["Price"]) # Store the price in a variable.
        quantity = int(row["Quantity"]) # Store the quantity in a variable.
        total = price * quantity # Calculate the total value of each product.
        print(row["Product"], total) # Print the product name and its total value.



