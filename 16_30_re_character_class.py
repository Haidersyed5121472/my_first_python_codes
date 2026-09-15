# Practice Question #30

# Import the built-in "re" module.

# Create a string:
# "I have a cat, a dog, and a cow."
# Use re.findall() with the pattern "[cd]"
# to find all occurrences of the letters "c" or "d".
# Store the result in a variable named result.
# Print the result.
# Print the type of result.

# Expected output:
# ['c', 'd', 'd', 'c']
# <class 'list'>

import re

text = "I have a cat, a dog, and a cow." # Store the string in a variable.
pattern = "[cd]" # Create the pattern to find given letters.
result = re.findall(pattern, text) # Find all occurrences of "c" and "d" using re.findall().
print(result) # Print the result.
print(type(result)) # Print the data type.


