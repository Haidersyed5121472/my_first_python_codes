# Practice Question #1
#
# Create a CSV file named "students.csv".
#
# Store the following data:
#
# Name,Age,Course
# Ali,20,Python
# Ahmed,22,Excel
# Sara,21,Data Science
#
# Then:
# 1. Import the csv module.
# 2. Open "students.csv" in read mode.
# 3. Use csv.reader() to read the file.
# 4. Use a for loop to print each row.

import csv

with open ("students.csv", "r", newline="") as file: # Open "students.csv" in read mode.
    reader = csv.reader(file) # Use csv.reader() to read the file.

    for row in reader: # Iterate through each row in the CSV file.
        print(row) # Print each row.



