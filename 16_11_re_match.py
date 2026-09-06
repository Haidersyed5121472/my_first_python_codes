# Practice Question #11

# Import the built-in "re" module.

# Create a variable named text.
# Store this value:
# "Python is easy to learn."
# Use re.match() to search for the word "Python".
# Store the result in a variable named result.
# Print result.
# Then print the data type of result.

# Expected:
# A match object should be returned.
# <class 're.Match'>

import re

text = "Python is easy to learn." # Store the string in a variable.
result = re.match("Python", text) # Check if the text starts with "Python" using match().
print(result) # Print the result.
print(type(result)) # Print the data type.


