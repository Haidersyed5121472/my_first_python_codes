# Practice Question #32

# Import the built-in "re" module.

# Create a string:

# "Python Is Fun And Easy!"
# Use re.findall() with the pattern "[A-Z]"
# to find all uppercase letters in the string.
# Store the result in a variable named result.
# Print the result.
# Print the type of result.

# Expected output:
# ['P', 'I', 'F', 'A', 'E']
# <class 'list'>

import re

text = "Python Is Fun And Easy!" # Store the string in a variable.
pattern = "[A-Z]" # Create the pattern to find all uppercase letters.
result = re.findall(pattern, text) # Find all uppercase letters using re.findall().
print(result) # Print the result.
print(type(result)) # Print the data type.


