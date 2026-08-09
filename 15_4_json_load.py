import json

# Practice Question #4
#
# Import the built-in "json" module.
#
# Open the JSON file named "student.json"
# in read mode.
#
# Read the JSON data from the file
# using the appropriate function.
#
# Store the result in a variable named "student_data".
#
# Print:
#
# 1. The Python dictionary.
# 2. The data type of the Python dictionary.
#
# Expected Output:
#
# {'Name': 'Sara', 'Age': 21, 'Course': 'Python'}
#
# <class 'dict'>


with open ("student.json", "r") as z: # Open the JSON file named "student.json" in read mode.
    student_data = json.load(z) # Store the JSON data in a variable
    print(student_data) # Print the Python dictionary
    print(type(student_data)) # Print the data type of the Python dictionary


