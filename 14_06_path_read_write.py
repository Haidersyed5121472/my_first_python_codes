import pathlib

# Practice Question # 6
#
# Import the built-in "pathlib" module.
#
# Create a folder named:
#
# Notes
#
# Inside the "Notes" folder,
# create a file named:
#
# python_notes.txt
#
# Write the following text into the file:
#
# Learning Pathlib Module
# Python Automation Journey
#
# Then:
#
# 1. Read the complete file content.
# 2. Print the file content.
# 3. Print whether the file exists.
# 4. Print the absolute path of the file.
#
# Methods / Properties to Practice:
#
# Path()
# mkdir()
# touch()
# write_text()
# read_text()
# exists()
# resolve()

folder_path = pathlib.Path("Notes")
file_path = pathlib.Path("Notes/python_notes.txt")

folder_path.mkdir(exist_ok=True)
file_path.touch(exist_ok=True)

file_path.write_text("Learning Pathlib Module\nPython Automation Journey")

read_file = file_path.read_text()
print(read_file)

print(file_path.exists())
print(file_path.resolve())


