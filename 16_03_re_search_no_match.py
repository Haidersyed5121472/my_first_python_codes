
# Practice Question #3

# Import the built-in "re" module.

# Create a variable named text.

# Store this value:

# "I am learning Python."

# Use re.search() to search for the word "Java".

# Store the result in a variable named result.

# Print result.

# Then print the data type of result.

# Expected:

# None

# <class 'NoneType'>

import re

text = "I am learning Python." # store the string in a variable.
result = re.search("Java", text) # Search for "Java" in the string.
print(result) # Print the result.
print(type(result)) # Print the data type.




