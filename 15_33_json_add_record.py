# Practice Question #33
#
# Import the built-in "json" module.
#
# Create a list named "employees_16".
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
# -----------------------------------
#
# Create a JSON file named
# "employees_16.json"
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
# Create a new employee dictionary:
#
# Name : Ayesha
# Age  : 26
# Department : Finance
#
# Add this new employee
# to the existing employees_data list.
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
# Employee added successfully.
#
# Then print the complete updated list.
#
# Expected Output:
#
# Employee added successfully.
#
# [
#     {'Name': 'Ali', 'Age': 22, 'Department': 'IT'},
#     {'Name': 'Sara', 'Age': 21, 'Department': 'HR'},
#     {'Name': 'Ahmed', 'Age': 24, 'Department': 'IT'},
#     {'Name': 'Ayesha', 'Age': 26, 'Department': 'Finance'}
# ]



import json

employees_16 = [
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
    }
] # Store employee records in a list.

with open("employees_16.json", "w") as z: # Open the JSON file in write mode.
    json.dump(employees_16, z, indent=4) # Write the list to the JSON file with formatted indentation.

with open("employees_16.json", "r") as y: # Open the JSON file in read mode.
    employees_data = json.load(y) # Read the JSON data and store it in a variable.

new_employee = {
    "Name" : "Ayesha",
    "Age" : 26,
    "Department" : "Finance"
} # Create a dictionary for the new employee.

employees_data.append(new_employee) # Add the new employee to the list.

with open("employees_16.json", "w") as x: # Open the JSON file in write mode.
    json.dump(employees_data, x, indent=4) # Write the list to the JSON file with formatted indentation.

print("Employee added successfully.") # Print the success message
print(employees_data) # Print the complete list of employees.



