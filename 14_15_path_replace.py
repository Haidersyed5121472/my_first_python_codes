import pathlib

# Practice Question # 15
#
# Import the built-in "pathlib" module.
#
# Create a folder named:
#
# Backup
#
# Inside the folder, create two files:
#
# report.txt
# old_report.txt
#
# Then:
#
# 1. Replace old_report.txt with report.txt
#    using the replace() method.
#
# 2. Print:
#
#    - Whether report.txt exists.
#    - Whether old_report.txt exists.
#    - The file name returned by replace().
#    - The complete path returned by replace().
#
# Expected Output (similar to):
#
# False
# True
# old_report.txt
# Backup/old_report.txt
#
# Methods / Properties to Practice:
#
# Path()
# joinpath()
# mkdir()
# touch()
# replace()
# exists()
# name


folder_path = pathlib.Path("Backup") # Path for folder

file_path = folder_path.joinpath("report.txt") # Path for file

file_1_path = folder_path.joinpath("old_report.txt") # Path for file

folder_path.mkdir(exist_ok=True) # Create the folder using the Path object

file_path.touch(exist_ok=True) # Create the file using the Path object

file_1_path.touch(exist_ok=True) # Create the file using the Path object

replaced_file = file_path.replace(file_1_path) # Replace new file from old file using .replace()

print(file_path.exists()) # Check original file exists using .exists()

print(replaced_file.exists()) # Check replaced file exists using .exists()

print(replaced_file.name) # Print the new file name

print(replaced_file) # Print the new file Path

