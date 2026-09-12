# Practice Question #23

# Import the built-in "re" module.

# Create a string:
# "Python 3.14 is easy!"
# Use re.findall() with the pattern \w
# to find all word characters in the string.
# Store the result in a variable named result.
# Print the result.
# Print the type of result.

# Expected output:
# ['P', 'y', 't', 'h', 'o', 'n', '3', '1', '4', 'i', 's', 'e', 'a', 's', 'y']
# <class 'list'>

import re

text = "Python 3.14 is easy!" # Store the string in a variable.
pattern = r"\w" # Create the pattern to find word characters.
result = re.findall(pattern, text) # Find all word characters using re.findall().
print(result) # Print the result.
print(type(result)) # Print the data type.


