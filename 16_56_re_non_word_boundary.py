# Practice Question #56

# Create a string:

# "Python python mypython."
# Create a regex pattern:
# r"\Bpython"
# Use re.findall() to find "python" when it is NOT at a word boundary.
# Store the result in a variable named result.
# Print the result.

# Expected output:
# ['python']
# Note:
# \B matches a position that is NOT a word boundary.

import re

text = "Python python mypython." # Store the string in a variable.
pattern = r"\Bpython" # Create the pattern.
result = re.findall(pattern, text) # Use re.findall() to find "python" when it is NOT at a word boundary.
print(result) # Print the result.



