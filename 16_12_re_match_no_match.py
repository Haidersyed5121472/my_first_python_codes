# Practice Question #12

# Import the built-in "re" module.

# Create a variable named text.
# Store this value:
# "I am learning Python."
# Use re.match() to search for the word "Python".
# Store the result in a variable named result.

# Print result.
# Then print the data type of result.

# Expected:
# None
# <class 'NoneType'>
# Note:
# The result should be None because the text does not start with "Python".

import re

text = "I am learning Python." # Store the string in a variable.
result = re.match("Python", text) # Check if the text starts with "Python" using match().
print(result) # Print the result.
print(type(result)) # Print the data type.

