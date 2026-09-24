# Practice Question #47

# Create a string:
# "Python is easy."
# Create a pattern:
# r"Python"
# Use re.fullmatch() to check whether
# the entire string matches the pattern.
# Store the result in a variable named result.
# Print the result.
# Print the type of the result.

# Expected output:
# None
# <class 'NoneType'>


import re

text = "Python is easy." # Store the string in a variable.
pattern = r"Python" # Create the pattern.
result = re.fullmatch(pattern, text) # Use re.fullmatch() to check whether the entire string matches the pattern.
print(result) # Print the result.
print(type(result)) # Print the data type.

