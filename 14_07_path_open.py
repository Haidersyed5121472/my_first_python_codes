import pathlib

# Practice Question # 7
#
# Import the built-in "pathlib" module.
#
# Create a folder named:
#
# Journal
#
# Inside the "Journal" folder,
# create a file named:
#
# daily_log.txt
#
# Then:
#
# 1. Write the following text into the file:
#
# Day 1: Learned Path.open()
#
# 2. Open the same file in append mode
#    and add:
#
# Day 2: Practiced append mode
#
# 3. Read the complete file content.
#
# 4. Print the file content.
#
# 5. Print whether the file exists.
#
# 6. Print the absolute path of the file.
#
# Methods / Properties to Practice:
#
# Path()
# mkdir()
# touch()
# open()
# exists()
# resolve()

folder_path = pathlib.Path("Journal")  # Path for folder
file_path = folder_path.joinpath("daily_log.txt")  # Path for file

folder_path.mkdir(exist_ok=True)  # Create the folder using the Path object
file_path.touch(exist_ok=True)  # Create the file using the Path object

with file_path.open("w") as file:  # Open the file in write mode
    file.write("Day 1: Learned Path.open()")  # Write text into the file

with file_path.open("a") as file_2:  # Open the file in append mode
    file_2.write("\nDay 2: Practiced append mode")  # Append new text to the file

with file_path.open("r") as file_3:  # Open the file in read mode
    content = file_3.read()  # Read the complete file content
    print(content)  # Print the file content

print(file_path.exists())  # Check whether the file exists using the .exists() method
print(file_path.resolve())  # Print the absolute path using the .resolve() method



