import json

# Practice Question #14
#
# Import the built-in "json" module.
#
# Create a dictionary named "student".
#
# Store the following data:
#
# Name : Ali
# Age  : 22
#
# Create a JSON file named
# "student_data.json"
# in write mode.
#
# Write the dictionary into the file
# using an indentation of 4 spaces.
#
# -----------------------------------
#
# Now open the same JSON file
# in read mode.
#
# Read the JSON data and store it
# in a variable named "student_data".
#
# Add a new key:
#
# Course : Python
#
# -----------------------------------
#
# Open the same JSON file again
# in write mode.
#
# Save the updated dictionary
# back into the file
# using an indentation of 4 spaces.
#
# Print:
#
# Student data updated successfully.
#
# Expected Output:
#
# Student data updated successfully.
#
# Final JSON File:
#
# {
#     "Name": "Ali",
#     "Age": 22,
#     "Course": "Python"
# }




student = {
    "Name" : "Ali",
    "Age" : 22
} # Store student information in a dictionary

with open ("student_data.json", "w") as z: # Open the JSON file in write mode
    json.dump(student, z, indent=4) # Write the dictionary to the JSON file with formatted indentation


with open("student_data.json", "r") as y: # Open the JSON file in read mode
    student_data = json.load(y) # Read the JSON data and store it in a variable
    student_data["Course"] = "Python" # Add a new key-value pair to the dictionary

with open("student_data.json", "w") as x: # Open the JSON file in write mode
    json.dump(student_data, x, indent=4) # Save the updated dictionary to the JSON file

print("Student data updated successfully.") # Print the success message




