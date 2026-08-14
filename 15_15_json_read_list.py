import json

# Practice Question #15
#
# Import the built-in "json" module.
#
# Create a list named "products".
#
# Store the following dictionaries
# inside the list:
#
# Product 1
# Name  : Laptop
# Price : 95000
#
# Product 2
# Name  : Mouse
# Price : 2500
#
# Product 3
# Name  : Keyboard
# Price : 4500
#
# Create a JSON file named
# "products.json"
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
# "products_data".
#
# Print:
#
# 1. The list of products.
# 2. The data type.
#
# Expected Output:
#
# [
#     {"Name": "Laptop", "Price": 95000},
#     {"Name": "Mouse", "Price": 2500},
#     {"Name": "Keyboard", "Price": 4500}
# ]
#
# <class 'list'>


products = [
    {
        "Name" : "Laptop",
        "Price" : 95000
    },

    {
        "Name" : "Mouse",
        "Price" : 2500
    },

    {
        "Name" : "Keyboard",
        "Price" : 4500
    }
] # Store products in a list

with open ("products.json", "w") as z: # Open the JSON file in write mode.
    json.dump(products, z, indent=4) # Write the list to the JSON file with formatted indentation


with open ("products.json", "r") as y: # Open the JSON file in read mode.
    products_data = json.load(y) # Read the JSON data and store it in a variable
print(products_data) # Print the list of products
print(type(products_data)) # Print the data type of the list



