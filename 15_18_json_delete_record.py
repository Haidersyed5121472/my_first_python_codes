import json

# Practice Question #18
#
# Import the built-in "json" module.
#
# Create a list named "students".
#
# Store the following dictionaries
# inside the list:
#
# Student 1
# Name   : Ali
# Age    : 22
# Course : Python
#
# Student 2
# Name   : Sara
# Age    : 21
# Course : Data Science
#
# Student 3
# Name   : Ahmed
# Age    : 24
# Course : Machine Learning
#
# Create a JSON file named
# "students_2.json"
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
# "students_data".
#
# Remove the student
# whose name is:
#
# Sara
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
# Student record deleted successfully.
#
# Expected Output:
#
# Student record deleted successfully.
#
# Final JSON File:
#
# [
#     {
#         "Name": "Ali",
#         "Age": 22,
#         "Course": "Python"
#     },
#     {
#         "Name": "Ahmed",
#         "Age": 24,
#         "Course": "Machine Learning"
#     }
# ]


students = [
    {
        "Name" : "Ali",
        "Age" : 22,
        "Course" : "Python"
    },
    {
        "Name" : "Sara",
        "Age" : 21,
        "Course" : "Data Science"
    },
    {
        "Name" : "Ahmed",
        "Age" : 24,
        "Course" : "Machine Learning"
    }
] # Store student records in a list.

with open ("students_2.json", "w") as z: # Open the JSON file in write mode.
    json.dump(students, z, indent=4) # Write the list to the JSON file with formatted indentation.

with open ("students_2.json", "r") as y: # Open the JSON file in read mode.
    students_2_data = json.load(y) # Read the JSON data and store it in a variable.

for i in students_2_data: # Loop through the list.
    if i["Name"] == "Sara": # Check whether the student's name is Sara.
        students_2_data.remove(i) # Remove the matching student record from the list.
        print(i) # Print the removed student record.


with open ("students_2.json", "w") as x: # Open the JSON file in write mode.
    json.dump(students_2_data, x, indent=4) # Save the updated list to the JSON file.

print("Student record deleted successfully.") # Print the success message.



