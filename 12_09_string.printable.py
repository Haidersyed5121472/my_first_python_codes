import string

# Practice Question #1
#
# Import the built-in "string" module.
#
# Store string.printable
# in a variable.
#
# Print:
#
# 1. The complete value using repr().
# 2. Its data type.
# 3. Its length.
#
# Expected Output:
#
# (Complete printable string)
#
# <class 'str'>
#
# 100

a = string.printable

print(repr(a))

print(type(a))

print(len(a))


# Practice Question #2
#
# Import the built-in "string" module.
#
# Create the following string:
#
# text = "Python@2026\tAI\n"
#
# Using a loop and string.printable,
# print only those characters
# that are present in string.printable.
#
# Print each character using repr().
#
# Expected Output:
#
# 'P'
# 'y'
# 't'
# ...
# '@'
# '2'
# ...
# '\t'
# 'A'
# 'I'
# '\n'

text = "Python@2026\tAI\n"

for i in text:
    if i in string.printable:
        print(repr(i))


# Practice Question #3
#
# Import the built-in "string" module.
#
# Create the following string:
#
# text = "Python@2026 AI!"
#
# Using ONE loop,
# count how many characters
# belong to string.printable.
#
# Print the total count.
#
# Expected Output:
#
# 15

text = "Python@2026 AI!"


count = 0
for i in (text):
    if i in string.printable:
        count += 1

print(count)


