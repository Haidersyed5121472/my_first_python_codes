# Practice Question #29

# Import the built-in "re" module.

# Create a string:
# "I am learning Python"
# Use re.search() with the pattern "Python$"
# to check whether the string ends with "Python".
# Store the result in a variable named result.
# Print the result.

# Expected output:
# <re.Match object ...>

import re

text = "I am learning Python" # Store the string in a variable.
pattern = r"Python$" # Create the pattern to check if string ends with given word.
result = re.search(pattern, text) # Check if string ends with "Python".
print(result) # Print the result.



