import os

# Practice Question # 1
#
# Create a folder named "Python".
#
# Rename the folder from
# "Python" to "Python Basics"
# using os.rename().
#
# Print:
#
# Folder renamed successfully.
#
# Expected Output:
#
# Folder renamed successfully.

os.mkdir("Python") # Create the folder.

os.rename("Python", "Python Basics") # Rename the folder.

print("Folder renamed successfully.")


# Practice Question # 2
#
# Create a folder named "Temp".
#
# Rename the folder to "Backup".
#
# Print the list of files and folders
# in the current working directory.
#
# Expected Output:
#
# ['Backup', 'main.py', 'notes.txt']

os.mkdir("Temp") # Create the folder.

os.rename("Temp", "Backup") # Rename the folder.

a = os.listdir() # # List files and folders in the current directory.
print(a)