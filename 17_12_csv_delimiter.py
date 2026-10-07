# Practice Question #12
#
# Create a CSV file named "students_semicolon.csv".
#
# Store the following data using semicolon (;) instead of comma:
#
# Name;Age;Course
# Ali;20;Python
# Ahmed;22;Excel
# Sara;21;Data Science
#
# Use csv.writer() to create the file.
#
# Then:
# - Use delimiter=";" while creating the writer.
# - Write the header using writerow().
# - Write all three students using writerows().


import csv

with open ("students_semicolon.csv", "w", newline="") as file: # Open CSV file in write mode.
    writer = csv.writer(file, delimiter=";") # Use delimiter=";" while creating the writer.
    writer.writerow(["Name", "Age", "Course"]) # Write the header using writerow().
    writer.writerows([
        ["Ali", 20, "Python"],
        ["Ahmed", 22, "Excel"],
        ["Sara", 21, "Data Science"]
    ]) # Write all three students using writerows().


