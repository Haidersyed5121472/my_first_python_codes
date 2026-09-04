# Practice Question #8

# Import the built-in "re" module.

# Create a variable named text.

# Store this value:
# "I am learning Python and Python is easy."
# Use re.search() to search for the word pattern:
# Python
# Store the result in a variable named result.

# Print result.
# Then print the data type of result.

# Expected:
# A match object should be returned for the first "Python".
# <class 're.Match'>

import re

text = "I am learning Python and Python is easy." # Store the string in a variable.
result = re.search("Python", text) # Check if "Python" is in the string.
print(result) # Print the result.
print(type(result)) # Print the data type.



