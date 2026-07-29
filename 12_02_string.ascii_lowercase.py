import string

# Practice Question #1
#
# Import the built-in "string" module.
#
# Store string.ascii_lowercase
# in a variable.
#
# Print:
#
# 1. The complete lowercase alphabet.
# 2. The data type.
#
# Expected Output:
#
# abcdefghijklmnopqrstuvwxyz
#
# <class 'str'>

a = string.ascii_lowercase

print(a)

print(type(a))


# Practice Question #2
#
# Import the built-in "string" module.
#
# Store string.ascii_lowercase
# in a variable.
#
# Without typing any alphabet manually,
# print every 3rd lowercase letter.
#
# Expected Output:
#
# adgjmpsvy

y = string.ascii_lowercase

print(y[0:26:3])

# There is another way to do this.
print(y[::3])


# Practice Question #3
#
# Import the built-in "string" module.
#
# Store string.ascii_lowercase
# in a variable.
#
# Without typing any alphabet manually,
# use a loop to print each lowercase
# letter with its index.
#
# Expected Output:
#
# 0 -> a
# 1 -> b
# 2 -> c
# ...
# 25 -> z

x = string.ascii_lowercase

for index, letter in enumerate(x) :
    print(index,"->",letter)


# Practice Question #4
#
# Import the built-in "string" module.
#
# Store string.ascii_lowercase
# in a variable.
#
# Using a loop and a condition,
# print only the vowels.
#
# Do NOT type:
# abcdefghijklmnopqrstuvwxyz
#
# Expected Output:
#
# a
# e
# i
# o
# u


w = string.ascii_lowercase
vwl = "aeiou"
for i in w :
    if i in vwl:
        print(i)




