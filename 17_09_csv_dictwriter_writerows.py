# Practice Question #9
#
# Create a CSV file named "products_1.csv".
#
# Use csv.DictWriter() to write the following data:
#
# Product,Price,Quantity
# Laptop,80000,5
# Mouse,2500,20
# Keyboard,5000,10
#
# Use writeheader() to add the header.
# Use writerows() to add all three product records.
#
# Store each product record as a dictionary.

import csv

with open ("products_1.csv", "w", newline="") as file: # Open CSV file in write mode.
    writer = csv.DictWriter(file, fieldnames=["Product", "Price", "Quantity"]) # Use csv.DictWriter() to write the data.
    writer.writeheader() # Use writeheader() to add the header.
    writer.writerows([
        {"Product": "Laptop", "Price": 80000, "Quantity": 5}, 
        {"Product": "Mouse", "Price": 2500, "Quantity": 20}, 
        {"Product": "Keyboard", "Price": 5000, "Quantity": 10}
    ]) # Use writerows() to add all three product records.


