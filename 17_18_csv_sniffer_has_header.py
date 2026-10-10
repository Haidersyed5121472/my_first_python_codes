# Practice Question #18
#
# Use the existing "students_semicolon.csv" file.
#
# Use csv.Sniffer().has_header() to check whether the CSV file has a header.
# Print the result.

import csv

with open("students_semicolon.csv", "r", newline="") as file: # Open CSV file in read mode.
    sample = file.read(1024) # Read the file.
    has_header = csv.Sniffer().has_header(sample) # Use csv.Sniffer().has_header() to check whether the CSV file has a header.
    print(has_header) # Print the result.



