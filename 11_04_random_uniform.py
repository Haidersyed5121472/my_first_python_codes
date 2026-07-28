import random

# Practice Question #1
#
# Import the built-in "random" module.
#
# Generate one random floating-point number
# between 1.5 and 10.5
# using the appropriate function.
#
# Store the result in a variable.
#
# Print:
#
# 1. The random floating-point number.
# 2. The data type of the returned value.
#
# Expected Output:
#
# 7.483921...
#
# <class 'float'>
#
# (The random number will be different each time.)

deci_num = random.uniform(1.5, 10.5)

print(deci_num)

print(type(deci_num))


# Practice Question #2
#
# Import the built-in "random" module.
#
# A weather station needs to simulate
# a random temperature.
#
# Generate one random floating-point number
# between 20.0 and 40.0
# using the appropriate function.
#
# Store the result in a variable.
#
# Print:
#
# 1. The temperature.
#
# Then:
#
# If the temperature is greater than or equal to 30.0,
# print:
#
# Hot Weather
#
# Otherwise, print:
#
# Pleasant Weather
#
# Expected Output:
#
# 34.728391...
# Hot Weather
#
# OR
#
# 24.182736...
# Pleasant Weather
#
# (The temperature will be different each time.)

temp = random.uniform(20.0, 40.0)

print(temp)

if temp >= 30.0 :
    print("Hot Weather")
else:
    print("Pleasant Weather")


