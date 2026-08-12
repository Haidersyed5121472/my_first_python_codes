import json


# Practice Question #11
#
# Import the built-in "json" module.
#
# Create a dictionary named "product".
#
# Store the following data:
#
# Name     : Laptop
# Brand    : HP
# Price    : 95000
# In_Stock : True
#
# Convert the dictionary into a JSON string
# using the appropriate function.
#
# Format the JSON string with:
#
# 1. An indentation of 4 spaces.
#
# Store the result in a variable named
# "json_data".
#
# Print:
#
# 1. The formatted JSON string.
# 2. The data type of the JSON string.
#
# Expected Output:
#
# {
#     "Name": "Laptop",
#     "Brand": "HP",
#     "Price": 95000,
#     "In_Stock": true
# }
#
# <class 'str'>


product = {
    "Name"     : "Laptop",
    "Brand"    : "HP",
    "Price"    : 95000,
    "In_Stock" : True
} # Store product details in a dictionary

json_data = json.dumps(product, indent=4) # Convert the dictionary to a JSON string

print(json_data) # Print the JSON string
print(type(json_data)) # Print the data type of the JSON string


