import pathlib

# Practice Question # 3
#
# Import the built-in "pathlib" module.
#
# Create the following two Path objects:
#
# 1. A folder named "Projects"
# 2. A file named "Projects/data.csv"
#
# (Do NOT create them on your computer.
# Only create Path objects.)
#
# Then print the following information:
#
# ---------- Folder ----------
#
# 1. Does the folder exist?
# 2. Is it a directory?
# 3. Is it a file?
# 4. Is the path absolute?
#
# ---------- File ----------
#
# 5. Does the file exist?
# 6. Is it a file?
# 7. Is it a directory?
# 8. Is the path absolute?
#
# Methods / Properties to Practice:
#
# Path()
# exists()
# is_dir()
# is_file()
# is_absolute()

import pathlib

folder_name = "Projects"
file_name = "Projects/data.csv"

folder_path = pathlib.Path(folder_name)
file_path = pathlib.Path(file_name)

print(folder_name)
print(file_name)
print(folder_path.exists())
print(file_path.exists())
print(folder_path.is_dir())
print(file_path.is_dir())
print(folder_path.is_file())
print(file_path.is_file())
print(folder_path.is_absolute())
print(file_path.is_absolute())




