# Practice Question #13

# Import the built-in "re" module.

# Create a variable named text.
# Store this value:
# "Python is easy. Python is powerful. Python is popular."
# Use re.finditer() to find all occurrences of the word "Python".
# Store the result in a variable named result.
# Use a for loop to iterate through result.
# Print each match.

# Expected:
# Three match objects should be printed.

import re


text = "Python is easy. Python is powerful. Python is popular." # Store the string in a variable.
result = re.finditer("Python", text) # Find all occurrences of "Python" in the text using finditer().

for i in result: # Loop through the result.
    print(i) # Print the result.


