# Practice Question #14
#
# Create a CSV file named "quotes.csv".
#
# Use csv.writer() to write:
#
# Name,Comment
# Ali,Hello World
# Ahmed,Python is easy
# Sara,I love Python
#
# Use quotechar='"' while creating the writer.
#
# Then:
# - Write the header using writerow().
# - Write all three records using writerows().

import csv

with open ("quotes.csv", "w", newline="") as z: # Open CSV file in write mode.
    writer = csv.writer(z, quotechar='"') # Use csv.writer() to write.

    writer.writerow(["Name", "Comment"]) # Write the header using writerow().

    writer.writerows([
        ["Ali", "Hello World"],
        ["Ahmed", "Python is easy"],
        ["Sara", "I love Python"]
    ]) # Write all three records using writerows().


