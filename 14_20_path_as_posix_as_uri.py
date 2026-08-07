import pathlib

# Practice Question # 20
#
# Import the built-in "pathlib" module.
#
# Create a Path object for:
#
# Reports/annual_report.pdf
#
# (Do NOT create any folders or files.)
#
# Then print:
#
# 1. The original path.
# 2. The path using as_posix().
# 3. The absolute path.
# 4. The file URI using as_uri().
#
# Expected Output (similar to):
#
# Original Path:
# Reports/annual_report.pdf
#
# POSIX Path:
# Reports/annual_report.pdf
#
# Absolute Path:
# C:\Users\...\Reports\annual_report.pdf
#
# File URI:
# file:///C:/Users/.../Reports/annual_report.pdf
#
# Methods / Properties to Practice:
#
# Path()
# resolve()
# as_posix()
# as_uri()


file_path = pathlib.Path("Reports/annual_report.pdf") # Path for file

print(file_path) # Print Original path

print(file_path.as_posix()) # Print file path using .as_posix()

file = file_path.resolve() # Store the absolute path

print(file) # Print the absolute path

print(file.as_uri()) # Print the file URI using the .as_uri() method



