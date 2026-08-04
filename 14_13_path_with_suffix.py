import pathlib

# Practice Question # 13
#
# Import the built-in "pathlib" module.
#
# Create a folder named:
#
# Files
#
# Inside the folder, create a file:
#
# report.txt
#
# Then:
#
# 1. Create a new Path object by changing only the
#    file extension to:
#
#    .pdf
#
#    (Do NOT rename the actual file.)
#
# 2. Print:
#
#    - Original file name
#    - New file name
#    - Original suffix
#    - New suffix
#    - Original Path
#    - New Path
#
# Expected Output (similar to):
#
# Original File:
# report.txt
#
# New File:
# report.pdf
#
# Original Suffix:
# .txt
#
# New Suffix:
# .pdf
#
# Original Path:
# Files/report.txt
#
# New Path:
# Files/report.pdf
#
# Methods / Properties to Practice:
#
# Path()
# joinpath()
# mkdir()
# touch()
# with_suffix()
# name
# suffix


import pathlib

folder_path = pathlib.Path("Files") # Path for folder

file_path = folder_path.joinpath("report.txt") # Path for file

folder_path.mkdir(exist_ok=True) # Create the folder using the Path object

file_path.touch(exist_ok=True) # Create the file using the Path object

new_path = file_path.with_suffix(".pdf") # Create a new Path object using the with_suffix() method

print("Original file :", file_path.name) # Print the original file name

print("New file :", new_path.name) # Print the new file name

print("Original suffix :", file_path.suffix) # Print the original file extension using the .suffix property

print("New suffix :", new_path.suffix) # Print the new file extension using the .suffix property

print(file_path) # Print the original file path

print(new_path) # Print the new file path

