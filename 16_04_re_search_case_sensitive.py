
# Practice Question #4

# Import the built-in "re" module.

# Create a variable named text.

# Store this value:

# "I am learning Python."

# Use re.search() to search for the word "python".

# Store the result in a variable named result.

# Print result.

# Then print the data type of result.

# Expected:

# None

# <class 'NoneType'>

# Note:

# The search should return None because "Python" and "python"

# have different uppercase/lowercase letters.

import re

text = "I am learning Python." # store the string in a variable.
result = re.search("python", text) # Search for "python" in the string.
print(result) # Print the result.
print(type(result)) # Print the data type.


