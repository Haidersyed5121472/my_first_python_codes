# Practice Question #35
#
# Import the built-in "json" module.
#
# Create a list named "employees_18".
#
# Store the following dictionaries inside the list:
#
# Employee 1
# Name : Ali
# Age : 22
# Department : IT
# Address:
#     City : Rawalpindi
#     Country : Pakistan
#
# Employee 2
# Name : Sara
# Age : 21
# Department : HR
# Address:
#     City : Islamabad
#     Country : Pakistan
#
# Employee 3
# Name : Ahmed
# Age : 24
# Department : IT
# Address:
#     City : Lahore
#     Country : Pakistan
#
# Employee 4
# Name : Ayesha
# Age : 26
# Department : Finance
# Address:
#     City : Karachi
#     Country : Pakistan
#
# Employee 5
# Name : Bilal
# Age : 23
# Department : IT
# Address:
#     City : Karachi
#     Country : Pakistan
#
# -----------------------------------
#
# Create a JSON file named
# "employees_18.json"
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
# Find all employees
# whose Department is "IT".
#
# Store them in a new list
# named "it_employees".
#
# Sort "it_employees"
# by Age in ascending order.
#
# -----------------------------------
#
# Open the same JSON file
# in write mode.
#
# Save the sorted IT employees
# back into the JSON file
# using an indentation of 4 spaces.
#
# Print:
#
# IT employees sorted successfully.
#
# Then print the complete
# updated list.
#
# Expected Output:
#
# IT employees sorted successfully.
#
# [
#     {
#         'Name': 'Ali',
#         'Age': 22,
#         'Department': 'IT',
#         'Address': {
#             'City': 'Rawalpindi',
#             'Country': 'Pakistan'
#         }
#     },
#     {
#         'Name': 'Bilal',
#         'Age': 23,
#         'Department': 'IT',
#         'Address': {
#             'City': 'Karachi',
#             'Country': 'Pakistan'
#         }
#     },
#     {
#         'Name': 'Ahmed',
#         'Age': 24,
#         'Department': 'IT',
#         'Address': {
#             'City': 'Lahore',
#             'Country': 'Pakistan'
#         }
#     }
# ]


import json


employees_18 = [
    {
        "Name" : "Ali",
        "Age" : 22,
        "Department" : "IT",
        "Address" :{
            "City" : "Rawalpindi",
            "Country" : "Pakistan"
        }
                
    },
    {
        "Name" : "Sara",
        "Age" : 21,
        "Department" : "HR",
        "Address":{
            "City" : "Islamabad",
            "Country" : "Pakistan"
        }
    },
    {
        "Name" : "Ahmed",
        "Age" : 24,
        "Department" : "IT",
        "Address":{
            "City" : "Lahore",
            "Country" : "Pakistan"
        }
    },
    {
        "Name" : "Ayesha",
        "Age" : 26,
        "Department" : "Finance",
        "Address":{
            "City" : "Karachi",
            "Country" : "Pakistan"
        }
    },
    {
        "Name" : "Bilal",
        "Age" : 23,
        "Department" : "IT",
        "Address":{
            "City" : "Karachi",
            "Country" : "Pakistan"
        }
    }
] # Store employee records in a list.


with open ("employees_18.json", "w") as z: # Open the JSON file in write mode.
    json.dump(employees_18, z, indent=4) # Write the list to the JSON file with formatted indentation.

with open ("employees_18.json", "r") as y: # Open the JSON file in read mode.
    employees_data = json.load(y) # Read the JSON data and store it in a variable.
    it_employees = [] # Create an empty list for IT employees.
    for i in employees_data: # Loop through all employee records.
        if i["Department"] == "IT": # Check if the employee belongs to the IT department.
            it_employees.append(i) # Add the IT employee to the list.

sort_age = sorted(it_employees, key=lambda i: i["Age"]) # Sort IT employees by age in ascending order.

with open ("employees_18.json", "w") as x: # Open the JSON file in write mode.
    json.dump(sort_age, x, indent=4) # Write the list to the JSON file with formatted indentation.

print("IT employees sorted successfully.") # Print the success message.
print(sort_age) # Print the sorted list.




