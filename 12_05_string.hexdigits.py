import string

# Practice Question #1
#
# Import the built-in "string" module.
#
# Store string.hexdigits
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
# 0123456789abcdefABCDEF
#
# <class 'str'>
#
# 22

a = string.hexdigits

print(a)

print(type(a))

print(len(a))


# Practice Question #2
#
# Import the built-in "string" module.
#
# Store string.hexdigits
# in a variable.
#
# Using a loop and a condition,
# print only the alphabetic
# hexadecimal characters.
#
# Expected Output:
#
# a
# b
# c
# d
# e
# f
# A
# B
# C
# D
# E
# F

b = string.hexdigits

letters = "abcdefABCDEF"
for i in b:
    if i in letters:
        print(i)



