# Practice Question #37

# Create a string:

# "I have 123 apples and 45 oranges."
# Create a pattern using the "{n}" quantifier
# to match exactly 3 digits together.
# Use re.findall() to find all matches.
# Store the result in a variable named result.
# Print the result.
# Print the type of result.

# Expected output:
# ['123']
# Note:
# The "{n}" quantifier matches exactly n occurrences
# of the preceding character or pattern.

import re

text = "I have 123 apples and 45 oranges." # Store the string in a variable.
pattern = r"\d{3}" # Create the pattern to match exactly 3 digits together.
result = re.findall(pattern, text) # Find all matches using re.findall().
print(result) # Print the result.
print(type(result)) # Print the data type.


