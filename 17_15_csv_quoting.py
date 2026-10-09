# Practice Question #15
#
# Create a CSV file named "employees_quotes.csv".
#
# Write the following data:
#
# Name,Department,Salary
# Ali,Sales,50000
# Ahmed,IT,70000
# Sara,HR,60000
#
# Use csv.writer() with:
# quoting=csv.QUOTE_ALL
#
# Then:
# - Write the header using writerow().
# - Write all three employees using writerows().


import csv

with open ("employees_quotes.csv", "w", newline="") as file: # Open CSV file in write mode.
    writer = csv.writer(file, quoting=csv.QUOTE_ALL) # Use csv.writer() with quoting=csv.QUOTE_ALL

    writer.writerow(["Name", "Department", "Salary"]) # Write the header using writerow().

    writer.writerows([
        ["Ali", "Sales", 50000],
        ["Ahmed", "IT", 70000],
        ["Sara", "HR", 60000]
    ]) # Write all three employees using writerows().


