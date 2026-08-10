import json

# Practice Question #7
#
# Import the built-in "json" module.
#
# Create a dictionary named "student".
#
# Store the following data:
#
# Name    : Ali
# City    : لاہور
# Country : پاکستان
#
# Create a JSON file named "student_info.json"
# in write mode.
#
# Write the dictionary into the JSON file
# using the appropriate function.
#
# Format the JSON file with:
#
# 1. An indentation of 4 spaces.
# 2. Unicode characters displayed correctly.
#
# Print:
#
# Student information saved successfully.
#
# Expected Output:
#
# Student information saved successfully.
#
# After running the program,
# the file "student_info.json"
# should look similar to:
#
# {
#     "Name": "Ali",
#     "City": "لاہور",
#     "Country": "پاکستان"
# }


student = {
    "Name"    : "Ali",
    "City"    : "لاہور",
    "Country" : "پاکستان"
} # Store student information in a dictionary

with open ("student_info.json", "w") as z: # Open the JSON file in write mode
    json.dump(student, z, indent=4, ensure_ascii=False) # Write the dictionary to the JSON file with formatted indentation and Unicode characters
print("Student information saved successfully.") # Print a success message



# In order to print urdu text i wrote another code below

student = {
    "Name"    : "Ali",
    "City"    : "لاہور",
    "Country" : "پاکستان"
} # Store student information in a dictionary

with open ("student_info.json", "w", encoding="utf-8") as z: # Open the JSON file in write mode using UTF-8 encoding
    json.dump(student, z, indent=4, ensure_ascii=False) # Write the dictionary to the JSON file with formatted indentation and Unicode characters
print("Student information saved successfully.") # Print a success message



