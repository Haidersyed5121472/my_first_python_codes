# Practice Question #19
#
# Use the existing "products_1.csv" file.
#
# Read the CSV using csv.DictReader().
# Filter products whose Price is greater than 5000.
# Create a new CSV file named "expensive_products.csv".
# Write the filtered products into the new CSV file.
# Keep the same headers: Product, Price, Quantity.

import csv

with open("products_1.csv", "r", newline="") as file: # Open CSV file in read mode.
    reader = csv.DictReader(file) # Use csv.DictReader() to read the CSV file.
    filtered_products = [] # Create an empty list to store filtered products.
    for row in reader: # Use for loop to iterate through the remaining CSV rows.
        if int(row["Price"]) > 5000: # Filter products whose Price is greater than 5000.
            filtered_products.append(row) # Add the filtered row to the list.

with open("expensive_products.csv", "w", newline="") as z: # Open CSV file in write mode.
    writer = csv.DictWriter(z, fieldnames=["Product", "Price", "Quantity"]) # Use csv.DictWriter() to write the CSV file.
    writer.writeheader() # Use writeheader() to write the header.
    writer.writerows(filtered_products) # Use writerows() to write the rows.



