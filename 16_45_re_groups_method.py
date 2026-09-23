# Practice Question #45

# Create a string:
# "Ali is 25 years old."
# Create a pattern using two groups ()
# to match the name "Ali" and the age "25".
# Use re.search() to find both groups.
# Store the result in a variable named result.
# Print the result.
# Print the groups using groups().
# Print the type of the result.

# Expected output:
# <re.Match object ...>
# ('Ali', '25')
# <class 're.Match'>
# Note:
# groups() returns all captured groups as a tuple.

import re

text = "Ali is 25 years old." # Store the string in a variable.
pattern = r"(Ali)\s+is\s+(\d{2})" # Create a pattern using two groups () to match the name "Ali" and the age "25".
result = re.search(pattern, text) # Use re.search() to find both groups.
print(result) # Print the result.
print(result.groups()) # Print the groups using groups().
print(type(result)) # Print the type of the result.


