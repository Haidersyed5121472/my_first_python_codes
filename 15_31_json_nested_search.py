import json

# Practice Question #31
#
# Import the built-in "json" module.
#
# Create a list named "employees_14".
#
# Store the following dictionaries
# inside the list:
#
# Employee 1
# Name : Ali
# Age  : 22
# Address:
#     City    : Rawalpindi
#     Country : Pakistan
#
# Employee 2
# Name : Sara
# Age  : 21
# Address:
#     City    : Islamabad
#     Country : Pakistan
#
# Employee 3
# Name : Ahmed
# Age  : 24
# Address:
#     City    : Lahore
#     Country : Pakistan
#
# Employee 4
# Name : Ayesha
# Age  : 26
# Address:
#     City    : Karachi
#     Country : Pakistan
#
# -----------------------------------
#
# Create a JSON file named
# "employees_14.json"
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
# Search for the employee
# whose city is:
#
# Karachi
#
# Print the complete dictionary
# of that employee.
#
# Expected Output:
#
# {'Name': 'Ayesha', 'Age': 26,
#  'Address': {'City': 'Karachi', 'Country': 'Pakistan'}}


employees_14 = [
    {
        "Name" : "Ali",
        "Age" : 22,
        "Address" :{
            "City" : "Rawalpindi",
            "Country" : "Pakistan"
        }
                
    },
    {
        "Name" : "Sara",
        "Age" : 21,
        "Address":{
            "City" : "Islamabad",
            "Country" : "Pakistan"
        }
    },
    {
        "Name" : "Ahmed",
        "Age" : 24,
        "Address":{
            "City" : "Lahore",
            "Country" : "Pakistan"
        }
    },
    {
        "Name" : "Ayesha",
        "Age" : 26,
        "Address":{
            "City" : "Karachi",
            "Country" : "Pakistan"
        }
    }
] # Store employee records in a list. 


with open ("employees_14.json", "w") as z: # Open the JSON file in write mode.
    json.dump(employees_14, z, indent=4) # Write the list to the JSON file with formatted indentation.

with open ("employees_14.json", "r") as y: # Open the JSON file in read mode.
    employees_data = json.load(y) # Read the JSON data and store it in a variable.
    print(employees_data[3]) # Print the complete dictionary.
    



