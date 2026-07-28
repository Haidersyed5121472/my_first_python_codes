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
# Select one random color
# using the appropriate function
# and store it in a variable.
#
# Print:
#
# 1. The selected color.
# 2. The data type of the returned value.
#
# Expected Output:
#
# Green
#
# <class 'str'>
#
# OR
#
# Red
#
# <class 'str'>
#
# (The selected color will be different each time.)

colors = ["Red", "Blue", "Green", "Yellow", "Black"]

rand_choice = random.choice(colors)

print(rand_choice)

print(type(rand_choice))


# Practice Question #2
#
# Import the built-in "random" module.
#
# Create a tuple containing
# the following fruits:
#
# Apple
# Mango
# Orange
# Banana
# Grapes
#
# Select one random fruit
# using the appropriate function
# and store it in a variable.
#
# Print:
#
# 1. The selected fruit.
#
# Then:
#
# If the selected fruit is "Mango",
# print:
#
# Favorite Fruit Selected!
#
# Otherwise, print:
#
# Another Fruit Selected!
#
# Expected Output:
#
# Mango
# Favorite Fruit Selected!
#
# OR
#
# Apple
# Another Fruit Selected!
#
# (The selected fruit will be different each time.)

fruits = ("Apple", "Mango", "Orange", "Banana", "Grapes")

selection = random.choice(fruits)

print(selection)

if selection == "Mango" :
    print("Favorite Fruit Selected!")
else:
    print("Another Fruit Selected!")


