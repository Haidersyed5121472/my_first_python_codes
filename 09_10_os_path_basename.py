import os

# Practice Question # 1
#
# Create a variable containing
# the following path:
#
# C:\Users\Alli computer\Desktop\Python\notes.txt
#
# Store the last part of the path
# in another variable.
#
# Print the result.
#
# Expected Output:
#
# notes.txt

path = r"C:\Users\Alli computer\Desktop\Python\Built-in Modules\OS Module\notes.txt"

a = os.path.basename(path)

print(a)


# Practice Question # 2
#
# Create a variable containing
# the following path:
#
# C:\Users\Alli computer\Desktop\Python\Built-in Modules\OS Module
#
# Store the last part of the path
# in another variable.
#
# Print the result.
#
# Expected Output:
#
# OS Module

path_1 = r"C:\Users\Alli computer\Desktop\Python\Built-in Modules\OS Module"

b = os.path.basename(path_1)

print(b)