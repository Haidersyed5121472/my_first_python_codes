# Practice Question #17

# Import the built-in "re" module.

# Create a string:
# "I like Python. Python is easy."
# Use re.sub() to replace every occurrence
# of "Python" with "Java".
# Store the result in a variable named result.

# Print the result.
# Print the type of result.

# Expected output:
# I like Java. Java is easy.
# <class 'str'>

import re

text = "I like Python. Python is easy." # Store the string in a variable.
result = re.sub("Python", "Java", text) # Replace "Python" with "Java" using re.sub.
print(result) # Print the result.
print(type(result)) # Print the data type.


