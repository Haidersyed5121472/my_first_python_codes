# Practice Question #2
 
 
# Import the built-in "re" module.

# Create a variable named text.

# Store this value:

# "My phone number is 03001234567."

# Use re.search() to search for the phone number

# "03001234567".

# Store the result in a variable named result.

# Print result.

# Then print the data type of result.

# Expected:

# A match object should be returned.

# The data type should be:

# <class 're.Match'>


import re



text = "My phone number is 03001234567." # store the string in a variable.
result = re.search("03001234567", text) # Search for "03001234567" in the string.
print(result) # Print the match object.
print(type(result)) # Print the data type.


