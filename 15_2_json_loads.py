import json

# Practice Question #2
#
# Import the built-in "json" module.
#
# Create a JSON string named "employee_data".
#
# Store the following JSON data:
#
# {"Name": "Haider", "Age": 25, "Department": "IT"}
#
# Convert the JSON string into a Python dictionary
# using the appropriate function.
#
# Store the result in a variable named "employee".
#
# Print:
#
# 1. The Python dictionary.
# 2. The data type of the Python dictionary.
#
# Expected Output:
#
# {'Name': 'Haider', 'Age': 25, 'Department': 'IT'}
#
# <class 'dict'>


employee_data = '{"Name": "Haider", "Age": 25, "Department": "IT"}' # Store the JSON string in a variable

employee = json.loads(employee_data) # Convert the JSON string into a Python dictionary

print(employee) # Print the Python dictionary
 
print(type(employee)) # Print the data type of the Python dictionary



