# Practice Question #5

# Import the built-in "re" module.

# Create a variable named text.

# Store this value:
# "I am learning Python."
# Use re.search() to search for the word "python".
# Make the search case-insensitive using re.IGNORECASE.
# Store the result in a variable named result.
# Print result.
# Then print the data type of result.

# Expected:

# A match object should be returned.
# <class 're.Match'>

import re

text = "I am learning Python." # Store the string in a variable.
result = re.search("python", text, re.IGNORECASE) # Search for "python" in the string using case-insensitive search.
print(type(result)) # Print the data type.


