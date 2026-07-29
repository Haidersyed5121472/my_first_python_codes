import string

# Practice Question #1
#
# Import the built-in "string" module.
#
# Print the value of
# string.ascii_letters.
#
# Then print its data type.
#
# Expected Output:
#
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
#
# <class 'str'>

a = string.ascii_letters

print(a)
print(type(a))


# Practice Question #2
#
# Import the built-in "string" module.
#
# Store string.ascii_letters
# in a variable.
#
# Print:
#
# 1. Total number of characters.
# 2. First character.
# 3. Last character.
#
# Expected Output:
#
# 52
# a
# Z

b = string.ascii_letters

print(len(b))

print(b[0])

print(b[51])

# There is another way to get the last character.
print(b[-1])


# Practice Question #3
#
# Import the built-in "string" module.
#
# Store string.ascii_letters
# in a variable.
#
# Print:
#
# 1. Characters from index 0 to 25.
# 2. Characters from index 26 to the end.
#
# Expected Output:
#
# abcdefghijklmnopqrstuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ

z = string.ascii_letters

print(z[0:26])

print(z[26:])


