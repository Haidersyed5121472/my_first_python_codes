# Practice Question #59

# Create a string:

# "Price: $500 and Price: $300"
# Create a regex pattern that:
# 1. Finds numbers only when they are immediately preceded by "$".
# 2. Uses a lookbehind to check for "$" without including "$" in the match.
# Use re.findall() to find the matching numbers.
# Store the result in a variable named result.
# Print the result.

# Expected output:
# ['500', '300']
# Note:
# (?<=\$) checks that "$" comes immediately before the number,
# but does not include "$" in the match.

import re

text = "Price: $500 and Price: $300" # Store the string in a variable.
pattern = r"(?<=\$)\d+" # Create the pattern.
result = re.findall(pattern, text) # Use re.findall() to find the matching numbers. 
print(result) # Print the result.


