# Practice Question #7

# Import the built-in "re" module.

# Create a variable named text.

# Store this value:
# "My age is 25 years."
# Use re.search() to search for the digit pattern:
# \d+
# Store the result in a variable named result.
# Print result.
# Then print the data type of result.

# Expected:
# A match object should be returned.
# <class 're.Match'>

import re

text = "My age is 25 years." # Store the string in a variable.
pattern = r"\d+" # Use \d+ to match one or more digits.
result = re.search(pattern, text) # Search for the digit.
print(result) # Print the result.
print(type(result)) # Print the data type.
