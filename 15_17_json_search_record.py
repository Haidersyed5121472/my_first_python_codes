import json

# Practice Question #17
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
# "students.json"
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
# Search for the student
# whose name is:
#
# Ahmed
#
# Print the complete dictionary
# of that student.
#
# Expected Output:
#
# {
#     "Name": "Ahmed",
#     "Age": 24,
#     "Course": "Machine Learning"
# }


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

with open ("students.json", "w") as z: # Open the JSON file in write mode.
    json.dump(students, z, indent=4) # Write the list to the JSON file with formatted indentation.

with open ("students.json", "r") as y: # Open the JSON file in read mode.
    students_data = json.load(y) # Read the JSON data and store it in a variable.


for i in students_data: # Loop through the list.
     if i["Name"] == "Ahmed": # Check whether the student's name is Ahmed.
         print(i) # Print the matching student record.




