import shutil

# Practice Question # 1
#
# Import the built-in "shutil" module.
#
# Create a file named:
#
# notes.txt
#
# Write any text into it.
#
# Create a copy of the file named:
#
# backup.txt
#
# Print:
#
# File copied successfully.
#
# Expected Output:
#
# File copied successfully.

with open ("notes.txt", "w") as z:
    z.write("Shutil Module")

shutil.copyfile("notes.txt", "backup.txt")

print("File Copied Successfully")


# Practice Question # 2
#
# Create a file named:
#
# report.txt
#
# Write any text into it.
#
# Create a copy named:
#
# report_backup.txt
#
# Check whether the copied file exists.
#
# Print:
#
# Backup Created:
# <True or False>
#
# Expected Output:
#
# Backup Created:
# True

with open ("report.txt", "w") as x:
    x.write("Shutil is Built-in Module")

shutil.copyfile("report.txt", "report_backup.txt")

import os

check_existence = os.path.exists("report_backup.txt")
print(f"Backup Created:", check_existence)


