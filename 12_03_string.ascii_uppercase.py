import string

# Practice Question #1
#
# Import the built-in "string" module.
#
# Store string.ascii_uppercase
# in a variable.
#
# Print:
#
# 1. The complete uppercase alphabet.
# 2. The data type.
#
# Expected Output:
#
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
#
# <class 'str'>

a = string.ascii_uppercase

print(a)

print(type(a))


# Practice Question #2
#
# Import the built-in "string" module.
#
# Store string.ascii_uppercase
# in a variable.
#
# Using a loop and enumerate(),
# print only those uppercase letters
# whose index is divisible by 5.
#
# Expected Output:
#
# 0 -> A
# 5 -> F
# 10 -> K
# 15 -> P
# 20 -> U
# 25 -> Z

b = string.ascii_uppercase

for index, letters in enumerate(b):
    if index % 5 == 0:
        print("Index :",index,"->", "Letter :",letters)


