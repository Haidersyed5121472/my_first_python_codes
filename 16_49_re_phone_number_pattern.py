# Practice Question #49

# Create a string:

# "My phone number is 03001234567."
# Create a pattern using:
# \d{11}
# Use re.search() to find the phone number.
# Store the result in a variable named result.
# Print the result.
# Print the matched phone number using group().

# Expected output:
# <re.Match object ...>
# 03001234567

import re

text = "My phone number is 03001234567." # Store the string in a variable.
pattern = r"\d{11}" # Create the pattern.
result = re.search(pattern, text) # Use re.search() to find the phone number.
print(result) # Print the result.
print(result.group()) # Print the matched phone number using group().


