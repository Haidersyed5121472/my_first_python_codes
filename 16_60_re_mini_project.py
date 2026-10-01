# Practice Question #60

# Create a string:

# "Name: Ali, Email: ali123@gmail.com, Phone: 03001234567"
# Create three regex patterns to find:
# 1. The name "Ali" using a named group.
# 2. The email address using an email pattern.
# 3. The phone number using a digit pattern.
# Use re.search() for each pattern.
# Store the three results in:
# name_result
# email_result
# phone_result
# Print the matched name, email, and phone number using .group().

# Expected output:
# Ali
# ali123@gmail.com
# 03001234567
# Concepts to use:
# - Named groups (?P<name>...)
# - re.search()
# - Email pattern
# - \d
# - .group()


import re

text = "Name: Ali, Email: ali123@gmail.com, Phone: 03001234567" # Store the string in a variable.
name_pattern = "(?P<name>Ali)" # Create the pattern for name.
email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}" # Create the pattern for email.
phone_pattern = r"\d{11}" # Create the pattern for Phone Number.
name_result = re.search(name_pattern, text) # Use re.search() to find the name.
email_result = re.search(email_pattern, text) # Use re.search() to find the email.
phone_result = re.search(phone_pattern, text) # Use re.search() to find the Phone Number.
print(name_result.group("name")) # Print the matched name using .group().
print(email_result.group()) # Print the matched email using .group().
print(phone_result.group()) # Print the matched Phone Number using .group().




