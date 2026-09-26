
# Practice Question #51

# Create a string:
# "Ali_123"
# Create a pattern:
# r"^[A-Za-z0-9_]+$"
# Use re.fullmatch() to check whether
# the entire string contains only letters,
# digits, and underscores.
# Store the result in a variable named result.
# Print the result.
# Print the matched username using group().

# Expected output:
# <re.Match object ...>
# Ali_123

import re

text = "Ali_123" # Store the string in a variable.
pattern = r"^[A-Za-z0-9_]+$" # Create the pattern.
result = re.fullmatch(pattern, text) # Use re.fullmatch() to check whether the entire string contains only letters, digits, and underscores.
print(result) # Print the result.
print(result.group()) # Print the matched username using group().


