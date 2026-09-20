# Practice Question #39

# Create a string:

# "I like Python and Java."
# Create a pattern using the "|" OR operator
# to match either "Python" or "Java".
# Use re.findall() to find all matches.
# Store the result in a variable named result.
# Print the result.
# Print the type of result.

# Expected output:
# ['Python', 'Java']
# Note:
# The "|" operator means OR.

import re

text = "I like Python and Java." # Store the string in a variable.
pattern = r"Python|Java" # Create the pattern to match either "Python" or "Java".
result = re.findall(pattern, text) # Use re.findall() to find all matches.
print(result) # Print the result.
print(type(result)) # Print the data type.




