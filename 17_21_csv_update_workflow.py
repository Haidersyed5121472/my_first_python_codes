# Practice Question #21
#
# Use the existing "products_1.csv" file.
#
# Read the CSV using csv.DictReader().
# Change the Price of "Mouse" to 3000.
# Keep all other product data unchanged.
# Write all products into a new CSV file named "products_updated.csv".
# Keep the same headers: Product, Price, Quantity.


import csv

with open("products_1.csv", "r", newline="") as file: # Open CSV file in read mode.
    reader = csv.DictReader(file) # Use DictReader() to read the file.

    updated_products = [] # Create an empty list.
    for row in reader: # Use for loop to iterate through the remaining csv rows.
        if row["Product"] == "Mouse": # Use if condition to check the product.
            row["Price"] = "3000" # Update the price.
        updated_products.append(row) # Use append() method to update the list.


with open("products_updated.csv", "w", newline="") as z: # Open CSV file in write mode.
    writer = csv.DictWriter(z, fieldnames=["Product", "Price", "Quantity"]) # Write CSV file using DictWriter().
    writer.writeheader() # Use writeheader() to write the header.
    writer.writerows(updated_products) # Use writerows to write rows.


