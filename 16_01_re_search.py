# Practice Question #1

# Import the built-in "re" module.

# Create a variable named text.

# Store this value:

# "I am learning Python."

# Use re.search() to search for the word "Python".

# Store the result in a variable named result.

# Print result.

# Then print the data type of result.

# Expected:

# A match object should be returned.

# The data type should be:

# <class 're.Match'>


import re

text = "I am learning Python." # Store the string in a variable.
result = re.search("Python", text) # Search for "Python" in the string.
print(result) # Print the match object.
print(type(result)) # Print the data type.



