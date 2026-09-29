# Practice Question #58

# Create a string:

# "Python3 Java2 C++"
# Create a regex pattern that:
# 1. Finds a word only when it is immediately followed by a digit.
# 2. Uses a lookahead to check for the digit without including it in the match.
# Use re.findall() to find the matching words.
# Store the result in a variable named result.
# Print the result.

# Expected output:
# ['Python', 'Java']
# Note:
# (?=\d) checks that a digit comes next, but does not include the digit in the match.

import re

text = "Python3 Java2 C++" # Store the string in a variable.
pattern = r"\w+(?=\d)" # Create the pattern.
result = re.findall(pattern, text) # Use re.findall() to find the matching words.
print(result) # Print the result.


