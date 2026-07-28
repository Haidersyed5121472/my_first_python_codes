import random

# Practice Question #1
#
# Import the built-in "random" module.
#
# Generate one random integer
# between 10 and 19
# using the appropriate function.
#
# Store the result in a variable.
#
# Print:
#
# 1. The random integer.
# 2. The data type of the returned value.
#
# Expected Output:
#
# 14
#
# <class 'int'>
#
# (The random integer will be different each time.)

num_gen = random.randrange(10, 20)

print(num_gen)

print(type(num_gen))


# Practice Question #2
#
# Import the built-in "random" module.
#
# Generate one random even integer
# between 2 and 20 (both included)
# using the appropriate function.
#
# Use the step parameter
# to make sure only even numbers
# can be generated.
#
# Store the result in a variable.
#
# Print:
#
# 1. The random even integer.
# 2. The data type of the returned value.
#
# Expected Output:
#
# 2
#
# OR
#
# 8
#
# OR
#
# 20
#
# <class 'int'>
#
# (Only even numbers should be generated.)

even_num = random.randrange(2, 21, 2)

print(even_num)

print(type(even_num))


