import json

# Practice Question #21
#
# Import the built-in "json" module.
#
# Create a list named "employees_4".
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
# "employees_4_filter.json"
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
# whose age is:
#
# Greater than or equal to 23
#
# Print the complete dictionary
# of each matching employee.
#
# Expected Output:
#
# {'Name': 'Ahmed', 'Age': 24}
#
# {'Name': 'Ayesha', 'Age': 26}
#
# {'Name': 'Bilal', 'Age': 23}



employees_4 = [
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
    },
    {
        "Name" : "Bilal",
        "Age" : 23
    }
] # Store employee records in a list.


with open ("employees_4_filter.json", "w") as z: # Open the JSON file in write mode.
    json.dump(employees_4, z, indent=4) # Write the list to the JSON file with formatted indentation.


with open ("employees_4_filter.json", "r") as y: # Open the JSON file in read mode.
    employees_data = json.load(y) # Read the JSON data and store it in a variable.

    for i in employees_data: # Loop through the list of employees.
        if i["Age"] >= 23: # Check if the employee's age is 23 or greater.
            print(i) # Print the matching employee record.

