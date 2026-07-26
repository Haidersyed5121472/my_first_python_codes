import os

# Practice Question # 1
#
# Create a variable containing
# the following file name:
#
# notes.txt
#
# Store the absolute path
# in another variable.
#
# Print the absolute path.
#
# Expected Output:
#
# C:\...\notes.txt
#
# (The exact path depends on
# your current working directory.)

file = "notes.txt"

file_path = os.path.abspath(file)
print(file_path)


# Practice Question # 2
#
# Create a variable containing
# the following folder name:
#
# Python Projects
#
# Store the absolute path
# in another variable.
#
# Print:
#
# 1. The absolute path.
# 2. The data type of the result.
#
# Expected Output:
#
# C:\...\Projects
#
# <class 'str'>

folder = "Python Projects"

folder_path = os.path.abspath(folder)

print(folder_path)

print(type(folder_path))

