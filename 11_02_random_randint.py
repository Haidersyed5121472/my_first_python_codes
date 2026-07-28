import random

# Practice Question #1
#
# Import the built-in "random" module.
#
# Generate one random integer
# between 1 and 100 (both included)
# and store it in a variable.
#
# Print:
#
# 1. The random integer.
# 2. The data type of the returned value.
#
# Expected Output:
#
# 57
#
# <class 'int'>
#
# (The random integer will be different each time.)

num_generator = random.randint(1, 100)

print(num_generator)

print(type(num_generator))


# Practice Question #2
#
# Import the built-in "random" module.
#
# Simulate a dice roll by generating
# one random integer between 1 and 6
# (both included).
#
# Store the result in a variable.
#
# Print:
#
# 1. The dice value.
#
# Then:
#
# If the value is 6,
# print:
#
# Congratulations! You rolled the highest number.
#
# Otherwise, print:
#
# Try Again!
#
# Expected Output:
#
# 6
# Congratulations! You rolled the highest number.
#
# OR
#
# 3
# Try Again!
#
# (The dice value will be different each time.)

dice_simulator = random.randint(1, 6)

print(dice_simulator)

if dice_simulator == 6:
    print("Congrulations! You rolled the highest number.")
else:
    print("Try Again!")


