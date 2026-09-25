# Practice Question #50

# Create a string:

# "My email is ali123@gmail.com."
# Create a pattern to match the email address:
# r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Za-z]{2,}"
# Use re.search() to find the email address.
# Store the result in a variable named result.
# Print the result.
# Print the matched email using group().

# Expected output:
# <re.Match object ...>
# ali123@gmail.com

import re

text = "My email is ali123@gmail.com." # Store the string in a variable.
pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}" # Create a pattern to match the email address.
result = re.search(pattern, text) # Use re.search() to find the email address.
print(result) # Print the result.
print(result.group()) # Print the matched email using group().


