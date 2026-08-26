import json

# Practice Question #28
#
# Import the built-in "json" module.
#
# Create a list named "employees_11".
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
# Employee 4
# Name : Ayesha
# Age  : 26
#
# Employee 5
# Name : Bilal
# Age  : 23
#
# Create a JSON file named
# "employees_11.json"
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
# Sort the employee records
# by Age
# in ascending order.
#
# Store the sorted list
# in a variable named
# "sorted_employees".
#
# Print:
#
# Sorted Employees:
#
# Then print the complete
# sorted list.
#
# Expected Output:
#
# Sorted Employees:
#
# {'Name': 'Sara', 'Age': 21}
# {'Name': 'Ali', 'Age': 22}
# {'Name': 'Bilal', 'Age': 23}
# {'Name': 'Ahmed', 'Age': 24}
# {'Name': 'Ayesha', 'Age': 26}


employees_11 = [
    {
        "Name" : "Ali",
        "Age"  : 22
    },
    {
        "Name" : "Sara",
        "Age"  : 21
    },
    {
        "Name" : "Ahmed",
        "Age"  : 24
    },
    {
        "Name" : "Ayesha",
        "Age"  : 26
    },
    {
        "Name" : "Bilal",
        "Age"  : 23
    }
] # Store employee records in a list.


with open ("employees_11.json", "w") as z: # Open the JSON file in write mode.
    json.dump(employees_11, z, indent=4) # Write the list to the JSON file with formatted indentation.

with open ("employees_11.json", "r") as y: # Open the JSON file in read mode.
    employees_data = json.load(y) # Read the JSON data and store it in a variable.
    sorted_employees = sorted(employees_data, key=lambda i: i["Age"]) # Sort the list of employees by age using lambda.
print("Sorted Employees:")
print(sorted_employees) # Print the sorted list.



