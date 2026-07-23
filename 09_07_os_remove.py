import os

# Practice Question # 1
#
# Create a file named "temp.txt".
#
# Write the text:
# "Temporary File"
# into the file.
#
# Delete the file using os.remove().
#
# Print:
#
# File removed successfully.
#
# Expected Output:
#
# File removed successfully.

z = open("temp.txt", "w") # Create the file (txt file).
file = z.write("Temporary File") # write a text in file.
print(file)

z.close()

os.remove("temp.txt") # Remove txt file.

print("File removed successfully.")


# Practice Question # 2
#
# Create a file named "notes.txt".
#
# Write the text:
# "Python Built-in Modules"
# into the file.
#
# Print the list of files
# in the current working directory.
#
# Delete the file using os.remove().
#
# Print:
#
# File removed successfully.
#
# Expected Output:
#
# ['main.py', 'notes.txt']
#
# File removed successfully.

with open("notes.txt", "w") as z: # create the file (txt file).
    z.write("Python Built-in Modules") # write a text in file.

files_list = os.listdir() # Files list in current directory.
print(files_list)

os.remove("notes.txt") # Remove the file (txt file).

print("File removed successfully.")
