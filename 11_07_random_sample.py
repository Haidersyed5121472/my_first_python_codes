import random

# Practice Question #1
#
# Import the built-in "random" module.
#
# Create a list containing
# the following programming languages:
#
# Python
# Java
# C++
# JavaScript
# Go
#
# Select three unique random languages
# using the appropriate function.
#
# Store the result in a variable.
#
# Print:
#
# 1. The selected languages.
# 2. The data type of the returned value.
#
# Expected Output:
#
# ['Python', 'Go', 'Java']
#
# <class 'list'>
#
# OR
#
# ['C++', 'JavaScript', 'Python']
#
# <class 'list'>
#
# (The selected languages will be different each time.
# Duplicate languages are not allowed.)

lang = ["Python", "Java", "C++", "JavaScript", "Go"]

rand_selection = random.sample(lang, k=3)

print(rand_selection)

print(type(rand_selection))


# Practice Question #2
#
# Import the built-in "random" module.
#
# Create a tuple containing
# the following employee IDs:
#
# EMP101
# EMP102
# EMP103
# EMP104
# EMP105
# EMP106
#
# Select four unique employee IDs
# using the appropriate function.
#
# Store the result in a variable.
#
# Print:
#
# 1. The selected employee IDs.
#
# Then:
#
# Check whether "EMP101"
# is present in the selected employee IDs.
#
# If it is present, print:
#
# EMP101 Selected
#
# Otherwise, print:
#
# EMP101 Not Selected
#
# Expected Output:
#
# ['EMP106', 'EMP101', 'EMP104', 'EMP102']
# EMP101 Selected
#
# OR
#
# ['EMP103', 'EMP106', 'EMP105', 'EMP104']
# EMP101 Not Selected
#
# (The selected employee IDs will be different each time.
# Duplicate employee IDs are not allowed.)

emp = ("EMP101", "EMP102", "EMP103", "EMP104", "EMP105", "EMP106")

selection = random.sample(emp, k=4)

print(selection)

if "EMP101" in selection :
    print("EMP101 Selected")
else:
    print("EMP101 Not Selected")


