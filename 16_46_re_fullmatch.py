# Practice Question #46

# Create a string:
# "Python"
# Create a pattern:
# r"Python"
# Use re.fullmatch() to check whether
# the entire string matches the pattern.
# Store the result in a variable named result.
# Print the result.
# Print the type of the result.

# Expected output:
# <re.Match object ...>
# <class 're.Match'>

import re

text = "Python" # Store the string in a variable.
pattern = r"Python" # Create a pattern.
result = re.fullmatch(pattern, text) # Use re.fullmatch() to check whether the entire string matches the pattern.
print(result) # Print the result.
print(type(result)) # Print the type of the result.


