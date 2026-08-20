import json

# Practice Question #27
#
# Import the built-in "json" module.
#
# Create a list named "employees_10".
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
# "employees_10.json"
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
# Calculate the average age
# of all employees.
#
# Store the result
# in a variable named
# "average_age".
#
# Print:
#
# Average Age:
# 23.2
#
# Expected Output:
#
# Average Age:
# 23.2



employees_10 = [
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


with open ("employees_10.json", "w") as z: # Open the JSON file in write mode.
    json.dump(employees_10, z, indent=4) # Write the list to the JSON file with formatted indentation.

with open ("employees_10.json", "r") as y: # Open the JSON file in read mode.
    employees_data = json.load(y) # Read the JSON data and store it in a variable.


    total_age = 0 # Create a variable to store the total age of employees.
    for i in employees_data: # Loop through the list.
        total_age += i["Age"] # Add each employee's age to the total age.
    total_employee = len(employees_data) # Count the total number of employees using the len() method.
    average_age = total_age/total_employee # Store average age of employees in a variable.
    print("Total Employee: ",total_employee) # Print total employees.
    print("Total Age: ",total_age) # Print total age.
    print("Average Age:") 
    print(average_age) # Print the average age of employees.

 

