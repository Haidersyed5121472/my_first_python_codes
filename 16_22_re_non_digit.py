# Practice Question #22

# Import the built-in "re" module.

# Create a string:
# "My age is 25 and my brother's age is 30."
# Use re.findall() with the pattern \D
# to find all non-digit characters in the string.
# Store the result in a variable named result.
# Print the result.
# Print the type of result.

# Expected output should be a list containing
# all characters that are NOT digits.

import re

text = "My age is 25 and my brother's age is 30." # Store the string in a variable.
pattern = r"\D" # Create the pattern to find all non-digit characters.
result = re.findall(pattern, text) # Find all non-digit characters using re.findall().
print(result) # Print the result.
print(type(result)) # Print the data type.


