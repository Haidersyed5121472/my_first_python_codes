import shutil

# Practice Question # 1
#
# Import the built-in "shutil" module.
#
# Create a folder named:
#
# Backup
#
# Create a file named:
#
# notes.txt
#
# Write any text into it.
#
# Copy the file into the
# Backup folder.
#
# Print:
#
# File copied successfully.
#
# Expected Output:
#
# File copied successfully.

import os

os.mkdir("Backup")

with open ("notes.txt", "w") as z:
    z.write("Learning Shutil Module")

shutil.copy("notes.txt", "Backup")

print("File Copied Successfully.")


# Practice Question # 2
#
# Create a folder named:
#
# Documents
#
# Create a file named:
#
# report1.txt
#
# Write any text into it.
#
# Copy the file into the
# Documents folder with the
# new name:
#
# final_report1.txt
#
# Check whether the copied file exists.
#
# Print:
#
# Copy Successful:
# <True or False>
#
# Expected Output:
#
# Copy Successful:
# True

import os

os.mkdir("Documents")

with open("report1.txt", "w") as x:
    x.write("Learning Built-in Modules.")

shutil.copy("report1.txt", "Documents/final_report1.txt")

file_existence_check = os.path.exists("Documents/final_report1.txt")
print("Copy Successful :", file_existence_check)



