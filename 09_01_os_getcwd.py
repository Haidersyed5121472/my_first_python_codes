
# Practice Question # 1
#
# Import the built-in "os" module.
#
# Then print the current working directory.
#
# Expected Output:
# Current Working Directory:
# <your current folder path>

import os 

f = os.getcwd() # Current working directory (cwd)
print(f)


# Practice Question # 2
#
# Import the built-in "os" module.
#
# Print the current working directory.
#
# Then print the data type of the value returned by os.getcwd().
#
# Expected Output:
#
# Current Working Directory:
# C:\Users\YourName\Desktop\Python Codes\Built-in Modules\OS
#
# Data Type:
# <class 'str'>

a = os.getcwd()
print(a)

print(type(a))


# Practice Question # 3
#
# Import the built-in "os" module.
#
# Store the current working directory in a variable.
#
# Print the following information:
#
# Current Working Directory:
# <directory path>
#
# Length of Directory Path:
# <number of characters>
#
# Expected Output:
#
# Current Working Directory:
# C:\Users\YourName\Desktop\Python Codes\Built-in Modules\OS
#
# Length of Directory Path:
# 62

cur_dir = os.getcwd()

print(cur_dir)
print(len(cur_dir))
