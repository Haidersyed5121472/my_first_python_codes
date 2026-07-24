import os

# Practice Question # 1
#
# Import the built-in "os" module.
#
# Check whether a folder named
# "Projects" exists in the
# current working directory
# using os.path.exists().
#
# Print the result.
#
# Expected Output:
#
# True
#
# OR
#
# False

a = os.path.exists("Projects")
print(a)


# Practice Question # 2
#
# Create a folder named "Python Files".
#
# Check whether the folder exists
# using os.path.exists().
#
# Print:
#
# Folder Exists:
# <True or False>
#
# Expected Output:
#
# Folder Exists:
# True

os.mkdir("Python Files")

b = os.path.exists("Python Files")

print("Folder Exists:", b)


# Practice Question # 3
#
# Check whether a file named
# "notes.txt" exists in the
# current working directory
# using os.path.exists().
#
# If the file exists,
# print:
#
# File Found
#
# Otherwise print:
#
# File Not Found
#
# Expected Output:
#
# File Found
#
# OR
#
# File Not Found

if os.path.exists("notes.txt"):
    print("File Found")
else:
    print("File Not Found")