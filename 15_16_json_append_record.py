import json


# Practice Question #16
#
# Import the built-in "json" module.
#
# Create a list named "employees_1".
#
# Store the following dictionaries
# inside the list:
#
# Employee 1
# Name : Ali
# Age  : 22
#
# Employee 2
# Name : Sara
# Age  : 21
#
# Create a JSON file named
# "employees_1.json"
# in write mode.
#
# Write the list into the JSON file
# using an indentation of 4 spaces.
#
# -----------------------------------
#
# Open the same JSON file
# in read mode.
#
# Read the JSON data
# and store it
# in a variable named
# "employees_1_data".
#
# Create a new dictionary:
#
# Name : Ahmed
# Age  : 24
#
# Add the new dictionary
# to the existing list.
#
# -----------------------------------
#
# Open the same JSON file
# in write mode.
#
# Save the updated list
# back into the file
# using an indentation of 4 spaces.
#
# Print:
#
# Employee record added successfully.
#
# Expected Output:
#
# Employee record added successfully.
#
# Final JSON File:
#
# [
#     {
#         "Name": "Ali",
#         "Age": 22
#     },
#     {
#         "Name": "Sara",
#         "Age": 21
#     },
#     {
#         "Name": "Ahmed",
#         "Age": 24
#     }
# ]




employees_1 = [
    {
        "Name" : "Ali",
        "Age" : 22
    },
    {
        "Name" : "Sara",
        "Age" : 21
    }
] # Store employees information in a list.

with open ("employees_1.json", "w") as z: # Open the JSON file in write mode.
    json.dump(employees_1, z, indent=4) # Write the list to the JSON file with formatted indentation.

with open ("employees_1.json", "r") as y: # Open the JSON file in read mode.
    employees_1_data = json.load(y) # Read the JSON data and store it in a variable.

new_employee = {
        "Name" : "Ahmed",
        "Age" : 24
    } # Store the new employee data in a dictionary.

employees_1_data.append(new_employee) # Add the new employee to the existing list.

with open ("employees_1.json", "w") as x:  # Open the JSON file in write mode.
    json.dump(employees_1_data, x, indent=4) # Write the list to the JSON file with formatted indentation.

print("Employee record added successfully.") # Print the success message.
 


