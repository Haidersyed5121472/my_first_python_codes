# Practice Question #21

# Import the built-in "re" module.

# Create a string:
# "My age is 25 and my brother's age is 30."
# Use re.findall() with the pattern \d
# to find all individual digits in the string.
# Store the result in a variable named result.
# Print the result.
# Print the type of result.

# Expected output:
# ['2', '5', '3', '0']
# <class 'list'>

import re

text = "My age is 25 and my brother's age is 30." # Store the string in a variable.
pattern = r"\d" # Create the pattern to find the digits.
result = re.findall(pattern, text) # Find digits using re.findall().
print(result) # Print the result.
print(type(result)) # Print the data type.


