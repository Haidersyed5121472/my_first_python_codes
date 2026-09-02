# Practice Question #6

# Import the built-in "re" module.

# Create a variable named text.
# Store this value:
# "Python is easy. I am learning Python."
# Use re.search() to search for the word "Python".
# Start the search from index 20 using the "pos" parameter.
# Store the result in a variable named result.
# Print result.
# Then print the data type of result.

# Expected:

# A match object should be returned for the second "Python".
# <class 're.Match'>

import re

text = "Python is easy. I am learning Python." # Store the string in a variable.
pattern = re.compile("Python") # Create a compiled regex pattern.
result = pattern.search(text, pos=20) # Search for "Python" starting from index 20.
print(result) # Print the result.
print(type(result)) # Print the data type.


