import random

# Practice Question #1
#
# Import the built-in "random" module.
#
# Generate one random floating-point number
# using the appropriate function
# and store it in a variable.
#
# Print:
#
# 1. The random number.
# 2. The data type of the returned value.
#
# Expected Output:
#
# 0.847362918273...
#
# <class 'float'>
#
# (The random number will be different each time.)

number = random.random()
print(number)

print(type(number))


# Practice Question #2
#
# Import the built-in "random" module.
#
# Generate one random floating-point number
# and store it in a variable.
#
# Print the generated number.
#
# Then:
#
# If the number is less than 0.5,
# print:
#
# Low
#
# Otherwise, print:
#
# High
#
# Expected Output:
#
# 0.284731928...
# Low
#
# OR
#
# 0.817362891...
# High
#
# (The random number will be different each time.)

special_number = random.random()

print(special_number)

if special_number < 0.5 :
    print("Low")
else:
    print("High")


