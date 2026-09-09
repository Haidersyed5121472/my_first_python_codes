# Practice Question #18

# Import the built-in "re" module.

# Create a string:

# "Python is easy. python is popular. PYTHON is powerful."
# Use re.sub() with re.IGNORECASE
# to replace every occurrence of "python"
# with "Java".
# Store the result in a variable named result.

# Print the result.

# Expected output:
# Java is easy. Java is popular. Java is powerful.

import re

text = "Python is easy. python is popular. PYTHON is powerful." # Store the string in a variable.
result = re.sub("python", "Java", text, flags=re.IGNORECASE) # Replace all occurrences of "python" with "Java" using re.sub() and re.IGNORECASE.
print(result) # Print the result


