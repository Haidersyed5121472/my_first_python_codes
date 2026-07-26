import os

# Practice Question # 1
#
# Create a folder named:
#
# Python Files
#
# Check whether it is
# a directory.
#
# Print the result.
#
# Expected Output:
#
# True

os.mkdir("Python Files")

folder = "Python Files"

check_directory = os.path.isdir(folder)

print(check_directory)


# Practice Question # 2
#
# Create a file named:
#
# report.txt
#
# Check whether it is
# a directory.
#
# Print:
#
# Is Directory:
# <True or False>
#
# Expected Output:
#
# Is Directory:
# False

with open ("report.txt", "w") as x:
    x.write("Os Modules.")

file = "report.txt"

check_directory_1 = os.path.isdir(file)

print(f"Is Directory:" ,check_directory_1)

