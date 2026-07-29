import string

# Practice Question #1
#
# Import the built-in "string" module.
#
# Store string.whitespace
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
# ' \t\n\r\x0b\x0c'
#
# <class 'str'>
#
# 6

a = string.whitespace

print(repr(a))

print(type(a))

print(len(a))


# Practice Question #2
#
# Import the built-in "string" module.
#
# Create the following string:
#
# text = "Hello\tPython\n2026 World"
#
# Using a loop and string.whitespace,
# print only the whitespace characters
# present in the text.
#
# Use repr() while printing each character
# so the whitespace is visible.
#
# Expected Output:
#
# '\t'
# '\n'
# ' '

text = "Hello\tPython\n2026 World"

for i in text :
    if i in string.whitespace:
        print(repr(i))



