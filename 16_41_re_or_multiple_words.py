# Practice Question #41

# Create a string:
# "I use Python, Java, and C++."
# Create a pattern using the "|" OR operator
# to match "Python", "Java", or "C++".
# Use re.findall() to find all matches.
# Store the result in a variable named result.
# Print the result.
# Print the type of result.
# Expected output:
# ['Python', 'Java', 'C++']
# Note:
# Use "|" to match multiple alternatives.

import re
 
text = "I use Python, Java, and C++." # Store the string in a variable.
pattern = r"Python|Java|C\+\+" # Create a pattern using the "|" OR operator.
result = re.findall(pattern, text) # Use re.findall() to find all matches.
print(result) # Print the result.
print(type(result)) # Print the data type.


