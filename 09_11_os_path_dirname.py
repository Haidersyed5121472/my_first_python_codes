import os

# Practice Question # 1
#
# Create a variable containing
# the following path:
#
# C:\Users\Alli computer\Desktop\Python\Built-in Modules\OS Module\notes.txt
#
# Store the directory path
# in another variable.
#
# Print the result.
#
# Expected Output:
#
# C:\Users\Alli computer\Desktop\Python\Built-in Modules\OS Module

path = r"C:\Users\Alli computer\Desktop\Python\Built-in Modules\OS Module\notes.txt"

t = os.path.dirname(path)

print(t)


# Practice Question # 2
#
# Create a variable containing
# the following path:
#
# C:\Users\Alli computer\Desktop\Python\Projects\Reports\report.pdf
#
# Print:
#
# 1. The directory path.
# 2. The last part of the path.
#
# Expected Output:
#
# C:\Users\Alli computer\Desktop\Python\Projects\Reports
#
# report.pdf

path_1 = r"C:\Users\Alli computer\Desktop\Python\Projects\Reports\report.pdf"

d = os.path.dirname(path_1)
print(d)

c = os.path.basename(path_1)
print(c)