# Practice Question #15

# Import the built-in "re" module.

# Create a variable named text.
# Store this value:
# "Python is easy and Python is powerful."
# Use re.split() to split the text wherever a space occurs.
# Store the result in a variable named result.

# Print result.
# Then print the data type of result.

# Expected:
# A list containing each word should be returned.
# <class 'list'>

import re

text = "Python is easy and Python is powerful." # Store the string in a variable.
result = re.split(" ",text) # Split the string using re.split().
print(result) # Print the result. 
print(type(result)) # Print the data type.

