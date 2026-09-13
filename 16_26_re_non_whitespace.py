# Practice Question #26

# Import the built-in "re" module.

# Create a string:
# "Python is easy to learn."
# Use re.findall() with the pattern \S
# to find all non-whitespace characters in the string.
# Store the result in a variable named result.
# Print the result.
# Print the type of result.

# Expected output:
# ['P', 'y', 't', 'h', 'o', 'n', 'i', 's', 'e', 'a', 's', 'y', 't', 'o', 'l', 'e', 'a', 'r', 'n', '.']
# <class 'list'>

import re

text = "Python is easy to learn." # Store the string in a variable.
pattern = r"\S" # Create the pattern to find all non-whitespace characters.
result = re.findall(pattern, text) # Find all non-whitespace characters using re.findall().
print(result) # Print the result.
print(type(result)) # Print the data type.



