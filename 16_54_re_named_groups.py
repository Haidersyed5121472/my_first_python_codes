# Practice Question #54

# Create a string:

# "Name: Ali, Age: 25"
# Create a pattern using named groups:
# (?P<name>...)
# (?P<age>...)
# Use re.search() to find the name and age.
# Store the result in a variable named result.
# Print the result.
# Print the name using group("name").
# Print the age using group("age").

# Expected output:
# <re.Match object ...>
# Ali
# 25


import re

text = "Name: Ali, Age: 25" # Store the string in a variable.
pattern = "(?P<name>Ali)" # Create a pattern for name.
pattern1 = "(?P<age>25)" # Create a pattern for age.
result = re.search(pattern+", Age: "+pattern1, text) # Use re.search() to find the name and age.
print(result) # Print the result.
print(result.group("name")) # Print the name using group("name").
print(result.group("age")) # Print the age using group("age").



