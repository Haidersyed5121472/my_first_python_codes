# Practice Question #14

# Import the built-in "re" module.

# Create a variable named text.
# Store this value:
# "Python is easy. Python is powerful."
# Use re.finditer() to find all occurrences of the word "Python".
# Store the result in a variable named result.
# Use a for loop to iterate through result.
# Inside the loop, print the start position of each match
# using the start() method.

# Expected:
# 0
# 16

import re

text = "Python is easy. Python is powerful." # Store the string in a variable.
result = re.finditer("Python", text) # Find all occurrences of "Python" in the text using finditer().

for i in result: # Loop through the result.
    print(i.start()) # Print the start of all occurrences.


