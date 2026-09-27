# Practice Question #53

# Create a string:
# "Python123"
# Create a pattern:
# r"^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$"
# Use re.fullmatch() to check whether
# the password:
# 1. Contains at least one uppercase letter.
# 2. Contains at least one digit.
# 3. Contains only letters and digits.
# 4. Contains at least 8 characters.
# Store the result in a variable named result.
# Print the result.
# Print the matched password using group().

# Expected output:
# <re.Match object ...>
# Python123

import re

text = "Python123" # Store the string in a variable.
pattern = r"^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$" # Create a pattern.
result = re.fullmatch(pattern, text) # Use re.fullmatch().
print(result) # Print the result.
print(result.group()) # Print the matched password using group().

