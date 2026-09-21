
# Practice Question #42

# Create a string:
# "My phone number is 03001234567."
# Create a pattern using a group ()
# to match the complete phone number.
# Use re.search() to find the phone number.
# Store the result in a variable named result.
# Print the result.
# Print the matched group using group().
# Print the type of result.

# Expected output:
# <re.Match object ...>
# 03001234567
# <class 're.Match'>
# Note:
# Parentheses () are used to create a group in a regex pattern.

import re
 
text = "My phone number is 03001234567." # Store the string in a variable.
pattern = r"(\d{11})" # Create the pattern to match the complete phone number.
result = re.search(pattern, text) # Use re.search() to find the phone number.
print(result) # Print the result.
print(result.group()) # Print the matched group using group().
print(type(result)) # Print the data type of result.


