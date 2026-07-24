import os

# Practice Question # 1
#
# Create a variable containing
# the following file name:
#
# report.pdf
#
# Store the result in
# another variable.
#
# Print:
#
# 1. The complete result.
# 2. The data type of the result.
#
# Expected Output:
#
# ('report', '.pdf')
#
# <class 'tuple'>

a = os.path.splitext("report.pdf")
print(a)
print(type(a))


# Practice Question # 2
#
# Create a variable containing
# the following file name:
#
# python_notes.txt
#
# Store the file name
# and file extension
# in two separate variables.
#
# Print:
#
# 1. File Name
# 2. File Extension
#
# Expected Output:
#
# File Name: python_notes
#
# File Extension: .txt


file = os.path.splitext("python_notes.txt")

print("File Name:", file[0])
print("File Extension:", file[1])

# That is another way 

file_name, file_extension = os.path.splitext("python_notes.txt")

print("File Name:", file_name)
print("File Extension", file_extension)