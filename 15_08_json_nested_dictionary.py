import json

# Practice Question #8
#
# Import the built-in "json" module.
#
# Create a dictionary named "employee".
#
# Store the following data:
#
# Name : Haider
# Age  : 25
#
# Create another dictionary named "address".
#
# Store the following data:
#
# City    : Rawalpindi
# Country : Pakistan
#
# Add the "address" dictionary
# inside the "employee" dictionary
# using the key:
#
# Address
#
# Create a JSON file named
# "employee_details.json"
# in write mode.
#
# Write the dictionary into the JSON file
# using the appropriate function.
#
# Format the JSON file with:
#
# 1. An indentation of 4 spaces.
#
# Print:
#
# Employee details saved successfully.
#
# Expected Output:
#
# Employee details saved successfully.
#
# After running the program,
# the file should look similar to:
#
# {
#     "Name": "Haider",
#     "Age": 25,
#     "Address": {
#         "City": "Rawalpindi",
#         "Country": "Pakistan"
#     }
# }



employee = {
    "Name" : "Haider",
    "Age" : 25
}

address = {
    "City" : "Rawalpindi",
    "Country" : "Pakistan"
}

employee["Address"] = address

with open ("employee_details.json", "w") as z:
    json.dump(employee, z, indent=4)

print("Employee details saved successfully.")



