import pathlib

# Practice Question # 5
#
# Import the built-in "pathlib" module.
#
# Create the following folder structure:
#
# Reports
# └── Monthly
#
# Requirements:
#
# 1. Create a Path object for "Reports".
# 2. Create another Path object for "Reports/Monthly".
# 3. Create both folders.
#
# The program should NOT raise an error
# even if the folders already exist.
#
# Then print:
#
# 1. Whether "Reports" exists.
# 2. Whether "Monthly" exists.
# 3. Whether both are directories.
# 4. The absolute path of "Monthly".
#
# Methods / Properties to Practice:
#
# Path()
# mkdir()
# exists()
# is_dir()
# resolve()

import pathlib


Reports_path = pathlib.Path("Reports")
Monthly_path = pathlib.Path("Reports/Monthly")

Reports_path.mkdir(exist_ok=True)
Monthly_path.mkdir(exist_ok=True)

print(Reports_path)
print(Monthly_path)

print(Reports_path.exists())
print(Monthly_path.exists())

print(Reports_path.is_dir())
print(Monthly_path.is_dir())

print(Monthly_path.resolve())



