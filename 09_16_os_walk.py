import os

# Practice Question # 1
#
# Create a variable containing
# the current working directory.
#
# Use a loop to print only
# the current folder path
# returned while traversing.
#
# Expected Output:
#
# C:\...\OS Module
#
# C:\...\OS Module\Projects
#
# C:\...\OS Module\Projects\Reports
#
# ...

a = os.getcwd()
print(a)

current_dir = a

for folder, subfolders, files in os.walk(current_dir):
    print(folder)


# Practice Question # 2
#
# Create a variable containing
# the current working directory.
#
# Use a loop to print only
# the list of subfolders.
#
# Expected Output:
#
# ['Projects', 'Images']
#
# ['Reports']
#
# []
#
# ...

path = os.getcwd()
print(path)

for folder, subfolders, files in os.walk(path):
    print(subfolders)


# Practice Question # 3
#
# Create a variable containing
# the current working directory.
#
# Use a loop to print only
# the list of files.
#
# Expected Output:
#
# ['main.py', 'notes.txt']
#
# ['project1.py']
#
# ['report.pdf']
#
# ...

cur_dir_path = os.getcwd()
print(cur_dir_path)

for folder, subfolders, files in os.walk(cur_dir_path):
    print(files)


# Practice Question # 4
#
# Create a variable containing
# the current working directory.
#
# Traverse all folders.
#
# Print:
#
# Folder:
# <current folder path>
#
# Files:
# <list of files>
#
# Print a blank line after
# each folder.
#
# Expected Output:
#
# Folder:
# C:\...\OS Module
#
# Files:
# ['main.py', 'notes.txt']
#
# Folder:
# C:\...\OS Module\Projects
#
# Files:
# ['project1.py']
#
# ...

cur_working_dir = os.getcwd()
print(cur_working_dir)

for folder, subfolders, files in os.walk(cur_working_dir):
    print(f"Folder:", folder)
    print(f"Files:", files)
    print()

