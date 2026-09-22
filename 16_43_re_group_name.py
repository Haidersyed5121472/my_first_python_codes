# Practice Question #43

# Create a string:
# "My name is Ali."
# Create a pattern using a group ()
# to match the name "Ali".
# Use re.search() to find the name.
# Store the result in a variable named result.
# Print the result.
# Print the matched group using group().
# Print the type of result.

# Expected output:
# <re.Match object ...>
# Ali
# <class 're.Match'>
# Note:
# Parentheses () are used to create a group in a regex pattern.

import re
 
text = "My name is Ali." # Store the string in a variable.
pattern = r"(Ali)" # Create the pattern to find the name.
result = re.search(pattern, text) # Use re.search() to find the name.
print(result) # Print the result.
print(result.group()) # Print the matched group using group().
print(type(result)) # Print the data type.


