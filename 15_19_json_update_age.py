import json

# Practice Question #19
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
# Name : Sara
# Age  : 21
#
# Employee 3
# Name : Ahmed
# Age  : 24
#
# Create a JSON file named
# "employees_2.json"
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
# "employees_2_data".
#
# Find the employee
# whose name is:
#
# Ahmed
#
# Update:
#
# Age : 25
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
# Employee age updated successfully.
#
# Expected Output:
#
# Employee age updated successfully.
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
#         "Age": 25
#     }
# ]



employees = [
    {
        "Name" : "Ali",
        "Age" : 22
    },
    {
        "Name" : "Sara",
        "Age" : 21
    },
    {
        "Name" : "Ahmed",
        "Age" : 24
    }
] # Store employee records in a list.


with open ("employees_2.json", "w") as z: # Open the JSON file in write mode.
    json.dump(employees, z, indent=4) # Write the list to the JSON file with formatted indentation.


with open ("employees_2.json", "r") as y: # Open the JSON file in read mode.
    employees_2_data = json.load(y) # Read the JSON data and store it in a variable.


for i in employees_2_data: # Loop through the list.
    if i["Name"] == "Ahmed": # Check whether the employee's name is Ahmed.
        i["Age"] = 25 # Update the age of the matching employee.
        print(i) # Print the updated employee record.


with open ("employees_2.json", "w") as x: # Open the JSON file in write mode.
    json.dump(employees_2_data, x, indent=4) # Save the updated list to the JSON file.

print("Employee age updated successfully.") # Print the success message.



