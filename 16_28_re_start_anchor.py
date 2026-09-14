# Practice Question #28

# Import the built-in "re" module.
# Create a string:
# "Python is easy to learn."
# Use re.search() with the pattern "^Python"
# to check whether the string starts with "Python".
# Store the result in a variable named result.
# Print the result.

# Expected output:
# <re.Match object ...>

import re

text = "Python is easy to learn." # Store the string in a variable.
pattern = r"^Python" # Create the pattern to check if string starts with given word.
result = re.search(pattern, text) # Check if string starts with given word using re.search.
print(result) # Print the result.



