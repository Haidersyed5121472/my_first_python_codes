# Practice Question #3
#
# Use the existing "students.csv" file.
#
# The CSV file contains:
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
# 4. Skip the header row.
# 5. Use a for loop to iterate through the remaining rows.
# 6. Print only the student's name.


import csv

with open ("students.csv", "r", newline="") as x: # Open "students.csv" in read mode.
    reader = csv.reader(x) # Use csv.reader() to read the file.
    next(reader) # Skip the header row.

    for row in reader: # Use a for loop to iterate through the remaining rows.
        print(row[0]) # Print only the student's name.


