# Practice Question #20
#
# Use the existing "products_1.csv" file.
#
# Read the CSV using csv.DictReader().
# Calculate Total = Price × Quantity for each product.
# Create a new CSV file named "sales_report.csv".
# Write Product and Total columns into the new CSV file.


import csv

with open("products_1.csv", "r", newline="") as file: # Open CSV file in read mode.
    reader = csv.DictReader(file) # Use DictReader() to read the file.

    total_products = [] # Create the empty list.
    for row in reader: # Use for loop to iterate through the remaining CSV rows.
        price = int(row["Price"]) # Store price in a variable.
        quantity = int(row["Quantity"]) # Store quantity in a variable.
        total = price * quantity # Multiply price with quantity to get total.
        total_products.append({"Product": row["Product"], "Total": total}) # Add product and total in the list using .append().

with open("sales_report.csv", "w", newline="") as z: # Open CSV file in write mode.
    writer = csv.DictWriter(z, fieldnames=["Product", "Total"]) # Use DictWriter() to write the CSV file.
    writer.writeheader() # Use writeheader() to write the header.
    writer.writerows(total_products) # Use writerows() to write rows.




