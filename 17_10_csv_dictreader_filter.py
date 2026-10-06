# Practice Question #10
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
# - Print only products whose price is greater than 5000.
# - Print the product name and price.

import csv

with open ("products_1.csv", "r", newline="") as z: # Open CSV file in read mode.
    reader = csv.DictReader(z) # Use csv.DictReader() to read the CSV file.

    for row in reader: # Use a for loop to iterate through the remaining rows.
        if int(row["Price"]) > 5000: # Use an if condition to get products whose price is greater than 5000.
            print(row["Product"], row["Price"]) # Print the product name and price.


