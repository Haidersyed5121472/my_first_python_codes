import json

# Practice Question #29
#
# Import the built-in "json" module.
#
# Create a list named "employees_12".
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
# -----------------------------------
#
# Create a JSON file named
# "employees_12.json"
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
# Access and print:
#
# 1. Ali's city
# 2. Sara's city
# 3. Ahmed's city
#
# Expected Output:
#
# Rawalpindi
# Islamabad
# Lahore



employees_12 = [
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
    }
] # Store employee records in a list.

with open ("employees_12.json", "w") as z: # Open the JSON file in write mode. 
    json.dump(employees_12, z, indent=4) # Write the list to the JSON file with formatted indentation.

with open ("employees_12.json", "r") as y: # Open the JSON file in read mode.
    employees_data = json.load(y) # Read the JSON data and store it in a variable.

    print(employees_data[0]["Address"]["City"]) # Print employee 1's city using index.
    print(employees_data[1]["Address"]["City"]) # Print employee 2's city using index.
    print(employees_data[2]["Address"]["City"]) # Print employee 3's city using index.
            

