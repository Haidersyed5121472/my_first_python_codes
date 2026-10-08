# Practice Question #13
#
# Use the existing "students_semicolon.csv" file.
#
# The file contains:
#
# Name;Age;Course
# Ali;20;Python
# Ahmed;22;Excel
# Sara;21;Data Science
#
# Use csv.reader() to read the CSV file.
#
# Then:
# - Use delimiter=";" while creating the reader.
# - Skip the header.
# - Print each student's name and course.

import csv

with open ("students_semicolon.csv") as file: # Open CSV file in read mode.
    reader = csv.reader(file, delimiter=";") # Use csv.reader() to read the CSV file.
    next(reader) # Skip the header.

    for row in reader: # Use for loop to iterate through the remaining lines.
        print(row[0], row[2]) # Print each student's name and course.



