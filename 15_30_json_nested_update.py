import json

# Practice Question #30
#
# Import the built-in "json" module.
#
# Create a list named "employees_13".
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
# "employees_13.json"
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
# Find the employee whose name is:
#
# Ahmed
#
# Update Ahmed's city to:
#
# Karachi
#
# -----------------------------------
#
# Open the same JSON file
# in write mode.
#
# Save the updated list
# back into the JSON file
# using an indentation of 4 spaces.
#
# Print:
#
# Employee city updated successfully.
#
# Expected Output:
#
# Employee city updated successfully.
#
# Final Ahmed Address:
#
# {
#     "City": "Karachi",
#     "Country": "Pakistan"
# }




employees_13 = [
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

with open ("employees_13.json", "w") as z: # Open the JSON file in write mode. 
    json.dump(employees_13, z, indent=4) # Write the list to the JSON file with formatted indentation.

with open ("employees_13.json", "r") as y: # Open the JSON file in read mode.
    employees_data = json.load(y) # Read the JSON data and store it in a variable.
    employees_data[2]["Address"]["City"] = "Karachi" # Update Ahmed's city using indexing.

with open ("employees_13.json", "w") as x: # Open the JSON file in write mode.
    json.dump(employees_data, x, indent=4) # Write the list to the JSON file with formatted indentation.

print("Employee city updated successfully.") # Print success message


