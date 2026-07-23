import os


# Practice Question # 1
#
# Import the built-in "os" module.
#
# Print the current working directory.
#
# Change the current working directory to another folder
# on your computer using os.chdir().
#
# Then print the current working directory again.
#
# Expected Output:
#
# Before Changing Directory:
# C:\Users\YourName\Desktop\Python Codes\Built-in Modules\OS
#
# After Changing Directory:
# C:\Users\YourName\Desktop

c_dir = os.getcwd()
print(c_dir)

chng_dir = os.chdir(r"C:\test folder")

cur_dir = os.getcwd()
print(cur_dir)


