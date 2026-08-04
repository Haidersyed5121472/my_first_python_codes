import pathlib

# Practice Question # 11
#
# Import the built-in "pathlib" module.
#
# Create the following folder structure
# using the joinpath() method wherever possible:
#
# Projects
# ├── Python
# │   ├── pathlib_notes.txt
# │   └── practice.py
# └── Data
#     ├── dataset.csv
#     └── results.xlsx
#
# Requirements:
#
# 1. Create a Path object for "Projects".
# 2. Use joinpath() to create Path objects for:
#    - Python folder
#    - Data folder
#    - pathlib_notes.txt
#    - practice.py
#    - dataset.csv
#    - results.xlsx
#
# 3. Create all folders.
# 4. Create all files.
#
# Then print:
#
# 1. Whether the "Projects" folder exists.
# 2. Whether the "Python" folder exists.
# 3. Whether the "Data" folder exists.
# 4. The names of all files.
#
# Expected Output (similar to):
#
# True
# True
# True
#
# pathlib_notes.txt
# practice.py
# dataset.csv
# results.xlsx
#
# Methods / Properties to Practice:
#
# Path()
# joinpath()
# mkdir()
# touch()
# exists()
# name


folder_path = pathlib.Path("Projects") # Path for folder

sub_folder_python = folder_path.joinpath("Python") # Path for subfolder

txt_file_path = sub_folder_python.joinpath("pathlib_notes.txt") # Path for file

py_file_path = sub_folder_python.joinpath("practice.py") # Path for file

sub_folder_data = folder_path.joinpath("Data") # Path for subfolder

csv_file_path = sub_folder_data.joinpath("dataset.csv") # Path for file

xlsx_file_path = sub_folder_data.joinpath("results.xlsx") # Path for file


folder_path.mkdir(exist_ok=True) # Create folder using path object

sub_folder_python.mkdir(exist_ok=True) # Create subfolder using path object
txt_file_path.touch(exist_ok=True) # Create file using path object
py_file_path.touch(exist_ok=True) # Create file using path object

sub_folder_data.mkdir(exist_ok=True) # Create subfolder using path object
csv_file_path.touch(exist_ok=True) # Create file using path object
xlsx_file_path.touch(exist_ok=True) # Create file using path object

print(folder_path.exists()) # Check folder exists using exists()

print(sub_folder_python.exists()) # Check subfolder exists using exists()

print(sub_folder_data.exists()) # Check subfolder exists using exists()

print(txt_file_path.name) # Print the file name using the .name property

print(py_file_path.name) # Print the file name using the .name property

print(csv_file_path.name) # Print the file name using the .name property

print(xlsx_file_path.name) # Print the file name using the .name property


