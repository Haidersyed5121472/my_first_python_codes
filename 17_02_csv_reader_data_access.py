# Practice Question #2
#
# Use the existing "students.csv" file.
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
# 4. Use a for loop to iterate through each row.
# 5. Print only the student's name and course.


import csv

with open ("students.csv", "r", newline="") as z: # Open "students.csv" in read mode.
    reader = csv.reader(z) # Use csv.reader() to read the file.

    for row in reader: # Use a for loop to iterate through each row.
        print(row[0], row[2]) # Print only the student's name and course.


