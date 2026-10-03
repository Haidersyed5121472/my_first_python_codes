# Practice Question #4
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
# 6. Print only the students whose course is "Python".


import csv

with open("students.csv", "r", newline="") as x: # Open "students.csv" in read mode.
    reader = csv.reader(x) # Use csv.reader() to read the file.
    next(reader) # Skip the header row.

    for row in reader: # Use a for loop to iterate through the remaining rows.
        if row[2] == "Python": # Use condition to get row of "Python".
            print(row[0]) # Print only the students whose course is "Python".



