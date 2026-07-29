import string

# Practice Question #1
#
# Import the built-in "string" module.
#
# Store string.octdigits
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
# 01234567
#
# <class 'str'>
#
# 8

a = string.octdigits

print(a)

print(type(a))

print(len(a))


# Practice Question #2
#
# Import the built-in "string" module.
#
# Store string.octdigits
# in a variable.
#
# Using a loop and enumerate(),
# print only those octal digits
# whose index is EVEN.
#
# Expected Output:
#
# 0 -> 0
# 2 -> 2
# 4 -> 4
# 6 -> 6


b = string.octdigits

for index, digit in enumerate(b):
    if index % 2 == 0:
        print(f"Index : {index} -> Digit : {digit}")


