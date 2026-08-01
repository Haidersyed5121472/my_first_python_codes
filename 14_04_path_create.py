import pathlib

# Practice Question # 4
#
# Import the built-in "pathlib" module.
#
# Create a folder named:
#
# Reports
#
# Inside the "Reports" folder,
# create an empty file named:
#
# summary.txt
#
# Then print:
#
# 1. Whether the folder exists.
# 2. Whether the file exists.
# 3. Whether "Reports" is a directory.
# 4. Whether "summary.txt" is a file.
#
# Finally:
#
# Print the complete path of the file.
#
# Methods / Properties to Practice:
#
# Path()
# mkdir()
# touch()
# exists()
# is_dir()
# is_file()
# resolve()


folder_path = pathlib.Path("Reports")
file_path = pathlib.Path("Reports/summary.txt")

folder_path.mkdir()

file_path.touch()

print(folder_path)
print(file_path)

print(folder_path.exists())
print(file_path.exists())
print(folder_path.is_dir())
print(file_path.is_file())
print(file_path.resolve())





