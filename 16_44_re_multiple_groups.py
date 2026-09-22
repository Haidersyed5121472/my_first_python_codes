# Practice Question #44

# Create a string:
# "Ali is 25 years old."
# Create a pattern using two groups ()
# to match the name "Ali" and the age "25".
# Use re.search() to find both groups.
# Store the result in a variable named result.
# Print the result.
# Print the first group using group(1).
# Print the second group using group(2).
# Expected output:
# <re.Match object ...>
# Ali
# 25
# Note:
# group(1) returns the first captured group.
# group(2) returns the second captured group.

import re
 
text = "Ali is 25 years old." # Store the string in a variable.
pattern = r"(Ali)\s+is\s+(\d{2})" # Create a pattern using two groups () to match the name "Ali" and the age "25".
result = re.search(pattern, text) # Use re.search() to find both groups.
print(result) # Print the result.
print(result.group(1)) # Print the first group using group(1).
print(result.group(2)) # Print the second group using group(2).


