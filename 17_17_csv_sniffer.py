# Practice Question #17
#
# Use the existing "students_semicolon.csv" file.
#
# Use csv.Sniffer().sniff() to automatically detect the delimiter.
# Then use the detected delimiter to read the CSV file.
# Skip the header and print each student's Name and Course.


import csv

with open("students_semicolon.csv", "r", newline="") as file: # Open CSV file in read mode.

    sample = file.read(1024) # Read the file.
    dialect = csv.Sniffer().sniff(sample) # Use csv.Sniffer().sniff() to automatically detect the delimiter.
    file.seek(0) # Move the file pointer back to the beginning.
    reader = csv.reader(file, dialect) # Use csv.reader() to read the CSV file.
    next(reader) # Skip the header

    for row in reader: # Use for loop to iterate through the remaining rows.
        print(row[0], row[2]) # Print each student's Name and Course.



