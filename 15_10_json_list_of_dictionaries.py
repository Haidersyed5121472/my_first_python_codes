import json

# Practice Question #10
#
# Import the built-in "json" module.
#
# Create a list named "employees".
#
# Store the following dictionaries
# inside the list:
#
# Employee 1
# Name : Ali
# Age  : 22
#
# Employee 2
# Name : Ahmed
# Age  : 24
#
# Employee 3
# Name : Sara
# Age  : 21
#
# Create a JSON file named
# "employees.json"
# in write mode.
#
# Write the list into the JSON file
# using the appropriate function.
#
# Format the JSON file with:
#
# 1. An indentation of 4 spaces.
#
# Print:
#
# Employees data saved successfully.
#
# Expected Output:
#
# Employees data saved successfully.
#
# After running the program,
# the file should look similar to:
#
# [
#     {
#         "Name": "Ali",
#         "Age": 22
#     },
#     {
#         "Name": "Ahmed",
#         "Age": 24
#     },
#     {
#         "Name": "Sara",
#         "Age": 21
#     }
# ]


employees = [
    {"Name" : "Ali", "Age" : 22},
    {"Name" : "Ahmed", "Age" : 24},
    {"Name" : "Sara","Age" : 21}
] # Store employee records in a list of dictionaries

with open ("employees.json", "w") as z: # Open the JSON file in write mode
    json.dump(employees, z, indent=4) # Write the list to the JSON file with formatted indentation

print("Employees data saved successfully.") # Print a success message


