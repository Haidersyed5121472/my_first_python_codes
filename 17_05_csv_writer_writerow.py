# Practice Question #5
#
# Create a new CSV file named "employees.csv".
#
# Then:
# 1. Import the csv module.
# 2. Open "employees.csv" in write mode.
# 3. Use csv.writer() to create a writer object.
# 4. Use writerow() to write the header:
#    Name,Department,Salary
# 5. Use writerow() three times to add:
#    Ali,Sales,50000
#    Ahmed,IT,70000
#    Sara,HR,60000
# 6. Close the file automatically using with.


import csv

with open ("employees.csv", "w", newline="") as z: # Open "employees.csv" in write mode.
    writer = csv.writer(z) # Use csv.writer() to create a writer object.
    writer.writerow(["Name", "Department", "Salary"]) # Use writerow() to write the header.
    writer.writerow(["Ali", "Sales", 50000]) # Add Ali,Sales,50000 into csv file.
    writer.writerow(["Ahmed", "IT", 70000]) # Add Ahmed,IT,70000 into csv file.
    writer.writerow(["Sara", "HR", 60000]) # Add Sara,HR,60000 into csv file.


