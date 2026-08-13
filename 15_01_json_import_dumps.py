import json


# Practice Question #1
#
# Import the built-in "json" module.
#
# Create a dictionary named "student".
#
# Store the following data:
#
# Name : Ali
# Age  : 22
# City : Lahore
#
# Convert the dictionary into a JSON string
# using the appropriate function.
#
# Store the result in a variable named "json_data".
#
# Print:
#
# 1. The JSON string.
# 2. The data type of the JSON string.
#
# Expected Output:
#
# {"Name": "Ali", "Age": 22, "City": "Lahore"}
#
# <class 'str'>

student = {
    "Name" : "Ali",
    "Age" : 22 ,
    "City" : "Lahore"
} # Store student information in a dictionary

json_data = json.dumps(student) # Convert the dictionary into a JSON string

print(json_data) # Print the JSON string

print(type(json_data)) # Print the data type of the JSON string




