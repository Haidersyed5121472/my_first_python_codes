# Practice Question #34
#
# Import the built-in "json" module.
#
# Create a list named "employees_17".
#
# Store the following dictionaries inside the list:
#
# Employee 1
# Name : Ali
# Age  : 22
# Department : IT
#
# Employee 2
# Name : Sara
# Age  : 21
# Department : HR
#
# Employee 3
# Name : Ahmed
# Age  : 24
# Department : IT
#
# Employee 4
# Name : Ayesha
# Age  : 26
# Department : Finance
#
# -----------------------------------
#
# Create a JSON file named
# "employees_17.json"
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
# "employees_data".
#
# Find the employee
# whose name is "Sara".
#
# Remove Sara's complete dictionary
# from the employees_data list.
#
# -----------------------------------
#
# Open the same JSON file
# in write mode.
#
# Save the updated list
# back into the JSON file
# using an indentation of 4 spaces.
#
# Print:
#
# Employee removed successfully.
#
# Then print the complete updated list.
#
# Expected Output:
#
# Employee removed successfully.
#
# [
#     {'Name': 'Ali', 'Age': 22, 'Department': 'IT'},
#     {'Name': 'Ahmed', 'Age': 24, 'Department': 'IT'},
#     {'Name': 'Ayesha', 'Age': 26, 'Department': 'Finance'}
# ]

import json

employees_17 = [
    {
        "Name" : "Ali",
        "Age" : 22,
        "Department" : "IT"
    },
    {
        "Name" : "Sara",
        "Age" : 21,
        "Department" : "HR"
    },
    {
        "Name" : "Ahmed",
        "Age" : 24,
        "Department" : "IT"
    },
    {
    "Name" : "Ayesha",
    "Age" : 26,
    "Department" : "Finance"
    }
] # Store employee records in a list.

with open("employees_17.json", "w") as z: # Open the JSON file in write mode.
    json.dump(employees_17, z, indent=4) # Write the list to the JSON file with formatted indentation.

with open("employees_17.json", "r") as y: # Open the JSON file in read mode.
    employees_data = json.load(y) # Read the JSON data and store it in a variable.
    for i in employees_data: # Loop through the list.
        if i["Name"] == "Sara": # Find the employee named "Sara".
            employees_data.remove(i) # Remove Sara's dictionary from the list.

with open("employees_17.json", "w") as x: # Open the JSON file in write mode.
    json.dump(employees_data, x, indent=4) # Write the list to the JSON file with formatted indentation.

print("Employee removed successfully.") # Print the success message.
print(employees_data) # Print the updated list.
            


