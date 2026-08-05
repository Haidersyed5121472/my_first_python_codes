import pathlib

# Practice Question # 14
#
# Import the built-in "pathlib" module.
#
# Create a folder named:
#
# Documents_1
#
# Inside the folder, create a file:
#
# report.txt
#
# Then:
#
# 1. Rename the file to:
#
#    final_report.txt
#
# 2. Print:
#
#    - Whether the renamed file exists.
#    - The new file name.
#    - The complete path of the renamed file.
#
# Expected Output (similar to):
#
# True
# final_report.txt
# Documents/final_report.txt
#
# Methods / Properties to Practice:
#
# Path()
# joinpath()
# mkdir()
# touch()
# rename()
# exists()
# name

folder_path = pathlib.Path("Documents_1") # Path for folder

file_path = folder_path.joinpath("report.txt") # Path for file

folder_path.mkdir(exist_ok=True) # Create the folder using the Path object

file_path.touch(exist_ok=True) # Create the file using the Path object

new_name = file_path.rename("Documents_1/final_report.txt") # Rename the original file using .rename()

print(new_name.exists()) # Check new file exists using .exists()

print(new_name.name) # Print new file name

print(new_name) # Print new file Path

