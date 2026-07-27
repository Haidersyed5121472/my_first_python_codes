import shutil
import os

# Practice Question # 1
#
# Import the built-in "shutil" module.
#
# Create a folder named:
#
# Copy2_Backup
#
# Create a file named:
#
# notes1.txt
#
# Write any text into it.
#
# Copy the file into the
# Backup folder using
# shutil.copy2().
#
# Print:
#
# File copied successfully.
#
# Expected Output:
#
# File copied successfully.

os.mkdir("Copy2_Backup")

with open("notes1.txt", "w") as z:
    z.write("Practicing Built-in Module.")

shutil.copy2("notes1.txt", "Copy2_Backup")

print("File Copied Successfully.")


# Practice Question # 2
#
# Create a folder named:
#
# Archive
#
# Create a file named:
#
# archive_report.txt
#
# Write any text into it.
#
# Copy the file into the
# Archive folder with the
# new name:
#
# final_report.txt
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

os.mkdir("Archive")

with open ("archive_report.txt", "w") as x:
    x.write("Learning shutil module.")

shutil.copy2("archive_report.txt", "Archive/final_report.txt")

check_file_existence = os.path.exists("Archive/final_report.txt")
print("Copy Successful :", check_file_existence)


