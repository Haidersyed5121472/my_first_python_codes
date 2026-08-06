import pathlib

# Practice Question # 16
#
# Import the built-in "pathlib" module.
#
# Create a folder named:
#
# Temp
#
# Inside the folder, create a file:
#
# temporary.txt
#
# Then:
#
# 1. Print whether the file exists.
#
# 2. Delete the file using the unlink() method.
#
# 3. Print whether the file exists after deletion.
#
# 4. Print whether the folder still exists.
#
# Expected Output (similar to):
#
# Before deleting file:
# True
#
# After deleting file:
# False
#
# Folder still exists:
# True
#
# Methods / Properties to Practice:
#
# Path()
# joinpath()
# mkdir()
# touch()
# unlink()
# exists()


folder_path = pathlib.Path("Temp") # Path for folder

file_path = folder_path.joinpath("temporary.txt") # Path for file

folder_path.mkdir(exist_ok=True) # Create the folder using the Path object

file_path.touch(exist_ok=True) # Create the file using the Path object

print(file_path.exists()) # Check file exists using exists()

file_path.unlink() # Delete file using unlink()

print(file_path.exists()) # Check file exists using exists()

print(folder_path.exists()) # Check folder exists using exists()




