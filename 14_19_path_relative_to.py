import pathlib

# Practice Question # 19
#
# Import the built-in "pathlib" module.
#
# Create a Path object for:
#
# Projects/Python/Automation/Scripts/report.py
#
# (Do NOT create any folders or files.)
#
# Then:
#
# 1. Print the original path.
#
# 2. Print the path relative to:
#
#    Projects
#
# 3. Print the path relative to:
#
#    Projects/Python
#
# 4. Print the path relative to:
#
#    Projects/Python/Automation
#
# Expected Output (similar to):
#
# Original Path:
# Projects/Python/Automation/Scripts/report.py
#
# Relative to Projects:
# Python/Automation/Scripts/report.py
#
# Relative to Projects/Python:
# Automation/Scripts/report.py
#
# Relative to Projects/Python/Automation:
# Scripts/report.py
#
# Methods / Properties to Practice:
#
# Path()
# relative_to()


file_path = pathlib.Path("Projects/Python/Automation/Scripts/report.py") # Path for file

print("Original Path :",file_path) # Print the original Path

print("Relative to Projects:",file_path.relative_to("Projects")) # Print the Path relative to projects
print("Relative to Projects/Python:",file_path.relative_to("Projects/Python")) # Print the Path Relative to Projects/Python
print("Relative to Projects/Python/Automation:",file_path.relative_to("Projects/Python/Automation")) # Print the Path Relative to Projects/Python/Automation



