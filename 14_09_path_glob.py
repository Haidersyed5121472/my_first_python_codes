import pathlib

# Practice Question # 9
#
# Import the built-in "pathlib" module.
#
# Create the following folder structure:
#
# Documents
# ├── report.pdf
# ├── invoice.pdf
# ├── sales.csv
# ├── employees.csv
# ├── notes.txt
# └── image.png
#
# Requirements:
#
# 1. Create the "Documents" folder.
# 2. Create all the files shown above.
#
# Then:
#
# 1. Use glob("*.pdf") to print only PDF files.
# 2. Use glob("*.csv") to print only CSV files.
# 3. Use glob("*.txt") to print only TXT files.
# 4. Print only the file names (not the complete paths).
#
# Expected Output (similar to):
#
# PDF Files:
# report.pdf
# invoice.pdf
#
# CSV Files:
# sales.csv
# employees.csv
#
# TXT Files:
# notes.txt
#
# Methods / Properties to Practice:
#
# Path()
# mkdir()
# touch()
# glob()
# name


import pathlib

folder_path = pathlib.Path("Documents") # Path for folder

file_path = pathlib.Path("Documents/report.pdf") # Path for file
file_1_path = pathlib.Path("Documents/invoice.pdf") # Path for file
file_2_path = pathlib.Path("Documents/sales.csv") # Path for file
file_3_path = pathlib.Path("Documents/employees.csv") # Path for file
file_4_path = pathlib.Path("Documents/notes.txt") # Path for file
file_5_path = pathlib.Path("Documents/image.png") # Path for file

folder_path.mkdir(exist_ok=True) # Create the folder using the Path object

file_path.touch(exist_ok=True) # Create the file using the Path object
file_1_path.touch(exist_ok=True) # Create the file using the Path object
file_2_path.touch(exist_ok=True) # Create the file using the Path object
file_3_path.touch(exist_ok=True) # Create the file using the Path object
file_4_path.touch(exist_ok=True) # Create the file using the Path object
file_5_path.touch(exist_ok=True) # Create the file using the Path object

for item in folder_path.glob("*.pdf"): # Use a for loop with the glob() method
    print("PDF Files", item.name) # Print the matching file name

for item in folder_path.glob("*.csv"): # Use a for loop with the glob() method
    print("CSV Files", item.name) # Print the matching file name

for item in folder_path.glob("*.txt"): # Use a for loop with the glob() method
    print("TXT Files", item.name) # Print the matching file name


