import pathlib

# Practice Question # 17
#
# Import the built-in "pathlib" module.
#
# Create the following folder structure:
#
# EmptyFolder
#
# Requirements:
#
# 1. Create the folder.
#
# 2. Print whether the folder exists.
#
# 3. Delete the folder using the rmdir() method.
#
# 4. Print whether the folder exists after deletion.
#
# Expected Output (similar to):
#
# Before deleting folder:
# True
#
# After deleting folder:
# False
#
# Methods / Properties to Practice:
#
# Path()
# mkdir()
# rmdir()
# exists()


folder_path = pathlib.Path("EmptyFolder") # Path for folder

folder_path.mkdir(exist_ok=True) # Create the folder using Path object

print(folder_path.exists()) # Check whether the folder exists using the .exists() method

folder_path.rmdir() # Delete the folder using the .rmdir() method

print(folder_path.exists()) # Check whether the folder exists using the .exists() method



