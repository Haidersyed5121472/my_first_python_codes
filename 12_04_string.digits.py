import string

# Practice Question #1
#
# Import the built-in "string" module.
#
# Store string.digits
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
# 0123456789
#
# <class 'str'>
#
# 10

a = string.digits

print(a)

print(type(a))

print(len(a))


# Practice Question #2
#
# Import the built-in "string" module.
#
# Store string.digits
# in a variable.
#
# Using a loop,
# print only the EVEN digits.
#
# Do NOT type:
#
# 02468
#
# Expected Output:
#
# 0
# 2
# 4
# 6
# 8

b = string.digits
num = "02468"
for i in b:
    if i in num:
        print(i)


# Practice Question #3
#
# Import the built-in "string" module.
#
# Store string.digits
# in a variable.
#
# Using enumerate(),
# print only those digits
# whose index is ODD.
#
# Expected Output:
#
# 1 -> 1
# 3 -> 3
# 5 -> 5
# 7 -> 7
# 9 -> 9

c = string.digits

for index, digits in enumerate(c):
    if index % 2 == 1:
        print(f"Index : {index} -> Digits : {digits}")


