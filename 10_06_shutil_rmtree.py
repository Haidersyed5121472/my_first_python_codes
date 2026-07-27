import shutil
import os

# Practice Question # 1
#
# Import the built-in "shutil" module.
#
# Create a folder named:
#
# Project_1
#
# Inside the "Project_1" folder,
# create a file named:
#
# notes.txt
#
# Write any text into it.
#
# Delete the complete
# "Project_1" folder using
# shutil.rmtree().
#
# Print:
#
# Folder removed successfully.
#
# Expected Output:
#
# Folder removed successfully.


os.mkdir("Project_1")

with open ("Project_1/notes.txt", "w") as z:
    z.write("Learning methods of shutil module.")

shutil.rmtree("Project_1")

print("Folder removed successfully.")


# Practice Question # 2
#
# Create a folder named:
#
# Backup_1
#
# Inside the "Backup_1" folder,
# create another folder named:
#
# Reports
#
# Inside the "Reports" folder,
# create a file named:
#
# report.txt
#
# Write any text into it.
#
# Delete the complete
# "Backup_1" folder using
# shutil.rmtree().
#
# Check whether the folder exists.
#
# Print:
#
# Folder Exists:
# <True or False>
#
# Expected Output:
#
# Folder Exists:
# False

os.mkdir("Backup_1")
os.mkdir("Backup_1/Reports")

with open ("Backup_1/Reports/reports.txt","w") as x:
    x.write("Learning rmtree method.")

shutil.rmtree("Backup_1")

check_folder_existence = os.path.exists("Backup_1")
print("Folder Exists :", check_folder_existence)


