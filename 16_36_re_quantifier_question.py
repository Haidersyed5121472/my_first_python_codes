# Practice Question #36

# Create a string:

# "color colour"
# Create a pattern using the "?" quantifier
# to match both "color" and "colour".
# Use re.findall() to find all matches.
# Store the result in a variable named result.
# Print the result.
# Print the type of result.

# Expected output:
# ['color', 'colour']
# Note:
# The "?" quantifier means zero or one occurrence
# of the preceding character.

import re

text = "color colour" # Store the string in a variable.
pattern = "colou?r" # Create the pattern to match both "color" and "colour".
result = re.findall(pattern, text) # Match both "color" and "colour" using re.findall().
print(result) # Print the result.
print(type(result)) # Print the data type.

