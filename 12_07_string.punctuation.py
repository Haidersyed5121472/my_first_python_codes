import string

# Practice Question #1
#
# Import the built-in "string" module.
#
# Store string.punctuation
# in a variable.
#
# Print:
#
# 1. The complete string.
# 2. Its data type.
# 3. Its length.
#
# Expected Output:
#
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
#
# <class 'str'>
#
# 32

a = string.punctuation

print(a)

print(type(a))

print(len(a))


# Practice Question #2
#
# Import the built-in "string" module.
#
# Store string.punctuation
# in a variable.
#
# Using a loop,
# print only these punctuation marks:
#
# @
# #
# $
# _
#
# Do NOT type the complete punctuation string manually.
#
# Expected Output:
#
# @
# #
# $
# _

b = string.punctuation

special_characters = ("@#$_")

for i in b:
    if i in special_characters:
        print(i)


# Practice Question #3
#
# Import the built-in "string" module.
#
# Create the following string:
#
# text = "Hello@Python#2026!"
#
# Using a loop and string.punctuation,
# print only the punctuation characters
# present in the text.
#
# Expected Output:
#
# @
# #
# !

text = "Hello@Python#2026!"

for i in text :
    if i in string.punctuation:
        print(i)




