import json

# Practice Question #25
#
# Import the built-in "json" module.
#
# Create a list named "employees_8".
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
# "employees_8.json"
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
# with the highest age.
#
# Store the complete dictionary
# in a variable named
# "oldest_employee".
#
# Print:
#
# Oldest Employee:
#
# {'Name': 'Ayesha', 'Age': 26}
#
# Expected Output:
#
# Oldest Employee:
# {'Name': 'Ayesha', 'Age': 26}


employees_8 = [
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


with open("employees_8.json", "w") as z: # Open the JSON file in write mode.
    json.dump(employees_8, z, indent=4) # Write the list to the JSON file with formatted indentation.

with open("employees_8.json", "r") as y: # Open the JSON file in read mode.
    employees_data = json.load(y) # Read the JSON data and store it in a variable.

    oldest_employee = employees_data[0] # Assume the first employee is the oldest initially.
    for i in employees_data: # Loop through the list.
            if i["Age"] > oldest_employee["Age"]: # Compare the ages of employees.
                 oldest_employee = i # Update the oldest employee.
    print("Oldest Employee :")             
    print(oldest_employee) # Print the oldest employee.



