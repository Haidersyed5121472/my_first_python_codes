import json

# Practice Question #24
#
# Import the built-in "json" module.
#
# Create a list named "employees_7".
#
# Store the following dictionaries
# inside the list:
#
# Employee 1
# Name : Ali
# Department : IT
#
# Employee 2
# Name : Sara
# Department : HR
#
# Employee 3
# Name : Ahmed
# Department : IT
#
# Employee 4
# Name : Ayesha
# Department : Finance
#
# Employee 5
# Name : Bilal
# Department : IT
#
# Employee 6
# Name : Hina
# Department : HR
#
# Create a JSON file named
# "employees_7.json"
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
# Count how many employees
# belong to the IT department.
#
# Store the result
# in a variable named
# "it_count".
#
# Print:
#
# Total IT Employees: 3
#
# Expected Output:
#
# Total IT Employees: 3


employees_7 = [
    {
        "Name" : "Ali",
        "Department" : "IT"
    },
    {
        "Name" : "Sara",
        "Department" : "HR"
    },
    {
        "Name" : "Ahmed",
        "Department" : "IT"
    },
    {
        "Name" : "Ayesha",
        "Department" : "Finance"
    },
    {
        "Name" : "Bilal",
        "Department" : "IT"
    },
    {
        "Name" : "Hina",
        "Department" : "HR"
    }
] # Store employee records in a list.


with open ("employees_7.json", "w") as z: # Open the JSON file in write mode.
    json.dump(employees_7, z, indent=4) # Write the list to the JSON file with formatted indentation.

with open ("employees_7.json", "r") as y: # Open the JSON file in read mode.
    employees_data = json.load(y) # Read the JSON data and store it in a variable.

    it_count = 0 # Create a counter variable.
    for i in employees_data: # Loop through the list of employees.
        if i["Department"] == "IT": # Check whether the employee belongs to the IT department.
            it_count += 1 # Increase the IT employee count by 1.
    print("Total IT Employees :",it_count) # Print the total number of IT employees.


 
