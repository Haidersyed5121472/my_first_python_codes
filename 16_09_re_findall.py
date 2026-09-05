# Practice Question #9

# Import the built-in "re" module.
# Create a variable named text.
# Store this value:
# "Python is easy. Python is powerful. Python is popular."
# Use re.findall() to find all occurrences of the word "Python".
# Store the result in a variable named result.
# Print result.
# Then print the data type of result.

# Expected:
# ['Python', 'Python', 'Python']
# <class 'list'>


import re

text = "Python is easy. Python is powerful. Python is popular." # Store the string in a variable.
result = re.findall("Python", text) # Find all occurrences of "Python" using findall().
print(result) # Print the result.
print(type(result)) # Print the data type.



