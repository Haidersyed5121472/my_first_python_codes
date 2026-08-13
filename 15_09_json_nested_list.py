import json

# Practice Question #9
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
# Create a list named "subjects".
#
# Store the following subjects:
#
# Python
# SQL
# Excel
#
# Add the "subjects" list
# inside the "student" dictionary
# using the key:
#
# Subjects
#
# Create a JSON file named
# "student_subjects.json"
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
# Student subjects saved successfully.
#
# Expected Output:
#
# Student subjects saved successfully.
#
# After running the program,
# the file should look similar to:
#
# {
#     "Name": "Ali",
#     "Age": 22,
#     "Subjects": [
#         "Python",
#         "SQL",
#         "Excel"
#     ]
# }



student = {
    "Name" : "Ali",
    "Age" : 22
}


subject = ["Python", "SQL", "Excel"]

student["Subjects"] = subject

with open ("student_subjects.json", "w") as z:
    json.dump(student, z, indent=4)

print("Student subjects saved successfully.")




