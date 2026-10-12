# Practice Question #22
#
# Use the existing "products_1.csv" file.
#
# Read the CSV using csv.DictReader().
# Calculate Total = Price × Quantity for each product.
# Add a new column named "Total" to each product.
# Create a new CSV file named "inventory_report.csv".
# Write Product, Price, Quantity, and Total columns.
# Keep all products in the report.

import csv

with open("products_1.csv", "r", newline="") as file: # Open CSV file in read mode.
    reader = csv.DictReader(file) # Use DictReader() to read.

    total_product = [] # Create an empty list.
    for row in reader: # Use for loop to iterate through the remaining rows.
        price = int(row["Price"]) # Store price in a variable.
        quantity = int(row["Quantity"]) # Store quantity in a variable.
        total = price * quantity # Multiply price with quantity to get total.
        # Use append() method to update the list.
        total_product.append({"Product": row["Product"], "Price": row["Price"], "Quantity": row["Quantity"], "Total": total})

with open("inventory_report.csv", "w", newline="") as z: # Open CSV file in write mode.
    writer = csv.DictWriter(z, fieldnames=["Product", "Price", "Quantity", "Total"]) # Use DictWriter() to write CSV file.

    writer.writeheader() # Use writeheader() to write headers.
    writer.writerows(total_product) # Use writerows() to write the rows.

