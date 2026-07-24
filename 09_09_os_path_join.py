import os

# Practice Question # 1
#
# Import the built-in "os" module.
#
# Create a folder name:
# "Projects"
#
# Create a file name:
# "notes.txt"
#
# Join both names using
# os.path.join().
#
# Print the complete path.
#
# Expected Output:
#
# Projects\notes.txt
#
# (The separator may be different
# depending on your operating system.)

os.mkdir("Projects")

with open ("notes.txt", "w") as z:
    z.write("Os Built-in Module")

a = os.path.join("Projects", "notes.txt")
print(a)


# Practice Question # 2
#
# Create a folder named:
# "Python Files"
#
# Create a file named:
# "data.txt"
#
# Store the complete path in
# a variable.
#
# Print:
#
# 1. The complete path.
# 2. The data type of the result.
#
# Expected Output:
#
# Python Files\data.txt
#
# <class 'str'>

Folder = "Python Files"
File = "data.txt"

os.mkdir("Python Files")

s = os.path.join(Folder, File)
print(s)
print(type(s))

with open (s, "w") as y:
    y.write("Built-in Modules")
