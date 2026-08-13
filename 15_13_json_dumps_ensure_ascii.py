import json

# Practice Question #13
#
# Import the built-in "json" module.
#
# Create a dictionary named "city_info".
#
# Store the following data:
#
# City    : لاہور
# Country : پاکستان
# Language: اردو
#
# Convert the dictionary into a JSON string
# using the appropriate function.
#
# Format the JSON string with:
#
# 1. An indentation of 4 spaces.
# 2. Unicode characters displayed correctly.
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
#     "City": "لاہور",
#     "Country": "پاکستان",
#     "Language": "اردو"
# }
#
# <class 'str'>


city_info = {
    "City"    : "لاہور",
    "Country" : "پاکستان",
    "Language": "اردو"
} # Store city information in a dictionary


json_data = json.dumps(city_info, indent=4, ensure_ascii=False) # Convert the dictionary into a formatted JSON string

print(json_data) # Print the JSON string
print(type(json_data)) # Print the data type of the JSON string





