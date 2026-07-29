import string

# Practice Question #1
#
# Import the built-in "string" module.
#
# Create the following string:
#
# text = "hello python world"
#
# Use string.capwords()
# to convert the text.
#
# Print:
#
# 1. Original string.
# 2. Converted string.
#
# Expected Output:
#
# hello python world
#
# Hello Python World

text = "hello python world"

a = string.capwords(text)

print(text)

print(a)


# Practice Question #2
#
# Import the built-in "string" module.
#
# Create the following string:
#
# text_1 = "pYtHoN iS AwEsOmE"
#
# Use string.capwords()
# to convert the text.
#
# Print:
#
# 1. Original string.
# 2. Converted string.
#
# Expected Output:
#
# pYtHoN iS AwEsOmE
#
# Python Is Awesome

text_1 = "pYtHoN iS AwEsOmE"

b = string.capwords(text_1)

print(text_1)

print(b)


# Practice Question #3
#
# Import the built-in "string" module.
#
# Create the following string:
#
# text_2 = "    hello      python        world    "
#
# Use string.capwords()
# to convert the text.
#
# Print:
#
# 1. Original string.
# 2. Converted string.
#
# Observe carefully what happens
# to the extra spaces.
#
# Expected Output:
#
#     hello      python        world
#
# Hello Python World

text_2 = "    hello      python        world    "

c = string.capwords(text_2)

print(text_2)

print(c)


# Practice Question #4
#
# Import the built-in "string" module.
#
# Create the following string:
#
# text_4 = "hello-python-world"
#
# Use string.capwords()
# with the sep parameter
# to capitalize each word.
#
# Print:
#
# 1. Original string.
# 2. Converted string.
#
# Expected Output:
#
# hello-python-world
#
# Hello-Python-World

text_4 = "hello-python-world"

b = string.capwords(text_4, sep="-")

print(text_4)

print(b)


