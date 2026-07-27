import shutil
import os

# Practice Question # 1
#
# Import the built-in "shutil" module.
#
# Create a folder named:
#
# Projects_5
#
# Inside the "Projects_5" folder,
# create a file named:
#
# notes.txt
#
# Write any text into it.
#
# Create a ZIP archive named:
#
# Projects_5_Backup
#
# from the "Projects_5" folder
# using shutil.make_archive().
#
# Print:
#
# Archive created successfully.
#
# Expected Output:
#
# Archive created successfully.

os.mkdir("Projects_5")

with open ("Projects_5/notes.txt", "w") as z:
    z.write("Shutil Module.")

shutil.make_archive("Projects_5_Backup", "zip", "Projects_5")

print("Archive created successfully.")


