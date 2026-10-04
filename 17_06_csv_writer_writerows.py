# Practice Question #6
#
# Create a new CSV file named "products.csv".
#
# Then:
# 1. Import the csv module.
# 2. Open "products.csv" in write mode.
# 3. Use csv.writer() to create a writer object.
# 4. Use writerow() to write the header:
#    Product,Price,Quantity
# 5. Use writerows() to add these three rows:
#    Laptop,80000,5
#    Mouse,2500,20
#    Keyboard,5000,10
# 6. Close the file automatically using with.


import csv

with open ("products.csv", "w", newline="") as z: # Open "products.csv" in write mode.
    writer = csv.writer(z) # Use csv.writer() to create a writer object.
    writer.writerow(["Product", "Price", "Quantity"]) # Use writerow() to write the header.
    writer.writerows([
        ["Laptop", 80000, 5],
        ["Mouse", 2500, 20],
        ["Keyboard", 5000, 10]
        ]) # Use writerows() to add multiple rows.


