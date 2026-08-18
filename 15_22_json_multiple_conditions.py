import json

# Practice Question #22
#
# Import the built-in "json" module.
#
# Create a list named "employees_5".
#
# Store the following dictionaries
# inside the list:
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
# Employee 5
# Name : Bilal
# Age  : 23
# Department : IT
#
# Create a JSON file named
# "employees_5.json"
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
# Print only those employee records
# who satisfy BOTH conditions:
#
# 1. Department is "IT"
# 2. Age is greater than or equal to 23
#
# Print the complete dictionary
# of each matching employee.
#
# Expected Output:
#
# {'Name': 'Ahmed', 'Age': 24, 'Department': 'IT'}
#
# {'Name': 'Bilal', 'Age': 23, 'Department': 'IT'}


employees_5 = [
    {
        "Name" : "Ali",
        "Age"  : 22,
        "Department" : "IT"
    },
    {
        "Name" : "Sara",
        "Age"  : 21,
        "Department" : "HR"
    },
    {
        "Name" : "Ahmed",
        "Age"  : 24,
        "Department" : "IT"
    },
    {
        "Name" : "Ayesha",
        "Age"  : 26,
        "Department" : "Finance"
    },
    {
        "Name" : "Bilal",
        "Age"  : 23,
        "Department" : "IT"
    }
] # Store employee records in a list.

with open ("employees_5.json", "w") as z: # Open the JSON file in write mode.
    json.dump(employees_5, z, indent=4) # Write the list to the JSON file with formatted indentation.

with open ("employees_5.json", "r") as y: # Open the JSON file in read mode.
    employees_data = json.load(y) # Read the JSON data and store it in a variable.

    for i in employees_data: # Loop through the list of employees.
        # Check whether the employee belongs to the IT department and is at least 23 years old.
        if  i["Age"] >= 23 and i["Department"] == "IT":
            print(i) # Print the matching employee record.

