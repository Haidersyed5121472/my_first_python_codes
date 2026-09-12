# Practice Question #24

# Import the built-in "re" module.

# Create a string:
# "Python 3.14 is easy!"
# Use re.findall() with the pattern \W
# to find all non-word characters in the string.
# Store the result in a variable named result.
# Print the result.
# Print the type of result.

# Expected output:
# [' ', '.', ' ', ' ', '!']
# <class 'list'>

import re

text = "Python 3.14 is easy!" # Store the string in a variable.
pattern = r"\W" # Create the pattern to find non-word characters.
result = re.findall(pattern, text) # Find all non-word characters using re.findall().
print(result) # Print the result.
print(type(result)) # Print the data type.

