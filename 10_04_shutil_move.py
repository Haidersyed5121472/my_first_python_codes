import shutil
import os


# Practice Question # 1
#
# Import the built-in "shutil" module.
#
# Create a folder named:
#
# Destination
#
# Create a file named:
#
# destination_notes.txt
#
# Write any text into it.
#
# Move the file into the
# Destination folder using
# shutil.move().
#
# Print:
#
# File moved successfully.
#
# Expected Output:
#
# File moved successfully.

os.mkdir("Destination")

with open ("destination_notes.txt", "w") as z:
    z.write("Built-in Module Shutil")

shutil.move("destination_notes.txt", "Destination")

print("File moved successfully.")


# Practice Question # 2
#
# Create a folder named:
#
# Archive_1
#
# Create a file named:
#
# archive_1_report.txt
#
# Write any text into it.
#
# Move the file into the
# Archive folder with the
# new name:
#
# final_report1.txt
#
# Check whether the moved file exists.
#
# Print:
#
# Move Successful:
# <True or False>
#
# Expected Output:
#
# Move Successful:
# True

os.mkdir("Archive_1")

with open ("archive_1_report.txt", "w") as z:
    z.write("Practicing Shutil Module.")

shutil.move("archive_1_report.txt", "Archive_1/final_report1.txt")

existance_check = os.path.exists("Archive_1/final_report1.txt")
print("Move Successfully :", existance_check)


