import shutil
import os

# Practice Question # 1
#
# Import the built-in "shutil" module.
#
# Create a folder named:
#
# Projects
#
# Inside the "Projects" folder,
# create a file named:
#
# notes.txt
#
# Write any text into it.
#
# Create a complete copy of the
# "Projects" folder named:
#
# Projects_Backup
#
# Print:
#
# Folder copied successfully.
#
# Expected Output:
#
# Folder copied successfully.

os.mkdir("Projects")

with open ("Projects/notes.txt", "w") as x:
    x.write("Python is the best.")

shutil.copytree("Projects", "Projects_Backup")

print("Folder copied succesfully")


