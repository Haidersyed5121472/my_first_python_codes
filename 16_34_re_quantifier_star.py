# Practice Question #34

# Import the built-in "re" module.

# Create a string:
# "gooooal"
# Use re.search() with the pattern "go*"
# to match "g" followed by zero or more "o" characters.
# Store the result in a variable named result.
# Print the result.

# Expected output:
# <re.Match object ...>

import re

text = "gooooal" # Store the string in a variable.
pattern = "go*" # Create the pattern to match "g" followed by zero or more "o" characters.
result = re.search(pattern, text) # Find "g" followed by zero or more "o" characters.
print(result) # Print the result.

