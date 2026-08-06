import pathlib

# Practice Question # 18
#
# Import the built-in "pathlib" module.
#
# Create a Path object for:
#
# Projects/Python/Automation/report.txt
#
# (Do NOT create any folders or files.)
#
# Then print:
#
# 1. The original path.
# 2. Parent level 1.
# 3. Parent level 2.
# 4. Parent level 3.
# 5. Parent level 4.
#
# Expected Output (similar to):
#
# Original Path:
# Projects/Python/Automation/report.txt
#
# Parent Level 1:
# Projects/Python/Automation
#
# Parent Level 2:
# Projects/Python
#
# Parent Level 3:
# Projects
#
# Parent Level 4:
# .
#
# Methods / Properties to Practice:
#
# Path()
# parents


folder_path = pathlib.Path("Projects/Python/Automation/report.txt") # Path object for the file

print("Original Path :", folder_path) # Print the original Path
print("Parent Level 1 :",folder_path.parents[0]) # Print the Path of parent level 1 
print("Parent Level 2 :",folder_path.parents[1]) # Print the Path of parent level 2
print("Parent Level 3 :",folder_path.parents[2]) # Print the Path of parent level 3
print("Parent Level 4 :",folder_path.parents[3]) # Print the Path of parent level 4


