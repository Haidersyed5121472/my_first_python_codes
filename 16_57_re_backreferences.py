# Practice Question #57

# Create a string:

# "hello hello world"
# Create a regex pattern that:
# 1. Captures a word using a group.
# 2. Uses a backreference to find the same word repeated immediately.
# Use re.search() to find the repeated word.
# Store the result in a variable named result.
# Print the result.
# Also print the matched text using result.group().

# Expected output:
# <re.Match object; span=(0, 11), match='hello hello'>
# hello hello
# Note:
# \1 refers back to the text captured by the first group.


import re

text = "hello hello world" # Store the string in a variable.
pattern = r"(hello) \1" # Create the pattern.
result = re.search(pattern, text) # Use re.search() to find the repeated word.
print(result) # Print the result.
print(result.group()) # Print the matched text using result.group().


