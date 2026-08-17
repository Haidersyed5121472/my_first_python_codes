import json

# Practice Question #20
#
# Import the built-in "json" module.
#
# Create a list named "employees_3".
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
# Create a JSON file named
# "employees_3_count.json"
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
# Count the total number
# of employee records.
#
# Store the result
# in a variable named
# "total_employees".
#
# Print:
#
# Total Employees: 4
#
# Expected Output:
#
# Total Employees: 4


employees_3 = [
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
    },
    {
        "Name" : "Ayesha",
        "Age" : 26
    }
] # Store employee records in a list.

with open ("employees_3_count.json", "w") as z: # Open the JSON file in write mode. 
    json.dump(employees_3, z, indent=4) # Write the list to the JSON file with formatted indentation.


with open ("employees_3_count.json", "r") as y: # Open the JSON file in read mode.
    employees_data = json.load(y) # Read the JSON data and store it in a variable.
    total_employees = len(employees_data) # Count the total number of employee records.
    print("Total Employees :",total_employees) # Print total number of employees.



    

