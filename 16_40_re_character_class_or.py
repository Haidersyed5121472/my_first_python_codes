# Practice Question #40

# Create a string:

# "I have a cat, a dog, and a cow."
# Create a pattern using a character class
# to find all occurrences of either "c" or "d".
# Use re.findall() to find all matches.
# Store the result in a variable named result.
# Print the result.
# Print the type of result.

# Expected output:
# ['c', 'd', 'd', 'c']
# Note:
# A character class [cd] matches either "c" or "d".

import re
 
text = "I have a cat, a dog, and a cow." # Store the string in a variable.
pattern = r"[cd]" # Create the pattern to find all occurrences of either "c" or "d".
result = re.findall(pattern, text) # Use re.findall() to find all matches.
print(result) # Print the result.
print(type(result)) # Print the data type.


