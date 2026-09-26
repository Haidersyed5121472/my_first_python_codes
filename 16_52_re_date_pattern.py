# Practice Question #52

# Create a string:
# "My birth date is 25-12-2000."
# Create a pattern:
# r"\d{2}-\d{2}-\d{4}"
# Use re.search() to find the date.
# Store the result in a variable named result.
# Print the result.
# Print the matched date using group().

# Expected output:
# <re.Match object ...>
# 25-12-2000

import re

text = "My birth date is 25-12-2000." # Store the string in a variable.
pattern = r"\d{2}-\d{2}-\d{4}" # Create a pattern.
result = re.search(pattern, text) # Use re.search() to find the date.
print(result) # Print the result.
print(result.group()) # Print the matched date using group().


