import pathlib

# Practice Question # 12
#
# Import the built-in "pathlib" module.
#
# Create a folder named:
#
# Reports_1
#
# Inside the folder, create a file:
#
# annual_report.pdf
#
# Then:
#
# 1. Create a new Path object by changing only the
#    file name to:
#
#    monthly_report.pdf
#
#    (Do NOT rename the actual file.)
#
# 2. Print:
#
#    - Original file name
#    - New file name
#    - Original Path
#    - New Path
#
# Expected Output (similar to):
#
# Original File:
# annual_report.pdf
#
# New File:
# monthly_report.pdf
#
# Original Path:
# Reports_1/annual_report.pdf
#
# New Path:
# Reports_1/monthly_report.pdf
#
# Methods / Properties to Practice:
#
# Path()
# mkdir()
# touch()
# with_name()
# name


import pathlib

folder_path = pathlib.Path("Reports_1") # Path for folder

file_path = folder_path.joinpath("annual_report.pdf") # Path for file


folder_path.mkdir(exist_ok=True) # Create the folder using the Path object

file_path.touch(exist_ok=True) # Create the file using the Path object

new_path = file_path.with_name("monthly_report.pdf") # Create a new Path object using the with_name() method

print(file_path.name) # Print the original file name

print(new_path.name) # Print the new file name

print(file_path) # Print the original file path

print(new_path) # Print the new file path



