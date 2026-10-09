# Practice Question #16
#
# Create a CSV file named "products_numeric.csv".
#
# Write the following data:
#
# Product,Price,Quantity
# Laptop,80000,5
# Mouse,2500,20
# Keyboard,5000,10
#
# Use csv.writer() with:
# quoting=csv.QUOTE_NONNUMERIC
#
# Then:
# - Write the header using writerow().
# - Write all three products using writerows().


import csv

with open("products_numeric.csv", "w", newline="") as file: # Open CSV file in write mode.
    writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC) # Use csv.writer() with quoting=csv.QUOTE_NONNUMERIC.

    writer.writerow(["Product", "Price", "Quantity"]) # Write the header using writerow().

    writer.writerows([
        ["Laptop", 80000, 5],
        ["Mouse", 2500, 20],
        ["Keyboard", 5000, 10]
    ]) # Write all three products using writerows().


