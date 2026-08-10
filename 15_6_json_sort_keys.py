import json

# Practice Question #6
#
# Import the built-in "json" module.
#
# Create a dictionary named "book".
#
# Store the following data:
#
# Title  : Python Basics
# Author : Ahmed
# Pages  : 350
# Price  : 1500
#
# Create a JSON file named "book.json"
# in write mode.
#
# Write the dictionary into the JSON file
# using the appropriate function.
#
# Format the JSON file with:
#
# 1. An indentation of 4 spaces.
# 2. Keys sorted in alphabetical order.
#
# Print:
#
# Book data saved successfully.
#
# Expected Output:
#
# Book data saved successfully.
#
# After running the program,
# the file "book.json"
# should look similar to:
#
# {
#     "Author": "Ahmed",
#     "Pages": 350,
#     "Price": 1500,
#     "Title": "Python Basics"
# }


book = {
    "Title" : "Python Basics",
    "Author" : "Ahmed",
    "Pages" : 350,
    "Price" : 1500
} # Store book information in a dictionary

with open ("book.json", "w") as z: # Open the JSON file in write mode
    json.dump(book, z, indent=4, sort_keys=True) # Write the dictionary to the JSON file with formatted indentation and sorted keys
print("Book data saved successfully.") # Print a success message

