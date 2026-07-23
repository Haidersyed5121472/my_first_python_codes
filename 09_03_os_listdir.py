import os

# Practice Question # 1
#
# Import the built-in "os" module.
#
# Print all files and folders
# available in the current
# working directory using
# os.listdir().
#
# Expected Output:
#
# ['main.py', 'notes.txt', 'images', 'data.csv']

c = os.listdir()
print(c)


# Practice Question # 2
#
# Import the built-in "os" module.
#
# Store all files and folders from the
# current working directory in a variable.
#
# Print:
#
# 1. The complete list.
# 2. The total number of items.
# 3. The data type of the returned value.
#
# Expected Output:
#
# ['main.py', 'notes.txt', 'images', 'data.csv']
#
# Total Items:
# 4
#
# Data Type:
# <class 'list'>


d = os.listdir()

print(d) # 1. The complete list.

print(len(d)) # 2. The total number of items.

print(type(d)) # 3. The data type of the returned value.