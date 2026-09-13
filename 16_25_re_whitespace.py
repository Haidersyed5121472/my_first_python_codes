
# Practice Question #25

# Import the built-in "re" module.

# Create a string:
# "Python is easy to learn."

# Use re.findall() with the pattern \s
# to find all whitespace characters in the string.
# Store the result in a variable named result.
# Print the result.
# Print the type of result.

# Expected output:
# [' ', ' ', ' ', ' ']
# <class 'list'>

import re

text = "Python is easy to learn." # Store the string in a variable.
pattern = r"\s" # Create the pattern to find whitespaces. 
result = re.findall(pattern, text) # Find the whitespaces using re.findall().
print(result) # Print the result.
print(type(result)) # Print the data type.




