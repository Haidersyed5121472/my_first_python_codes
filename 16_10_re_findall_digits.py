# Practice Question #10


# Import the built-in "re" module.
# Create a variable named text.
# Store this value:
# "Ali is 25 years old and Haider is 30 years old."
# Use re.findall() to find all numbers from the text.
# Use the digit pattern:
# \d+
# Store the result in a variable named result.

# Print result.
# Then print the data type of result.

# Expected:
# ['25', '30']
# <class 'list'>


import re


text = "Ali is 25 years old and Haider is 30 years old." # Store the string in a variable. 
pattern = r"\d+" # Use \d+ to match digits.
result = re.findall(pattern, text) # Find all digits in the text.
print(result) # Print the result. 
print(type(result)) # Print the data type.


