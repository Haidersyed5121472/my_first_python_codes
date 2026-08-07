import pathlib

# Practice Question # 21
#
# Import the built-in "pathlib" module.
#
# Create a Path object using the following
# absolute Windows path:
#
# C:/Users/Public/Documents/report.pdf
#
# (Do NOT create any folders or files.)
#
# Then print:
#
# 1. The original path.
# 2. The drive.
# 3. The anchor.
# 4. The parent folder.
# 5. The file name.
#
# Expected Output (similar to):
#
# Original Path:
# C:\Users\Public\Documents\report.pdf
#
# Drive:
# C:
#
# Anchor:
# C:\
#
# Parent Folder:
# C:\Users\Public\Documents
#
# File Name:
# report.pdf
#
# Methods / Properties to Practice:
#
# Path()
# drive
# anchor
# parent
# name


file_path = pathlib.Path("C:/Users/Public/Documents/report.pdf") # Path for file

print(file_path) # Print original path

print(file_path.drive) # Print path drive using .drive

print(file_path.anchor) # Print path anchor using .anchor

print(file_path.parent) # Print path parent using .parent

print(file_path.name) # Print file name using .name



