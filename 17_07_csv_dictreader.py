# Practice Question #7
#
# Create a CSV file named "students.csv" with:
#
# Name,Age,Course
# Ali,20,Python
# Ahmed,22,Excel
# Sara,21,Data Science
#
# Use csv.DictReader() to read the CSV file.
#
# Then:
# - Print each student's name.
# - Print each student's course.

import csv

with open ("students.csv", "r", newline="") as file: # Open csv file in read mode.
    reader = csv.DictReader(file) # Use csv.DictReader() to read the CSV file.
    for row in reader: # Use a for loop to iterate through the remaining rows.
        print(row["Name"]) # Print student names.
        print(row["Course"]) # Print student courses.


