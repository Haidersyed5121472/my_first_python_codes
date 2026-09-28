# Practice Question #55

# Create a string:

# "Python is easy. I love Python."
# Create a regex pattern:
# r"\bPython\b"
# Use re.findall() to find "Python" as a complete word.
# Store the result in a variable named result.
# Print the result.

# Expected output:
# ['Python', 'Python']
# Note:
# \b matches a word boundary.

import re

text = "Python is easy. I love Python." # Store the string in a variable.
pattern = r"\bPython\b" # Create the pattern.
result = re.findall(pattern, text) # Use re.findall() to find "Python" as a complete word
print(result) # Print the result.


