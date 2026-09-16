# Practice Question #31

# Import the built-in "re" module.

# Create a string:
# "Python 3 is fun!"
# Use re.findall() with the pattern "[a-z]"
# to find all lowercase letters in the string.
# Store the result in a variable named result.
# Print the result.
# Print the type of result.

# Expected output:
# ['y', 't', 'h', 'o', 'n', 'i', 's', 'f', 'u', 'n']
# <class 'list'>

import re

text = "Python 3 is fun!" # Store the string in a variable.
pattern = "[a-z]" # Create the pattern to find all lowercase characters. 
result = re.findall(pattern, text) # Find all lowercase characters using re.findall().
print(result) # Print the result.
print(type(result)) # Print the data type.



