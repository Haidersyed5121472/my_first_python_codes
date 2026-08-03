import pathlib


# Practice Question # 8
#
# Import the built-in "pathlib" module.
#
# Create the following folder structure:
#
# Workspace
# ├── report.pdf
# ├── data.csv
# ├── notes.txt
# └── Images
#
# Requirements:
#
# 1. Create the "Workspace" folder.
# 2. Create the "Images" folder inside "Workspace".
# 3. Create the following empty files:
#    - report.pdf
#    - data.csv
#    - notes.txt
#
# Then:
#
# 1. Use iterdir() to loop through everything
#    inside the "Workspace" folder.
#
# 2. For each item, print:
#
#    - Name
#    - Is File?
#    - Is Directory?
#
# Expected Output (similar to):
#
# report.pdf     True    False
# data.csv       True    False
# notes.txt      True    False
# Images         False   True
#
# Methods / Properties to Practice:
#
# Path()
# mkdir()
# touch()
# iterdir()
# name
# is_file()
# is_dir()


import pathlib

folder_path = pathlib.Path("Workspace") # Path for folder
folder_1_path = pathlib.Path("Workspace/Images") # Path for sub-folder
file_path = pathlib.Path("Workspace/report.pdf") # Path for file
file_1_path = pathlib.Path("Workspace/data.csv") # Path for file
file_2_path = pathlib.Path("Workspace/notes.txt") # Path for file

folder_path.mkdir(exist_ok=True) # Create the folder using the Path object
folder_1_path.mkdir(exist_ok=True) # Create a sub-folder using path
file_path.touch(exist_ok=True) # Create the file using the Path object
file_1_path.touch(exist_ok=True) # Create the file using the Path object
file_2_path.touch(exist_ok=True) # Create the file using the Path object

for item in folder_path.iterdir(): # Use a for loop with the iterdir() method
    print(item.name, item.is_file() , item.is_dir()) # Print the name and check whether it is a file or directory






