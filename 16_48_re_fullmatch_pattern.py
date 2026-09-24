# Practice Question #48

# Create a string:
# "12345"
# Create a pattern:
# r"\d+"
# Use re.fullmatch() to check whether
# the entire string contains only digits.
# Store the result in a variable named result.
# Print the result.
# Print the matched value using group().

# Expected output:
# <re.Match object ...>
# 12345

import re

number = "12345" # Store the string in a variable.
pattern = r"\d+" # Create the pattern.
result = re.fullmatch(pattern, number) # Use re.fullmatch() to check whether the entire string contains only digits.
print(result) # Print the result.
print(result.group()) # Print the matched value using group().


