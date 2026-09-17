# Practice Question #33

# Import the built-in "re" module.

# Create a string:
# "Python 123!"
# Use re.findall() with the pattern "[^a-z]"
# to find all characters that are NOT lowercase letters.
# Store the result in a variable named result.
# Print the result.
# Print the type of result.

# Expected output:
# ['P', ' ', '1', '2', '3', '!']
# <class 'list'>

import re

text = "Python 123!" # Store the string in a variable.
pattern = "[^a-z]" # Create the pattern to find all characters that are not lowercase letters.
result = re.findall(pattern, text) # Find all characters that are not lowercase letters using re.findall().
print(result) # Print the result.
print(type(result)) # Print the data type.


