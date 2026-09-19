# Practice Question #38

# Create a string:

# "I have 2 apples, 123 oranges, and 4567 bananas."
# Create a pattern using the "{n,m}" quantifier
# to match numbers containing 2 to 3 digits.
# Use re.findall() to find all matches.
# Store the result in a variable named result.
# Print the result.
# Print the type of result.

# Expected output:
# ['123', '456']
# Note:
# The "{n,m}" quantifier matches between n and m
# occurrences of the preceding character or pattern.

import re

text = "I have 2 apples, 123 oranges, and 4567 bananas." # Store the string in a variable.
pattern = r"\d{2,3}" # Create the pattern to match numbers containing 2 to 3 digits.
result = re.findall(pattern, text) # Use re.findall() to find all matches.
print(result) # Print the result.
print(type(result)) # Print the data type.


