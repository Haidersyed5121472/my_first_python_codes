# Practice Question #8
#
# Create a CSV file named "employees_1.csv".
#
# Use csv.DictWriter() to write the following data:
#
# Name,Department,Salary
# Ali,Sales,50000
# Ahmed,IT,70000
# Sara,HR,60000
#
# Then write the data into the CSV file using dictionaries.

import csv

with open ("employees_1.csv", "w", newline="") as z: # Create a CSV file named "employees_1.csv".
    writer = csv.DictWriter(z, fieldnames=["Name", "Department", "Salary"]) # Use csv.DictWriter() to write dictionary data into the CSV file.
    writer.writeheader() # Use writeheader() to add Name, Department, and Salary headers.
    writer.writerow({"Name":"Ali", "Department":"Sales", "Salary":50000}) # Use writerow() to add Ali,Sales,50000.
    writer.writerow({"Name":"Ahmed", "Department":"IT", "Salary":70000}) # Use writerow() to add Ahmed,IT,70000.
    writer.writerow({"Name":"Sara", "Department":"HR", "Salary":60000}) # Use writerow() to add Sara,HR,60000.


