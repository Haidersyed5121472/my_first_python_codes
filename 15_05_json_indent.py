import json

# Practice Question #5
#
# Import the built-in "json" module.
#
# Create a dictionary named "employee".
#
# Store the following data:
#
# Name       : Haider
# Age        : 25
# Department : IT
# Salary     : 85000
#
# Create a JSON file named "employee.json"
# in write mode.
#
# Write the dictionary into the JSON file
# using the appropriate function.
#
# Format the JSON file with an indentation
# of 4 spaces.
#
# Print:
#
# Employee data saved successfully.
#
# Expected Output:
#
# Employee data saved successfully.
#
# After running the program,
# the file "employee.json"
# should look similar to:
#
# {
#     "Name": "Haider",
#     "Age": 25,
#     "Department": "IT",
#     "Salary": 85000
# }


employee = {
    "Name" : "Haider",
    "Age" : 25,
    "Department" : "IT",
    "Salary" : 85000
} # Create dictionary in a variable (employee).

with open ("employee.json", "w") as z: # Store employee information in a dictionary 
    json.dump(employee, z, indent=4) # Open the JSON file in write mode
    print("Employee data saved successfully.") # Print a success message


