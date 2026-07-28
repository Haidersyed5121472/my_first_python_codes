import random

# Practice Question #1
#
# Import the built-in "random" module.
#
# Create a list containing
# the following colors:
#
# Red
# Blue
# Green
# Yellow
# Black
#
# Select three random colors
# using the appropriate function.
#
# Store the result in a variable.
#
# Print:
#
# 1. The selected colors.
# 2. The data type of the returned value.
#
# Expected Output:
#
# ['Blue', 'Red', 'Blue']
#
# <class 'list'>
#
# OR
#
# ['Green', 'Yellow', 'Black']
#
# <class 'list'>
#
# (The selected colors will be different each time.
# Duplicate colors are allowed.)

colors = ["Red", "Blue", "Green", "Yellow", "Black"]

colors_choices = random.choices(colors, k=3)

print(colors_choices)
print(type(colors_choices))


# Practice Question #2
#
# Import the built-in "random" module.
#
# Create a string containing
# the following characters:
#
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
#
# Select six random characters
# using the appropriate function.
#
# Store the result in a variable.
#
# Print:
#
# 1. The selected characters.
# 2. The data type of the returned value.
#
# Expected Output:
#
# ['A', 'Q', 'M', 'A', 'Z', 'C']
#
# <class 'list'>
#
# OR
#
# ['P', 'B', 'K', 'T', 'Y', 'Y']
#
# <class 'list'>
#
# (The selected characters will be different each time.
# Duplicate characters are allowed.)

stri = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

stri_choice = random.choices(stri, k=6)

print(stri_choice)

print(type(stri_choice))


