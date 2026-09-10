# Practice Question #20

# Import the built-in "re" module.

# Create a string:
# "Ali is 25 years old and Haider is 30 years old."
# Use re.findall() with a regex pattern
# to find all names in the string.
# Store the result in a variable named result.

# Print the result.
# Print the type of result.

# Expected output:
# ['Ali', 'Haider']
# <class 'list'>


import re

text = "Ali is 25 years old and Haider is 30 years old." # Store the string in a variable.
pattern = r"[A-Z]+[a-z]+" # Create the pattern to find names.
result = re.findall(pattern, text) # Find all names using re.findall().
print(result) # Print the result.
print(type(result)) # Print the data type.




