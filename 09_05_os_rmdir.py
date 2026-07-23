import os

# Practice Question # 1
#
# Create a folder named "Temp".
#
# Remove the "Temp" folder
# using os.rmdir().
#
# Print:
#
# Folder removed successfully.
#
# Expected Output:
#
# Folder removed successfully.

os.mkdir("Temp") # Create The Folder

os.rmdir("Temp") # Remove The Folder

print("Folder removed successfully.")


# Practice Question # 2
#
# Create a folder named "Test Folder".
#
# Print the list of files and folders
# in the current working directory.
#
# Remove the "Test Folder".
#
# Print the list of files and folders
# again after removing it.
#
# Expected Output:
#
# Before Removing:
# ['main.py', 'Test Folder', 'notes.txt']
#
# After Removing:
# ['main.py', 'notes.txt']

os.mkdir("Test Folder") # Create the folder

a = os.listdir() # List of current directory
print(a)

os.rmdir("Test Folder") # Remove the folder

b = os.listdir() # List of current directory after removing the folder
print(b)