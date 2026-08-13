import json

# Practice Question #3
#
# Import the built-in "json" module.
#
# Create a dictionary named "student".
#
# Store the following data:
#
# Name  : Sara
# Age   : 21
# Course: Python
#
# Create a JSON file named "student.json"
# in write mode.
#
# Write the dictionary into the JSON file
# using the appropriate function.
#
# Print:
#
# Data saved successfully.
#
# Expected Output:
#
# Data saved successfully.
#
# After running the program,
# the file "student.json"
# should contain:
#
# {"Name": "Sara", "Age": 21, "Course": "Python"}


student = {
    "Name" : "Sara" ,
    "Age" : 21 ,
    "Course" : "Python"
} # Store student information in a dictionary

with open ("student.json", "w") as z: # Open the JSON file in write mode
    json.dump(student, z) # Save the dictionary into the JSON file
    print("Data saved successfully.") # Print a success message



