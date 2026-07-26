import os

# Practice Question # 1
#
# Create a file named:
#
# python_notes.txt
#
# Check whether it is a file.
#
# Print the result.
#
# Expected Output:
#
# True

with open ("python_notes.txt", "w") as z:
    z.write("Learning Os Modules in python.")

file = "python_notes.txt"

check_file = os.path.isfile(file)
print(check_file)


# Practice Question # 2
#
# Create a folder named:
#
# Documents
#
# Check whether it is a file.
#
# Print:
#
# Is File:
# <True or False>
#
# Expected Output:
#
# Is File:
# False

os.mkdir("Documents")

file_1 = "Documents"

check_file_1 = os.path.isfile(file_1)

print(f"Is File:", check_file_1)

