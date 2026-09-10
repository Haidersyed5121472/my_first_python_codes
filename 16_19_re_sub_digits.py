# Practice Question #19

# Import the built-in "re" module.
# Create a string:
# "My phone numbers are 03001234567 and 03111234567."
# Use re.sub() to replace every sequence of digits
# with the word "NUMBER".
# Store the result in a variable named result.
# Print the result.

# Expected output:
# My phone numbers are NUMBER and NUMBER.


import re

text = "My phone numbers are 03001234567 and 03111234567." # Store the string in a variable.
pattern = r"\d+" # Create the pattern for digits.
result = re.sub(pattern, "NUMBER", text) # Replace the digits with "NUMBER" using re.sub().
print(result) # Print the result.

