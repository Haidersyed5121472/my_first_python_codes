# Practice Question #16

# Import the built-in "re" module.

# Create a string:
# "Python,is;easy"
# Use re.split() to split the string
# wherever a comma (,) OR semicolon (;)
# occurs.
# Store the result in a variable named result.

# Print the result.
# Print the type of result.

# Expected output:
# ['Python', 'is', 'easy']
# <class 'list'>

import re

text = "Python,is;easy" # Store the string in a variable.
result = re.split(r"[,;]", text) # Split the string using re.split().
print(result) # Print the result.
print(type(result)) # Print the data type.

