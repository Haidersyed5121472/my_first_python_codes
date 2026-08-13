import json

# Practice Question #12
#
# Import the built-in "json" module.
#
# Create a dictionary named "car".
#
# Store the following data:
#
# Model : Civic
# Brand : Honda
# Year  : 2024
# Color : White
#
# Convert the dictionary into a JSON string
# using the appropriate function.
#
# Format the JSON string with:
#
# 1. An indentation of 4 spaces.
# 2. Keys sorted in alphabetical order.
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
#     "Brand": "Honda",
#     "Color": "White",
#     "Model": "Civic",
#     "Year": 2024
# }
#
# <class 'str'>


car = {
    "Model" : "Civic",
    "Brand" : "Honda",
    "Year"  : 2024,
    "Color" : "White"
} # Store car details in a dictionary

# Convert the dictionary into a formatted JSON string with sorted keys
json_data = json.dumps(car, indent=4, sort_keys=True)

print(json_data) # Print the JSON string
print(type(json_data)) # Print the data type of the JSON string


