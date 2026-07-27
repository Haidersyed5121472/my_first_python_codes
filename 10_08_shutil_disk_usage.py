import shutil
import os

# Practice Question # 1
#
# Import the built-in "shutil" module.
#
# Store the disk usage information
# of the current working directory
# in a variable.
#
# Print:
#
# 1. Total Space
# 2. Used Space
# 3. Free Space
#
# Expected Output:
#
# Total Space:
# <value in bytes>
#
# Used Space:
# <value in bytes>
#
# Free Space:
# <value in bytes>

path = os.getcwd()

total, used, free = shutil.disk_usage(path)
print("Total Space :", total)
print("Used Space :", used)
print("Free Space :", free)


# Practice Question # 2
#
# Import the built-in "shutil" module.
#
# Store the disk usage information
# of the current working directory
# in a single variable.
#
# Print:
#
# 1. The complete returned object.
# 2. The data type of the returned object.
#
# Expected Output:
#
# usage(total=..., used=..., free=...)
#
# OR
#
# (total, used, free)
#
# <class 'shutil.usage'>
#
# OR
#
# <class 'tuple'>
#
# (Depending on your Python version)

cur_path = os.getcwd()

usage = shutil.disk_usage(cur_path)
print(usage)

print(type(usage))


