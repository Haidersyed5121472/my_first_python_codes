# Practice Question #27

# Import the built-in "re" module.
# Create a string:
# "cat, bat, hat, mat"
# Use re.findall() with the pattern ".at"
# to find all words that contain any character
# followed by "at".
# Store the result in a variable named result.
# Print the result.
# Print the type of result.

# Expected output:
# ['cat', 'bat', 'hat', 'mat']
# <class 'list'>


import re

text = "cat, bat, hat, mat" # Store the string in a variable.
pattern = r".at" # Create the pattern to find all words containing ".at".
result = re.findall(pattern, text) # Find all words containing "at" using re.findall().
print(result) # Print the result.
print(type(result)) # Print the data type.


